# AccessCare Backend

Node.js + Express API server for the AccessCare accessibility super-app.

## Setup

1. Install dependencies:
```bash
npm install
```

2. Create `.env` file with:
```
MONGODB_URI=mongodb://localhost:27017/accesscare
PORT=5000
JWT_SECRET=your_jwt_secret_key
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_token
CLOUDINARY_CLOUD_NAME=your_cloudinary_name
CLOUDINARY_API_KEY=your_cloudinary_key
CLOUDINARY_API_SECRET=your_cloudinary_secret
```

3. Run the server:
```bash
npm start
```

## API Structure

- `/api/health` - Health record management
- `/api/payment` - Payment processing
- `/api/medicine` - Medicine reminders
- `/api/sos` - Emergency SOS features
- `/api/auth` - Authentication routes

## OCR Service

The OCR microservice is available in `/ocr-service` and runs on a separate Flask server.
