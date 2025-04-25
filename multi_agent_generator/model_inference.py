"""
Model inference class for IBM WatsonX AI integration.
"""
from ibm_watsonx_ai.foundation_models import Model
from ibm_watsonx_ai.foundation_models.utils.enums import DecodingMethods
from typing import Dict, Any, Optional, List


class ModelInference:
    """
    Wrapper for IBM WatsonX AI model inference.
    
    This class provides a simplified interface for text generation
    using IBM's WatsonX AI foundation models.
    """
    
    def __init__(
        self,
        model_id: str,
        params: Dict[str, Any],
        credentials: Dict[str, str],
        project_id: Optional[str] = None
    ):
        """
        Initialize the model inference client.
        
        Args:
            model_id: The ID of the model to use
            params: Generation parameters (like max_tokens, temperature, etc.)
            credentials: API credentials including url and apikey
            project_id: Optional IBM Watson project ID
        """
        self.model_id = model_id
        self.params = params
        self.credentials = credentials
        self.project_id = project_id
        
        # Initialize the model
        self.model = Model(
            model_id=model_id,
            params=self._convert_params(params),
            credentials=credentials,
            project_id=project_id
        )
    
    def _convert_params(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Convert string parameter names to WatsonX enum types where needed."""
        converted = params.copy()
        
        # Convert decoding method string to enum if present
        if "decoding_method" in converted:
            method = converted["decoding_method"].upper()
            if hasattr(DecodingMethods, method):
                converted["decoding_method"] = getattr(DecodingMethods, method)
        
        return converted
    
    def generate_text(
        self, 
        prompt: str, 
        guardrails: bool = False
    ) -> str:
        """
        Generate text based on the prompt.
        
        Args:
            prompt: The text prompt to generate from
            guardrails: Whether to apply content safety filters
            
        Returns:
            The generated text response
        """
        try:
            # Generate text using the model
            response = self.model.generate_text(
                prompt=prompt,
                guardrails=guardrails
            )
            return response
        except Exception as e:
            print(f"Error in text generation: {e}")
            return f"Error generating text: {str(e)}"
    
    def generate_text_stream(
        self, 
        prompt: str, 
        guardrails: bool = False
    ) -> List[str]:
        """
        Generate text in a streaming fashion.
        
        Args:
            prompt: The text prompt to generate from
            guardrails: Whether to apply content safety filters
            
        Returns:
            List of text chunks from the stream
        """
        try:
            # Generate text using the model with streaming
            responses = []
            for chunk in self.model.generate_text_stream(
                prompt=prompt,
                guardrails=guardrails
            ):
                responses.append(chunk)
            return responses
        except Exception as e:
            print(f"Error in streaming text generation: {e}")
            return [f"Error generating text: {str(e)}"]