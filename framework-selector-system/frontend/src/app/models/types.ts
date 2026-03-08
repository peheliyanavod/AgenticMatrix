export interface FeatureWeights {
  reasoning_capabilities: number;
  tool_usage: number;
  memory_management: number;
  multi_agent_collaboration: number;
  documentation_maturity: number;
  ecosystem_activity: number;
}

export interface FrameworkData {
  id: string;
  name: string;
  description: string;
  scores: FeatureWeights;
}

export interface ScoredFramework {
  framework: FrameworkData;
  final_score: number;
}

export interface EvaluationResponse {
  extracted_weights: FeatureWeights;
  recommendations: ScoredFramework[];
}