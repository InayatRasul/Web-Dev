import { Component, signal } from '@angular/core';
import { GreetingComponent } from '../component/greeting/greeting.component';
import { CounterComponent } from '../component/counter/counter.component';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-home',
  imports: [GreetingComponent, CounterComponent, CommonModule],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {
  message = signal('Hello user, how are you');

  keyUpHandler(event: KeyboardEvent){
    console.log(`user pressed the ${event.key} key`);
  }

}
