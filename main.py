import mysql.connector
from dotenv import load_dotenv
import os
import time

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

# Função menu
def menu():
    while True:
        print('|| Biblioteca de jogos ||')
        print()
        print('''
    [ 1 ] Adicionar jogos.
    [ 2 ] Listar jogos adicionados.
    [ 3 ] Editar registros
    [ 4 ] Excluir registros
    [ 5 ] Sair...''')
        print()
        option = input('Escolher uma opção: ')
        if option == '1':
            adicionar()
        elif option == '2':
            listar()
            print('Deseja voltar ao menu?')
            resp = input('Sim/Não: ').strip().upper()
            while resp not in ['SIM','NÃO','NAO']:
                print('Digite SIM ou NÃO.')
                resp = input('Sim/Não: ').strip().upper()
            if resp == 'SIM':
                continue
            else:
                break
        elif option == '3':
            editar()
        elif option == '4':
            excluir()
        elif option == '5':
            break
        else:
            print('Opção inválida!')
        print('Voltando ao menu...')
        time.sleep(1)

# Função adicionar
def adicionar():
    nome = input('Nome do jogo: ').strip()
    while nome == '':
        print('Adicione um nome!')
        nome = input('Nome do jogo: ').strip()
    while True:
        try:
            tempo = float(input('Tempo de jogo: ').replace(',','.'))
            if tempo > 0:
                break
            else:
                print('O tempo deve ser maior que zero!')
        except ValueError:
            print('Valor inválido')
    platina = input('Concluido 100% (S/N): ').strip().upper()
    while platina not in ['S', 'N']:
        print('Você deve confirmar se possui conclusão 100%')
        platina = input('Concluido 100% (S/N): ').strip().upper()
    cursor.execute(
        'INSERT INTO jogos_concluidos (nome, tempo, platina) VALUES (%s,%s,%s)', (nome, tempo, platina)
    )
    conexao.commit()
    print()
    print('Jogo adicionado com sucesso!')
    print()

# Função listar
def listar():
    cursor.execute(
        'SELECT * FROM jogos_concluidos'
    )
    resultado = cursor.fetchall()
    if not resultado:
        print('Nenhum jogo cadastrado.')
        return
    for resultados in resultado:
        print(resultados)

# Função editar  
def editar():
    while True:
        try:
            id_jogo = int(input('Digite o ID: ').strip())
            break
        except ValueError:
            print('Digite um ID válido')
    cursor.execute(
        'SELECT * FROM jogos_concluidos WHERE ID = %s',(id_jogo,)
    )
    resultado = cursor.fetchone()
    if resultado is None:
        print('ID não encontrado!')
        return
    print()
    print('|| Registro atual ||')
    print(f'Nome: {resultado[1]}')
    print(f'Tempo: {resultado[2]}')
    print(f'Conclusão: {resultado[3]}')
    print('|| Registro atual ||')
    print()

    novo_nome = input('Digite o nome: ').strip()    
    while novo_nome == '':
        print('Nome inválido!')
        novo_nome = input('Digite o nome: ').strip()
    while True:
        try:
            novo_tempo = float(input('Tempo de jogo: ').replace(',','.'))
            if novo_tempo > 0:
                break
            else:
                print('Tempo precisa ser superior a 0')
        except ValueError:
            print('Valor inválido!')
    novo_platina = input('Concluido 100% (S/N): ').strip().upper()
    while novo_platina not in ['S','N']:
        print('Valor inválido!')
        print('Você deve confirmar se possui conclusão 100%')
        novo_platina = input('Concluido 100% (S/N): ').strip().upper()

    print('|||| EDIÇÃO ||||')
    print(f'{novo_nome}')
    print(f'{novo_tempo}')
    print(f'{novo_platina}')
    print()
    print('Deseja confirmar as alterações?')
    resp = input('(SIM/NÃO): ').strip().upper()
    while resp not in ['SIM','NÃO','NAO']:
        print('Digite SIM ou NÃO.')
        resp = input('(SIM/NÃO): ').strip().upper()
    if resp == 'SIM':
        cursor.execute(
            '''
            UPDATE jogos_concluidos
            SET nome = %s, tempo = %s, platina = %s
            WHERE ID = %s
            ''',
            (novo_nome, novo_tempo, novo_platina, id_jogo)
        )
        conexao.commit()
        print('Registro atualizado com sucesso!')
    else:
        return

# Função excluir
def excluir():
    while True:
        try:
            id_ex = int(input('Qual ID deseja excluir? ').strip())
            break
        except ValueError:
            print('Digite um ID válido')
    cursor.execute(
        'SELECT * FROM jogos_concluidos WHERE ID = %s', (id_ex,)
    )
    resultado = cursor.fetchone()
    if resultado is None:
        print('O ID não foi localizado.')
        return
    print(f'\nID selecionado: {resultado[0]}\nNome: {resultado[1]}\nTempo: {resultado[2]}\nConclusão: {resultado[3]}')
    print()
    confir = input('Deseja EXCLUIR? (SIM/NÃO): ').strip().upper()
    while confir not in ['SIM','NÃO','NAO']:
        print('Digite SIM ou NÃO')
        confir = input('Deseja EXCLUIR? (SIM/NÃO): ').strip().upper()
    if confir == 'SIM':
        cursor.execute(
            'DELETE FROM jogos_concluidos WHERE ID = %s',(id_ex,)
        )
        conexao.commit()
        print('Registro excluído com sucesso!')

menu()