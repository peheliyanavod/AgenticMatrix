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
    allow_origins=["http://localhost:4200"],
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
                (weights.ease_of_use * fw["scores"]["ease_of_use"]) +
                (weights.documentation * fw["scores"]["documentation"]) +
                (weights.community * fw["scores"]["community"]) +
                (weights.multi_agent * fw["scores"]["multi_agent"]) +
                (weights.integration * fw["scores"]["integration"]) +
                (weights.production * fw["scores"]["production"]) +
                (weights.state_memory * fw["scores"]["state_memory"]) +
                (weights.control * fw["scores"]["control"]) +
                (weights.rag * fw["scores"]["rag"]) +
                (weights.observability * fw["scores"]["observability"]) +
                (weights.cost * fw["scores"]["cost"]) +
                (weights.enterprise * fw["scores"]["enterprise"])
            )
            
            total_weight = sum(weights.model_dump().values())
            final_score = score / total_weight if total_weight > 0 else 0
            
            scored_frameworks.append(ScoredFramework(framework=fw, final_score=round(final_score, 4)))
            
        scored_frameworks.sort(key=lambda x: x.final_score, reverse=True)
        
        return EvaluationResponse(
            extracted_weights=weights,
            recommendations=scored_frameworks[:3] 
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))