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
        elif self.provider not in ("openai", "anthropic", "google", "gemini"):
            raise ValueError("provider must be OpenAI, Anthropic, Google/Gemini, or Ollama")

    def run(self, system_prompt: str, user_prompt: str) -> str:
        if self.provider == "openai":
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                max_tokens=self.max_tokens,
            )
            return response.choices[0].message.content
        if self.provider == "anthropic":
            response = self.client.completions.create(
                model=self.model_name,
                prompt=f"{system_prompt}\n\n{user_prompt}",
                max_tokens_to_sample=self.max_tokens,
            )
            return response.completion
        if self.provider in ("google", "gemini"):
            response = self.client.generate_text(
                model=self.model_name,
                prompt=f"{system_prompt}\n\n{user_prompt}",
                max_output_tokens=self.max_tokens,
            )
            return response.text
        if self.provider == "ollama":
            response = self.client.generate(
                model=self.model_name,
                prompt=f"{system_prompt}\n\n{user_prompt}",
                max_tokens=self.max_tokens,
            )
            return response.text
        raise ValueError("provider must be OpenAI, Anthropic, Google/Gemini, or Ollama")