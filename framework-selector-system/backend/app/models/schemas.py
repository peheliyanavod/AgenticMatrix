from pydantic import BaseModel, Field
from typing import List

class FeatureWeights(BaseModel):
    reasoning_capabilities: float = Field(..., ge=0.0, le=1.0)
    tool_usage: float = Field(..., ge=0.0, le=1.0)
    memory_management: float = Field(..., ge=0.0, le=1.0)
    multi_agent_collaboration: float = Field(..., ge=0.0, le=1.0)
    documentation_maturity: float = Field(..., ge=0.0, le=1.0)
    ecosystem_activity: float = Field(..., ge=0.0, le=1.0)

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