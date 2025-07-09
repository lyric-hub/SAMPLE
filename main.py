from datasets import patients
from patient_embeddings import PatientEmbeddings
from faissindex import PatientEmbedingsIndex, PatientSearch

patient_embedding =PatientEmbeddings(patients)
index=PatientEmbedingsIndex(patient_embedding)
query = "Elderly diabetic patient with kidney complications"
patients_id=PatientSearch(query, index)
print(patients_id)