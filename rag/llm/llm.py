class LLM:
    def generate_text(self, history: list) -> str:
        """Generate text using the LLM"""
        raise NotImplementedError("Subclasses must implement generate_text()")