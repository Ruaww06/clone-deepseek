# import os
# from langchain.memory import ConversationBufferMemory
from langchain_deepseek import ChatDeepSeek
from langchain.chains import ConversationChain


def get_deepseek_response(prompt, memory, deepseek_api_key):
    model = ChatDeepSeek(model="deepseek-chat", api_key=deepseek_api_key)
    chain = ConversationChain(llm=model, memory=memory) # 带记忆的对话链

    response = chain.invoke({"input": prompt})
    return response["response"]

# memory = ConversationBufferMemory(return_messages=True)
# print(get_deepseek_response("中国的首都是哪里？", memory, os.getenv("DEEPSEEK_API_KEY")))
# print(get_deepseek_response("美国的呢？", memory, os.getenv("DEEPSEEK_API_KEY")))