
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load the dataset
df = pd.read_csv('mldata.csv')

# Columns that need encoding
categorical_col = df[['self-learning capability?', 'Extra-courses did', 'reading and writing skills', 
                      'memory capability score', 'Taken inputs from seniors or elders', 'Management or Technical', 
                      'hard/smart worker', 'worked in teams ever?', 'Introvert', 'interested career area ']]

# Encoding binary categorical columns
binary_cols = ["self-learning capability?", "Extra-courses did", "Taken inputs from seniors or elders", "worked in teams ever?", "Introvert"]
for col in binary_cols:
    df[col] = df[col].map({"yes": 1, "no": 0})

# Encoding ordinal categorical columns
ordinal_cols = ["reading and writing skills", "memory capability score"]
ordinal_mapping = {"poor": 0, "medium": 1, "excellent": 2}
for col in ordinal_cols:
    df[col] = df[col].map(ordinal_mapping)

# Encoding remaining categorical columns as codes
category_cols = ['certifications', 'workshops', 'Interested subjects', 'interested career area ', 
                 'Type of company want to settle in?', 'Interested Type of Books']
for col in category_cols:
    df[col] = df[col].astype('category')
    df[col + "_code"] = df[col].cat.codes

# Print the list of categorical features
print("\n\nList of Categorical features: \n", df.select_dtypes(include=['object']).columns.tolist())

# Create dummy variables for specific columns
df = pd.get_dummies(df, columns=["Management or Technical", "hard/smart worker"], prefix=["A", "B"])

# Select relevant features
feed = df[['Logical quotient rating', 'coding skills rating', 'hackathons', 'public speaking points', 
           'self-learning capability?', 'Extra-courses did', 'Taken inputs from seniors or elders', 
           'worked in teams ever?', 'Introvert', 'reading and writing skills', 'memory capability score',  
           'B_hard worker', 'B_smart worker', 'A_Management', 'A_Technical', 'Interested subjects_code', 
           'Interested Type of Books_code', 'certifications_code', 'workshops_code', 
           'Type of company want to settle in?_code', 'interested career area _code', 'Suggested Job Role']]

# Independent variables
df_train_x = feed.drop('Suggested Job Role', axis=1)

# Target variable
df_train_y = feed['Suggested Job Role']

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(df_train_x, df_train_y, test_size=0.20, random_state=42)

# Train the Random Forest Classifier
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(x_train, y_train)

# Predict on the test set
y_pred = rf.predict(x_test)

# Print the accuracy score
print("\n\nAccuracy Score: ", accuracy_score(y_test, y_pred))

# New user data (example)
userdata = pd.DataFrame([[
    7,  # Logical quotient rating
    6,  # coding skills rating
    6,  # hackathon attended
    8,  # public speaking points
    1,  # self-learning capability? (yes -> 1)
    0,  # Extra-courses did (no -> 0)
    1,  # Taken inputs from seniors or elders (yes -> 1)
    1,  # worked in teams ever? (yes -> 1)
    0,  # Introvert (no -> 0)
    1,  # reading and writing skills (medium -> 1)
    2,  # memory capability score (excellent -> 2)
    1,  # B_hard worker (yes -> 1)
    0,  # B_smart worker (no -> 0)
    1,  # A_Management (yes -> 1)
    0,  # A_Technical (no -> 0)
    3,  # Interested subjects_code (example)
    2,  # Interested Type of Books_code (example)
    5,  # certifications_code (example)
    4,  # workshops_code (example)
    1,  # Type of company want to settle in?_code (example)
    2   # interested career area _code (example)
]], columns=df_train_x.columns)

# Logical quotient rating: Typically a numerical score, assume range 1-10.
# coding skills rating: Typically a numerical score, assume range 1-10.
# hackathons: Number of hackathons participated in, assume range 0-10.
# public speaking points: Typically a numerical score, assume range 1-10.
# self-learning capability?: Binary, 1 for "yes" and 0 for "no".
# Extra-courses did: Binary, 1 for "yes" and 0 for "no".
# Taken inputs from seniors or elders: Binary, 1 for "yes" and 0 for "no".
# worked in teams ever?: Binary, 1 for "yes" and 0 for "no".
# Introvert: Binary, 1 for "yes" and 0 for "no".
# reading and writing skills: Ordinal, 0 for "poor", 1 for "medium", and 2 for "excellent".
# memory capability score: Ordinal, 0 for "poor", 1 for "medium", and 2 for "excellent".
# B_hard worker: Binary, 1 for "yes" and 0 for "no".
# B_smart worker: Binary, 1 for "yes" and 0 for "no".
# A_Management: Binary, 1 for "Management" and 0 for "Technical".
# A_Technical: Binary, 1 for "Technical" and 0 for "Management".
# Interested subjects_code: Categorical, assuming range 0-n where n is the number of unique subjects minus one.
# Interested Type of Books_code: Categorical, assuming range 0-n where n is the number of unique book types minus one.
# certifications_code: Categorical, assuming range 0-n where n is the number of unique certifications minus one.
# workshops_code: Categorical, assuming range 0-n where n is the number of unique workshops minus one.
# Type of company want to settle in?_code: Categorical, assuming range 0-n where n is the number of unique company types minus one.
# interested career area _code: Categorical, assuming range 0-n where n is the number of unique career areas minus one.


# Predict the job role for new user data
pred = rf.predict(userdata)
print("\n\nPredicted Job Role: ", pred)

# Save the model as a pickle file
pickle.dump(rf, open('model.pkl', 'wb'))

