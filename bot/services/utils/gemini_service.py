import google.generativeai as genai

from utils.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def ask_gemini(prompt: str) -> str:
    """
        Sends a prompt to Gemini and returns the response.
            """

                try:
                        response = model.generate_content(prompt)
                                return response.text

                                    except Exception as e:
                                            return f"❌ Gemini Error:\n{str(e)}"