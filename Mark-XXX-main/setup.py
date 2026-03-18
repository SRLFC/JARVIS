import subprocess
import sys
import os

# Get the directory where setup.py is actually located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REQ_PATH = os.path.join(BASE_DIR, "requirements.txt")

print(f"Installing requirements from: {REQ_PATH}...")
try:
    subprocess.run([sys.executable, "-m", "pip", "install", "-r", REQ_PATH], check=True)
    
    print("Installing Playwright browsers...")
    subprocess.run([sys.executable, "-m", "playwright", "install"], check=True)
    
    print("\n✅ Setup complete! Run 'python main.py' to start your assistant.")
except subprocess.CalledProcessError as e:
    print(f"\n❌ Setup failed: {e}")
