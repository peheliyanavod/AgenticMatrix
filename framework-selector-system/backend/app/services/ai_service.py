import os
import json
from dotenv import load_dotenv
from google import genai
from google.genai import types
from app.models.schemas import FeatureWeights

load_dotenv() 

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def extract_weights_from_prompt(user_prompt: str) -> FeatureWeights:
    system_instruction = """
    You are an AI architecture expert. Analyze the user's project requirement and assign importance weights (from 0.0 to 1.0) to the following 6 agentic framework features.
    """
    
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=f"{system_instruction}\n\nUser Requirement: {user_prompt}",
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=FeatureWeights,
            temperature=0.1
        )
    )
    
    weights_dict = json.loads(response.text)
    return FeatureWeights(**weights_dict)