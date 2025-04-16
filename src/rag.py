# rag.py
import os
import faiss
import pickle
from sentence_transformers import SentenceTransformer
import numpy as np

EMBED_MODEL_NAME = "all-MiniLM-L6-v2"  # Used for retrieval, not for generation
DB_PATH = "vectorstore/faiss_index"

class RAGRetriever:
    def __init__(self):
        self.embedder = SentenceTransformer(EMBED_MODEL_NAME)
        self.index = None
        self.text_chunks = []

    def build_index(self, chunks):
        self.text_chunks = chunks
        embeddings = self.embedder.encode(chunks, convert_to_numpy=True)
        dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(embeddings)

        os.makedirs("vectorstore", exist_ok=True)
        faiss.write_index(self.index, f"{DB_PATH}.bin")
        with open(f"{DB_PATH}_texts.pkl", "wb") as f:
            pickle.dump(chunks, f)

        print(f"[INFO] FAISS index created with {len(chunks)} chunks.")

    def load_index(self):
        if not os.path.exists(f"{DB_PATH}.bin"):
            raise FileNotFoundError("[ERROR] Vector index not found. Please build it first.")

        self.index = faiss.read_index(f"{DB_PATH}.bin")
        with open(f"{DB_PATH}_texts.pkl", "rb") as f:
            self.text_chunks = pickle.load(f)

    def retrieve(self, query, top_k=3):
        query_embedding = self.embedder.encode([query], convert_to_numpy=True)
        distances, indices = self.index.search(query_embedding, top_k)
        return [self.text_chunks[i] for i in indices[0] if i < len(self.text_chunks)]