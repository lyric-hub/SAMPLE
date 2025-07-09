from load_model import MODEL , TOKENIZER
import faiss
from embedding import GetEmbedding
from sklearn.preprocessing import normalize
from datasets import patient_data, patients

def PatientEmbedingsIndex(patient_embeddings):
    # Build FAISS index
    dim = patient_embeddings.shape[1]
    index = faiss.IndexFlatIP(dim)  # Inner product for cosine similarity with normalized vectors
    index.add(patient_embeddings)
    return index
def PatientSearch(query,index,num_preferences=3,patients=patients):
    query = "Elderly diabetic patient with kidney complications"
    query_embedding = normalize(GetEmbedding(query, MODEL, TOKENIZER).reshape(1, -1))
    num_preferences = 3  # top-k similar patients
    _, indices = index.search(query_embedding, num_preferences)
    similar_patient_id={}
    for _, idx in enumerate(indices[0]):
        similar_patient_id[int(idx)]=patients[idx]
    return similar_patient_id