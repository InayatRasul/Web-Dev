import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, CommonModule, FormsModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'introToAngular';
  numbers: number[];
  students: any[];
  isMessage: boolean;
  message: string;
  display: string;
  items: string[];

  constructor(){
    this.numbers = [2,4,5];
    this.message = 'Hello'
    this.display = 'placeholderKnown';
    this.students = [
      {
        id: '23B030300',
        full_name: "Student 1",
        gpa: 3.9
      },
      {
        id: '23B030301',
        full_name: "Student 2",
        gpa: 4
      },
      {
        id: '23B030302',
        full_name: "Student 3",
        gpa: 3.9
      }
    ];
    this.isMessage = false;
    this.items = [
    ];
  }
  btnClick(){
    this.isMessage = !this.isMessage;
    // console.log('btn is clicked');
    //if changes occur in variables, then it runs html code again with updated values
  }
  addItem(){
    if(this.display !== ''){
      this.items.push(this.display);
      this.display = '';
    }
  }
  removeItem(index: number){
    this.items.splice(index,1);

  }

}

