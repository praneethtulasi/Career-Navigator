import csv
import random

# Define the file path
file_path = 'mldata.csv'

# Define choices
books_choices = [
    'Guide', 'Health', 'Horror', 'Self help', 'Biographies', 'Science fiction', 'Fantasy',
    'History', 'Childrens', 'Autobiographies', 'Science', 'Dictionaries', 'Journals', 'Drama',
    'Mystery', 'Travel', 'Poetry', 'Action and Adventure', 'Cookbooks', 'Comics', 'Art', 'Series',
    'Math'
]

career_areas_choices = [
    'AI Research', 'Big Data Analytics', 'Blockchain Development', 'Cloud Computing',
    'Cybersecurity', 'Data Science', 'DevOps', 'IoT Solutions', 'Machine Learning',
    'Quantum Computing', 'Robotics', 'Software Development', 'Systems Analysis', 'Web Development'
]

certifications_choices = [
    'devops certified engineer', 'blockchain developer',
    'ai for healthcare', 'robotics process automation (RPA)', 'ar/vr development', 'Data Science',
    'Cybersecurity', 'Machine Learning', 'Product Management Professional (PMP)', 'Certified ERP Consultant',
    'Certified AI Engineer', 'Robotics Engineering Certification', 'Quantum Computing Certification'
]

workshops_choices = [
    'IoT Solutions', 'Blockchain Technologies', 'Big Data Analytics',
    'AI for Healthcare', 'Robotic Process Automation (RPA)', 'Data Science', 'Cybersecurity',
    'Machine Learning', 'Product Management', 'ERP Systems', 'AI Engineering', 'Robotics Engineering',
    'Quantum Computing'
]

company_choices = [
    'Service Based', 'Web Services', 'BPA', 'Testing and Maintainance Services', 'Product based',
    'Finance', 'Cloud Services', 'product development', 'Sales and Marketing', 'SAaS services',
    'Blockchain Technology Firms', 'AI Research Labs', 'Big Data Companies',
    'IoT Startups', 'Cybersecurity Firms', 'Software Development Firms', 'Systems Analysis Firms', 'Data Science Firms'
]

def generate_rand_row():
    lqr = random.randint(1, 10)
    hack = random.randint(0, 10)
    csr = random.randint(1, 10)
    psp = random.randint(1, 10)
    slc = random.choice(['yes', 'no'])
    ecd = random.choice(['yes', 'no'])
    cert = random.choice(certifications_choices)
    wc = 'Cloud Computing'
    cas = 'Cloud Computing'
    cc = 'developer'
    job_role = 'Cloud Solutions Architect'
    mt = 'Technical'
    if cert == 'devops certified engineer':
        wc = 'DevOps'
        cas = 'DevOps'
        cc = random.choice(['developer', 'security', 'Web Services', 'Product based', 'IoT Startups', 'Systems Analysis Firms', 'Data Science Firms', 'Testing and Maintainance Services'])
        job_role = 'DevOps Engineer'
        mt = 'Technical'
    elif cert == 'blockchain developer':
        wc = 'Blockchain Technologies'
        cas = 'Blockchain Development'
        cc = random.choice(['Blockchain Technology Firms', 'developer', 'security', 'Product based', 'Big Data Companies', 'Systems Analysis Firms', 'Data Science Firms'])
        job_role = 'Blockchain Developer'
        mt = 'Technical'
    elif cert == 'cloud solutions architect':
        wc = 'Cloud Computing'
        cas = 'Cloud Computing'
        cc = random.choice(['Cloud Services', 'Web Services', 'developer', 'security', 'Product based', 'IoT Startups', 'AI Research Labs', 'Systems Analysis Firms', 'Data Science Firms', 'Cybersecurity Firms'])
        job_role = 'Cloud Solutions Architect'
        mt = 'Technical'
    elif cert == 'ai for healthcare':
        wc = 'AI for Healthcare'
        cas = 'AI Research'
        cc = random.choice(['AI Research Labs', 'Web Services', 'developer', 'security', 'Product based', 'Big Data Companies'])
        job_role = 'AI Specialist'
        mt = 'Technical'
    elif cert == 'robotics process automation (RPA)':
        wc = 'Robotic Process Automation (RPA)'
        cas = 'Robotics'
        cc = random.choice(['Web Services', 'developer', 'security', 'Product based', 'Big Data Companies', 'IoT Startups','Cybersecurity Firms','AI Research Labs', 'Data Science Firms'])
        job_role = 'IT Project Manager'
        mt = 'Management'
    elif cert == 'ar/vr development':
        wc = 'AR/VR Development'
        cas = random.choice(['Software Development', 'Web Development'])
        cc = random.choice(['Web Services', 'developer', 'Product based', 'Big Data Companies', 'Sales and Marketing', 'IoT Startups'])
        job_role = 'Systems Analyst'
        mt = 'Technical'
    elif cert == 'Data Science':
        wc = random.choice(['Data Science', 'Machine Learning', 'AI'])
        cas = random.choice(['Data Science', 'Machine Learning', 'AI'])
        cc = random.choice(['Data Science Firms', 'Web Services', 'developer', 'security', 'Product based', 'Big Data Companies', 'IoT Startups', 'AI Research Labs'])
        job_role = random.choice(['Data Scientist', 'Big Data Engineer'])
        mt = 'Technical'
    elif cert == 'Cybersecurity':
        wc = random.choice(['Cybersecurity', 'Machine Learning', 'AI'])
        cas = random.choice(['Cybersecurity', 'Machine Learning', 'AI'])
        cc = random.choice(['Cybersecurity Firms', 'Web Services', 'developer', 'security', 'Product based', 'Big Data Companies', 'IoT Startups', 'AI Research Labs'])
        job_role = 'Cybersecurity Analyst'
        mt = 'Technical'
    elif cert == 'Machine Learning':
        wc = random.choice(['Machine Learning', 'AI'])
        cas = random.choice(['Machine Learning', 'AI'])
        cc = random.choice(['Web Services', 'developer', 'security', 'Product based', 'Big Data Companies', 'IoT Startups', 'AI Research Labs', 'Data Science Firms'])
        job_role = 'Machine Learning Engineer'
        mt = 'Technical'
    elif cert == 'Product Management Professional (PMP)':
        wc = 'Product Management'
        cas = 'Product Management'
        cc = random.choice(['Service Based', 'Product based', 'Sales and Marketing', 'Finance'])
        job_role = 'Product Manager'
        mt = 'Management'
    elif cert == 'Certified ERP Consultant':
        wc = 'ERP Systems'
        cas = 'ERP'
        cc = random.choice(['Service Based', 'Product based', 'Sales and Marketing', 'Finance'])
        job_role = 'ERP Consultant'
        mt = 'Management'
    elif cert == 'AI Engineer':
        wc = 'AI Engineering'
        cas = 'AI'
        cc = random.choice(['AI Research Labs', 'Big Data Companies', 'IoT Startups', 'Cloud Services'])
        job_role = 'AI Engineer'
        mt = 'Technical'
    elif cert == 'Quantum Computing':
        wc = 'Quantum Computing'
        cas = 'Quantum Computing'
        cc = random.choice(['Quantum Computing Firms', 'AI Research Labs', 'Big Data Companies', 'IoT Startups', 'Cloud Services'])
        job_role = 'Quantum Computing Scientist'
        mt = 'Technical'
    
    rws = random.choice(['excellent', 'very good', 'good', 'medium'])
    mcs = random.choice(['excellent', 'very good', 'good', 'medium'])
    isub = random.choice(['cloud computing', 'developer', 'security'])
    seniors = random.choice(['yes', 'no'])
    book = random.choice(books_choices)
    worker = random.choice(['smart worker', 'hard worker'])
    team = random.choice(['yes', 'no'])
    intro = random.choice(['yes', 'no'])
    
    return [
        lqr, hack, csr, psp, slc, ecd, cert, wc, rws, mcs, isub, cas, cc, seniors, book, mt, worker, team, intro, job_role
    ]

# Open the CSV file in append mode
with open(file_path, mode='a', newline='') as file:
    writer = csv.writer(file)
    
    # Generate and write 50 new rows
    for _ in range(500):
        writer.writerow(generate_rand_row())

print("200 new rows have been added to the CSV file.")

