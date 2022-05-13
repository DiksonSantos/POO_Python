from datetime import datetime
import pytz
from random import randint


class ContaCorrente:

    """Cria um objeto 'Conta COrrente' """
    @staticmethod
    def _data_hora():
        fuso_confuso = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_confuso)
        return horario_BR.strftime('%d/%m/%Y')

    def __init__(self, nome, cpf, ag, cc):
        """ Dois __ (Underlines) Significa= Esconder informação/conteudo da variavel ==
        'Imprintavel'  """
        self.nome = nome
        self.cpf = cpf
        self._saldo = 0
        self._limite = 0  # OU None
        self.agencia = ag
        self.num_cont = cc
        self._transations = []
        self._cartoes = []


    def conultar_saldo(self):
        return f"Valor em Conta: {self._saldo:,.2f} R$"   # :,.2f

    def depositar(self, valor):
        self._saldo += valor
        self.conultar_saldo()
        self._transations.append([valor, "Saldo:", self._saldo, "R$", ContaCorrente._data_hora()])

    def _limite_conta(self):
        """o underline no inicio sinaliza que o metodo foi feito exclusivamente para ser usado dentro de outro
        método. OU, ele nao e editavel (EX: Saldo) Como em outros casos onde inserimos um novo valor fora desta DEF
        para a variavel
         que existe dentro dela. EX; self.limite = 'Outro_Valor'  -> Isso nao seria possivel, graças ao _limit...
         Para modificar esta Variavel, então, seria necessário Criar Outro método (para fazer isso)."""
        """Cheque especial de 1.000 R$ """
        self._limite = -1000
        return self._limite

    def sacar(self, saque):
        if self._saldo - saque < self._limite_conta():
            print('Saldo Insuficiente')
            print(self.conultar_saldo())
            breakpoint()
        else:
            self._saldo -= saque
            print(f"Valor do Saque: {saque:,.2f} R$ - Restante: {conta_Dikson._saldo:,.2f} R$ \n"
                  f"Limite Disponivel: {self._limite * -1:,.2f} R$")
            self._transations.append([saque, "Saldo:", self._saldo, ContaCorrente._data_hora()])

    def consultar_Limites(self):
        lim = self._limite * -1
        return lim

    def consultar_historico(self):
        print("Historico de Transações")
        for transation in self._transations:
            print(transation)

    def transferir(self, valor, destino):

        self._saldo -= valor
        self._transations.append([-valor, self._saldo, ContaCorrente._data_hora()])
        destino._saldo += valor
        return destino._transations.append([-valor, self._saldo, ContaCorrente._data_hora()])


class CartaoCredito:

    @staticmethod
    def _data_hora():
        fuso_confuso = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_confuso)
        return horario_BR #.strftime('%Y')   # Podemos usar -> .moth OU .year

    def __init__(self, titular, Conta_Corrente):
        # Gera numeros aleatorios de 1 até 9
        self.numero = randint(1000000000000000, 9999999999999999)
        self.titular = titular
        # Usando a classe Estática de cima  -   O '+5'  Adiciona os 5 anos de validade do cartão.
        self.validade = f" Mês: {CartaoCredito._data_hora().month}, Ano: {CartaoCredito._data_hora().year+5}"  # Como aqui
        self.Cod_Seg = f" {randint(0, 9)}{randint(0, 9)}{randint(0, 9)}" # Gera numeros entre 0 & 9
        self.Limite = 1.000
        # Precisaria de um Método SET pra redefinir o valor de _senha:
        self._senha = '1234'
        self.Conta_Corrente = Conta_Corrente
        # Adicionando todas as caracteristicas/informações do CC a cima, na Lista -> Use -> Conta_Nome._cartoes
        Conta_Corrente._cartoes.append(self)

# METODO GET
    @property
    def senha(self):
        """@property torna isto um atributo"""
        return f"Sua senha Atual é: {self._senha}"

# METODO SET
    @senha.setter
    def senha(self, valor):
        """Isso cria uma logica regulamentando as propriedades de mudança de senha
        No caso-> Ter 4 digitos e ser do tipo numerica"""
        if len(valor) == 4 and valor.isnumeric():
            self._senha = valor
            print('Senha alterada com Sucesso !')
        else:
            print('Nova senha Invalida')# Nãoa ceitou um Return nesta linha




# # Testando  -  Criando Conta
conta_Dikson = ContaCorrente('Dikson', '333555333-06', '1775', '000333')

# Metodo Direto:
# conta_Dikson.saldo = 10000
#depositar = float(input("Valor a Depositar: "))
depositar = 20.000
# Usando Função p/ Depositar:
conta_Dikson.depositar(depositar)


print(conta_Dikson.conultar_saldo())
#print(conta_Dikson.cpf)

# Sacando:
#sacar = float(input("Valor Do Saque: R$ "))
#conta_Dikson.sacar(sacar)

#print(conta_Dikson.conultar_saldo())
#print(f"Agência: {conta_Dikson.agencia}, Conta_Corrente: {conta_Dikson.num_cont}")

print("--"*20)

#print(conta_Dikson.transations)
#print(conta_Dikson.consultar_historico())

conta_reserva = ContaCorrente('Reserva', '333555444-09', '1775', '000555')
#print('Saldo Conta Reserva: ', conta_reserva._saldo)

# Transferindo $ P/ COnta Reserva:
# BUG -> Ele não esta verificando se tem saldo na conta de origem, por isso sempre vai constar os 5 MIL no Saldo reserva.
#conta_Dikson.transferir(5000, conta_reserva)
#print('Saldo Da Conta Reserva: ', conta_reserva._saldo)

#print(help(ContaCorrente))


# RODANDO CLASS CARTÃO DE CREDITO:

conta_Dikson = ContaCorrente("Gow Dikson Rodrigues dos Santos", "111,222,333,45", 4444, 4562)

# Este objeto recebeu como parametro um outro Objeto, que contém a Classe ContaCorrente e seus itens
# ..agora o objeto Cartão_Dikson pode acessar informações da classe 'ContaCorrente' EX:
# print(Cartao_Dikson.Conta_Corrente.nome) A informação 'nome' vem da Conta Corrente, (acessada pela Classe Cartão de Credito)
Cartao_Dikson = CartaoCredito('Dikson Santos', conta_Dikson)
print(Cartao_Dikson.Conta_Corrente.agencia)
print(Cartao_Dikson.Conta_Corrente.num_cont)

# Informações em Caertão De Credito:
print('Titular: ',conta_Dikson._cartoes[0].titular)
print('Número do Cartão: ',conta_Dikson._cartoes[0].numero)
print('Codigo de Segurança: ',conta_Dikson._cartoes[0].Cod_Seg)




#print(conta_Dikson._cartoes[0].Conta_Corrente.agencia)

# Conferindo Data e Hora
print(f"Ano de Validade Do cartão: {Cartao_Dikson.validade}")


Cartao_Dikson.senha = '3636'
print(Cartao_Dikson.senha)

Cartao_Dikson.senha = '36'
print(Cartao_Dikson.senha)

#print(conta_Dikson.__dict__)


infos_conta = []

infos_conta.append(conta_Dikson.__dict__)

for I in infos_conta:
    print(I)

print(Cartao_Dikson.__dict__)
