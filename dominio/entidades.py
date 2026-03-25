import random
from dominio.base import EntidadEspacial

class Proyectil(EntidadEspacial):
    def __init__(self, posicion_horizontal, posicion_vertical):
        # Llamamos al constructor del padre y le pasamos el icono de fuego
        super().__init__(posicion_horizontal, posicion_vertical, "🔺")

    def actualizar(self):
        """Mueve el proyectil hacia arriba en cada turno."""
        if self.esta_viva == True:
            # Restamos 1 a la posicion vertical para que suba
            self.y = self.y - 1
            
            # Si el proyectil se sale por la parte de arriba del mapa
            if self.y < 0:
                self.morir()

class NaveJugador(EntidadEspacial):
    def __init__(self, posicion_horizontal, posicion_vertical):
        super().__init__(posicion_horizontal, posicion_vertical, "🚀")
        # Atributo privado para la salud de la nave
        self.__energia_escudos = 100
        
    @property
    def energia(self):
        return self.__energia_escudos

    def mover(self, cambio_en_x, cambio_en_y, limite_ancho, limite_alto):
        """Calcula el movimiento y verifica que no choque con las paredes invisibles."""
        nueva_posicion_x = self.x + cambio_en_x
        

        # --- Lógica de Bordes Invisibles ---
        # Verificamos que no se salga por la izquierda (0) ni por la derecha (ancho)
        if nueva_posicion_x >= 0 and nueva_posicion_x <= (limite_ancho - 1):
            self.x = nueva_posicion_x
            

    def disparar(self):
        """Crea una nueva instancia de Proyectil justo arriba de la nave."""
        # Creamos la bala en la misma X de la nave, pero una Y mas arriba
        nueva_bala = Proyectil(self.x, self.y - 1)
        return nueva_bala

    def recibir_danio(self, cantidad_de_danio):
        """Resta energia y mata a la nave si llega a cero."""
        self.__energia_escudos = self.__energia_escudos - cantidad_de_danio
        if self.__energia_escudos <= 0:
            self.morir()

    def actualizar(self): #polimorfismo pasivo
       pass

class Enemigo(EntidadEspacial):
    def __init__(self, posicion_horizontal, posicion_vertical):
        super().__init__(posicion_horizontal, posicion_vertical, "👾")
        # El enemigo aguanta entre 3 y 5 disparos (Requisito cumplido)
        self.__puntos_de_vida = random.randint(3, 5)

    @property
    def vida_actual(self):
        return self.__puntos_de_vida

    def recibir_impacto(self):
        """Reduce la vida cuando una bala lo toca."""
        self.__puntos_de_vida = self.__puntos_de_vida - 1
        
        # Si la vida llega a cero, el objeto muere
        if self.__puntos_de_vida <= 0:
            self.morir()

    def actualizar(self):
        """El enemigo siempre intenta bajar hacia la posicion del jugador."""
        if self.esta_viva == True:
            # Sumamos 1 a la posicion vertical para que baje
            self.y = self.y + 1