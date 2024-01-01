import os
import google.generativeai as genai


class Gemini:
    def __init__(self):
        # Set up the API key
        api_key = os.environ.get("GOOGLE_API_KEY")

        genai.configure(api_key=api_key)
        # Set up the model
        generation_config = {
            "temperature": 0.9,
            "top_p": 1,
            "top_k": 1,
            "max_output_tokens": 2048,
        }

        safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
        ]

        self.model = genai.GenerativeModel(model_name="gemini-pro",
                                           generation_config=generation_config,
                                           safety_settings=safety_settings)

    def generate(self, prompt):
        prompt_parts = [prompt]

        response = self.model.generate_content(prompt_parts)
        return response.text
