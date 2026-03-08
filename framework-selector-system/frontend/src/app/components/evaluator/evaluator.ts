import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { EvaluatorService } from '../../services/evaluator.service';
import { EvaluationResponse } from '../../models/types';

@Component({
  selector: 'app-evaluator',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './evaluator.html'
})
export class EvaluatorComponent {
  private evaluatorService = inject(EvaluatorService);
  
  userRequirement: string = '';
  isEvaluating: boolean = false;
  results: EvaluationResponse | null = null;

  submitRequirement() {
    if (!this.userRequirement.trim()) return;

    this.isEvaluating = true;
    this.results = null;

    this.evaluatorService.evaluateRequirements(this.userRequirement).subscribe({
      next: (response) => {
        this.results = response;
        this.isEvaluating = false;
      },
      error: (err) => {
        console.error('Evaluation failed', err);
        this.isEvaluating = false;
      }
    });
  }

  formatKey(key: string): string {
    return key.split('_').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
  }
}