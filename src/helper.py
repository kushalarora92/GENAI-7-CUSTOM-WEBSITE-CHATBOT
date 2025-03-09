import os

from langchain.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQAWithSourcesChain

import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if OPENAI_API_KEY is None:
    raise ValueError("OPENAI_API_KEY is not set")

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

def load_documents(urls):
    loader = UnstructuredURLLoader(urls=urls)
    documents = loader.load()
    return documents

def split_documents(documents):
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_documents(documents)
    return chunks

def create_vector_store(chunks):
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_documents(chunks, embeddings)
    return vector_store

def create_retrieval_chain(vector_store):
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.5)
    retriever = vector_store.as_retriever()
    chain = RetrievalQAWithSourcesChain.from_llm(
        llm=llm,
        retriever=retriever
    )
    return chain
