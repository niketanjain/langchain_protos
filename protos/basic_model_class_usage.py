import os
from dotenv import load_dotenv
from langchain_openrouter import ChatOpenRouter
from langchain.agents import create_agent
from model_provider_key_map import get_model_info

# 1. Load the environment variables from the .env file
load_dotenv()  # Looks for a .env file in the current directory

selected_model = get_model_info("OPENROUTER_NORTH_MINI_CODE")
# Verify the key is loaded (LangChain models automatically check os.environ)
if not os.getenv(selected_model["key_env_var"]):
    raise ValueError(
        f"{selected_model['key_env_var']} not found. Please check your .env file."
    )


# 2. Define a tool for the agent to use
# The docstring acts as the tool description so the LLM knows when to use it.
def multiply_numbers(a: float, b: float) -> float:
    """Multiplies two numbers together and returns the result."""
    return a * b


# 3. Initialize the Language Model
# It automatically picks up the OPENROUTER_API_KEY from the environment
llm = ChatOpenRouter(model=selected_model["model"], temperature=0)

# 4. Create the agent with the defined tool
# The framework passes the tool array directly to the underlying model loop
agent = create_agent(
    model=llm,
    tools=[multiply_numbers],
    system_prompt="You are a helpful assistant. Use your tools when mathematical equations need calculation.",
)

# 5. Run the agent
if __name__ == "__main__":
    query = "What is 423 multiplied by 982?"
    print(f"User: {query}\n")

    # Run the agent over the problem
    response = agent.invoke({"messages": [("user", query)]})

    # Output the final message from the agent's state history
    print(f"Agent: {response['messages'][-1].content}")
