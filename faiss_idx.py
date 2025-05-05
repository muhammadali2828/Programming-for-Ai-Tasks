import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from restaurant_data import restaurant_data

model = SentenceTransformer('all-MiniLM-L6-v2')

embeddings = model.encode(restaurant_data, convert_to_numpy=True)

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

def get_answer(user_query):
    query_embedding = model.encode([user_query])
    D, I = index.search(query_embedding, k=1)
    if D[0][0] < 1.0: 
        return restaurant_data[I[0][0]]
    else:
        return "Sorry, I could not find relevant info. Please ask something else about the restaurant."
