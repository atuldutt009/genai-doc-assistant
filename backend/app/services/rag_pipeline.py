from app.services.embeddings import EmbeddingService
from app.services.vector_store import VectorStore
from transformers import pipeline

class RAGPipeline:
    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.vector_store = VectorStore()
        self.generator = pipeline(
            "text-generation",
            model="distilgpt2"
        )

    def add_documents(self, texts: list[str]):
        embeddings = self.embedding_service.embed_documents(texts)
        self.vector_store.add(embeddings, texts)

    def query(self, question: str):
        query_embedding = self.embedding_service.embed_query(question)
        context_chunks = self.vector_store.search(query_embedding)

        context = "\n".join(context_chunks)

        prompt = f"""
        Answer the question based on the context below.

        Context:
        {context}

        Question:
        {question}

        Answer:
        """

        result = self.generator(prompt, max_length=200, num_return_sequences=1)

        return result[0]["generated_text"]
