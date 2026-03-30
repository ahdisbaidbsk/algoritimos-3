def anos_caninos(anos_humanos):

    """
    Converte anos humanos para anos caninos:
    - até 2 anos humanos: cada ano = 10.5 anos caninos
    - após 2 anos: primeiros 2 anos = 2 * 10.5, cada ano adicional = 4 anos caninos
    """
    if anos_humanos < 0:
        raise ValueError("Idade não pode ser negativa.")
    if anos_humanos <= 2:
        return anos_humanos * 10.5
    else:
        return 2 * 10.5 + (anos_humanos - 2) * 4

def main():
    try:
        entrada = input("Informe a idade em anos cronológicos (ex.: 3.5): ").strip()
        anos = float(entrada)
    except ValueError:
        print("Entrada inválida. Informe um número (ex.: 3 ou 3.5).")
        return

    try:
        canino = anos_caninos(anos)
    except ValueError as e:
        print("Erro:", e)
        return

    if canino.is_integer():
        print(f"{anos:.0f} anos cronológicos correspondem a {int(canino)} anos caninos.")
    else:
        print(f"{anos} anos cronológicos correspondem a {canino:.1f} anos caninos.")

if __name__ == "__main__":
    main()