from classes import Debtor
import mysql.connector
import os

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='34313605',
    database='emprestimos',
    )
cursor = conexao.cursor()


def create_user(user_name, phone_number, indicated, cpf):

    user_name_ = user_name
    phone_number_ = phone_number
    indicated_ = indicated
    cpf_ = cpf
    comando = f'INSERT INTO customers (user_name, phone_number, indicated, cpf) VALUES ("{user_name_}", {phone_number_},"{indicated_}",{cpf_})'
    cursor.execute(comando)
    conexao.commit()


def create_debtor():

    name = input('coloque o nome do devedor:')
    while True:
        if contem_apenas_letras(name):
            break
        else:  
            name = input("Por favor, digite apenas letras: ")
    
    telefone = input('Digite o Celular: ')
    while True:
        if contem_apenas_numeros(telefone):
            break
        else:  
            telefone = input("Por favor, digite apenas numeros: ")

    cpf_ = input('digite o cpf do devedor:')
    while True:
        if contem_apenas_numeros(cpf_):
            break
        else:
            cpf_ = input("Por favor, digite apenas numeros: ")

    indicacao = input('foi por indicação? digite s ou n')
    while True:
        if contem_apenas_letras(indicacao):
            break
        else:
            indicacao = input("Por favor, digite apenas letras: ")
    
    if indicacao == 's':
        indicacao = input('digite o nome do indicador')
        while True:
            if not indicacao.isalpha():
                indicacao = input("Por favor, digite apenas letras: ")
            else:
                break
    else:
        indicacao = 'sem indicação'

    name = Debtor(name, telefone, cpf_, indicacao)

    name.display_info()

    create_user(name. name, telefone, indicacao, cpf_)

    return name.name


def create_loan():

    usuario = input("digite o nome do usuario que fez o emprestimo: ")
    while True:
        if contem_apenas_letras(usuario):
            break
        else:
            usuario = input("Por favor, digite apenas letras: ")

    total_amount = input("agora o valor do emprestimo:")
    while True:
        if contem_apenas_numeros(total_amount):
            break
        else:
            total_amount = input("Por favor, digite apenas numeros: ")

    num_installments = input("Por fim em quantas parcelas:")
    while True:
        if contem_apenas_numeros(num_installments):
            break
        else:  
            num_installments = input("Por favor, digite apenas numeros: ")

    consulta = "SELECT * FROM customers  "
    cursor.execute(consulta)
    resultado = cursor.fetchall()

    for linha in resultado:
        if usuario == linha[1]:
            usuario_certo = linha[0]
            break

    id_ = usuario_certo
    total_amount_ = total_amount
    num_installments_ = num_installments
    comando = f'INSERT INTO loans (customers_id, total_amount, num_installments) VALUES ({id_}, {total_amount_},{num_installments_})'
    cursor.execute(comando)
    conexao.commit()
    os.system('cls')
    print(f"Foi criado um emprestimo no valor de R$:{total_amount_},00 para o usuario:{usuario}")


def list_all_users():
    consulta = "SELECT * FROM customers  "
    cursor.execute(consulta)
    resultado = cursor.fetchall()

    for linha in resultado:
        print(f'Nome: {linha[1]}')
        print(f'Telefone: {linha[2]}')
        print(f'Indicação: {linha[3]}')
        print(f'Cpf: {linha[4]}')


def list_all_loans_user(user):

    consulta = "SELECT * FROM customers  "
    cursor.execute(consulta)
    resultado = cursor.fetchall()

    for linha in resultado:
        if user == linha[1]:
            usuario_certo = linha[0]
            break

    id_ = usuario_certo

    consulta = f"SELECT * FROM loans WHERE customers_id ={id_} "
    cursor.execute(consulta)
    retorno = cursor.fetchall()

    if retorno == []:
        os.system('cls')
        print("usuario sem emprestimos pendentes")
    else:
        for linha in retorno:
            print(f"{user}")
            print(f"Valor total={linha[1]}")
            print(f"Parcelas totais={linha[2]}")


def set_pagamento(user, valor_pagamento):

    consulta = "SELECT * FROM customers "
    cursor.execute(consulta)
    resultado = cursor.fetchall()

    for linha in resultado:
        if user == linha[1]:
            usuario_certo = linha[0]
            break

    id_ = usuario_certo

    consulta = f"SELECT * FROM loans WHERE customers_id ={id_} "
    cursor.execute(consulta)
    retorno_1 = cursor.fetchall()

    for linha in retorno_1:
        interno = int(linha[1])

    print(f"{user} Fez um pagamento no valor de:{valor_pagamento}")
    estado_atual = int(interno) - int(valor_pagamento)
    consulta = f"UPDATE loans SET total_amount = {estado_atual} WHERE customers_id = {id_}"
    cursor.execute(consulta)
    conexao.commit()
    cursor.fetchall
    print(f'Pronto, pagamento efetuado, o valor restante é {estado_atual}')
    
    if estado_atual <= 0:
        comando = f'DELETE FROM loans WHERE customers_id = {id_}'
        cursor.execute(comando)
        conexao.commit()
        print("Esse emprestimo teve fim")
    if estado_atual < 0:
        estado_atual = abs(estado_atual)
        print(f"O usuario pagou {estado_atual} a mais do que devia")


def contem_apenas_letras(texto):
    for caractere in texto:
        if caractere != ' ' and not caractere.isalpha():
            return False
    return True

def contem_apenas_numeros(input_):
    for caractere in input_:
        if caractere != ' ' and  not caractere.isdigit():
            return False
    return True

def delete_user(user):
    consulta = "SELECT * FROM customers  "
    cursor.execute(consulta)
    resultado = cursor.fetchall()
        
    for linha in resultado:
        if user == linha[1]:
            usuario_certo = linha[0]
            break

    id_ = usuario_certo

    comando = f'DELETE FROM customers  WHERE id = {id_}'
    cursor.execute(comando)
    conexao.commit() 


def create_payment():
    while True:
        request = input("por favor digite pra quem vai ser esse pagamento")
        if contem_apenas_letras(request):
            break
        else:  
            print("Por favor, digite apenas letras: ")
    while True:
        resquest_pay = input("por favor o valor do pagamento")
        if contem_apenas_numeros(resquest_pay):
            break
        else:  
            print("Por favor, digite apenas numeros: ")
    while True:
        try:
            os.system('cls')
            set_pagamento(request,resquest_pay) 
            break
        except UnboundLocalError:
                print("você precisa digitar um usuario cadastrado, e com dividas")
                create_payment()

def delete_user_from_db():
    user = input("Por favor digite o nome do usuario que vai ser deletado")
    while True:
        if contem_apenas_letras(user):
            break
        else:  
            user = input("Por favor, digite apenas letras: ")
    while True:
        try:
            delete_user(user)
            os.system("cls")
            print(f'Pronto o usuario:{user} foi deletado com sucesso')
            break 
        except UnboundLocalError:
            os.system('cls')
            print('Este usuario não esta cadastrado')
            break
