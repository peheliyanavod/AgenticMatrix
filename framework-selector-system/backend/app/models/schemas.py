from pydantic import BaseModel, Field
from typing import List

class FeatureWeights(BaseModel):
    ease_of_use: float = Field(..., ge=0.0, le=1.0)
    documentation: float = Field(..., ge=0.0, le=1.0)
    community: float = Field(..., ge=0.0, le=1.0)
    multi_agent: float = Field(..., ge=0.0, le=1.0)
    integration: float = Field(..., ge=0.0, le=1.0)
    production: float = Field(..., ge=0.0, le=1.0)
    state_memory: float = Field(..., ge=0.0, le=1.0)
    control: float = Field(..., ge=0.0, le=1.0)
    rag: float = Field(..., ge=0.0, le=1.0)
    observability: float = Field(..., ge=0.0, le=1.0)
    cost: float = Field(..., ge=0.0, le=1.0)
    enterprise: float = Field(..., ge=0.0, le=1.0)

class FrameworkData(BaseModel):
    id: str
    name: str
    description: str
    scores: FeatureWeights

class RequirementRequest(BaseModel):
    user_prompt: str

class ScoredFramework(BaseModel):
    framework: FrameworkData
    final_score: float

class EvaluationResponse(BaseModel):
    extracted_weights: FeatureWeights
    recommendations: List[ScoredFramework]