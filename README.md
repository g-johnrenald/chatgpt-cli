#Constantly Developing
See issues

# chatgpt-cli
This is a command-line interface (CLI) application that allows for easy communication with ChatGPT API. It provides two options to call the ChatGPT API which are via langchain using memory and 
direct call. 

## Requirements

1. Python 3.11

2. .env file containes OPENAI_API_KEY

## Installation

1. Clone this repository or download the source code as a ZIP file.

2. Install the dependencies by running the following command:

```
pip install -r requirements.txt
```

3. Create a .env file and put OPENAI_API_KEY inside.

## Usage

1. Open a terminal/command prompt and navigate to the root directory of the project.

2. Run the application using the following command:

```
python3 main.py
```

3. You will be presented with a prompt where you can input your prompt. 

4. Select Langchain or not.

5. Type in your promp and hit Enter. The program will automatically call the ChatGPT API and return the response.

6. To quit the program, type "q" and hit Enter.

## Useage of Docker (pull image from docker hub)
1. Pull docker image
```
docker pull johngarcines/chatgpt-cli:latest
```

2. Run docker image in interactive mode
```
docker run --name chatgpt-cli -it johngarcines/chatgpt-cli:latest
```

## Usage of Docker (build image from Dockerfile)
1. Build docker image
```
docker build -t chatgpt-cli .
```

2. Run docker image in interactive mode
```
docker run --name chatgpt-cli -it johngarcines/chatgpt-cli:latest
```

## Contributing

Contributions are welcome! If you find a bug or have an idea for a potential improvement, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
