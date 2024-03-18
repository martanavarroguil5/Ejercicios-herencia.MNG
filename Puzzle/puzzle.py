'''
class Base: 
 
    def __init__(self): 
        self.a = "a" 
        self.b = "b" 
        self.c = "c" 
 
    def A(self): 
        print(self.a) 
 
    def B(self): 
        print(self.b) 
 
    def C(self): 
        print(self.c) 
 
class Derivada(Base): 
 
    def __init__(self): 
        self.a = "aa" 
        super().__init__() 
        self.c = "cc" 
 
    def A(self): 
        print(self.a) 
 
    def B(self): 
        self.b = "bb" 
        super().B() 
        print(self.b) 
 
base = Base() 
derivada = Derivada() 
 
base.A() 
derivada.A() 
print() 
base.B() 
derivada.B() 
base.C() 
derivada.C() 
derivada = base 
derivada.C() '''

class Base: 
 
#Nombro los atributos mas adecuadamente
    def __init__(self): 
        self.atributo_a = "a" 
        self.atributo_b = "b" 
        self.atributo_c = "c" 
 
# Nombro lo métodos con nombres más comprensibles
    def mostrar_a(self): 
        print(self.atributo_a) 
 
    def mostrar_b(self): 
        print(self.atributo_b) 
 
    def mostrar_c(self): 
        print(self.atributo_c) 

    
class Derivada(Base):

    def __init__(self):
        # Se establece el valor propio de la clase derivada para los atributos atributo_a, atributo_b y atributo_c 
        self.atributo_a = "aa" 
        # Llama al constructor de la clase base para inicializar atributos comunes (se podria evitar porque no existen, todos cambian)
        super().__init__() # Hereda de clase base
        self.atributo_c = "cc"
    
    # Renombro el método que muestra el valor de a en la clase derivada a mostrar_a
    def mostrar_a(self):
    # Observamos que cumple la misma función que ne la clase base, asi que también se podría hacer por herencia
        print(self.atributo_a)

    def mostrar_b(self):
        self.atributo_b = "bb"
        # Llama al método mostrar_b() de la clase base para mostrar el valor de 'atributo_b'
        super().mostrar_b() 
        print(self.atributo_b)# Propio de la función en la subclase
    

# Instancias de las clases Base y Derivada
base = Base()
derivada = Derivada()

# Llamar al método A en la instancia de la clase Base y de la clase Derivada
print("Llamadas al método A:")
base.mostrar_a()
derivada.mostrar_a()
print()

# Llamar al método B en la instancia de la clase Base y de la clase Derivada
print("Llamadas al método B:")
base.mostrar_b()
derivada.mostrar_b()
print()

# Llamar al método C en la instancia de la clase Base y de la clase Derivada
print("Llamadas al método C:")
base.mostrar_c()
derivada.mostrar_c()
print()

# Asignar la instancia de la clase Base a la variable derivada
derivada = base

# Llamar al método C en la nueva instancia de la clase Derivada (ahora es una instancia de la clase Base)
print("Llamada al método C en la instancia de la clase Base asignada a la variable derivada:")
derivada.mostrar_c()

 