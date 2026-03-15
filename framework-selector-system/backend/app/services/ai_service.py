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
    You are an expert consultant specializing in AI agent frameworks. Your role is to help users select the optimal agentic framework based on their specific requirements.
    
    Analyze the user's project requirement and assign importance weights to the following 12 framework features:
    ease_of_use, documentation, community, multi_agent, integration, production, state_memory, control, rag, observability, cost, enterprise.
    
    CRITICAL RULE: The sum of all 12 weights MUST equal exactly 1.0. 
    If a feature is not relevant to the user's prompt, assign it a weight of 0.0 or a very low value (e.g., 0.05). Ensure the highest weights go to the features most critical to the user's request.
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