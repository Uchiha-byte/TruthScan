#!/usr/bin/env python3
"""
TruthScan - Defending Digital Truth Through Intelligent Content Verification Platform
Startup script for the TruthScan application
"""

import subprocess
import sys
import os
import webbrowser
import time
import threading

def install_requirements():
    """Install required packages"""
    print("🔧 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Requirements installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing requirements: {e}")
        return False

def start_backend():
    """Start the Flask backend server"""
    print("🚀 Starting TruthScan backend server...")
    try:
        from backend import app
        app.run(debug=True, port=5000, host='0.0.0.0')
    except Exception as e:
        print(f"❌ Error starting backend: {e}")

def open_browser():
    """Open browser after a short delay"""
    time.sleep(3)
    print("🌐 Opening TruthScan in your browser...")
    webbrowser.open('http://localhost:5000')

def main():
    """Main startup function"""
    print("=" * 60)
    print("🔍 TRUTHSCAN - Defending Digital Truth Through Intelligent Content Verification PLATFORM")
    print("=" * 60)
    print()
    
    # Check if requirements are installed
    try:
        import flask
        import flask_cors
        from PIL import Image
        print("✅ All required packages are already installed!")
    except ImportError:
        if not install_requirements():
            print("❌ Failed to install requirements. Please install manually:")
            print("   pip install -r requirements.txt")
            return
    
    print()
    print("🎯 Starting TruthScan services...")
    print("   • Backend API: http://localhost:5000")
    print("   • Frontend: http://localhost:5000")
    print("   • Dashboard: http://localhost:5000/dashboard")
    print("   • Detection: http://localhost:5000/detection")
    print("   • Intelligence: http://localhost:5000/intelligence")
    print("   • Reports: http://localhost:5000/reports")
    print()
    print("💡 Press Ctrl+C to stop the server")
    print("=" * 60)
    
    # Start browser in a separate thread
    browser_thread = threading.Thread(target=open_browser)
    browser_thread.daemon = True
    browser_thread.start()
    
    # Start the backend server
    start_backend()

if __name__ == "__main__":
    main()
