barulho = int(input("digite um nível de volume em decibéis:"))
if barulho == 130:
    print("britadeira")
elif barulho == 106:
    print("cortador de grama")
elif barulho == 70:
    print("despertador")
elif barulho == 40:
    print("sala silenciosa")
elif barulho > 130:
    print("mais barulhento que uma britadeira")
elif barulho < 40:
    print("menos barulhento que uma sala silenciosa")
elif 106 < barulho < 130:
    print("o barulho está entre o cortador de grama e a britadeira")
elif 70 < barulho < 106:
    print("o barulho está entre o despertador e o cortador de grama")
elif 40 < barulho < 70:
    print("o barulho está entre a sala silenciosa e o despertador")
else:
    print("valor não identificado")