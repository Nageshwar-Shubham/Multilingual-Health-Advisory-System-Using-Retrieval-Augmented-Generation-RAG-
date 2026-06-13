# from dotenv import load_dotenv
# import os
# from langchain_groq import ChatGroq

# load_dotenv(override=True)

# print("KEY:", os.getenv("GROQ_API_KEY"))

# llm = ChatGroq(
#     model="llama-3.1-8b-instant",
#     api_key=os.getenv("GROQ_API_KEY")
# )

# print(llm.invoke("hello"))

from store import vectordb
print(vectordb._collection.count())

# from store import embeddings

# test_embedding = embeddings.embed_query("hello")
# print(len(test_embedding))