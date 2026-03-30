feriados_nacionais = {
    "01/01": "Confraternização universal",
    "21/04": "Tiradentes",
    "01/05": "Dia do trabalho",
    "07/09": "Independência do Brasil",
    "12/10": "Nossa Senhora Aparecida",
    "02/11": "Finados",
    "15/11": "Proclamação da República",
    "25/12": "Natal"
}

data_norm = input("Digite a data (DD/MM): ")

if data_norm in feriados_nacionais:
    print(f"A data digitada é um feriado nacional: {feriados_nacionais[data_norm]}")
else:
    print("A data digitada não é um feriado nacional.")