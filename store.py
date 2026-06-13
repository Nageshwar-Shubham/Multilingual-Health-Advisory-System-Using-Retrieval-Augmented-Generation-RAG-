import os
import chroma_db
from dotenv import load_dotenv
from src.utils import load_pdf_files, filter_to_minimal_docs, text_split, download_embeddings
from langchain_chroma import Chroma

load_dotenv()

Groq_api_key=os.environ.get('Groq_api_key')

os.environ["Groq_api_key"] = Groq_api_key
 
 
extracted_data = load_pdf_files(data="data/")
filter_data = filter_to_minimal_docs(extracted_data)
text_chunks = text_split(filter_data)


embeddings = download_embeddings()

persist_directory = "./chroma_latest"

vectordb = Chroma.from_documents(
    documents=text_chunks,
    collection_name="medical-chatbot",
    embedding=embeddings,
    persist_directory=persist_directory 
)

print("done !")