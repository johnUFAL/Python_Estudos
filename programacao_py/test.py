# criar conjunto
x = set([1, 2, 3, 4])

#criar tupla 
x = (1, 2, 3, 4)

#criar dicionário
x = { 
    "Namorado" : "João", 
     "Namorada": "Bea" 
    }

# criando modulos
import modulo_inicial
print(modulo_inicial.funcao_modulo())

#modulos built-in
b = 8
print(f"valor absoluto: {abs(b)}")
print(f"valor binário: {bin(b)}")
print(f"classe: {type(x)}")

# POO
class pessoa:
    nome = ""
    def fala(self, nome):
        self.fala = nome

pessoa_1 = pessoa()
pessoa_1.nome = "João"
print("Nome da pessoa: ", pessoa_1.nome)