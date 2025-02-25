import os
from dotenv import load_dotenv

from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

## langsmith tracking
os.environ['LANGCHAIN_API_KEY1'] = os.getenv("LANGCHAIN_API_KEY1")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

##prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respond to a question asked"),
        ("user","Question:{question}")
    ]
)

## streamlit framework
st.title("Langchain Demo with Gemma model")
input_text = st.text_input("what question do you have in mind?")


## ollama llama2 model 
llm = Ollama(model="gemma:2b")
Output_Parser = StrOutputParser()
chain = prompt|llm|Output_Parser

if input_text:
    st.write(chain.invoke({"question":input_text}))