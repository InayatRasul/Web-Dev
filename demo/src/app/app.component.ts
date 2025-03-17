import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { HeaderComponent } from './component/header/header.component';
// import { HeaderComponent } from './component/header/header.component.component';
// import { RouterOutlet } from '@angular/router';
// import { CommonModule } from '@angular/common';


@Component({
  selector: 'app-root',
  standalone: true,
  imports:[RouterOutlet,HeaderComponent],
  template: `
  <app-header />
  <main>
    
  <router-outlet />
  
  </main>
  `,
  styles:[
    `
      main{
        padding:16px;

      }
    `,
  ],
})
export class AppComponent {
  title = 'demo';
  constructor(){
    console.log('constructor method is running');

  }
}
