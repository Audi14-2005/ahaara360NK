#!/usr/bin/env python3
"""
Deployment script for AAHAARA 360
This script helps prepare the project for deployment to Render
"""

import os
import subprocess
import sys

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e.stderr}")
        return False

def main():
    print("🚀 AAHAARA 360 Deployment Preparation")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists('manage.py'):
        print("❌ Error: manage.py not found. Please run this script from the project root.")
        sys.exit(1)
    
    # Install dependencies
    if not run_command("pip install -r requirements.txt", "Installing dependencies"):
        sys.exit(1)
    
    # Collect static files
    if not run_command("python manage.py collectstatic --noinput", "Collecting static files"):
        sys.exit(1)
    
    # Run migrations
    if not run_command("python manage.py migrate", "Running database migrations"):
        sys.exit(1)
    
    # Sync Capacitor
    if not run_command("npx cap sync android", "Syncing Capacitor project"):
        print("⚠️  Warning: Capacitor sync failed, but continuing...")
    
    print("\n✅ Deployment preparation completed!")
    print("\nNext steps:")
    print("1. Push your code to GitHub")
    print("2. Deploy to Render using the render.yaml configuration")
    print("3. Set environment variables in Render dashboard")
    print("4. Test your deployment")
    print("\nFor detailed instructions, see DEPLOYMENT_GUIDE.md")

if __name__ == "__main__":
    main()
