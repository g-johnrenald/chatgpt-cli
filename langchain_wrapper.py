from langchain import ConversationChain
from langchain.callbacks.base import CallbackManager
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)

from src.StreamingPrintCallbackHandler import StreamingPrintCallbackHandler


class LangChainGpt:
    def __init__(self, system_message):
        self.prompt = ChatPromptTemplate.from_messages([
            SystemMessagePromptTemplate.from_template(system_message),
            MessagesPlaceholder(variable_name="history"),
            HumanMessagePromptTemplate.from_template("{input}")
        ])
        self.llm = ChatOpenAI(streaming=True, callback_manager=CallbackManager([StreamingPrintCallbackHandler()]),
                              verbose=True, temperature=0)
        self.memory = ConversationBufferMemory(return_messages=True)
        self.conversation = ConversationChain(memory=self.memory, prompt=self.prompt, llm=self.llm)

    def predict(self, user_prompt):
        return self.conversation.predict(input=user_prompt)
