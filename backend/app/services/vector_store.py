import faiss
import numpy as np


class VectorStore:
    def __init__(self, dim: int = 384):
        self.index = faiss.IndexFlatL2(dim)
        self.texts = []

    def add(self, embeddings, texts):
        self.index.add(np.array(embeddings).astype("float32"))
        self.texts.extend(texts)

    def search(self, query_embedding, k=3):
        distances, indices = self.index.search(
            np.array([query_embedding]).astype("float32"), k
        )
        print(f"Texts are: {self.texts}")

        results = []
        for i in indices[0]:
            if 0 <= i < len(self.texts):
                results.append(self.texts[i])

        return results
