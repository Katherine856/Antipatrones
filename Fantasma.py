from math import sqrt, asin, pi

class CalAr():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def operacion (self):
        s = (self.a + self.b + self.c) / 2.0
        return sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

class CalAn():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def operacion(self):
        ca = CalAr(self.a, self.b, self.c)
        s = ca.operacion()
        return 180 / pi * asin(2.0 * s / (self.b * self.c))

if __name__ == '__main__':

    l1 = float(input('lado a: '))
    l2 = float(input('lado b: '))
    l3 = float(input('lado c: '))

    ar = CalAr(l1, l2, l3)
    an = CalAn(l1, l2, l3)

    print('')
    print('Respuesta :', ar.operacion())
    print('Respuesta 2:', an.operacion())

