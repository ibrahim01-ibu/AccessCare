# AccessCare Frontend

React Native (Expo) mobile app for the AccessCare accessibility super-app.

## Setup

1. Install dependencies:
```bash
npm install
```

2. Copy `.env.example` to `.env` and update with your API endpoints:
```bash
cp .env.example .env
```

3. Run the app:
```bash
# For Android
npm run android

# For iOS (macOS required)
npm run ios

# For web
npm run web
```

## Features

- **Accessibility First**: Voice-guided navigation and screen reader support
- **OCR Integration**: Text extraction from images using EasyOCR
- **Health Records**: Manage health documents and medications
- **Payment Processing**: Send and receive money with voice guidance
- **SOS Features**: Emergency contacts and location sharing
- **Voice Navigation**: Text-to-speech for all UI elements

## Project Structure

- `src/screens/` - Feature-specific screens (HealthRecordScreen.js, PaymentScreen.js, etc.)
- `src/components/` - Reusable UI components
- `src/services/` - API service modules by feature
- `src/assets/` - Images, fonts, accessibility aid files

## Dependencies

- React Navigation for app navigation
- Axios for API communication
- Expo Camera for image capture
- Expo Location for GPS services
- React Native TTS for voice output
- Expo Haptics for tactile feedback
