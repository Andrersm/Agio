

class Debtor:
    def __init__(self, name, phonenumber, cpf, indicated=''):
        self.name = name
        self.phonenumber = phonenumber
        self.indicated = indicated
        self.cpf = cpf
        self.emprestimos = []

    def add_lending(self, Lending):
        self.emprestimos.append(Lending)

    def display_info(self):
        print('Informações do devedor')
        print(f'Nome: {self.name}')
        print(f'CPF: {self.cpf}')
        print(f'Indicado por: {self.indicated}')
        print(f'Celular: {self.phonenumber}')


class Loan():
    def __init__(self, total_amount, num_installments, ):
        self.total_amount = total_amount
        self.num_installments = num_installments
        self.remaining_installments = None

    def __repr__(self):
        class_name = self.__class__.__name__
        return f'{class_name} valor total={self.total_amount}, parcelas='
        f'{self.num_installments} '

    def calculate_installment_value(self):

        pass

    def make_payment(self, amount_paid):

        pass
