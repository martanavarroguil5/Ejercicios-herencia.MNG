from tip_orientacion import TipoOrientacion

# Creo la clase pared con el atributo orientacion que pertenece a la clase enum
class Pared:

    # Constructor
    def __init__(self, orientacion):
        if not isinstance(orientacion, TipoOrientacion): # Para que peretenezca al enum
            raise ValueError('La orientación debe ser una orientacion correcta')
        self.orientacion = orientacion
    
    # Getter
    def get_orientacion(self):
        return self.orientacion.name


# La clase ParedCortina hereda de la clase Pared ya que tiene atributos en común
class ParedCortina(Pared):

    # Constructor
    def __init__(self, orientacion, superficie_acristalada):
        super().__init__(orientacion) # Herencia de constructor de Pared
        self.superficie_acristalada = superficie_acristalada # Atributo propio

    # Getter
    def get_superficie_acristalada(self):
        return self.superficie_acristalada
    
# Creo la clase ventana
class Ventana:

    # Constructor
    def __init__(self, pared, superficie, proteccion):
        self.pared = pared
        self.superficie = superficie
        if proteccion is None:
            raise Exception("Protección obligatoria") # Este atributo no puede estar vacío
        self.proteccion = proteccion

    # Getters
    def get_pared(self):
        return self.pared
    
    def get_superficie(self):
        return self.superficie
    
    def get_proteccion(self):
        return self.proteccion
    
# Creo la clase Casa con el atributo paredes
class Casa:

    # Constructor
    def __init__(self, paredes):
        self.paredes = paredes
        self.ventanas = [] # las ventanas no pertenecen al constructor de casa, solo a sus métodos

    # Getter
    def get_paredes(self):
        return self.paredes
    
    # Método para agregar ventanas a la lista
    def agregar_ventana(self, ventana):
        if ventana.pared in self.paredes:
            self.ventanas.append(ventana)  
        else:
            raise ValueError("La ventana no está asociada a ninguna pared de la casa") 
    
    # Con este método se va a calcular la superficie total acristalada
    def superficie_acristalada(self):

        # Se inicia con 0  y se le ira sumando
        total_acristalado = 0 

        # Empieza con un bucle que va a evaluar a cada pared que pertenezca a las paredes de la casa
        for pared in self.paredes:

            # Se requiere que dicha pared se clase pared cortina, ya que esta acrstalada, 
            #si no, no es relevante para el cálculo
            if isinstance(pared, ParedCortina):
                total_acristalado += pared.superficie_acristalada # Se suma su valor a la lista
            else:
                # Si no se trata de una pared acristalada, se hace los misma para el caso de las ventanas
                for ventana in self.ventanas_de_pared(pared):
                    total_acristalado += ventana.superficie
        return total_acristalado

    def ventanas_de_pared(self, pared):
        # Simplemente devuelve una lista vacía para simular la obtención de ventanas
        ventanas = []
        for ventana in self.ventanas:
            if ventana.pared == pared:
                ventanas.append(ventana)
        return ventanas
    

# Ejempo de las paredes
pared_norte = Pared(TipoOrientacion.NORTE)
pared_oeste = Pared(TipoOrientacion.OESTE)
pared_sur = Pared(TipoOrientacion.SUR)
pared_este = Pared(TipoOrientacion.ESTE)

# Ejemplo de las ventanas
ventana_norte = Ventana(pared_norte, 0.5, "Persiana")
ventana_oeste = Ventana(pared_oeste, 1, "Estor")
ventana_sur = Ventana(pared_sur, 2, "Cortina")
ventana_este = Ventana(pared_este, 1, "Persiana")

# Ejemplo de de la casa con las 4 paredes
casa = Casa([pared_norte, pared_oeste, pared_sur, pared_este])
casa.agregar_ventana(ventana_norte)
casa.agregar_ventana(ventana_oeste)
casa.agregar_ventana(ventana_sur)
casa.agregar_ventana(ventana_este)

print(casa.superficie_acristalada())