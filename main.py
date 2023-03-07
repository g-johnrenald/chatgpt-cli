import os
import openai
from rich import print
from dotenv import load_dotenv
from langchain.llms import OpenAIChat
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationSummaryBufferMemory


class ChatGpt:
    def __init__(self, key, temperature, initial_prompt):
        openai.api_key = key
        self.temperature = temperature
        self.prefix_messages = initial_prompt

    model = "gpt-3.5-turbo"

    def predict(self, prompt):
        res = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system",
                 "content": self.prefix_messages},
                {"role": "user", "content": prompt},
            ],
            temperature=self.temperature
        )
        return res.choices[0].message.content


class LangChainGpt:
    def __init__(self, initial_content):
        self.prefix_messages = [{"role": "system",
                                 "content": initial_content}]
        self.llm = OpenAIChat(temperature=0, prefix_messages=self.prefix_messages)
        self.llm_chain = ConversationChain(
            llm=self.llm,
            memory=ConversationSummaryBufferMemory(llm=self.llm))

    def predict(self, user_prompt):
        return self.llm_chain.predict(input=user_prompt)


if __name__ == '__main__':
    # Load environment variables
    load_dotenv()
    token = os.getenv("OPENAI_API_KEY")

    initial_prompt = "You are a helpful assistant that is very good at problem solving who thinks step by step."

    chat_gpt = ChatGpt(key=token, temperature=1, initial_prompt=initial_prompt)
    langchain_gpt = LangChainGpt(initial_content=initial_prompt)

    command = input("Use langchain? (y/n), q to quit: ")
    while True:
        if command != "y" and command != "n" and command != "q" and command != "o":
            print("Invalid input. Please try again.")
            continue

        if command == "q":
            break

        if command == "o":
            command = input("Use langchain? (y/n): ")

        # contents = []
        # print("Prompt: ")
        # while True:
        #     line = input()
        #     if line:
        #         contents.append(line)
        #     else:
        #         break
        # user_prompt = "\n".join(contents)

        user_prompt = input("Prompt (q to quit): ")

        if user_prompt == "q":
            break

        if command == "y":
            answer = langchain_gpt.predict(user_prompt)
            print(f"Langchain: {answer}\n")
        else:
            # print(user_prompt.strip())
            answer = chat_gpt.predict(user_prompt)
            print(f"GPT: {answer}\n")
