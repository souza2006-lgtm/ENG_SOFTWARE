from autenticacao import fazer_login, criar_conta
from vagas import carregar_vagas, obter_setores_disponiveis, filtrar_por_setor
from alertas import verificar_alerta_setor

def exibir_detalhes_vagas(lista_vagas: list[dict]):
    if not lista_vagas:
        print("\n[!] Nenhum setor encontrado com este nome.")
        return

    print("\n" + "-" * 50)
    print(f"{'SETOR':<25} | {'DISPONÍVEIS':<12} | {'STATUS'}")
    print("-" * 50)
    for v in lista_vagas:
        disp_txt = f"{v['disponiveis']}/{v['totais']}"
        print(f"{v['setor']:<25} | {disp_txt:<12} | {v['status']}")
        verificar_alerta_setor(v)
    print("-" * 50)

def menu_estacionamento(usuario: str):
    while True:
        print(f"\n--- MENU ESTACIONAMENTO (Usuário: {usuario}) ---")
        print("1. Ver todas as vagas")
        print("2. Consultar vagas por setor")
        print("0. Sair / Logout")
        
        opcao = input("Opção: ").strip()
        
        if opcao == "1":
            vagas = carregar_vagas()
            exibir_detalhes_vagas(vagas)
            
        elif opcao == "2":
            setores = obter_setores_disponiveis()
            print("\nSetores disponíveis:")
            for idx, s in enumerate(setores, 1):
                print(f"  {idx}. {s}")
            
            termo = input("\nDigite o nome ou parte do nome do setor: ").strip()
            vagas_filtradas = filtrar_por_setor(termo)
            exibir_detalhes_vagas(vagas_filtradas)
            
        elif opcao == "0":
            print("\nSaindo da sessão...")
            break
        else:
            print("Opção inválida! Tente novamente.")

def main():
    print("==================================================")
    print("    SISTEMA DE ESTACIONAMENTO DO CAMPUS - CLI")
    print("==================================================")
    
    while True:
        print("\n--- TELA INICIAL ---")
        print("1. Fazer Login")
        print("2. Criar Nova Conta")
        print("0. Encerrar Programa")
        
        opcao = input("Opção: ").strip()
        
        if opcao == "1":
            usr = input("Usuário: ")
            pwd = input("Senha: ")
            sucesso, msg = fazer_login(usr, pwd)
            print(f"\n> {msg}")
            if sucesso:
                menu_estacionamento(usr)
                
        elif opcao == "2":
            usr = input("Escolha um Nome de Usuário: ")
            pwd = input("Escolha uma Senha (mínimo 4 caracteres): ")
            sucesso, msg = criar_conta(usr, pwd)
            print(f"\n> {msg}")
            menu_estacionamento(usr)
            
        elif opcao == "0":
            print("\nPrograma encerrado.")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()

# ==============================================================================
# AUTOAVALIAÇÃO (Passo 3):
# Critérios Atingidos: Todos os 6 critérios atendidos com sucesso.
# Maior Dificuldade: Tratar a criptografia simples sem depender de bibliotecas
# externas (resolvido com módulo padrão 'base64').
# Resolução do Fluxo CLI: A divisão de menus facilitou a validação antes da
# navegação pelas vagas.
# Uso da IA: Ajudou a gerar os protótipos de manipulação do CSV e formatação em tabela.
# ==============================================================================