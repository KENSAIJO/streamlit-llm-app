
from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

import streamlit as st

st.title("課題アプリ：乗り物に関する質問に答えます")

st.write("##### 動作モード1: 自動車に関する質問")
st.write("入力フォームに質問テキストを入力し、「実行」ボタンを押すことで専門家からの回答が得られます。")
st.write("##### 動作モード2: 鉄道に関する質問")
st.write("入力フォームに質問テキストを入力し、「実行」ボタンを押すことで専門家からの回答が得られます。")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["自動車に関する質問", "鉄道に関する質問"]
)

st.divider()

if selected_item == "自動車に関する質問":
    input_message = st.text_input(label="自動車に関する質問を入力してください。")
else:
    input_message = st.text_input(label="鉄道に関する質問を入力してください。")
 


def process_input(input_message, selected_item):
    if selected_item == "自動車に関する質問":
        messages = [
            SystemMessage(content="You are a helpful assistant espacially autocars and automotive."),
            HumanMessage(content=input_message),
        ]
    else:
        messages = [
            SystemMessage(content="You are a helpful assistant espacially train and railway."),
            HumanMessage(content=input_message),
        ]
    return messages


if st.button("実行"):
    st.divider()

    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
    
    messages = process_input(input_message, selected_item)
    
    result = llm(messages)
    st.write(result.content) 









