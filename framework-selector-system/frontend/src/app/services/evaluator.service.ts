import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { EvaluationResponse } from '../models/types';

@Injectable({
  providedIn: 'root'
})
export class EvaluatorService {
  private http = inject(HttpClient);
  
  private apiUrl = 'http://localhost:8000/api/evaluate'; 

  evaluateRequirements(prompt: string): Observable<EvaluationResponse> {
    return this.http.post<EvaluationResponse>(this.apiUrl, { user_prompt: prompt });
  }
}