mes = input("digite o nome de um mes:")
if mes in ("janeiro", "março", "maio", "julho", "agosto", "outubro", "dezembro"):
    print("seu mês contém 31 dias")
elif mes == "fevereiro":
    print("seu mês contém 28 ou 29 dias")
elif mes in ("abril", "junho", "setembro", "novembro"):
    print("seu mês contém 30 dias")
else:
    print("mês inválido")