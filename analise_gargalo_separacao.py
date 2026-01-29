# Análise de gargalo na separação de pedidos
# Autor: Luiz Sérgio Ribeiro Pereira

pedidos_por_hora = [120, 135, 90, 80, 150, 160, 110]
meta_por_hora = 130

print("Análise de Gargalo na Separação de Pedidos\n")

for hora, quantidade in enumerate(pedidos_por_hora, start=1):
    if quantidade < meta_por_hora:
        print(f"Hora {hora}: GARGALO detectado ({quantidade} pedidos)")
    else:
        print(f"Hora {hora}: Produção OK ({quantidade} pedidos)")

media = sum(pedidos_por_hora) / len(pedidos_por_hora)

print("\nResumo do período:")
print(f"Média de pedidos por hora: {media:.2f}")

if media < meta_por_hora:
    print("⚠️ Atenção: média abaixo da meta. Avaliar reforço operacional.")
else:
    print("✅ Operação dentro da meta média.")
