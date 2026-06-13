from flask import Flask, render_template, jsonify, request
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from src.utils import download_embeddings
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os


app = Flask(__name__) # initlizitng flask


load_dotenv()

Groq_api_key=os.environ.get('Groq_api_key')

os.environ["Groq_api_key"] = Groq_api_key

# Embedding Model
embeddings = download_embeddings()

# Load Existing ChromaDB
vectordb = Chroma(
    collection_name="medical-chatbot",
    persist_directory="./chroma_db",
    embedding_function=embeddings
)

retriever = vectordb.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)

# Groq LLM
llm = ChatGroq(
    groq_api_key=Groq_api_key,
    model_name="llama-3.1-8b-instant",
    temperature=0
)




retriever = vectordb.as_retriever(search_type="similarity", search_kwargs={"k":3})

llama = ChatGroq(
    model="llama-3.3-70b-versatile"
)
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)



question_answer_chain = create_stuff_documents_chain(llama, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)


@app.route("/")
def index():
    return render_template('chat.html')


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    response = rag_chain.invoke({"input": msg})
    print("Response : ", response["answer"])
    return str(response["answer"])



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
