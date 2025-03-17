from rag.llm.llm import LLM
import json
import requests as rq

class GeminiLLM(LLM):
    def __init__(self, config):
        super().__init__()
        self.model_name = config.get('model_name', 'gemini-1.5-flash')
        self.gemini_key = config.get('gemini_key', '')
        if self.gemini_key == "":
            raise ValueError("Please add gemini_key in config file!")
        
    def create_assistant_chat(self, message:str) -> dict:
        return {"role": "model", "parts": [{"text": message}]}
    
    def create_user_chat(self, message:str) -> dict:
        return {"role": "user", "parts": [{"text": message}]}
    
    def chat(self, history:list) -> str:
        chat_history = []
        for item in history:
            role = item['role']
            message = item['content']
            if role == 'assistant':
                chat_history.append(self.create_assistant_chat(message))
            if role == 'user':
                chat_history.append(self.create_user_chat(message))
            else:
                raise ValueError("role không xác định: " + role)
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{self.model_name}:generateContent?key={self.gemini_key}"
        payload = json.dumps({"contents": chat_history})
        headers = {"Content-Type": "application/json"}
        response = rq.post(url, headers=headers, data=payload)
        try:
            return response.json()['candidates'][0]['content']['parts'][0]['text']
        except json.JSONDecodeError:
            return {"error": "Invalid JSON response"}
        
if __name__ == "__main__":
    llm  = GeminiLLM({'gemini_key':'AIzaSyCMChcFML_dA97fNRD0i-gm2xXBA3PVz0Q'})
    print(llm.chat([{'role':'user','content':'How are you today'}]))

        