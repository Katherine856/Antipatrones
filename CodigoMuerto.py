from math import sqrt, asin, pi

def at(a, b, c):
    s = (a + b + c) / 2.0
    return sqrt(s * (s - a) * (s - b) * (s - c))

def aa(a, b, c):
    s = at(a, b, c)
    return 180 / pi * asin(2.0 * s / (b * c))

def p(a, b, c):
    return a+b+c

a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

ar = at(a, b, c)
an = aa(a, b, c)

print('')
print('Respuesta :', ar)
print('Respuesta 2:', an)


