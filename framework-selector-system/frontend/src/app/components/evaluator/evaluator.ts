import { Component, inject, ChangeDetectorRef } from '@angular/core';
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
  private cdr = inject(ChangeDetectorRef); // 1. Inject ChangeDetectorRef
  
  userRequirement: string = '';
  isEvaluating: boolean = false;
  results: EvaluationResponse | null = null;

  submitRequirement() {
    if (!this.userRequirement.trim()) return;

    this.isEvaluating = true;
    this.results = null;

    this.evaluatorService.evaluateRequirements(this.userRequirement).subscribe({
      next: (response) => {
        console.log("Success! Data received in Angular:", response);
        this.results = response;
        this.isEvaluating = false;
        this.cdr.detectChanges(); 
      },
      error: (err) => {
        console.error('Evaluation failed! Check the Network tab.', err);
        this.isEvaluating = false;
        this.cdr.detectChanges();
      }
    });
  }

  formatKey(key: any): string {
    if (!key) return '';
    return String(key).split('_').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
  }
}