# import google.generativeai as genai
import langchain
import getpass
import os
from langchain.document_loaders import UnstructuredFileLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
import nltk
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("")


def load_pdf(pdf_path):
    loader = UnstructuredFileLoader(pdf_path)
    pages = loader.load()
    return pages

# genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
#model = genai.GenerativeModel("gemini-1.5-flash")
embeddings_function = GoogleGenerativeAIEmbeddings(model= "models/embedding-001", google_api_key='')

pages = load_pdf('./metasploit.pdf')
text_to_chunks = CharacterTextSplitter(chunk_size = 500, chunk_overlap=0)
chunks_of_text = text_to_chunks.split_documents(pages)

docsearch = Chroma.from_documents(chunks_of_text, embeddings_function)
chain = RetrievalQA.from_chain_type(llm=GoogleGenerativeAI(model="gemini-pro", google_api_key=''), chain_type='stuff', retriever=docsearch.as_retriever())

qa_res = chain.invoke("how can I scan vulnerabilities with NeXpose?")
print(qa_res)