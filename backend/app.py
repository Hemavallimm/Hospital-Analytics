from fastapi import FastAPI
import pyodbc
import pandas as pd

app = FastAPI()
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=DESKTOP-GP6TT9B;"
    "DATABASE=HospitalDashboard;"
    "Trusted_Connection=yes;"
)

@app.get("/patients")
def get_patients():
    df = pd.read_sql("SELECT * FROM Patients", conn)
    return df.to_dict(orient="records")

@app.get("/admissions")
def get_admissions():
    df = pd.read_sql("SELECT * FROM Admissions", conn)
    return df.to_dict(orient="records")

@app.get("/doctors")
def get_doctors():
    df = pd.read_sql("SELECT * FROM Doctors", conn)
    return df.to_dict(orient="records")

@app.get("/schedules")
def get_schedules():
    df = pd.read_sql("SELECT * FROM Schedules", conn)
    return df.to_dict(orient="records")

@app.get("/billing")
def get_billing():
    df = pd.read_sql("SELECT * FROM Billing", conn)
    return df.to_dict(orient="records")
