#O requisito implementado é o sistema de autenticação para acessar o sistema
#A função principal na verdade são 2: fazer_login e criar_conta e tem algumas auxiliares

import csv
import os
import base64

#BANCO DE DADOS EXTERNO EM CSV:
ARQUIVO_USUARIOS = "usuarios.csv"

#Função que pega uma string e retorna criptografado:
def _codificar(texto: str) -> str:
    """Criptografia simples usando codificação Base64."""
    return base64.b64encode(texto.encode('utf-8')).decode('utf-8')

#Função que pega uma criptografia e retorna em string decodificada:
def _decodificar(texto_codificado: str) -> str:
    """Descriptografa a string em Base64."""
    return base64.b64decode(texto_codificado.encode('utf-8')).decode('utf-8')

#Função que cria o arquivo do banco de dados caso ele nn exista:
def inicializar_base_usuarios():
    if not os.path.exists(ARQUIVO_USUARIOS):
        with open(ARQUIVO_USUARIOS, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["usuario", "senha"])

#Função que busca todos os usuarios e senhas no banco de dados:
def buscar_usuarios() -> dict:
    inicializar_base_usuarios()
    usuarios = {}
    with open(ARQUIVO_USUARIOS, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader, None)  #Pula o cabeçalho
        for row in reader:
            if len(row) == 2:
                usr_descripto = _decodificar(row[0])
                pwd_descripto = _decodificar(row[1])
                usuarios[usr_descripto] = pwd_descripto
    return usuarios

#Função para criar conta, validando se a senha tem 4 caracteres ou mais, valida nome de usuario, se ele ja esta no banco e retorna sucesso se passar em tudo:
def criar_conta(usuario: str, senha: str) -> tuple[bool, str]:
    if len(senha) < 4:
        return False, "Erro: A senha deve ter no mínimo 4 caracteres."
    
    usuario = usuario.strip()
    if not usuario:
        return False, "Erro: O nome de usuário não pode ser vazio."

    usuarios_existentes = buscar_usuarios()
    if usuario in usuarios_existentes:
        return False, f"Erro: O usuário '{usuario}' já está cadastrado."

    # Salva codificado no CSV
    usr_cripto = _codificar(usuario)
    pwd_cripto = _codificar(senha)
    
    with open(ARQUIVO_USUARIOS, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([usr_cripto, pwd_cripto])
        
    return True, f"Conta criada com sucesso para '{usuario}'!"

#Função para logar, verificando se usuario e senha correspondem ao que exite no banco de dados:
def fazer_login(usuario: str, senha: str) -> tuple[bool, str]:
    usuario = usuario.strip()
    usuarios_existentes = buscar_usuarios()

    if usuario not in usuarios_existentes:
        return False, "Erro: Usuário não registrado."

    if usuarios_existentes[usuario] != senha:
        return False, "Erro: Senha incorreta."

    return True, f"Login bem-sucedido! Bem-vindo(a), {usuario}."