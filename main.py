import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

print('|| Python + MySQL ||\n')
print('|| Meus Jogos Concluidos ||\n')

conexao = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_DATABASE")
)
print('Conexão realizada com sucesso!\n')

cursor = conexao.cursor()

cursor.execute('SELECT * FROM jogos_concluidos')

resultado = cursor.fetchall()

for jogo in resultado:
    print(jogo)

nome = input('Nome do jogo: ')
tempo = input('Horas jogadas: ')
platina = input('Possui platina? (S/N): ')

cursor.execute(
    "INSERT INTO jogos_concluidos (nome, tempo, platina) VALUES (%s, %s, %s)", (nome, tempo, platina)
)

conexao.commit()
print('Jogo cadastrado com sucesso!')