import os
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter 
from typing import List
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
import chromadb 
from langchain_chroma import Chroma



# Extraction text from PDF files
def load_pdf_files(data):
    loader = DirectoryLoader(
        data,
        glob="*.pdf",
        loader_cls=PyPDFLoader
    )
    
    documents = loader.load()
    return documents


def filter_to_minimal_docs(docs: List[Document]) -> List[Document]:
    minimal_docs: List[Document] = []
    for doc in docs:
        src = doc.metadata.get("source")
        minimal_docs.append(
            Document(
                page_content=doc.page_content,
                metadata={
                    "source": doc.metadata.get("source"),
                    "pages": doc.metadata.get("page"), 
                    "book": "Gale Encyclopedia of Medicine edition 2"
                }
            )
        )
    return minimal_docs


# Chunking the documents .
def text_split(minimal_docs):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separators=["\n\n", "\n", " ", ""]
    )
    texts_chunk = text_splitter.split_documents(minimal_docs)
    return texts_chunk


# Downloading the embeddings from HuggingFace

def download_embeddings():
    model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    embeddings = HuggingFaceEmbeddings(
        model_name=model_name
    )
    return embeddings
embeddings = download_embeddings()