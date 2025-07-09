
import json
with open("patients.json") as f:
    patient_data = json.load(f)
patients = [p["text"] for p in patient_data]