import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from restaurant_data import restaurant_data

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
print("Model loaded:", model)

embeddings = model.encode(restaurant_data, convert_to_numpy=True)
print("Embedding shape:", embeddings.shape)

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

def get_answer(user_query):
    query_embedding = model.encode([user_query], convert_to_numpy=True)
    D, I = index.search(query_embedding, k=1)
    
    print(f"Distance: {D[0][0]:.4f}")
    print(f"Matched Text: {restaurant_data[I[0][0]]}")
    
    return restaurant_data[I[0][0]]
