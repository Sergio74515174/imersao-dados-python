# Análise de Gargalo na Esteira de Separação
# Distribuidora de Medicamentos
# Autor: Luiz Sérgio Ribeiro Pereira

# Capacidade máxima da esteira (pedidos por hora)
capacidade_esteira = 150

# Pedidos separados por hora (exemplo de um turno)
pedidos_por_hora = {
    "08:00 - 09:00": 140,
    "09:00 - 10:00": 155,
    "10:00 - 11:00": 170,
    "11:00 - 12:00": 160,
    "13:00 - 14:00": 145,
    "14:00 - 15:00": 180
}

print("📦 Análise Operacional – Esteira de Separação\n")

gargalos = []

for horario, pedidos in pedidos_por_hora.items():
    if pedidos > capacidade_esteira:
        excesso = pedidos - capacidade_esteira
        gargalos.append((horario, pedidos, excesso))
        print(f"⚠️ Gargalo identificado | {horario} | Pedidos: {pedidos} | Excesso: {excesso}")
    else:
        print(f"✅ Operação normal | {horario} | Pedidos: {pedidos}")

print("\n📊 Resumo da Análise")

if gargalos:
    print(f"Total de períodos com gargalo: {len(gargalos)}")
    pior_gargalo = max(gargalos, key=lambda x: x[2])
    print(
        f"Pior gargalo ocorreu em {pior_gargalo[0]} "
        f"com excesso de {pior_gargalo[2]} pedidos."
    )
else:
    print("Nenhum gargalo identificado no período analisado.")
