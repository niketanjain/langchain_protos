from langchain.agents import create_agent
from dotenv import load_dotenv
import os
from model_provider_key_map import get_model_info

# 1. Load the environment variables from the .env file
load_dotenv()  # Looks for a .env file in the current directory


def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


def get_agent_with_prompt(model):
    agent = create_agent(
        model=model,
        tools=[get_weather],
        system_prompt="You are a helpful assistant",
    )
    return agent


def get_result(model):
    agent = get_agent_with_prompt(model)
    result = agent.invoke(
        {"messages": [{"role": "user", "content": "What's the weather like?"}]}
    )
    print(result["messages"][-1].content_blocks)


selected_model = get_model_info("OPENROUTER_NORTH_MINI_CODE")
# Verify the key is loaded (LangChain models automatically check os.environ)
if not os.getenv(selected_model["key_env_var"]):
    raise ValueError(
        f"{selected_model['key_env_var']} not found. Please check your .env file."
    )

get_result(f'{selected_model["provider"]}:{selected_model["model"]}')
