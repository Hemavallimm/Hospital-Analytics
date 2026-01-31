-- Create HospitalDashboard database
CREATE DATABASE HospitalDashboard;
GO
USE HospitalDashboard;
GO

-- Patients
CREATE TABLE Patients (
    PatientID INT IDENTITY(1,1) PRIMARY KEY,
    Name NVARCHAR(100),
    Age INT,
    Gender NVARCHAR(10),
    InsuranceType NVARCHAR(50)
);

-- Doctors
CREATE TABLE Doctors (
    DoctorID INT IDENTITY(1,1) PRIMARY KEY,
    Name NVARCHAR(100),
    Department NVARCHAR(50)
);

-- Admissions
CREATE TABLE Admissions (
    AdmissionID INT IDENTITY(1,1) PRIMARY KEY,
    PatientID INT FOREIGN KEY REFERENCES Patients(PatientID),
    Department NVARCHAR(50),
    ProcedureCode NVARCHAR(20),
    AdmissionDate DATETIME,
    DischargeDate DATETIME,
    Outcome NVARCHAR(50)
);

-- Doctor Schedules
CREATE TABLE Schedules (
    ScheduleID INT IDENTITY(1,1) PRIMARY KEY,
    DoctorID INT FOREIGN KEY REFERENCES Doctors(DoctorID),
    PatientID INT FOREIGN KEY REFERENCES Patients(PatientID),
    StartTime DATETIME,
    EndTime DATETIME
);

-- Billing
CREATE TABLE Billing (
    BillID INT IDENTITY(1,1) PRIMARY KEY,
    PatientID INT FOREIGN KEY REFERENCES Patients(PatientID),
    TotalCost DECIMAL(10,2),
    InsuranceCovered DECIMAL(10,2),
    PaidAmount DECIMAL(10,2)
);
GO
SELECT COUNT(*) FROM Patients;
SELECT COUNT(*) FROM Doctors;
SELECT COUNT(*) FROM Admissions;
SELECT COUNT(*) FROM Schedules;
SELECT COUNT(*) FROM Billing;