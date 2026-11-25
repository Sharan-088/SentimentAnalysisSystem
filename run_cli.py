"""
Launcher script to run the CLI application from src folder
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Run main
from src.main import main

if __name__ == "__main__":
    main()
