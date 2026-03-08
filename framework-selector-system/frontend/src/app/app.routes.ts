import { Routes } from '@angular/router';
import { HomeComponent } from './components/home/home';
import { LearnComponent } from './components/learn/learn';
import { EvaluatorComponent } from './components/evaluator/evaluator';

export const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'learn', component: LearnComponent },
  { path: 'evaluate', component: EvaluatorComponent },
  { path: '**', redirectTo: '' }
];