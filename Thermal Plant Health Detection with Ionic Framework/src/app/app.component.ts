// import { Component, OnInit } from '@angular/core';
// import { ApiService } from './api.service';

// @Component({
//   selector: 'app-root',
//   templateUrl: './app.component.html',
//   styleUrls: ['./app.component.scss']
// })
// export class AppComponent implements OnInit {
//   apiData: any;

//   constructor(private apiService: ApiService) { }

//   ngOnInit(): void {
//     // Call the API when the component initializes
//     this.fetchDataFromApi();
//   }

//   fetchDataFromApi(): void {
//     // Replace 'endpoint' with the actual endpoint of the API you want to call
//     this.apiService.get('color-detection').subscribe(
//       (response) => {
//         console.log('API Response:', response);
//         this.apiData = response; // Save the API response data
//       },
//       (error) => {
//         console.error('API Error:', error);
//         // Handle errors here
//       }
//     );
//   }
// }

import { Component, OnInit } from '@angular/core';
import { ApiService } from './api.service';
import { LocalNotifications } from '@capacitor/local-notifications'; // Import the LocalNotifications plugin

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent implements OnInit {
  apiData: any;

  constructor(private apiService: ApiService) {}

  ngOnInit(): void {
    // Call the API when the component initializes
    this.fetchDataFromApi();
  }

  fetchDataFromApi(): void {
    this.apiService.get('color-detection').subscribe(
      (response) => {
        console.log('API Response:', response);
        this.apiData = response; // Save the API response data

        // Display local notification if Red Percentage is greater than 20
        if (this.apiData['Red Percentage'] > 20) {
          this.showNotification('Plant Unhealthy!', 'Status: Plant Unhealthy!');
        }
      },
      (error) => {
        console.error('API Error:', error);
        // Handle errors here
      }
    );
  }

  // Function to show local notification
  async showNotification(title: string, body: string) {
    await LocalNotifications.requestPermissions(); // Request permission to show notifications (required for iOS)

    await LocalNotifications.schedule({
      notifications: [
        {
          title: title,
          body: body,
          id: 1,
          schedule: { at: new Date(Date.now() + 1000) }, // Show the notification after 1 second
          actionTypeId: '', // Optional: Set an action type ID for handling actions when the notification is clicked
          extra: null, // Optional: Add extra data to the notification payload
        },
      ],
    });
  }
}

