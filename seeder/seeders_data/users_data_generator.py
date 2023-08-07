import secrets
import pandas

first_names = [
    [
        'Abd Alrahman',
        'Abd Alghani',
        'Abd Allah',
        'Ahmad',
        'Mohammad',
        'Mahmoud',
        'Saeed',
        'Suliman',
        'Osama',
        'Ismaiel',
        'Mustafa',
        'Moayyad',
        'Kamel',
        'Fadi',
        'Ahmad',
        'Mazen',
        'Anas',
        'Ammar',
        'Khaled',
        'Issam',
        'Bilal',
        'Munzer',
    ],
    [
        'Batoul',
        'Sara',
        'Sedra',
        'Nour',
        'Fatema',
        'Zainab',
        'Maya',
        'Mariam',
        'Aya',
        'Layan',
        'Raghad',
        'Asmaa',
        'Judy',
        'haifaa',
        'Hiba',
        'Ghofran',
        'Lilian',
        'Laila',
        'Reem',
        'Sali',
    ],
]

last_names = [
    'Abd Alrahim',
    'Abd Almalek',
    'Abd Almajeed',
    'Ahmad',
    'Mohammad',
    'Mahmoud',
    'Koja',
    'Halabi',
    'Horani',
    'Kurdi',
    'Awad',
    'Turkman',
    'Homsi',
    'Shamma',
    'Ibrahim',
    'Haj',
    'Habib',
    'Saleh',
    'Ali',
    'AlShami',
    'AlHelo',
    'AlMasri',
    'Zarefa',
]

cities_data = [
    ('Damascus', 'Syria'),
    ('Homs', 'Syria'),
    ('Aleppo', 'Syria'),
]

specializations_names = [
    'Cardiology',
    'Ophthalmology',
    'Gastroenterology',
    'Neurology',
    'Gynecology',
    'Orthopedics',
    'Pediatrics',
    'Psychiatry',
    'General',
]

chronic_disease = [
    'Diabetes',
    'Hypertension',
    'Arthritis',
    'Asthma',
    'Cancer',
    'Heart Disease',
    'Chronic Kidney Disease',
    'Obesity',
    'Alzheimers Disease',
    'Osteoporosis',
    'Chronic Obstructive Pulmonary Disease (COPD)',
    'Parkinsons Disease',
    'Multiple Sclerosis',
    'Crohns Disease',
    'Rheumatoid Arthritis',
    'Epilepsy',
    'Lupus',
    'Fibromyalgia',
    'Chronic Migraines',
    'HIV/AIDS'
]


genetic_diseases = [
    'Cystic Fibrosis',
    'Huntingtons Disease',
    'Sickle Cell Anemia',
    'Down Syndrome',
    'Muscular Dystrophy',
    'Color Blindness',
    'Tay-Sachs Disease',
    'Fragile X Syndrome',
    'Polycystic Kidney Disease',
    'Marfan Syndrome',
    'Hemophilia',
    'Phenylketonuria (PKU)',
    'Spinal Muscular Atrophy (SMA)',
    'Duchenne Muscular Dystrophy',
    'Turner Syndrome',
    'Klinefelter Syndrome',
    'Williams Syndrome',
    'Prader-Willi Syndrome',
    'Rett Syndrome',
    'Neurofibromatosis'
]


other_infos = [
    'Allergies: Penicillin, Peanuts',
    'Medications: Lisinopril, Metformin',
    'Previous Surgeries: Appendectomy (2015), Tonsillectomy (2008)',
    'Family History: Diabetes, Heart Disease',
    'Vaccination History: COVID-19 (Pfizer, 2 doses)',
    'Allergies: Shellfish',
    'Medications: Levothyroxine',
    'Previous Surgeries: Knee Replacement (2019)',
    'Family History: Cancer, Alzheimers Disease',
    'Vaccination History: Influenza (Yearly)',
    'Allergies: None',
    'Medications: None',
    'Previous Surgeries: None',
    'Family History: Hypertension, Stroke',
    'Vaccination History: Tetanus-Diphtheria (10 years ago)',
    'Allergies: Dust Mites, Pollen',
    'Medications: Sertraline',
    'Previous Surgeries: Gallbladder Removal (2020)',
    'Family History: Asthma, Allergies',
    'Vaccination History: None'
]

# ------------------------------------------------------------------

def get_specialization_name():
    length = len(specializations_names)
    return specializations_names[secrets.randbelow(length)]

def get_city_data():
    length = len(cities_data)
    return cities_data[secrets.randbelow(length)]

def get_chronic_disease():
    length = len(chronic_disease)
    return chronic_disease[secrets.randbelow(length)]

def get_genetic_disease():
    length = len(genetic_diseases)
    return genetic_diseases[secrets.randbelow(length)]

def get_other_infos():
    length = len(other_infos)
    return other_infos[secrets.randbelow(length)]

# ------------------------------------------------------------------

def get_first_name(gender):
    valid_choices = first_names[gender]
    length = len(valid_choices)
    return valid_choices[secrets.randbelow(length)]

def get_last_name():
    length = len(last_names)
    return last_names[secrets.randbelow(length)]

# ------------------------------------------------------------------

def get_email(first_name, last_name, idx):
    return f'{first_name}{last_name}{idx}@gmail.com'.replace(" ", "")

def get_phone_number():
    return f'09{secrets.randbelow(100000000)}'

def get_birth_date():
    return f'{secrets.randbelow(16)+1980}-{secrets.randbelow(12)+1}-{secrets.randbelow(28)+1}'

# ------------------------------------------------------------------

def get_weight():
    return secrets.randbelow(71)+50

def get_length():
    return secrets.randbelow(21)+160

def get_blood_type():
    return secrets.randbelow(8)

def get_gender():
    return secrets.randbelow(2)

def get_available_for_meeting():
    return secrets.randbelow(2)

def get_password():
    return '123123'

# ------------------------------------------------------------------

superuser_data = {}
superuser_data['email'] = [get_email('suliman', '', ''), get_email('saeed', '', '')]
superuser_data['password'] = [get_password(), get_password()]
superuser_file = pandas.DataFrame(superuser_data)
superuser_file.to_csv('superuser.csv', index=False)

# ------------------------------------------------------------------

patient_data = {}
patient_data['gender'] = []
patient_data['first_name'] = []
patient_data['last_name'] = []
patient_data['email'] = []
patient_data['password'] = []
patient_data['phone_number'] = []
patient_data['birth_date'] = []
patient_data['blood_type'] = []
patient_data['length'] = []
patient_data['weight'] = []
patient_data['chronic_disease'] = []
patient_data['genetic_disease'] = []
patient_data['other_info'] = []
for i in range(100):
    gender = get_gender()
    first_name = get_first_name(gender)
    last_name = get_last_name()
    email = get_email(first_name, last_name, i+1)
    patient_data['gender'].append(gender)
    patient_data['first_name'].append(first_name)
    patient_data['last_name'].append(last_name)
    patient_data['email'].append(email)
    patient_data['password'].append(get_password())
    patient_data['phone_number'].append(get_phone_number())
    patient_data['birth_date'].append(get_birth_date())
    patient_data['blood_type'].append(get_blood_type())
    patient_data['length'].append(get_length())
    patient_data['weight'].append(get_weight())
    patient_data['chronic_disease'].append(get_chronic_disease())
    patient_data['genetic_disease'].append(get_genetic_disease())
    patient_data['other_info'].append(get_other_infos())
patient_file = pandas.DataFrame(patient_data)
patient_file.to_csv('patient.csv', index=False)

doctor_data = {}
doctor_data['gender'] = []
doctor_data['first_name'] = []
doctor_data['last_name'] = []
doctor_data['email'] = []
doctor_data['password'] = []
doctor_data['phone_number'] = []
doctor_data['birth_date'] = []
doctor_data['available_for_meeting'] = []
for i in range(100):
    gender = get_gender()
    first_name = get_first_name(gender)
    last_name = get_last_name()
    email = get_email(first_name, last_name, i+101)
    doctor_data['gender'].append(gender)
    doctor_data['first_name'].append(first_name)
    doctor_data['last_name'].append(last_name)
    doctor_data['email'].append(email)
    doctor_data['password'].append(get_password())
    doctor_data['phone_number'].append(get_phone_number())
    doctor_data['birth_date'].append(get_birth_date())
    doctor_data['available_for_meeting'].append(get_available_for_meeting())
doctor_file = pandas.DataFrame(doctor_data)
doctor_file.to_csv('doctor.csv', index=False)