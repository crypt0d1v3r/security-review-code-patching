class ModelAPI:
    def __init__(self, model_name: str, provider: str, max_tokens: int = 4096):
        self.model_name = model_name
        self.provider = provider.strip().lower()
        self.max_tokens = max_tokens
        if self.provider == "openai":
            from openai import OpenAI

            self.client = OpenAI()
        if self.provider == "anthropic":
            from anthropic import Anthropic

            self.client = Anthropic()
        if self.provider in ("google", "gemini"):
            from google import genai

            self.client = genai.Client()
        if self.provider == "ollama":
            import ollama

            self.client = ollama.Client()

        raise ValueError("provider must be OpenAI, Anthropic, Google/Gemini, or Ollama")