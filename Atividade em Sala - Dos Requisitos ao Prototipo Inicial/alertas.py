def verificar_alerta_setor(dados_setor: dict):
    if dados_setor.get("restrito"):
        print("\n" + "=" * 55)
        print(f"[!] ALERTA DE RESTRIÇÃO: {dados_setor['setor']}")
        print("    Vagas EXCLUSIVAS para FUNCIONÁRIOS/CREDENCIADOS.")
        print("    Estacionar aqui sem credencial gera notificação.")
        print("=" * 55)