from flask import Flask, render_template, request, redirect, url_for, session
import pandas as pd
import joblib
import json
import os
from google.cloud import storage

# Set the environment variable for Google Cloud credentials

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'abcdefghijklmnopqrstuvwxyz'

# Your GCS bucket name
BUCKET_NAME = 'career-navigator-bucket'
USERS_FILE_NAME = 'users.json'

# Initialize the GCS client
storage_client = storage.Client()

def load_users():
    """Load users from the Google Cloud Storage bucket."""
    try:
        # Get the bucket and blob (file)
        bucket = storage_client.get_bucket(BUCKET_NAME)
        blob = bucket.blob(USERS_FILE_NAME)

        # Download the file content as a string
        if blob.exists():
            users_json = blob.download_as_text()
            return json.loads(users_json)
        return {}  # Return an empty dictionary if the file doesn't exist.
    except Exception as e:
        print(f"Error loading users from GCS: {e}")
        return {}

def save_users(users):
    """Save users to the Google Cloud Storage bucket."""
    try:
        # Get the bucket and blob (file)
        bucket = storage_client.get_bucket(BUCKET_NAME)
        blob = bucket.blob(USERS_FILE_NAME)

        # Convert the users data to JSON
        users_json = json.dumps(users, indent=4)

        # Upload the JSON data as a string
        blob.upload_from_string(users_json, content_type='application/json')
    except Exception as e:
        print(f"Error saving users to GCS: {e}")

# Load job roles data from JSON file
with open('desc.json', 'r') as f:
    job_roles = json.load(f)

# Load the trained model
model = joblib.load('model.pkl')

@app.route('/')
def index():
    """Render the login page or redirect to home if logged in."""
    if 'username' in session:
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """Handle user signup."""
    if request.method == 'POST':
        username = request.form['mailid']
        password = request.form['pass']
        confirm_password = request.form['conpass']

        if password != confirm_password:
            return render_template('signup.html', password_match=False)

        users = load_users()
        if username in users:
            return render_template('signup.html', email_exists=True)

        # Add the new user to the dictionary
        users[username] = {
            'password': password,  # No hashing, as per your request
            'predicted_job_role': []
        }

        save_users(users)
        return redirect(url_for('index'))

    return render_template('signup.html', password_match=True, email_exists=False)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handle user login."""
    if request.method == 'POST':
        username = request.form['mailid']
        password = request.form['pass']

        # Debugging: Print the loaded users
        users = load_users()
        print(f"Users loaded from file: {users}")  # Add this line to check users

        if username in users and users[username]['password'] == password:
            session['username'] = username
            return redirect(url_for('home'))
        return render_template('login.html', login_failed=True)

    return render_template('login.html', login_failed=False)

@app.route('/logout')
def logout():
    """Log the user out and redirect to login page."""
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/home')
def home():
    """Render the home page for logged-in users."""
    if 'username' not in session:
        return redirect(url_for('index'))
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Handle job role predictions."""
    if 'username' not in session:
        return redirect(url_for('index'))

    if request.method == 'POST':
        try:
            users = load_users()
            data = request.form

            smart_worker = 1 if data['hard_worker'] == '0' else 0
            technical = 1 if data['management'] == '0' else 0

            user_data = pd.DataFrame([[ 
                int(data['logical_quotient']), int(data['coding_skills']),
                int(data['hackathons']), int(data['public_speaking']),
                int(data['self_learning']), int(data['extra_courses']),
                int(data['seniors_inputs']), int(data['team_work']),
                int(data['introvert']), int(data['reading_writing']),
                int(data['memory_capability']), int(data['hard_worker']),
                smart_worker, int(data['management']), technical,
                int(data['interested_subjects']), int(data['interested_books']),
                int(data['certifications']), int(data['workshops']),
                int(data['company_type']), int(data['career_area'])
            ]], columns=[
                'Logical quotient rating', 'coding skills rating', 'hackathons', 'public speaking points',
                'self-learning capability?', 'Extra-courses did', 'Taken inputs from seniors or elders',
                'worked in teams ever?', 'Introvert', 'reading and writing skills', 'memory capability score',
                'B_hard worker', 'B_smart worker', 'A_Management', 'A_Technical', 'Interested subjects_code',
                'Interested Type of Books_code', 'certifications_code', 'workshops_code',
                'Type of company want to settle in?_code', 'interested career area _code'
            ])

            predicted_job_role = model.predict(user_data)[0]

            # Add the prediction to the user's data
            if 'username' in session:
                username = session['username']
                users[username]['predicted_job_role'].append(predicted_job_role)
                save_users(users)

            # Get job details
            job_data = next((item for item in job_roles['job_roles'] if item["role"] == predicted_job_role),
                            {"description": "Description not available.", "responsibilities": "Responsibilities not available."})

            return render_template('result.html', job_role=predicted_job_role, description=job_data['description'],
                                   responsibilities=job_data['responsibilities'], roadmap=job_data.get('roadmap', []))

        except Exception as e:
            return str(e)

@app.route('/new_prediction', methods=['GET', 'POST'])
def new_prediction():
    """Allow users to request a new prediction."""
    if 'username' not in session:
        return redirect(url_for('index'))

    if request.method == 'POST':
        return redirect(url_for('predict'))
    return render_template('new_prediction.html')

@app.route('/view_predictions')
def view_predictions():
    if 'username' not in session:
        return redirect(url_for('index'))
    
    users = load_users()
    username = session['username']
    predicted_roles = users.get(username, {}).get('predicted_job_role', [])
    
    return render_template('view_predictions.html', predicted_roles=predicted_roles)

if __name__ == '__main__':
    app.run(debug=True)
