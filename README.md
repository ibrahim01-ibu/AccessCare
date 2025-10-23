# AccessCare - Accessibility Super-App for Blind Users

A comprehensive mobile application designed to enhance independence and accessibility for blind and visually impaired users through integrated OCR, voice navigation, health management, and emergency services.

## 🚀 Quick Start

### Prerequisites
- Node.js 18+
- Python 3.9+
- MongoDB
- Expo CLI
- Docker (optional)

### Setup for Development

1. **Clone and setup:**
```bash
git clone <repository-url>
cd AccessCare
npm install
```

2. **Backend Setup:**
```bash
cd backend
npm install
cp ../shared/.env.example .env  # Update with your API keys
npm start
```

3. **OCR Service Setup:**
```bash
cd backend/ocr-service
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

4. **Frontend Setup:**
```bash
cd frontend
npm install
cp .env.example .env  # Update API URLs
npm start
```

### Docker Setup (Recommended)

```bash
# Start all services
docker-compose up --build

# Stop services
docker-compose down
```

## 📱 Features

### 🔍 OCR Text Recognition
- Real-time text extraction from images using EasyOCR
- Voice playback of extracted text
- Support for prescriptions, documents, and labels
- High accuracy optical character recognition

### 🏥 Health Management
- Digital health record storage
- Medicine reminder system with voice alerts
- Prescription tracking and refill reminders
- Voice-guided health data entry

### 💳 Payment Processing
- Voice-guided payment transfers
- Transaction history with audio playback
- Integration with major payment providers
- Secure authentication methods

### 🆘 Emergency SOS
- One-tap emergency alerts
- Automatic location sharing with contacts
- Voice-activated emergency calls
- Emergency contact management

### 🔊 Voice Navigation
- Complete voice-guided interface
- Screen reader compatibility
- Voice command recognition
- High-contrast, accessibility-focused UI

## 🏗️ Project Structure

```
AccessCare/
├── backend/                   # Node.js + Express API
│   ├── api/                   # Feature-specific API routes
│   ├── models/                # Mongoose DB schemas
│   ├── ocr-service/           # Flask OCR microservice
│   ├── middleware/            # Auth, logging, error handling
│   └── server.js              # Main backend entrypoint
├── frontend/                  # React Native (Expo) app
│   ├── src/
│   │   ├── screens/           # Feature screens
│   │   ├── components/        # Reusable UI components
│   │   ├── services/          # API service modules
│   │   └── assets/            # Images, fonts, etc.
│   └── App.js                 # Main frontend entrypoint
├── shared/                    # Shared documentation
│   ├── api-contracts.md       # Complete API specification
│   └── design-flows/          # UX flows and diagrams
├── docker/                    # Docker configurations
├── docs/                      # Documentation and pitch deck
└── docker-compose.yml         # Multi-service orchestration
```

## 👥 Team Collaboration

### Branching Model
- `main` - Production-ready code
- `feature/<feature-name>` - Individual feature branches
- `integration` - Integration testing branch

### Workflow Rules
1. Pull latest from `main` before starting new work
2. Create feature branches from `main`
3. Test integration locally before merging
4. Document API contracts in `/shared/api-contracts.md`
5. Update documentation in `/docs/` as features evolve

### Environment Setup for Teammates
1. Ensure identical folder structure locally
2. Copy `.env.example` files and add your API keys
3. Run services separately for development or use Docker
4. Test integration with at least one other teammate's feature before PR

## 🔧 Development Commands

```bash
# Backend
cd backend && npm start              # Start API server
cd backend/ocr-service && python app.py  # Start OCR service

# Frontend
cd frontend && npm start             # Start Expo development server
npm run android                      # Run on Android device/emulator
npm run ios                          # Run on iOS device (macOS only)
npm run web                          # Run in web browser

# Docker
docker-compose up --build            # Start all services
docker-compose down                  # Stop all services
docker-compose logs -f               # View logs
```

## 📋 API Overview

### Authentication
- `POST /api/auth/register` - User registration
- `POST /api/auth/login` - User login

### Health Records
- `GET /api/health/records` - Get user health records
- `POST /api/health/records` - Upload and OCR health documents

### Payments
- `GET /api/payment/history` - Payment history
- `POST /api/payment/send` - Send money to contacts

### Medicine
- `GET /api/medicine/reminders` - Get medicine reminders
- `POST /api/medicine/reminders` - Create new reminder

### SOS Emergency
- `POST /api/sos/trigger` - Trigger emergency alert
- `GET /api/sos/contacts` - Get emergency contacts

### OCR Service
- `POST /extract_text` - Extract text from images

## 🔒 Security & Privacy

- JWT-based authentication
- Encrypted data transmission (HTTPS)
- Secure image storage with Cloudinary
- HIPAA-compliant health data handling
- Regular security audits and updates

## 🌟 Accessibility Features

- Screen reader compatibility (VoiceOver, TalkBack)
- Voice command recognition
- High contrast UI design
- Large touch targets (44x44px minimum)
- Audio feedback for all actions
- Braille display support

## 🚀 Deployment

### Production Deployment
```bash
# Build and deploy Docker containers
docker-compose -f docker-compose.prod.yml up -d

# Deploy to Vercel (frontend)
cd frontend && npx vercel --prod

# Deploy to MongoDB Atlas (database)
# Update MONGODB_URI in production .env
```

### Environment Variables
```
# Backend
MONGODB_URI=mongodb://localhost:27017/accesscare
JWT_SECRET=your_jwt_secret
PORT=5000

# OCR Service
FLASK_ENV=production

# Frontend
API_BASE_URL=https://your-backend-url.com
OCR_SERVICE_URL=https://your-ocr-service.com
```

## 📞 Support & Contact

For hackathon support or questions:
- Join our Discord server
- Check `/docs/` for detailed guides
- Review `/shared/api-contracts.md` for API documentation

## 📄 License

MIT License - see LICENSE file for details

---

**Built for accessibility. Designed for independence.** ♿
>>>>>>> 114c9eb (Initial monorepo scaffold: backend, frontend, shared, docker configs)
