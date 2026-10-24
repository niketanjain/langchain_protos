# pip install -qU langchain langchain-ollama
from langchain.agents import create_agent

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

def get_agent_with_prompt(model):
    agent = create_agent(
        model=model,
        tools=[get_weather],
        system_prompt="You are a helpful assistant",
    )

def get_result(model):
    agent = get_agent_with_prompt(model)
    result = agent.invoke(
        {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]}
    )
    print(result["messages"][-1].content_blocks)


MODELS = {
  "OLLAMA": "ollama:devstral-2",
  "OPENAI": "openai:gpt-5.5",
  "GEMINI": "google_genai:gemini-2.5-flash-lite",
  "CLAUDE": "claude-sonnet-4-6",
  "OPENROUTER": "openrouter:anthropic/claude-sonnet-4-6",
  "FIREWORKS": "fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
  "BASETEN": "baseten:zai-org/GLM-5.2",
  "BEDROCK": "bedrock_converse:us.anthropic.claude-sonnet-4-6",
  "HUGGINGFACE": "huggingface:microsoft/Phi-3-mini-4k-instruct"

}


get_result(MODELS["OPENROUTER"])
