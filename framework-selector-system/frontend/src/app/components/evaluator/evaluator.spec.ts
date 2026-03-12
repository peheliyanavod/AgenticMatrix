import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EvaluatorComponent } from './evaluator';

describe('EvaluatorComponent', () => {
  let component: EvaluatorComponent;
  let fixture: ComponentFixture<EvaluatorComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [EvaluatorComponent],
    }).compileComponents();

    fixture = TestBed.createComponent(EvaluatorComponent);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
