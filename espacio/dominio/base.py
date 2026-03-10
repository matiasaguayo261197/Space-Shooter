from abc import ABC, abstractclassmethod

class EntidadEspacial(ABC):
    def __init__(self,x: int, y: int, icono: str):                     
        self.__x= x
        self.__y= y
        self.__icono= icono
        self.__esta_viva= True # Protegido (_): las clases hijas pueden usarlo.

    # GETTERS: Permitimos leer los datos, pero no modificarlos directamente.
    @property
    def x (self):
        return self.__x
    @x.setter
    def x (self,nuevo_valor):# Aquí puedes validar que la nave no se salga de la pantalla
        self.__x= nuevo_valor

    @property
    def y (self):
        return self.__y
    @y.setter
    def y(self, nuevo_valor):
      self.__y = nuevo_valor

    @property
    def icono (self):
        return self.__icono
    
    @property
    def esta_viva (self):
        return self.__esta_viva
    # POLIMORFISMO Y ABSTRACCIÓN: 
    # Obligamos a todas las hijas a implementar su propia lógica de actualización.
    @abstractclassmethod
    def actualizar(self):
        """Define cómo se mueve o actúa la entidad en cada turno."""
        pass
    def morir (self):
        """Un método común para todas las entidades."""
        self.__esta_viva= False