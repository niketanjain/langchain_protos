```bash
mkdir langchain-protos
cd langchain-protos
git init

uv python pin 3.11
uv init
uv add langchain
uv sync
uv add langchain-openai
uv add langchain-anthropic langchain-openrouter python-dotenv

# Load the environment variables here in .env 
touch .env .env.example
```

# Run Langchain script by loading .env (example)
```python 
## 1. Load the environment variables from the .env file
load_dotenv() # Looks for a .env file in the current directory

## Verify the key is loaded (LangChain models automatically check os.environ)
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY not found. Please check your .env file.")
```
