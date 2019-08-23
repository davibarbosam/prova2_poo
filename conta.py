class Conta:
	def __init__(self,numero,correntista,saldo=0):
		self.numero = numero
		self.correntista = correntista
		self.saldo = saldo

	#função criada para alterar o titular da conta
	def alterar_nome(self,correntista):
		self.correntista = correntista
		print("O nome do novo correntista é:",self.correntista)
		return

	#função criada para efetuar saques
	def sacar(self,valor):
		if (self.saldo > valor):
			self.saldo -= valor
			True
		else:
			False
		return

	#função criada para efetuar depositos
	def depositar(self,valor):
		self.saldo += valor
		return

	def extrato(self):
		print("Saldo disponivel atual é de:",self.saldo)
		return