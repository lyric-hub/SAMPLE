from load_model import MODEL , TOKENIZER
from embedding import GetEmbedding
from sklearn.preprocessing import normalize
from datasets import patients
from patient_embeddings import PatientEmbeddings
from faissindex import PatientEmbedingsIndex

patient_embedding =PatientEmbeddings(patients)
index=PatientEmbedingsIndex(patient_embedding)