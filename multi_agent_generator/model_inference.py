"""
Model inference utilities using LiteLLM for multiple providers.
"""
import os
from typing import Dict, List, Optional, Union
from pydantic import BaseModel
from dotenv import load_dotenv
from litellm import completion  # Unified API

# Load environment variables
load_dotenv()


class Message(BaseModel):
    role: str
    content: str


class ModelInference:
    """
    Unified LiteLLM-based model inference class.
    Supports OpenAI, WatsonX, Ollama, Anthropic, etc. via LiteLLM.
    """

    def __init__(
        self,
        model: str,
        api_key: Optional[str] = None,
        api_base: Optional[str] = None,
        **default_params
    ):
        self.model = model
        self.api_key = api_key or self._get_api_key_for_model(model)
        self.api_base = api_base or os.getenv("API_BASE")
        self.default_params = default_params

    def _get_api_key_for_model(self, model: str) -> Optional[str]:
        """Get the appropriate API key based on the model name."""
        if model.startswith("gemini"):
            return os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
        elif model.startswith("gpt") or model.startswith("text-davinci"):
            return os.getenv("OPENAI_API_KEY")
        elif model.startswith("watsonx"):
            return os.getenv("WATSONX_API_KEY")
        else:
            # Fallback to generic API_KEY
            return os.getenv("API_KEY") or os.getenv("OPENAI_API_KEY")

    def generate_text(
        self,
        messages: List[Union[Dict, Message]],
        **override_params
    ) -> str:
        """
        Synchronously generate text.
        """
        try:
            msg_list = [m.dict() if isinstance(m, Message) else m for m in messages]
            response = completion(
                model=self.model,
                messages=msg_list,
                api_key=self.api_key,
                api_base=self.api_base,
                **{**self.default_params, **override_params}
            )
            return response.choices[0].message.content

        except Exception as e:
            raise RuntimeError(f"Model inference failed: {e}")
