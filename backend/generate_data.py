import pyodbc
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# Connect to SQL Server
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=DESKTOP-GP6TT9B;"
    "DATABASE=HospitalDashboard;"
    "Trusted_Connection=yes;"
)
cur = conn.cursor()

departments = ['Cardiology','Oncology','Orthopedics','Pediatrics','Emergency','General Medicine']
procedures = ['PROC'+str(i).zfill(3) for i in range(1,21)]
insurance_types = ['Private','Government','None']

# Generate 200 Patients
patients = [(fake.name(), random.randint(1,90), random.choice(['Male','Female']), random.choice(insurance_types)) for _ in range(200)]
cur.executemany("INSERT INTO Patients (Name, Age, Gender, InsuranceType) VALUES (?,?,?,?)", patients)
conn.commit()

# Generate Doctors
doctors = [(fake.name(), random.choice(departments)) for _ in range(20)]
cur.executemany("INSERT INTO Doctors (Name, Department) VALUES (?,?)", doctors)
conn.commit()

# Fetch IDs
cur.execute("SELECT PatientID FROM Patients")
patient_ids = [row[0] for row in cur.fetchall()]

cur.execute("SELECT DoctorID, Department FROM Doctors")
doctor_data = cur.fetchall()

# Admissions, Schedules, Billing
admissions=[]
schedules=[]
billing=[]

for pid in patient_ids:
    dept = random.choice(departments)
    procedure = random.choice(procedures)
    admit_date = fake.date_time_between(start_date='-90d', end_date='now')
    discharge_date = admit_date + timedelta(days=random.randint(1,15))
    outcome = random.choice(['Recovered','Improved','Transferred','Deceased'])
    admissions.append((pid, dept, procedure, admit_date, discharge_date, outcome))

    # Assign doctor from same department
    doc_id = random.choice([d[0] for d in doctor_data if d[1]==dept])
    start_time = admit_date + timedelta(hours=random.randint(0,5))
    end_time = start_time + timedelta(minutes=random.randint(15,60))
    schedules.append((doc_id, pid, start_time, end_time))

    # Billing
    total = random.randint(1000,50000)
    insurance = random.randint(0,int(total*0.8))
    paid = total - insurance
    billing.append((pid, total, insurance, paid))

cur.executemany("INSERT INTO Admissions (PatientID, Department, ProcedureCode, AdmissionDate, DischargeDate, Outcome) VALUES (?,?,?,?,?,?)", admissions)
cur.executemany("INSERT INTO Schedules (DoctorID, PatientID, StartTime, EndTime) VALUES (?,?,?,?)", schedules)
cur.executemany("INSERT INTO Billing (PatientID, TotalCost, InsuranceCovered, PaidAmount) VALUES (?,?,?,?)", billing)
conn.commit()
conn.close()

print("Sample data generated successfully!")
