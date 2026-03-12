import json
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.models.schemas import RequirementRequest, EvaluationResponse, ScoredFramework
from app.services.ai_service import extract_weights_from_prompt
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Framework Selector API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"], # Angular's default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

with open("data/frameworks.json", "r") as f:
    FRAMEWORKS_DB = json.load(f)

@app.post("/api/evaluate", response_model=EvaluationResponse)
def evaluate_frameworks(request: RequirementRequest):
    try:
        weights = extract_weights_from_prompt(request.user_prompt)
        
        scored_frameworks = []
        for fw in FRAMEWORKS_DB:
            score = (
                (weights.reasoning_capabilities * fw["scores"]["reasoning_capabilities"]) +
                (weights.tool_usage * fw["scores"]["tool_usage"]) +
                (weights.memory_management * fw["scores"]["memory_management"]) +
                (weights.multi_agent_collaboration * fw["scores"]["multi_agent_collaboration"]) +
                (weights.documentation_maturity * fw["scores"]["documentation_maturity"]) +
                (weights.ecosystem_activity * fw["scores"]["ecosystem_activity"])
            )
            
            total_weight = sum(weights.model_dump().values())
            final_score = score / total_weight if total_weight > 0 else 0
            
            scored_frameworks.append(ScoredFramework(framework=fw, final_score=round(final_score, 4)))
            
        scored_frameworks.sort(key=lambda x: x.final_score, reverse=True)
        
        return EvaluationResponse(
            extracted_weights=weights,
            recommendations=scored_frameworks[:3] # Return top 3
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))