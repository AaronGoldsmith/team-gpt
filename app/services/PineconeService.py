from pinecone import Index

class PineconeService:
    def __init__(self, index_name):
        self.index = Index(index_name)

    def upsert_embeddings(self, id, embeddings):
        self.index.upsert([(id, embeddings)])

    def query_embeddings(self, embeddings, top_k):
        return self.index.query(queries=[embeddings], top_k=top_k)
