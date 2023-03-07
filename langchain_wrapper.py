from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    HumanMessage,
    SystemMessage
)
from langchain.callbacks.base import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler


class LangChainGpt:
    def __init__(self, system_message):
        self.sm = SystemMessage(content=system_message)
        self.chat = ChatOpenAI(streaming=True, callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
                               verbose=True, temperature=0)

    def predict(self, user_prompt):
        hm = HumanMessage(content=user_prompt)
        return self.chat([self.sm, hm])
