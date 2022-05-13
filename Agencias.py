from random import randint

class Agencias:
    def __init__(self, telefone, cnpj, numero_agencia):
        self.Telefone = telefone
        self.CNPJ = cnpj
        self.NUMERO = numero_agencia
        self.clientes = []
        self.recursos = 0
        self.emprestimos = []



    def verificar_recursos(self):
        if self.recursos < 1000000:
            print(f'Pouco Dinheiro em Caixa -> {self.recursos}')
        else:
            print(f'Valor Okay -> {self.recursos}')


    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.recursos > valor:
            self.emprestimos.append((valor, cpf, juros))
        else:
            print('Saldo Não disponivel')



    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))



class AgenciaVirtual(Agencias):
    """Se não criamos um '__init__' aqui. Esta classe simplesmente importa tudo da classe mãe
    ('Agencia').
     Caso definamos um __init__ aqui, este irá substituir o __ini__ da classe principal """
    # Anunciamos os recusroso que esta classe vai ter:
    def __init__(self, site, telefone, cnpj):
        self.SITE = site
        # Dos métodos anunciados a cima, serão usados os da classe superior (ao invés de serem criados aqui)
        # A baixo estamos usando (da classe superior) Telefone, CNPJ, Numero Da Agencia.
        super().__init__(telefone, cnpj, 1000)# Esta linha esta pegando os métodos da classe principal 'Agencias'
        self.recursos = 40000
        # Exclusivo desta classe
        self.caixa_paypal = 0

    def depositar_paypal(self, valor):
        # Retirou valor dos recursos
        self.recursos -= valor
        # Inseriu valor no PayPal
        self.caixa_paypal += valor

    def sacar_paypal(self, valor):
        # Retira da conta PayPal
        self.caixa_paypal -= valor
        # Insere Na conta comum
        self.recursos += valor


class AgenciaComum(Agencias):
    """Estes são os elementos/variaveis que esta DEF precisa"""
    def __init__(self, telefone, cnpj):
        # Estes são seus iguais provenientes da super Classe
        super().__init__(telefone, cnpj, numero_agencia=randint(1001, 9999))
        self.recursos = 1000000000000


class AgenciaPremium(Agencias):
    """Estes são os elementos/variaveis que esta DEF precisa"""
    def __init__(self, telefone, cnpj):
        # Estes são seus iguais provenientes da super Classe - POLIMORFISMO(?)
        super().__init__(telefone, cnpj, numero_agencia=randint(1001, 9999))
        self.recursos = 10000000

    """def adicionar_cliente(self, nome, cpf, patrimonio):
        if patrimonio > 1000000:
            super().adicionar_cliente(nome=nome, cpf=cpf, patrimonio=patrimonio)
        else:
            print('Patrimonio Inferior a Um Milhão')"""

    def adicionar_cliente(self, nome, cpf, patrimonio):
        if patrimonio > 1000000:
            super().adicionar_cliente(nome, cpf, patrimonio)
        else:
            print('O Cliente não tem o patrimônio mínimo necessário para entrar na Agência Premium')



# O Código a baixo só roda aqui, e Não nos Arquivos que importarem este Script:
if __name__ == '__main__':


    #agencia_01 = Agencias(2345678, 315315315.06, 000000.17)

    #agencia_01.recursos = 2000000

    #agencia_01.verificar_recursos()

    # Valor, CPF,
    #agencia_01.emprestar_dinheiro(1500, 31531531506, 0.02)
    #print(agencia_01.emprestimos)


    #agencia_01.adicionar_cliente('Tomé', 111222333.06, 1000000)
    #print(agencia_01.clientes)

    Ag_Virt = AgenciaVirtual('www.site.com.br', 2223355, 33355533306)
    #print(Ag_Virt.verificar_recursos())
    #print(Ag_Virt.recursos, Ag_Virt.SITE, Ag_Virt.CNPJ, Ag_Virt.clientes)



    agencia_comum = AgenciaComum(40283135, 33355533306)
    #print('CNPJ: ', agencia_comum.CNPJ)
    #print(agencia_comum.caixa)
    #agencia_comum.verificar_recursos()
    #print(agencia_comum.NUMERO)
    #print(agencia_comum.recursos)


    ag_premium = AgenciaPremium(222333666555, 555666444778899)
    #ag_premium.verificar_recursos()

    #Ag_Virt.depositar_paypal(5000)
    #print('Recursos Ag Virt: ', Ag_Virt.recursos)

    #print('Saldo no PayPal: ', Ag_Virt.caixa_paypal)


    #AgenciaPremium.adicionar_cliente(nome='Dikson', cpf=315, patrimonio=200000)


    agencia_comum.adicionar_cliente('Gow', 333, 200)
    print(agencia_comum.clientes)



    agencia_premium = AgenciaPremium(40282828, 31531531506)

    agencia_premium.adicionar_cliente('Diskon', 315, 20000000)
    print(agencia_premium.clientes)
