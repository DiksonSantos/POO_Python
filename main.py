from Contas_Bancos import ContaCorrente, Cartao_Dikson


# Testando  -  Criando Conta
#conta_Dikson = ContaCorrente('Dikson', '333555333-06', '1775', '000333')

conta_Dikson = ContaCorrente("Gow Dikson Rodrigues dos Santos", "111,222,333,45", 4444, 4562)

conta_Dikson.nome = 'Gow Dikson Santos'
print(conta_Dikson.nome)

Cartao_Dikson.senha = '3636'
print(Cartao_Dikson.senha)

infos_conta = []
infos_conta.append(conta_Dikson.__dict__)

print(Cartao_Dikson.__dict__)

