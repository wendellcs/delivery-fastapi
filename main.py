from fastapi import FastAPI
from passlib.context import CryptContext
from dotenv import load_dotenv
import os

app = FastAPI()
load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

from auth_routes import  auth_router
from order_routes import order_router

# Incluindo as rotas
app.include_router(auth_router)
app.include_router(order_router)

# Rest APIs
# Enviamos e recebos informações no formato JSON.

# endpoint: é a URL que o usuário vai acessar para interagir com a API.
# ex: /ordens -> path, caminho para acessar a API de ordens. 