"""
GABRIEL FELIPE FERDINANDI DE SOUZA - A2669480

===============================================================================
PLANO DA ATIVIDADE TDD (CICLO VERMELHO-VERDE-REFATORAR)
===============================================================================

1. CASOS A TESTAR:
   - Variacao 1 (Tamanho): Senha com menos de 8 caracteres deve ser invalida.
   - Variacao 2 (Caractere Especial): Senha sem caractere especial (@, #, !, etc.) deve ser invalida.
   - Variacao 3 (Numero): Senha sem nenhum digito numerico deve ser invalida.
   - Variacao 4 (Sucesso): Senha com tamanho >= 8, caractere especial e numero deve ser valida.

2. PADRAO DE PROJETO ESCOLHIDO:
   - Padrao: Chain of Responsibility (Comportamental).
   - Motivo da escolha: A validacao de senhas exige a execucao de multiplas regras
     independentes em sequencia. O padrao Chain of Responsibility permite desacoplar
     cada regra de validacao em seu proprio objeto (handler), permitindo adicionar,
     remover ou reordenar validacoes sem alterar as classes existentes (Principio Open/Closed).

3. ESTIMATIVA DE TEMPO POR FASE:
   - Passo 1 (Plano): 10 minutos
   - Fase RED (Escrever testes e ver falhar): 15 minutos
   - Fase GREEN (Implementacao minima para passar): 15 minutos
   - Fase REFACTOR (Aplicacao do padrao Chain of Responsibility): 60 minutos
   - Passo 3 (Autoavaliacao): 10 minutos
   - Total estimado: 110 minutos

4. USO DE INTELIGENCIA ARTIFICIAL:
   - A IA foi utilizada para auxiliar nas ideias doque realizar, 
   na escrita do plano de atividade e na explicação do padrao de projeto escolhido.
===============================================================================


Para rodar os testes, utilize o comando: python -m pytest -v no Windows.
"""

import pytest
from validador_senha import ValidadorSenha


@pytest.fixture
def validador():
    return ValidadorSenha()


#Variação 1: Teste de Tamanho Mínimo
def test_senha_com_tamanho_insuficiente_deve_falhar(validador):
    sucesso, mensagem = validador.validar("12345")
    assert sucesso is False
    assert "8 caracteres" in mensagem


#Variação 2: Teste de Caractere Especial
def test_senha_sem_caractere_especial_deve_falhar(validador):
    sucesso, mensagem = validador.validar("SenhaLonga123")
    assert sucesso is False
    assert "caractere especial" in mensagem


#Variação 3: Teste de Número
def test_senha_sem_numero_deve_falhar(validador):
    sucesso, mensagem = validador.validar("SenhaSemNum!")
    assert sucesso is False
    assert "dígito numérico" in mensagem or "digito numerico" in mensagem


#Variação 4: Cenário de Sucesso
def test_senha_valida_deve_passar(validador):
    sucesso, mensagem = validador.validar("SenhaForte123!")
    assert sucesso is True
    assert mensagem == "Senha válida!"