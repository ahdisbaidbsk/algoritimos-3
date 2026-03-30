triangulos= {
    'equilatero': lambda a, b, c: a == b == c,
    'isosceles': lambda a, b, c: a == b or b == c or a == c,
    'escaleno': lambda a, b, c: a != b and b != c and a != c
}
print('Digite os lados do triângulo:')
a = float(input('Lado A: '))
b = float(input('Lado B: '))
c = float(input('Lado C: '))
if a <= 0 or b <= 0 or c <= 0:
    print("Erro: os lados devem ser positivos!")
if triangulos['equilatero'](a, b, c):
    print("O triângulo é Equilátero.")
elif triangulos['isosceles'](a, b, c):
    print("O triângulo é Isósceles.")
elif triangulos['escaleno'](a, b, c):
    print("O triângulo é Escaleno.")  