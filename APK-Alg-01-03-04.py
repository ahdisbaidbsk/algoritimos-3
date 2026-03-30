poligonos = {
    3: "Triângulo",
    4: "Quadrilátero",
    5: "Pentágono",
    6: "Hexágono",
    7: "Heptágono",
    8: "Octógono",
    9: "Eneágono",
    10: "Decágono"
}

print("Identificador de Polígonos")
lados = int(input("Digite o número de lados (3 a 10): "))

if lados < 3 or lados > 10:
    print("Erro: número deve estar entre 3 e 10!")
else:
    nome = poligonos[lados]
    print(f"Um polígono com {lados} lados é um {nome}!")
