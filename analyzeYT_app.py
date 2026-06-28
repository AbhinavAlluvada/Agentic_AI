import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceEmbeddings

from langchain_core.prompts import PromptTemplate

from langchain_community.document_loaders import YoutubeLoader
from langchain_community.vectorstores import FAISS

from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

def create_vectordb(video_url: str) -> FAISS:
    loader = YoutubeLoader.from_youtube_url(video_url)
    transcript = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000,chunk_overlap = 100)
    docs = text_splitter.split_documents(transcript)
    
    db = FAISS.from_documents(docs , embeddings)
    return db

def get_response(db , query):
    docs = db.similarity_search(query)
    docs_page_content = " ".join([d.page_content for d in docs])

    llm = ChatOpenAI(
    model="meta-llama/llama-3.1-8b-instruct",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    temperature=0.5)
    
    prompt = PromptTemplate(
        input_variables=["query","docs"],
        template="""
        Using only the provided context, answer the user's question concisely and accurately.

        Context: {docs}
        Question: {query}

        Rules:
        - Use only the provided context.
        - If the answer is not in the context, say "The provided context does not contain the answer."
        - Keep the answer under 150 words unless more detail is necessary.
        """
        
    )
    chain = prompt | llm
    response = chain.invoke({
        "query": query,
        "docs": docs_page_content
        
    })
    return response.content
    


    