import os
import time
from rich import print
from dotenv import load_dotenv
from chat_gpt_wrapper import ChatGpt
from langchain_wrapper import LangChainGpt

if __name__ == '__main__':
    # Load environment variables
    load_dotenv() # this is for langchain
    token = os.getenv("OPENAI_API_KEY") # this is for chat gpt api

    # Load system message from file
    try:
        with open('system_message.txt', 'r') as f:
            system_message = f.read()
    except FileNotFoundError:
        print('File not found')

    # Initialize wrapper objects
    chat_gpt = ChatGpt(key=token, temperature=1, initial_prompt=system_message)
    langchain_gpt = LangChainGpt(system_message=system_message)

    # Start gpt chat
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
            command = input("Use langchain? (y/n), q to quit: ")
            continue

        if command == "y":
            print(f"\nLangchain:")
            langchain_gpt.predict(user_prompt)
            print("\n")
        elif command == "n":
            answer = chat_gpt.predict(user_prompt)
            print(f"\nGPT: {answer}\n")
        elif command == "q":
            break
        else:
            print("Invalid input. Please try again.")
