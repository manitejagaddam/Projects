import streamlit as st
from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.callbacks.base import BaseCallbackHandler

class StreamHandler(BaseCallbackHandler):
    def __init__(self, container, initial_text=""):
        self.container = container
        self.text = initial_text

    def on_llm_new_token(self, token: str, **kwargs) -> None:
        self.text += token
        self.container.markdown(self.text)

@st.cache_data()
def create_chain(system_prompt):
    api_token = "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" 
    repo_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"   
    llm = HuggingFaceHub(repo_id=repo_id, huggingfacehub_api_token=api_token)
    template = "{system_prompt} {question}"
    prompt = PromptTemplate(template=template, input_variables=["system_prompt", "question"])
    llm_chain = LLMChain(llm=llm, prompt=prompt)
    return llm_chain

st.set_page_config(page_title="Your own aiChat!")

st.header("Your own aiChat!")
system_prompt = st.text_area(
    label="System Prompt",
    value="You are a helpful AI assistant who answers questions in short sentences.",
    key="system_prompt"
)

llm_chain = create_chain(system_prompt)

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "How may I help you today?"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_prompt = st.text_input("Your message here", key="user_input")
if user_prompt:
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    formatted_prompt = {"system_prompt": system_prompt, "question": user_prompt}
    assistant_response = llm_chain.invoke(formatted_prompt)
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})
    with st.chat_message("assistant"):
        st.markdown(assistant_response['text'])