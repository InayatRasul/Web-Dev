import { Component, Input } from '@angular/core';
import { HousingLocation } from '../housing-location';
import { DetailsComponent } from '../details/details.component';

@Component({
  selector: 'app-housing-location',
  imports: [DetailsComponent],
  templateUrl: './housing-location.component.html',
  styleUrls: ['./housing-location.component.css']
})
export class HousingLocationComponent {
  @Input() housingLocation!:HousingLocation;
}
