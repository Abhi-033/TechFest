from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

print("API_KEY",API_KEY)   
