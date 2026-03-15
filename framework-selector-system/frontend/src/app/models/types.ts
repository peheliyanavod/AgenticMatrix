export interface FeatureWeights {
  ease_of_use: number;
  documentation: number;
  community: number;
  multi_agent: number;
  integration: number;
  production: number;
  state_memory: number;
  control: number;
  rag: number;
  observability: number;
  cost: number;
  enterprise: number;
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