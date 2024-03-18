# Creamos la clase padre A con un único atributo a
class A:
    def __init__(self, a):
        self.a = a

# Se crea una subclase B de A con dos atributos (a, heredado y b, propio)
class B(A):
    def __init__(self, b):
        super().__init__(b) # Herencia de A
        self.b = b

# Se crea una subclase C de A con dos atributos (a, heredado y c, propio)
class C(A):
    def __init__(self, c):
        super().__init__(c) #Herencia de A
        self.c = c

# Como vemos las clases B y C heredan ambas de a y tienen sus características propias y diferentes

# Por ultimo, creo la clase D que hereda de ambas clases, B y C
class D(B, C):
    def __init__(self, a, b, c):
        super().__init__(b)  # Se llama a la inicialización de B (y A)
        C.__init__(self, c)  # Se llama a la inicialización de C (y A)
        self.a = a  # Inicialización específica de D

''' 
Una clase puede tener solo una llamada a super() en su método __init__()'''

# Crear una instancia de D y mostrar los resultados
d = D(1, 2, 3)
print(isinstance(d, A), isinstance(d, B), isinstance(d, C))
print(d.a, d.b, d.c)