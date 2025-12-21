from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(title="AI-Powered Hospital Scheduler")

# Load trained model
model = joblib.load("scheduler_model.pkl")

# Input schema
class ScheduleRequest(BaseModel):
    patients_before: int
    doctor_experience_years: int
    patient_type: int  # 0 = follow-up, 1 = new
    day_of_week: int   # 0-6
    hour_of_day: int   # 8-17

@app.get("/healthz")
def health_check():
    return {"status": "ok"}

@app.post("/schedule")
def generate_schedule(data: ScheduleRequest):
    features = np.array([[  
        data.patients_before,
        data.doctor_experience_years,
        data.patient_type,
        data.day_of_week,
        data.hour_of_day
    ]])

    predicted_duration = model.predict(features)[0]

    return {
        "predicted_appointment_duration_minutes": round(float(predicted_duration), 1),
        "message": "Optimized appointment duration generated"
    }
