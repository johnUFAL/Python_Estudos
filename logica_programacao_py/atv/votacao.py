from fpdf import FPDF
import os

# retorna se é Falso ou Verdadeiro
# Recebe uma string
def validar_cpf(cpf: str) -> bool:
    # remove qualquer caracterte que n for digito
    cpf = ''.join(filter(str.isdigt, cpf))
    # join junta e filter filtra

    if len(cpf) != 11: return False    # Verifica se tem 11 digitos
    if cpf == cpf[0]*11: return False # Ferifica se n tem todos os digotos iguais a 1 ou 0

    soma = sum(int(cpf[i]) * (10-i) for i in range(9))
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto

    soma = sum(int(cpf[i]) * (11-i) for i in range(10))
    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto

    return cpf[-2:] == f'{digito1}{digito2}'


class Candidato:

    def __init__(self, nome):
        self.nome = nome
        self.votos = 0

        def recebe_voto(self):
            self.votos += 1

class SistemaVotacao:
    def __init__(self):
        self.candidatos = []
        self.cpf_votaram = set()
        self.brancos = 0
        self.nulos = 0

    