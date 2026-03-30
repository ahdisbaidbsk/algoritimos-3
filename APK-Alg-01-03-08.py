notas_base = {
    'C': 261.63,
    'D': 293.66,
    'E': 329.63,
    'F': 349.23,
    'G': 392.00,
    'A': 440.00,
    'B': 493.88
}

nota_entrada = input("Digite uma nota (ex: C4, A5, G3): ").upper()

letra = nota_entrada[0]
oitava = int(nota_entrada[1])

if letra in notas_base:
    frequencia_base = notas_base[letra]
    frequencia = frequencia_base * (2 ** (oitava - 4))
    print(f"A nota {nota_entrada} tem frequência de {frequencia:.2f} Hz")
else:
    print("Nota inválida!")
