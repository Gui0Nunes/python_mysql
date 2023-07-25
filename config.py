import mysql.connector
import os
import dotenv
from dotenv import load_dotenv
dotenv.load_dotenv(dotenv.find_dotenv('./env/.env'))

localhost = os.getenv('host')
login = os.getenv('user')
senha = os.getenv('password')
banco = os.getenv('database')

conexao = mysql.connector.connect(
    host=localhost,
    user=login,
    password=senha,
    database=banco
)
cursor = conexao.cursor()