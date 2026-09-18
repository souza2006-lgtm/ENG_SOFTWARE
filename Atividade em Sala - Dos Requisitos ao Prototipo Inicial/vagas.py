import csv
import os

ARQUIVO_VAGAS = "vagas.csv"

def inicializar_base_vagas():
    if not os.path.exists(ARQUIVO_VAGAS):
        with open(ARQUIVO_VAGAS, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["setor", "vagas_totais", "vagas_ocupadas", "restrito"])
            # Dados iniciais para teste
            writer.writerow(["Setor A - Central", "30", "18", "0"])
            writer.writerow(["Setor B - Biblioteca", "15", "12", "1"])
            writer.writerow(["Setor C - Bloco Didatico", "20", "20", "0"])

def carregar_vagas() -> list[dict]:
    inicializar_base_vagas()
    vagas = []
    with open(ARQUIVO_VAGAS, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            totais = int(row["vagas_totais"])
            ocupadas = int(row["vagas_ocupadas"])
            disponiveis = totais - ocupadas
            vagas.append({
                "setor": row["setor"],
                "totais": totais,
                "ocupadas": ocupadas,
                "disponiveis": disponiveis,
                "status": "Com Vagas" if disponiveis > 0 else "Lotado",
                "restrito": row["restrito"] == "1"
            })
    return vagas

def obter_setores_disponiveis() -> list[str]:
    vagas = carregar_vagas()
    return [v["setor"] for v in vagas]

def filtrar_por_setor(nome_setor: str) -> list[dict]:
    vagas = carregar_vagas()
    return [v for v in vagas if nome_setor.lower() in v["setor"].lower()]