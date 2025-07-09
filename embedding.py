import numpy
import torch
def GetEmbedding(text,model,tokenizer):
    with torch.no_grad():
        tokens = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
        output = model(**tokens)
        embeddings = output.last_hidden_state.mean(dim=1)  # Mean pooling
        return embeddings[0].numpy()