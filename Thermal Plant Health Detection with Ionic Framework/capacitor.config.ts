import { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
  appId: 'com.ms.myapp',
  appName: 'HydroTek Farm',
  webDir: 'www',
  server: {
    androidScheme: 'https'
  }

  plugins: {
    LocalNotifications: {
      smallIcon: 'ic_launcher', // Set the small icon for the notification (Android)
      iconColor: '#488aff', // Set the icon color for the notification (Android)
      sound: 'beep.mp3', // Optional: Set a custom sound file for the notification (Android)
    },
  },
};

export default config;
