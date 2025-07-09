from load_model import MODEL , TOKENIZER
from embedding import GetEmbedding
from sklearn.preprocessing import normalize
import numpy 

def PatientEmbeddings(patients):
    patient_embeddings = numpy.vstack([GetEmbedding(p, MODEL, TOKENIZER) for p in patients])
    patient_embeddings = normalize(patient_embeddings)
    return patient_embeddings
