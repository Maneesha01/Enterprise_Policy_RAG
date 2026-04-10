import os
from dotenv import load_dotenv
from openai import OpenAI
import glob
from pathlib import Path
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import DirectoryLoader,TextLoader
from langchain_chroma import Chroma
from langchain_text_splitters import MarkdownHeaderTextSplitter

load_dotenv(override=True)
embedding_model=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
model="llama3.2:1b"

KNOWLEDGE_BASE=str(Path(__file__).parent.parent/"knowledge-base")
DB_NAME=str(Path(__file__).parent.parent/"vector_db")

def fetch_documents():
    folders=glob.glob(str(Path(KNOWLEDGE_BASE)/"*"))
    documents=[]
    for folder in folders:
        doc_type=os.path.basename(folder)
        loader=DirectoryLoader(folder, glob="**/*.md", loader_cls=TextLoader, loader_kwargs={"encoding":"utf-8"})
        folder_docs=loader.load()
        for doc in folder_docs:
            doc.metadata["doc_type"] = doc_type
            documents.append(doc)
    return documents

def create_chunks(documents):
    headers_to_split_on = [
    ("#", "h1"),
    ("##", "h2")]

    text_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
    chunks = []
    for doc in documents:
        split_docs=text_splitter.split_text(doc.page_content)
        for chunk in split_docs:
            chunk.metadata.update(doc.metadata)
            chunks.append(chunk)
    return chunks

def create_embeddings(chunks):
    if os.path.exists(DB_NAME):
        Chroma(persist_directory=DB_NAME, embedding_function=embedding_model).delete_collection()

    vectorstore = Chroma.from_documents(
        documents=chunks, embedding=embedding_model, persist_directory=DB_NAME
    )

    collection = vectorstore._collection
    count = collection.count()

    sample_embedding = collection.get(limit=1, include=["embeddings"])["embeddings"][0]
    dimensions = len(sample_embedding)
    print(f"There are {count:,} vectors with {dimensions:,} dimensions in the vector store")
    return vectorstore

if __name__ == "__main__":
    documents = fetch_documents()
    chunks = create_chunks(documents)
    create_embeddings(chunks)
    print("Ingestion complete")
