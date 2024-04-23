#api_key=st.secrets["GROQ_API_KEY"]
#from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

api_key=st.secrets["GROQ_API_KEY"]
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOIN"]="https://api.smith.langchain.com"
os.environ["LANGCHAIN_API_KEY"] = "ls__7c56e62a6a694fd08991b5e975429793"
os.environ["LANGCHAIN_PROJECT"] = "Groq Application"

st.markdown("""
            <h1 style="text-align:center">Groq <Sapn style="color:#9980FA">Chatbot</span></h1>
            """,unsafe_allow_html=True)

#load_dotenv()

def groq_chat(input):
    outputparsor = StrOutputParser()
    prompt = ChatPromptTemplate.from_messages([
        ("system","you are a helpful assistant for resume building.giving reply not more than 30 words"),
        ("user","{query}")
    ])
    
    llm = ChatGroq()
    chain = prompt | llm | outputparsor
    
    return(chain.invoke({"query":input}))




if "hist" not in st.session_state:
    st.session_state.hist = []
    
for hist in st.session_state.hist:
    with st.chat_message(hist["role"]):
         st.markdown(hist["content"])  
         
user = st.chat_input("Try with Groq...") 

if user is not None:
    with st.chat_message("user"):
        st.markdown(user)   
    
    st.session_state.hist.append({"role":"user","content":user})    
    
    
    with st.chat_message("AI"):
        response = groq_chat(user) 
        st.write(response)    
    
    st.session_state.hist.append({"role":"assistant","content":response})    
           