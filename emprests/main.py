from func import (create_debtor, create_loan, list_all_users,
                  list_all_loans_user, contem_apenas_letras,
                  create_payment, delete_user_from_db)
from func import conexao, cursor
import mysql.connector
import os


print("Bem vindo ao AGIO")  # Agiotagem gourmet inteligente e organizada
while True:
    Instruction = input('Agora escolha a ação que deseja executar:\n(c)'
                        'Criar um novo usuario\n(r)Registrar um novo'
                        'pagamento\n(l)listar todos os usuarios \n(s)Sair do'
                        'programa\n(g)listar todos os emprestimos de um '
                        'usuario\n(e)Registrar novo emprestimo\n(d)Deletar'
                        ' usuario\n')
    instructionc = Instruction[0]
    instructionc = instructionc.upper()
    if instructionc == "C":
        while True:
            try:
                func_return = create_debtor()
                os.system('cls')
                print(f"parabens Você criou uma conta para {func_return}")
                break
            except mysql.connector.errors.IntegrityError:
                os.system('cls')
                print('O nome do usuario que você tentou criar já consta no'
                      'banco de dados, os nomes no banco de dados devem ser'
                      'unicos, digite novamente os dados!')

    elif instructionc == 'S':
        os.system('cls')
        break
    elif instructionc == 'E':
        while True:
            try:
                create_loan()
                break
            except UnboundLocalError:
                print("você precisa digitar um usuario cadastrado PATETA")

    elif instructionc == 'L':
        os.system('cls')
        list_all_users()

    elif instructionc == 'G':
        request = input("Por favor digite o nome do usuario que voce deseja"
                        "listar seus emprestimos: ")
        while True:
            if contem_apenas_letras(request):
                break
            else:
                request = input("Por favor, digite apenas letras: ")

        try:
            list_all_loans_user(request)

        except UnboundLocalError:
            os.system('cls')
            print("Usuario não cadastrato ")

    elif instructionc == 'R':
        resultado = create_payment()

    elif instructionc == 'D':
        delete_user_from_db()
    else:
        break

try:
    conexao.close()
    cursor.close()
    print('Programa finalizado')
except mysql.connector.Error as erro:
    print('não fechou essa bosta', erro)
