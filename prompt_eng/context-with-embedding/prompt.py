from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from redundant_filter_retriever import RedundantFilterRetriever
from handlers.chat_model_start_handler import ChatModelStartHandler
from dotenv import load_dotenv
import langchain

langchain.debug = True

load_dotenv()

handler = ChatModelStartHandler()
chat = ChatOpenAI(
    callbacks=[handler]
)


chat = ChatOpenAI()
embeddings = OpenAIEmbeddings()
db = Chroma(
    persist_directory="emb",
    embedding_function=embeddings
)
retriever = RedundantFilterRetriever(
    embeddings=embeddings,
    chroma=db
)

chain = RetrievalQA.from_chain_type(
    llm=chat,
    retriever=retriever,
    chain_type="stuff"
)


while True:
    content = input("\n\n[This is Group-3 AI agent providing 24/7 support]\nHow may I help you today? >> ")

    result = chain.run(content)

    #print(result["text"])

    #result = chain.run("Hi, there! Group3 support")

    print(result)
