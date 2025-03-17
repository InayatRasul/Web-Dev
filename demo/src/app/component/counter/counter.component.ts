import { Component, signal } from '@angular/core';
import { validateHeaderName } from 'http';

@Component({
  selector: 'app-counter',
  imports: [],
  templateUrl: './counter.component.html',
  styleUrl: './counter.component.css'
})
export class CounterComponent {
  counterValue = signal(0);
  increment(){
    this.counterValue.set(this.counterValue() + 1);
    // this.counterValue.update((val) => val + 1);
  }
  decrement(){
    this.counterValue.set(this.counterValue() - 1);
  }
  reset(){
    this.counterValue.set(0);
  }
}
