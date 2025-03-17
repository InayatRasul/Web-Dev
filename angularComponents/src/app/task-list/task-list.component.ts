import { Component} from '@angular/core';
import { Task } from '../task';
import { CommonModule } from '@angular/common';
import {FormsModule} from '@angular/forms';
import { TaskItemComponent } from '../task-item/task-item.component';

@Component({
  standalone:true,
  selector: 'app-task-list',
  imports: [CommonModule, FormsModule, TaskItemComponent],
  templateUrl: './task-list.component.html',
  styleUrls: ['./task-list.component.css']
})
export class TaskListComponent {
  newTasks: Task[];
  doneTasks: Task[];
  currentTask: Task;

  constructor(){
    this.newTasks = [];
    this.currentTask = new Task();
    this.doneTasks = [];
  }

  ngOnInit(): void{


  }
  addTodo(){
    if(this.currentTask.title !== ''){
      // this.currentTask.id = this.newTasks.length + 1;
      this.newTasks.push(this.currentTask);
      this.currentTask = new Task();// if you dont do so it will use same object for all array
    }
  }
  onNewTaskRemove(index: number){
    this.newTasks = this.newTasks.filter((x) => x.id !== index);
  }
  onDoneTaskRemove(index: number){
    this.doneTasks = this.doneTasks.filter((x) => x.id !== index);
  }
  onIsDoneChanged(task: Task){
    if(task.isDone){
      this.onNewTaskRemove(task.id);
      this.doneTasks.push(task);
      this.doneTasks.sort((a,b) => a.id > b.id ? 1 : -1);
    }else{
      // this.doneTasks = this.doneTasks.filter((x) => x.id !== task.id);
      this.onDoneTaskRemove(task.id);
      this.newTasks.push(task);
      this.newTasks.sort((a,b) => a.id > b.id ? 1 : -1);
    }
  }

}
