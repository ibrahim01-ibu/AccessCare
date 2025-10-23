# AccessCare API Contracts

## Overview

This document defines the API contracts between frontend, backend services, and the OCR microservice.

## Authentication Endpoints

### POST /api/auth/register
```json
Request:
{
  "email": "user@example.com",
  "password": "password123",
  "name": "John Doe",
  "phone": "+1234567890"
}

Response:
{
  "success": true,
  "token": "jwt_token_here",
  "user": {
    "id": "user_id",
    "email": "user@example.com",
    "name": "John Doe"
  }
}
```

### POST /api/auth/login
```json
Request:
{
  "email": "user@example.com",
  "password": "password123"
}

Response:
{
  "success": true,
  "token": "jwt_token_here",
  "user": {
    "id": "user_id",
    "email": "user@example.com",
    "name": "John Doe"
  }
}
```

## Health Records Endpoints

### GET /api/health/records
```json
Response:
{
  "success": true,
  "records": [
    {
      "id": "record_id",
      "title": "Blood Test Results",
      "type": "lab_result",
      "date": "2024-01-15",
      "extracted_text": "Blood pressure: 120/80",
      "imageUrl": "https://cloudinary.com/image.jpg"
    }
  ]
}
```

### POST /api/health/records
```json
Request:
{
  "title": "New Health Record",
  "image": "file_upload"
}

Response:
{
  "success": true,
  "record": {
    "id": "new_record_id",
    "title": "New Health Record",
    "extracted_text": "OCR extracted text here"
  }
}
```

## Payment Endpoints

### GET /api/payment/history
```json
Response:
{
  "success": true,
  "transactions": [
    {
      "id": "transaction_id",
      "amount": 50.00,
      "recipient": "Merchant Name",
      "date": "2024-01-15",
      "status": "completed"
    }
  ]
}
```

### POST /api/payment/send
```json
Request:
{
  "recipientPhone": "+1234567890",
  "amount": 25.50,
  "description": "Payment for groceries"
}

Response:
{
  "success": true,
  "transaction": {
    "id": "transaction_id",
    "status": "pending",
    "confirmationCode": "123456"
  }
}
```

## Medicine Reminders Endpoints

### GET /api/medicine/reminders
```json
Response:
{
  "success": true,
  "reminders": [
    {
      "id": "reminder_id",
      "medicineName": "Aspirin",
      "dosage": "100mg",
      "frequency": "daily",
      "time": "09:00",
      "nextDose": "2024-01-16T09:00:00Z"
    }
  ]
}
```

### POST /api/medicine/reminders
```json
Request:
{
  "medicineName": "Aspirin",
  "dosage": "100mg",
  "frequency": "daily",
  "time": "09:00"
}

Response:
{
  "success": true,
  "reminder": {
    "id": "new_reminder_id",
    "medicineName": "Aspirin",
    "dosage": "100mg",
    "frequency": "daily",
    "time": "09:00"
  }
}
```

## SOS Endpoints

### POST /api/sos/trigger
```json
Request:
{
  "location": {
    "latitude": 40.7128,
    "longitude": -74.0060
  },
  "message": "Need immediate assistance"
}

Response:
{
  "success": true,
  "alertId": "alert_id",
  "contactsNotified": ["contact1@example.com", "contact2@example.com"]
}
```

### GET /api/sos/contacts
```json
Response:
{
  "success": true,
  "contacts": [
    {
      "id": "contact_id",
      "name": "Emergency Contact",
      "phone": "+1234567890",
      "relation": "family"
    }
  ]
}
```

## OCR Service Endpoint

### POST /extract_text
```json
Request: Multipart form data with image file

Response:
{
  "success": true,
  "text_blocks": [
    {
      "text": "Extracted text block",
      "confidence": 0.95,
      "bbox": [[x1,y1], [x2,y2], [x3,y3], [x4,y4]]
    }
  ],
  "full_text": "Complete extracted text"
}

Error Response:
{
  "error": "Error message description"
}
```

## Error Response Format

All API endpoints follow this error response format:

```json
{
  "success": false,
  "error": "Error message",
  "code": "ERROR_CODE"
}
```

## HTTP Status Codes

- 200: Success
- 201: Created successfully
- 400: Bad request
- 401: Unauthorized
- 403: Forbidden
- 404: Not found
- 500: Internal server error

## Rate Limiting

- API endpoints: 100 requests per minute
- OCR service: 20 requests per minute
- Upload size limit: 10MB per image

## Authentication

All endpoints except `/api/auth/*` require JWT token in Authorization header:

```
Authorization: Bearer <jwt_token>
```
