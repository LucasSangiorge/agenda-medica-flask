import os 
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-change-me")
    DATABASE_PATH = os.getenv("DATABASE_PATH", "agenda.db")
    MOCK_API_URL = os.getenv("MOCK_API_URL", "http://localhost:5000/api/agendamentos")