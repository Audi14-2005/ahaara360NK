# AAHAARA 360 Deployment Guide

## Deploying to Render

### Prerequisites
1. Create a Render account at [render.com](https://render.com)
2. Connect your GitHub repository to Render

### Steps to Deploy

1. **Push your code to GitHub**:
   ```bash
   git add .
   git commit -m "Prepare for Render deployment"
   git push origin main
   ```

2. **Deploy on Render**:
   - Go to [render.com](https://render.com)
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select your repository
   - Use these settings:
     - **Name**: `aahaara-360-backend`
     - **Environment**: `Python 3`
     - **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
     - **Start Command**: `gunicorn myproject.wsgi:application`
     - **Plan**: Free

3. **Environment Variables**:
   Set these in Render dashboard:
   - `DEBUG`: `False`
   - `SECRET_KEY`: Generate a new secret key
   - `ALLOWED_HOSTS`: `aahaara-360-backend.onrender.com`
   - `GEMINI_API_KEY`: Your Gemini API key

4. **Deploy**:
   - Click "Create Web Service"
   - Wait for deployment to complete
   - Your app will be available at: `https://aahaara-360-backend.onrender.com`

## Mobile App Configuration

### Update Capacitor Config
The `capacitor.config.json` is already configured to point to your production URL.

### Build and Deploy Mobile App

1. **Sync the project**:
   ```bash
   npx cap sync android
   ```

2. **Open in Android Studio**:
   ```bash
   npx cap open android
   ```

3. **Build APK**:
   - In Android Studio, go to Build → Build Bundle(s) / APK(s) → Build APK(s)
   - The APK will be generated in `android/app/build/outputs/apk/`

## Testing the Deployment

1. **Test Backend**:
   - Visit: `https://aahaara-360-backend.onrender.com`
   - Check admin panel: `https://aahaara-360-backend.onrender.com/admin/`

2. **Test Mobile App**:
   - Install the APK on your Android device
   - Test all features and API connections

## Features Available

- 🍎 **Diet Planner**: Personalized Ayurvedic diet plans
- 📱 **Food Scanner**: AI-powered food analysis
- 🏥 **Medical OCR**: Document analysis
- 💬 **Health Chat**: AI health assistant
- 👤 **User Management**: Authentication and profiles

## Troubleshooting

### Common Issues

1. **Static files not loading**:
   - Run: `python manage.py collectstatic --noinput`
   - Check WhiteNoise configuration

2. **CORS errors**:
   - Verify CORS settings in `settings.py`
   - Check `ALLOWED_HOSTS` configuration

3. **Database issues**:
   - Run migrations: `python manage.py migrate`
   - Check database configuration

### Support

For issues or questions, check the logs in Render dashboard or contact the development team.
