posicao = input("Informe a posição (ex: a1, d5): ").lower()

coluna = posicao[0]
linha = int(posicao[1])

if coluna in ['a', 'c', 'e', 'g']:
    cor_coluna_inicial = 'preto'
else:
    cor_coluna_inicial = 'branco'

if linha % 2 == 1:
    cor_final = cor_coluna_inicial
else:
    cor_final = 'branco' if cor_coluna_inicial == 'preto' else 'preto'

print(f"O quadrado em {posicao} é {cor_final}.")