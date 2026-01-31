🏥 Hospital Resouce Utilization & Patients Outcomes Dashboard:
This project demonstrates an end-to-end hospital operations analytics solution using **FastAPI** for backend APIs and **Power BI** for interactive dashboards.
The goal is to show how hospital operational data can be exposed via APIs and analyzed through dashboards for better decision-making.

🚀 Live Deployment:
- API Base URL: https://hospital-api-m6j9.onrender.com  
- Swagger Docs: https://hospital-api-m6j9.onrender.com/docs  

🛠️ Tech Stack:
- Backend API: FastAPI
- Language: Python
- API Documentation: Swagger (OpenAPI)
- Deployment: Render
- Database (Analytics Source): SQL Server
- Visualization: Power BI

📡 FastAPI Backend Overview:
The FastAPI service exposes core hospital operational data through REST APIs.
Available Endpoints:
- `GET /` – Health check
- `GET /patients` – Patient details
- `GET /admissions` – Admission details

These endpoints demonstrate how hospital data can be securely exposed for integration and reporting purposes.
> Note: For demo purposes, the API returns a limited sample dataset.  
> The Power BI dashboards are built using a larger analytical dataset stored in SQL Server.

📊 Power BI Dashboards:

Power BI is used to build interactive dashboards that analyze hospital performance, patient demographics, and departmental efficiency.

The dashboards use multiple hospital tables such as:
- Patients
- Admissions
- Billing
- Doctors
- Schedules
- Outcomes

This separation reflects a real-world setup where APIs handle operational access, while BI tools consume analytical datasets.

1️⃣ Hospital Operational Overview (Executive Dashboard):
This dashboard provides a high-level view of overall hospital performance.
Key Metrics & Visuals:
- Total Admissions (Card)
- Average Cost per Patient (Card)
- Monthly Admission Trend (Line Chart)
- Monthly Treatment Cost Trend (Line Chart)
- Patient Outcomes (Donut Chart)
- Emergency vs Scheduled Admissions (Donut Chart)

Slicers:
- Department
- Gender
- Insurance Type
- Admission Date

2️⃣ Department Operations & Bottleneck Analysis:
This dashboard focuses on departmental efficiency and identifying operational bottlenecks.

Key Metrics & Visuals:
- Admissions by Department (Bar Chart)
- Average Length of Stay by Department (Clustered Bar Chart)
- Emergency vs Scheduled Cases by Department (Stacked Bar Chart)
- Readmissions by Department (Stacked Bar Chart)
- Peak Admission Hours (Stacked Column Chart)

Slicers:
- Department
- Age Group
- Gender
- Admission Date

3️⃣ Patient Demographics & Outcomes:
This dashboard analyzes patient characteristics and treatment outcomes.

Key Metrics & Visuals:
- Total Patients (Card)
- Average Patient Age (Card)
- Recovery Percentage (Card)
- Admissions by Age Group (Stacked Column Chart)
- Gender-wise Admissions (Donut Chart)
- Patient Outcomes by Gender (Stacked Bar Chart)
- Outcome Distribution by Age Group (100% Stacked Column Chart)

Slicers:
- Admission Date
- Gender
- Age Group
- Department

🎯 Project Outcome:
- Demonstrates API-based hospital data exposure using FastAPI
- Provides interactive Power BI dashboards for operational insights
- Helps visualize hospital performance, patient trends, and departmental efficiency
- Shows a scalable analytics architecture suitable for real-world healthcare systems

📁 Repository Contents:
- FastAPI application code
- API deployment configuration
- Power BI dashboard files
- Project documentation


📌 Author:

Hemavalli Mannemuddu
