import cohere
import streamlit as st
import pandas as pd
from streamlit_extras.stylable_container import stylable_container
# import pyautogui
import weaviate
import cohere
import uuid
import os
from streamlit_js_eval import streamlit_js_eval



def coherechatmodel(user_prompt,client,co):
    
    rag_response = ""

    results1 = client.query.get("Fiveyearhighlights", ["description", "year", "value"]
                                ).with_near_text(
                                    {"concepts": [user_prompt]}
                                ).with_limit(5).do()

    results2 = client.query.get("Abbdata", ["doc_text"]
                                ).with_near_text(
                                    {"concepts": [user_prompt]}
                                ).with_limit(3).do()

    results3 = client.query.get("bs_cf_spl_tables", ["bs_cf_spl_description", "bs_cf_spl_year", "bs_cf_spl_value"]
                                ).with_near_text(
                                    {"concepts": [user_prompt]}
                                ).with_limit(10).do()

    # prompt = f"first use {results1}{results3} data to answer the prompt. if the data is not enoughf then use {results2} data and answer the following question in simple sentence " +user_prompt

    greetings_prompt = "Hello! I am FinAnalyticaAI, please ask me about prompt related to Financial Report."
    preamble_override = f"if prompt is greetings like hi, hello. then please respond by using following text:{greetings_prompt}. Use {results1}{results3} data to answer the prompt. if the data is not enough then use {results2} data and answer the following question in simple sentence "+user_prompt+f"also consider history of chat from following data {rag_response}"
    # Chatbot response
    response = co.chat( message=user_prompt,
                        preamble_override=preamble_override,
                        stream=True,
                         #conversation_id=conversation_id,
                        return_chat_history=True)
    

    print(type(response))
    for event in response:
        if event.event_type == "text-generation":
            print(event.text, end='')
            rag_response = event.text
            
    return response.texts[0]



def initfn():
    chat_his=[]
    print("here comes the connection key code")
    WEAVIATE_API_KEY = "WaY9IXHEJFhX8XM9Lrde3ergGO07v8fancpg"
    WEAVIATE_CLUSTER = "https://weaviate-hackathon-cluster-5q6ns8o7.weaviate.network"
    COHERE_API_KEY = "xxxxxxxx"

    auth_config = weaviate.auth.AuthApiKey(api_key = WEAVIATE_API_KEY)
    weaviate_url = WEAVIATE_CLUSTER

    client = weaviate.Client(url = weaviate_url,
    additional_headers = {"X-Cohere-Api-Key":COHERE_API_KEY},
    auth_client_secret = auth_config)

    client.is_ready()
    co = cohere.Client(COHERE_API_KEY)
    return client,co

# print("once key established , client is ready")
# print("now call the fraUi def and get the input prompt and then ")

initMsg="Hello! I’m an AI assistant proficient in analyzing financial reports. Not only can I break down reports or provide a summary with key insights, but I can also give you an overview of how well the business is performing based on those reports. How may I assist you today?"
st.title("Financial Report Analyzer")
chat_his=[]

if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({"role": "assistant", "content": initMsg})
    client,co=initfn()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Begin typing here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        client,co=initfn()
        stream = coherechatmodel(prompt,client,co)
        st.write(stream)
    st.session_state.messages.append({"role": "assistant", "content": stream})
with stylable_container(
        key="bottom_content",
        css_styles="""
            {
                position: fixed;
                bottom: 115px;
            }
            """,
    ):
    if st.button('Restart'):
        streamlit_js_eval(js_expressions="parent.window.location.reload()")



# print("now comes the coherechatmodel function, this fn takes the prompt and then returns the response")
# # added above 

print("end of the oprn")
