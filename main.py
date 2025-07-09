from load_model import MODEL , TOKENIZER
from embedding import GetEmbedding
from sklearn.preprocessing import normalize
from datasets import patients
from patient_embeddings import PatientEmbeddings

patient_embedding =PatientEmbeddings(patients)
print(patient_embedding)