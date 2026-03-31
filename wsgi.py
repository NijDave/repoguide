import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
os.environ['PYTHONPATH'] = os.path.dirname(__file__)

from src.app import app

app.template_folder = os.path.join(os.path.dirname(__file__), 'src', 'templates')

if __name__ == "__main__":
    app.run()
