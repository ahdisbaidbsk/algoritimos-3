ano_bissesto = {
    "Qualquer ano é bissexto se for divisível por 4, exceto os anos múltiplos de 100, a menos que sejam também múltiplos de 400."
}
print("Identificador de Ano Bissexto")
ano = int(input("Digite um ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")
    