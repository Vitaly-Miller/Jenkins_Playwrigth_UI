"""
BASE DATA
"""
from dotenv import load_dotenv
import os

#=======================================================================================================================
# Reading _.env
load_dotenv()

class Base:
    # Base URL
    URL = os.getenv('BASE_URL')                     # Base URL

    # Admin data
    USERNAME = os.getenv('USERNAME')                # Username (Admin)
    PASSWORD = os.getenv('PASSWORD')                # Password (Admin)
    API_TOKEN = os.getenv('API_TOKEN')              # Сгенерирован в admin-аккаунте Jenkins

