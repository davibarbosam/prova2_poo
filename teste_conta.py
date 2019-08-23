from conta import Conta

conta1 = Conta("2009","David",800.0)

#mostrar para o usuario os dados atuais da conta
print("Numero da conta:",conta1.numero,"\nCorrentista:",conta1.correntista,"\nSaldo disponivel:",conta1.saldo)

novo_nome = input("\nDigite um novo nome para o correntista: ")
conta1.alterar_nome(novo_nome)

conta1.depositar(100)

deucerto = conta1.sacar(20)

if(deucerto):
	print("Saque efetuado com sucesso")
else:
	print("Saldo insuficiente!")
return

conta1.depositar(100)