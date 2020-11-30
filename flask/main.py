import os

from dotenv import load_dotenv

from bot import create_app

dotenv_path = os.path.join(os.path.dirname(__file__), ".flaskenv")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path, override=True)


app = create_app()
