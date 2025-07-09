import faiss

def PatientEmbedingsIndex(patient_embeddings):
    # Build FAISS index
    dim = patient_embeddings.shape[1]
    index = faiss.IndexFlatIP(dim)  # Inner product for cosine similarity with normalized vectors
    index.add(patient_embeddings)
    return index