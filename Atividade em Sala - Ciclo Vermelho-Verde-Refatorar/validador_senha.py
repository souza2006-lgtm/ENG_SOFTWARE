"""
GABRIEL FELIPE FERDINANDI DE SOUZA - A2669480

Implementação com o padrão Chain of Responsibility para validação de senhas, com testes unitários utilizando pytest.
"""

from abc import ABC, abstractmethod
import re
from typing import Optional, Tuple

#1. Handler Abstrato:
class ValidadorHandler(ABC):
    def __init__(self) -> None:
        self.proximo_validador: Optional["ValidadorHandler"] = None

    def definir_proximo(self, proximo: "ValidadorHandler") -> "ValidadorHandler":
        self.proximo_validador = proximo
        return proximo

    @abstractmethod
    def validar(self, senha: str) -> Tuple[bool, str]:
        pass

#2. Handlers Concretos:
class ValidadorTamanho(ValidadorHandler):
    def validar(self, senha: str) -> Tuple[bool, str]:
        if len(senha) < 8:
            return False, "A senha deve ter pelo menos 8 caracteres."
        if self.proximo_validador:
            return self.proximo_validador.validar(senha)
        return True, "Senha válida!"

class ValidadorCaractereEspecial(ValidadorHandler):
    def validar(self, senha: str) -> Tuple[bool, str]:
        simbolos = r"[@#!$%^&*()_+\-=\[\]{}|;:,.<>?]"
        if not re.search(simbolos, senha):
            return False, "A senha deve conter ao menos um caractere especial (ex: @, #, !)."
        if self.proximo_validador:
            return self.proximo_validador.validar(senha)
        return True, "Senha válida!"

class ValidadorNumero(ValidadorHandler):
    def validar(self, senha: str) -> Tuple[bool, str]:
        if not any(char.isdigit() for char in senha):
            return False, "A senha deve conter ao menos um dígito numérico."
        if self.proximo_validador:
            return self.proximo_validador.validar(senha)
        return True, "Senha válida!"

#3. Classe de Validação de Senha com encadeamento de validadores:
class ValidadorSenha:
    def __init__(self) -> None:
        self.validador_tamanho = ValidadorTamanho()
        self.validador_especial = ValidadorCaractereEspecial()
        self.validador_numero = ValidadorNumero()

        self.validador_tamanho.definir_proximo(self.validador_especial).definir_proximo(
            self.validador_numero
        )

    def validar(self, senha: str) -> Tuple[bool, str]:
        return self.validador_tamanho.validar(senha)


"""
===============================================================================
AUTOAVALIAÇÃO
===============================================================================
1. CRITÉRIOS ATINGIDOS:
   1: Testes em arquivo separado do código de produção (4 variações de testes).
   2: Histórico com três commits identificados (red, green, refactor).
   3: Commit 'red' com testes falhando sem implementação.
   4: Refatoração aplicando Chain of Responsibility com participantes nomeados.
   5: Suíte executada e com 100% dos testes passando após a refatoração.

2. MUDANÇAS NA ESTRUTURA DO CÓDIGO (VERDE VS. REFATORADA):
   - Na fase VERDE, a validação usava blocos 'if' sequenciais em uma única classe.
   - Na fase REFATORADA, cada regra foi isolada em uma classe concreta herdando
     de 'ValidadorHandler', promovendo alta coesão e o princípio OCP.

3. PARTE QUE DEU MAIS TRABALHO:
   - Configuração do encadeamento fluente da corrente e propagação dos retornos.

4. AVALIAÇÃO DO USO DE IA:
   - Ajudou na organização das ideias e plkano de implementação, 
   mas a lógica de validação foi desenvolvida manualmente.


CHAT DA IA GEMINI: https://gemini.google.com/app/efb2e59c633fc44d?hl=pt-BR
===============================================================================
"""