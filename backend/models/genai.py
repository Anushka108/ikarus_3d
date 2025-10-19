class GenAIModel:
    
    # ensure the text generation pipeline is working by first loading it .the model is loaded only once
    def __init__(self):
        self.generator = None

    def _ensure_loaded(self):
        if self.generator is not None:
            return
        try:
            from transformers import pipeline  #do this only when needed
        except Exception as e:
            raise ImportError("transformers is required for GenAIModel. Install with: pip install transformers") from e
        self.generator = pipeline("text-generation", model="distilgpt2")

    def generate_description(self, title, material, category):
        self._ensure_loaded()  # to load the generator model
        prompt = f"Generate a short, creative marketing description for a {material} {category} named '{title}'." # create nlp based to guide model
        out = self.generator(prompt, max_length=60, num_return_sequences=1, temperature=0.8)
        return out[0]['generated_text']
# return the generated description