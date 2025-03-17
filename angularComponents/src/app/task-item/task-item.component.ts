import { Component, EventEmitter, Input, OnChanges, OnDestroy, OnInit, Output, SimpleChanges} from '@angular/core';
import { Task } from '../task';
import { CommonModule } from '@angular/common';
import {FormsModule} from '@angular/forms';

@Component({
  selector: 'app-task-item',
  imports: [CommonModule, FormsModule],
  templateUrl: './task-item.component.html',
  styleUrl: './task-item.component.css'
})
export class TaskItemComponent implements OnInit, OnChanges, OnDestroy{
  @Input() task!: Task;
  @Output() remove = new EventEmitter(); //every output should be like this
  @Output() done = new EventEmitter();

  ngOnInit(): void {
    //Fetch Data from other resources
    console.log("TaskItemComponent: ngOnInit");
    //ng init when all data completly binded
  }
  ngOnChanges(changes: SimpleChanges): void {
    console.log("TaskItemComponent: ngOnChanges");
    //always when we have change in component
  }

  ngOnDestroy(): void {
    console.log("TaskItemComponent: ngOnDestroy");
    //closing part of some object
  }

  constructor(){
    console.log("TaskItemComponent: constructor");
  }
  removeTask(index: number){
    this.remove.emit(index);
    // this.newTasks = this.newTasks.filter((x) => x.id !== index);
  }
  isDoneChanged(){
    this.done.emit(this.task)
  }

}
