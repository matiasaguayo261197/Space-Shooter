from abc import ABC, abstractmethod

class EntidadEspacial(ABC):
    def __init__(self,x, y, icono):                     
        self.__x= x
        self.__y= y
        self.__icono= icono
        self.__esta_viva= True # "Privado (__): solo la clase base lo maneja"

    # GETTERS: Permitimos leer los datos, pero no modificarlos directamente.
    @property                         # @property: Permite leer el atributo privado desde el exterior como solo lectura.
    def x (self):
        return self.__x
    @x.setter                         # @x.setter: Habilita la modificación controlada del atributo privado '__x' desde el exterior.
    def x (self,nuevo_valor):
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
    @abstractmethod
    def actualizar(self):
        """Define cómo se mueve o actúa la entidad en cada turno."""
        pass
    def morir (self):
        """Un método común para todas las entidades."""
        self.__esta_viva= False