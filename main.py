import os
import time
from rich import print
from dotenv import load_dotenv
from tqdm import tqdm

from chat_gpt_wrapper import ChatGpt
from langchain_wrapper import LangChainGpt


def show_waiting_indicator(func):
    def wrapper(*args, **kwargs):
        progress_bar = tqdm(total=100, desc="Waiting for response...",
                            unit="%")
        for i in range(100):
            progress_bar.update(1)
            time.sleep(0.05)
        progress_bar.close()
        result = func(*args, **kwargs)
        return result

    return wrapper


if __name__ == '__main__':
    # Load environment variables
    load_dotenv()
    token = os.getenv("OPENAI_API_KEY")

    initial_prompt = "You are a helpful assistant that is very good at problem solving who thinks step by step."

    chat_gpt = ChatGpt(key=token, temperature=1, initial_prompt=initial_prompt)
    langchain_gpt = LangChainGpt(system_message=initial_prompt)

    command = input("Use langchain? (y/n), q to quit: ")
    while True:
        if command != "y" and command != "n" and command != "q" and command != "o":
            print("Invalid input. Please try again.")
            continue

        if command == "q":
            break

        user_prompt = input("Prompt (q to quit, o to option): ")

        if user_prompt == "q":
            break

        if user_prompt == "o":
            command = input("Use langchain? (y/n): ")
            continue

        if command == "y":
            print(f"\nLangchain:")
            langchain_gpt.predict(user_prompt)
            print("\n")
        elif command == "n":
            # print(user_prompt.strip())
            answer = chat_gpt.predict(user_prompt)
            print(f"\nGPT: {answer}\n")
        elif command == "q":
            break
        else:
            print("Invalid input. Please try again.")
