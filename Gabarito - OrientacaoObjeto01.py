# Criando nossa 1ª Classe em Python
# Sempre que você quiser criar uma classe, você vai fazer:
#
# class Nome_Classe:
#
# Dentro da classe, você vai criar a "função" (método) __init__
# Esse método é quem define o que acontece quando você cria uma instância da Classe
#
# Vamos ver um exemplo para ficar mais claro, com o caso da Televisão que a gente vinha comentando

#classes Para Usar nos programas.
class TV:

    # Parametro imutável:
    cor = 'preta'

    # O 'Self' no parenteses, faz com que esses atributos sejam acessiveis do lado
    #..de fora desta função DEF inicial Ex: tv_quarto.canal ...
    # Caso não houvesse o self EX Variavel = '4K'  -> Esta variavel só seria
    #..acessivel de dentro desta identação ou função.
    def __init__(self, tamanho): # Agora 'tamanho' deve ser passado como parametros/argumentos

        self.ligada = False
        self.tamanho = tamanho
        self.canal = "Netflix"
        self.volume = 10

    def mudar_canal(self, novo_canal):
        self.canal = novo_canal


    def aumentar_volume(self):
        self.volume += 10

    def diminuir_volume(self):
        self.volume -= 10



# Programa que usa a classe

# Agora o tamanho deve ser especificado como argumento da classe.
tv_sala = TV(55)
tv_quarto = TV(29)

#print('Tamanhos das TVs:\n', 'Quarto:', tv_quarto.tamanho, 'Sala: ', tv_sala.tamanho)


# Mudou de NetFlix para SBT Ou qualquer outro, graças á variavel na função.
tv_sala.mudar_canal("SBT")
tv_quarto.mudar_canal('Record')

# Mostra o novo canal
#print(tv_sala.canal)

# A da sala não teve o canal mudado. Então é mostrado o canal inicial
#print(tv_quarto.canal)

# Modificando um Atributo Herdado
#tv_quarto.tamanho = 22

# Agora o tamanho não é mais o padão da classe. Herdamos e modificamos o atributo.
#print('Tamanho da TV (Quarto): ', tv_quarto.tamanho)

tv_quarto.aumentar_volume()
#print('Volume: ', tv_quarto.volume)

# Mostrando o Atributo 'Imutavel'
print(tv_quarto.cor)

# Mudando o atributo 'Imutavel':
TV.cor = 'Roxo'


# Agora Todas as TVs são roxas:
print(tv_sala.cor)
