import { Injectable } from '@angular/core';
import { Observable, of, delay } from 'rxjs';
import { EvaluationResponse } from '../models/types';

@Injectable({
  providedIn: 'root'
})
export class EvaluatorService {
  constructor() { }

  evaluateRequirements(prompt: string): Observable<EvaluationResponse> {
    const dummyResponse: EvaluationResponse = {
      extracted_weights: {
        reasoning_capabilities: 0.9,
        tool_usage: 0.8,
        memory_management: 0.5,
        multi_agent_collaboration: 0.2,
        documentation_maturity: 0.7,
        ecosystem_activity: 0.6
      },
      recommendations: [
        {
          final_score: 0.86,
          framework: {
            id: 'langchain_langgraph',
            name: 'LangGraph',
            description: 'A library for building stateful, multi-actor applications with LLMs.',
            scores: { reasoning_capabilities: 0.8, tool_usage: 0.95, memory_management: 0.85, multi_agent_collaboration: 0.8, documentation_maturity: 0.95, ecosystem_activity: 0.95 }
          }
        },
        {
          final_score: 0.82,
          framework: {
            id: 'autogen',
            name: 'Microsoft AutoGen',
            description: 'Enables development of LLM applications using multiple conversing agents.',
            scores: { reasoning_capabilities: 0.85, tool_usage: 0.8, memory_management: 0.7, multi_agent_collaboration: 0.95, documentation_maturity: 0.85, ecosystem_activity: 0.9 }
          }
        }
      ]
    };

    return of(dummyResponse).pipe(delay(2000));
  }
}