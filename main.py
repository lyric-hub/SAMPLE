from datasets import patients
from patient_embeddings import PatientEmbeddings
from faissindex import PatientEmbedingsIndex, PatientSearch

def PatientList(query):
    query = query
    patient_embedding = PatientEmbeddings(patients)
    index = PatientEmbedingsIndex(patient_embedding)
    patients_id = PatientSearch(query, index)
    return patients_id