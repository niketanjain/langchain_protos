from typing import Dict
from pydantic import BaseModel, ConfigDict


class ModelProviderKeyMap(BaseModel):
    model_config = ConfigDict(extra="forbid")

    provider: str
    model: str
    pricing: Dict[str, float]
    description: str
    key_env_var: str


MODELS = {
    "OPENROUTER_NORTH_MINI_CODE": {
        "provider": "openrouter",
        "model": "cohere/north-mini-code:free",
        "pricing": {"input": 0.0, "output": 0.0},
        "description": "OpenRouter North Mini Code model for code generation and reasoning tasks.",
        "key_env_var": "OPENROUTER_API_KEY",
    },
    "OLLAMA_DEVSTRAL_2": {
        "provider": "ollama",
        "model": "devstral-2",
        "pricing": {"input": 0.0, "output": 0.0},
        "description": "Ollama Devstral 2 model for general-purpose tasks.",
        "key_env_var": "OLLAMA_API_KEY",
    },
    "OPENAI_GPT_5_5": {
        "provider": "openai",
        "model": "gpt-5.5",
        "pricing": {"input": 0.0, "output": 0.0},
        "description": "OpenAI GPT 5.5 model for advanced language understanding and generation.",
        "key_env_var": "OPENAI_API_KEY",
    },
    "GEMINI_GENAI_2_5_FLASH_LITE": {
        "provider": "google_genai",
        "model": "gemini-2.5-flash-lite",
        "pricing": {"input": 0.0, "output": 0.0},
        "description": "Google Gemini GenAI 2.5 Flash Lite model for lightweight language tasks.",
        "key_env_var": "GEMINI_API_KEY",
    },
    "CLAUDE_SONNET_4_6": {
        "provider": "anthropic",
        "model": "claude-sonnet-4-6",
        "pricing": {"input": 0.0, "output": 0.0},
        "description": "Claude Sonnet 4.6 model for advanced language understanding and generation.",
        "key_env_var": "CLAUDE_API_KEY",
    },
    "FIREWORKS_QWEN3P5_397B_A17B": {
        "provider": "fireworks",
        "model": "accounts/fireworks/models/qwen3p5-397b-a17b",
        "pricing": {"input": 0.0, "output": 0.0},
        "description": "Fireworks Qwen3p5 397B A17B model for general-purpose tasks.",
        "key_env_var": "FIREWORKS_API_KEY",
    },
    "BASETEN_GLM_5_2": {
        "provider": "baseten",
        "model": "zai-org/GLM-5.2",
        "pricing": {"input": 0.0, "output": 0.0},
        "description": "Baseten GLM 5.2 model for general-purpose tasks.",
        "key_env_var": "BASETEN_API_KEY",
    },
    "BEDROCK_CLAUDE_SONNET_4_6": {
        "provider": "bedrock_converse",
        "model": "us.anthropic.claude-sonnet-4-6",
        "pricing": {"input": 0.0, "output": 0.0},
        "description": "Bedrock Claude Sonnet 4.6 model for advanced language understanding and generation.",
        "key_env_var": "BEDROCK_API_KEY",
    },
    "HUGGINGFACE_PHI_3_MINI_4K_INSTRUCT": {
        "provider": "huggingface",
        "model": "microsoft/Phi-3-mini-4k-instruct",
        "pricing": {"input": 0.0, "output": 0.0},
        "description": "HuggingFace Phi 3 Mini 4K Instruct model for instruction-following tasks.",
        "key_env_var": "HUGGINGFACE_API_KEY",
    },
}

def get_model_info(model_name: str) -> ModelProviderKeyMap:
    """
    Retrieve model information from the modelS dictionary.

    Args:
        model_name (str): The name of the model. 

    Returns:
        dict: The information associated with the specified model.
    """
    return MODELS.get(model_name)




print(get_model_info("OPENROUTER_NORTH_MINI_CODE"))