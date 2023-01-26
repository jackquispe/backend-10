class Operaciones:
    def sumar(a,b):
        return a+b
    

    def multiplicar(a,b):
        return a*b

    def restar(a,b):
        return a-b

resultado = Operaciones.sumar(1,1)
resultado_2 = Operaciones.multiplicar(2,2)


class Operaciones_2:
    def __init__(self,a,b) -> None:
        self.primer_numero = a
        self.segundo_numero = b

    def restar(self):
        return self.primer_numero - self.segundo_numero

    def sumar(self):
        return self.primer_numero + self.segundo_numero

resultado_3 = Operaciones_2(3,4)
print(resultado_3.sumar())