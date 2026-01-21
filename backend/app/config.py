from dotenv import load_dotenv
import os

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "Nidan Vitals APIs")
DEBUG = os.getenv("DEBUG", "True") == "True"
HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", 8000))
ENV = os.getenv("ENV", "development")