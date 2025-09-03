#!/usr/bin/env python3
"""
Script to set up a virtual environment for the XBRL analysis tool
"""

import subprocess
import sys
import os


def setup_virtual_environment():
    """Set up a virtual environment and install dependencies"""
    try:
        # Create virtual environment
        print("Creating virtual environment...")
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
        
        # Determine the path to the virtual environment's Python executable
        if os.name == 'nt':  # Windows
            venv_python = os.path.join("venv", "Scripts", "python.exe")
        else:  # Unix/Linux/macOS
            venv_python = os.path.join("venv", "bin", "python")
        
        # Upgrade pip
        print("Upgrading pip...")
        subprocess.run([venv_python, "-m", "pip", "install", "--upgrade", "pip"], check=True)
        
        # Install dependencies from requirements.txt
        if os.path.exists("requirements.txt"):
            print("Installing dependencies...")
            subprocess.run([venv_python, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
        
        print("Virtual environment setup complete!")
        print("\nTo activate the virtual environment, run:")
        if os.name == 'nt':  # Windows
            print("  venv\\Scripts\\activate")
        else:  # Unix/Linux/macOS
            print("  source venv/bin/activate")
        
        print("\nTo run the XBRL analysis tool:")
        print("  python main.py --file <path_to_xbrl_file>")
        
    except subprocess.CalledProcessError as e:
        print(f"Error during setup: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print("Error: Python not found. Please ensure Python is installed and in your PATH.")
        sys.exit(1)


if __name__ == "__main__":
    setup_virtual_environment()