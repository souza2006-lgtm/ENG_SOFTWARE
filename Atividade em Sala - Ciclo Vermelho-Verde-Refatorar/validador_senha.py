"""
GABRIEL FELIPE FERDINANDI DE SOUZA - A2669480

Implementação direta e simples para fazer os testes passarem (Fase Green).
"""

import re

class ValidadorSenha:

    def validar(self, senha: str):
        #Validação 1: Tamanho mínimo:
        if len(senha) < 8:
            return False, "A senha deve ter pelo menos 8 caracteres."

        #Validação 2: Caractere Especial:
        simbolos = r"[@#!$%^&*()_+\-=\[\]{}|;:,.<>?]"
        if not re.search(simbolos, senha):
            return False, "A senha deve conter ao menos um caractere especial (ex: @, #, !)."

        #Validação 3: Número:
        if not any(char.isdigit() for char in senha):
            return False, "A senha deve conter ao menos um dígito numérico."

        return True, "Senha válida!"