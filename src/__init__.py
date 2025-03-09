from .helper import load_documents, split_documents, create_vector_store, create_retrieval_chain

URLs = [
    "https://www.nubosushi.com/",
    "https://www.nubosushi.com/food",
    "https://www.nubosushi.com/drink",
    "https://www.nubosushi.com/contact"
]

documents = load_documents(URLs)
chunks = split_documents(documents)
vector_store = create_vector_store(chunks)
retrieval_chain = create_retrieval_chain(vector_store)

def generate_response(query):
    result = retrieval_chain({"question": query, "return_only_outputs": True})
    return result["answer"]
