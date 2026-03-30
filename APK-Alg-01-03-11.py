import math

a = float(input("Digite a: "))
b = float(input("Digite b: "))
c = float(input("Digite c: "))

if a == 0:
    print("Erro: a não pode ser zero")
else:
    delta = b*b - 4*a*c
    
    if delta < 0:
        print("Sem raízes reais")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Uma raiz: {x}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")
