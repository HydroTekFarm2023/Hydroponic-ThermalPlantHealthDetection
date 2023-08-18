import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-api-data',
  templateUrl: './api-data.page.html',
  styleUrls: ['./api-data.page.scss'],
})
export class ApiDataPage implements OnInit {
  apiData: any;

  constructor(private apiService: ApiService) { }

  ngOnInit(): void {
    this.fetchDataFromApi();
  }

  fetchDataFromApi(): void {
    this.apiService.get('color-detection').subscribe(
      (response) => {
        console.log('API Response:', response);
        this.apiData = response; // Save the API response data
      },
      (error) => {
        console.error('API Error:', error);
        // Handle errors here
      }
    );
  }
}
