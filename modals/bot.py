import pandas as pd
import numpy as np
import re
from sentence_transformers import SentenceTransformer
import faiss

def clean_text(text):
    text=text.lower()
    text=re.sub(r'[^a-zA-z0-9\s]',' ',text)
    text=re.sub(r'\s+',' ',text)
    return text

# dataset=pd.read_csv("../data/processed_automotive_faults.csv")
# embeddings=np.load("chunk.npy")
# faiss_index=faiss.read_index("chunk_faiss_index.index")
dataset=pd.read_csv("./data/processed_automotive_faults.csv")
embeddings=np.load("./modals/chunk.npy")
faiss_index=faiss.read_index("./modals/chunk_faiss_index.index")
model=SentenceTransformer('all-MiniLM-L6-v2')

def get_similar_query(query,model=model,faiss_index=faiss_index,count=2):
    query=clean_text(query)
    query_embedding=model.encode([query])
    distance,indices=faiss_index.search(query_embedding,count)
    results=[]
    for i in range(count):
        results.append(dataset["chunk"].iloc[indices[0][i]])
    if not results:
        results.append("I'm sorry, I could not find a solution based on your input. Please consult a professional mechanic.")
    return results