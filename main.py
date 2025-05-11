import streamlit as st
from langchain.memory import ConversationBufferMemory
from utils import get_deepseek_response

st.title("🤖克隆DeepSeek")

with st.sidebar:
    deepseek_api_key = st.text_input("请输入DeepSeek API密钥", type="password")
    st.markdown("[获取DeepSeek API密钥](https://api-docs.deepseek.com/zh-cn/)")

    submit = st.button("开启新对话")

if submit:
    st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
    st.session_state["messages"] = [{"role": "ai",
                                     "content": "你好，我是你的AI助手， 有什么可以帮你"}]
    st.rerun()

if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
    st.session_state["messages"] = [{"role": "ai",
                                    "content": "你好，我是你的AI助手， 有什么可以帮你"}]

for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])


prompt = st.chat_input()
if prompt:
    if not deepseek_api_key:
        st.info("请输入你的OpenAI API密钥")
        st.stop()
    st.session_state["messages"].append({"role": "human", "content": prompt})
    st.chat_message("human").write(prompt)

    with st.spinner("AI正在思考中， 请稍后..."):
        response = get_deepseek_response(prompt, st.session_state["memory"],
                                     deepseek_api_key)
    msg = {"role": "ai", "content": response}
    st.session_state["messages"].append(msg)
    st.chat_message("ai").write(response)






