from fastapi import FastAPI

app = FastAPI(title="Hospital Operations API")

@app.get("/")
def home():
    return {
        "status": "running",
        "note": "Deployed API demo. Production DB is on-premise SQL Server."
    }

@app.get("/patients")
def patients():
    return [
        {"PatientID": 1, "Age": 45, "Gender": "Male", "Department": "Cardiology"},
        {"PatientID": 2, "Age": 32, "Gender": "Female", "Department": "Emergency"}
    ]

@app.get("/admissions")
def admissions():
    return [
        {"AdmissionID": 101, "Department": "Cardiology", "LengthOfStay": 4},
        {"AdmissionID": 102, "Department": "Emergency", "LengthOfStay": 2}
    ]
