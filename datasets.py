import json
import os
BASE_DIR = os.path.dirname(__file__)
json_path = os.path.join(BASE_DIR, "patients.json")
with open(json_path) as f:
    patient_data = json.load(f)
patients = [p["text"] for p in patient_data]