# Creo un clase que define los puntos de un plano (2D)

class Punto2D:

    #En el constructor habrá un atributibuto para cada posición del plano XY
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    #Getters y setters
    
    def get_x(self):
        if isinstance == (self.x, int):
            return self.x 
        else:
            raise ValueError("Los puntos deben estar definidos por numeros enteros.")
        
    def get_y(self):
        if isinstance == (self.y, int):
            return self.y
        else:
            raise ValueError("Los puntos deben estar definidos por numeros enteros.")
        
    def set_x(self, x):
        self.x = x 

    def set_y(self, y):
        self.y = y

    # Creo el método traslación que permite modificar los valores de x e y, 
    # sumándoles los valores que se proporcionen

    def traslacion(self, a, b):
        self.x += a
        self.y += b

    # Convierte un objeto Punto en una cadena de texto fácilmente legible.
    def __str__(self):
        return "X: {}; Y: {}".format(self.x, self.y)
    

class Punto3D(Punto2D):

# Creo el constructor al que solo hay que añadir self.z ya que podemos accedor al constructor de la 
# clase 2Dmediante herncia (super).
    def __init__(self, x, y, z):
            super().__init__(x, y)
            self.z = z

# Getters y setters
# Hereda automaticammente los getters y setters de x e y
    def get_z(self):
        if isinstance == (self.z, int):
            return self.z
        else:
            raise ValueError("Los puntos deben estar definidos por numeros enteros.")
        
    def set_z(self, z):
        self.z = z
         
    
# Vuelvo a hacer los métodos traslacion y __str__ pero solo para self.z ya que los otros puntos herdean 
# de la misma funcion en la clase 2D
    def traslacion(self, a, b, c):
        super().traslacion(a, b) # Hereda de 2D
        self.z += c # Propio de 3D
    
    def __str__(self):
            return super().__str__() + "; Z : {}".format(self.z)
    


# Crear instancia de Punto2D
punto_2d = Punto2D(1, 2)
print("Punto 2D antes de traslación:", punto_2d)
punto_2d.traslacion(-1, -2)
print("Punto 2D después de traslación:", punto_2d)


# Crear instancia de Punto3D
punto_3d = Punto3D(1, 2, 3)
print("Punto 3D antes de traslación:", punto_3d)
punto_3d.traslacion(0, -2, 1)
print("Punto 3D después de traslación:", punto_3d)