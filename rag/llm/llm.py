class LLM:
    def chat(self, history: list) -> str:
        """Generate text using the LLM"""
        raise NotImplementedError("Subclasses must implement generate_text()")