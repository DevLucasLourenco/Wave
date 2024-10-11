import subprocess
import sys

try:
    import openpyxl
except ImportError:
    subprocess.run([sys.executable, "-m", "pip", "install", "openpyxl"])

try:
    import pandas
except ImportError:
    subprocess.run([sys.executable, "-m", "pip", "install", "pandas"])
