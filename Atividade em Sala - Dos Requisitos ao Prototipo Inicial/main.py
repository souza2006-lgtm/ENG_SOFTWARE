from autenticacao import carregar_sessao
from vagas import listar_setores
from alertas import verificar_alerta_setor

def main():
    sessao = carregar_sessao()
    print(f"--> Sessão iniciada para: {sessao['usuario']} (Sem necessidade de login)\n")
    
    setores = listar_setores()
    print("--- STATUS DOS ESTACIONAMENTOS ---")
    for nome, info in setores.items():
        print(f"- {nome}: {info['disponiveis']}/{info['total']} vagas ({info['status']})")
        verificar_alerta_setor(nome, info)

if __name__ == "__main__":
    main()
    
