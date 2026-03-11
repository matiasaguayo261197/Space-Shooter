import random
# Importamos las clases de entidades usando sus nombres completos
from dominio.entidades import NaveJugador, Enemigo, Proyectil

class Game:
    def __init__(self):
        # --- CONFIGURACIÓN DEL ESPACIO DE JUEGO ---
        # Usamos nombres largos para que no haya duda del tamaño del mapa
        self.__ANCHO_DEL_MAPA = 20
        self.__ALTO_DEL_MAPA = 20
        
        # --- ESTADO INICIAL ---
        # Calculamos la mitad para que la nave aparezca centrada
        posicion_central_x = self.__ANCHO_DEL_MAPA // 2
        posicion_cerca_del_suelo_y = self.__ALTO_DEL_MAPA - 2
        
        self.__mi_nave_espacial = NaveJugador(posicion_central_x, posicion_cerca_del_suelo_y)
        
        # Listas con nombres claros para lo que estamos almacenando
        self.__lista_de_enemigos_activos = []
        self.__lista_de_proyectiles_en_vuelo = []
        
        # Control del progreso del jugador
        self.__puntuacion_acumulada = 0
        self.__el_juego_esta_funcionando = True

    # --- PROPIEDADES (Getters para que la UI pueda leer los datos) ---
    @property
    def nave(self): return self.__mi_nave_espacial
    
    @property
    def puntaje(self): return self.__puntuacion_acumulada

    @property
    def jugando(self): return self.__el_juego_esta_funcionando

    @property
    def ancho(self): return self.__ANCHO_DEL_MAPA

    @property
    def alto(self): return self.__ALTO_DEL_MAPA
    
    @property
    def lista_de_enemigos(self): return self.__lista_de_enemigos_activos

    @property
    def lista_de_proyectiles(self): return self.__lista_de_proyectiles_en_vuelo

    # --- LÓGICA DE CONTROL DEL JUEGO ---

    def procesar_entrada_del_usuario(self, tecla_ingresada: str):
        """Maneja el movimiento y el disparo enviando los limites del mapa."""
        # Pasamos siempre el ancho y alto para que la nave sepa donde frenar
        if tecla_ingresada == "a":
            self.__mi_nave_espacial.mover(-1, 0, self.__ANCHO_DEL_MAPA, self.__ALTO_DEL_MAPA)
        elif tecla_ingresada == "d":
            self.__mi_nave_espacial.mover(1, 0, self.__ANCHO_DEL_MAPA, self.__ALTO_DEL_MAPA)
        elif tecla_ingresada == "w":
            self.__mi_nave_espacial.mover(0, -1, self.__ANCHO_DEL_MAPA, self.__ALTO_DEL_MAPA)
        elif tecla_ingresada == "s":
            self.__mi_nave_espacial.mover(0, 1, self.__ANCHO_DEL_MAPA, self.__ALTO_DEL_MAPA)
        elif tecla_ingresada == "f":
            # La nave fabrica la bala, el motor la guarda en la lista de vuelo
            nuevo_proyectil = self.__mi_nave_espacial.disparar()
            self.__lista_de_proyectiles_en_vuelo.append(nuevo_proyectil)

    def generar_aparicion_de_enemigos(self):
        """Crea enemigos de forma aleatoria en la parte superior del mapa."""
        numero_aleatorio = random.random()
        # 25% de probabilidad de que aparezca un villano
        if numero_aleatorio < 0.25:
            columna_aleatoria = random.randint(0, self.__ANCHO_DEL_MAPA - 1)
            instancia_de_enemigo = Enemigo(columna_aleatoria, 0)
            self.__lista_de_enemigos_activos.append(instancia_de_enemigo)

    def actualizar_todo_el_mundo(self):
        """Actualiza la posicion de cada objeto y revisa las reglas del juego."""
        
        # 1. Actualizamos cada enemigo usando un nombre de iterador claro
        for enemigo_actual in self.__lista_de_enemigos_activos:
            enemigo_actual.actualizar()

        # 2. Actualizamos cada proyectil
        for proyectil_actual in self.__lista_de_proyectiles_en_vuelo:
            proyectil_actual.actualizar()

        # 3. La nave tambien tiene su actualizacion interna
        self.__mi_nave_espacial.actualizar()

        # 4. Verificamos si las balas chocaron con los marcianitos
        self.__revisar_si_hay_colisiones()

        # 5. Quitamos de las listas lo que ya no sirve
        self.__gestionar_limpieza_de_memoria()

        # 6. Si la nave muere, cambiamos el estado para terminar el bucle
        if self.__mi_nave_espacial.esta_viva == False:
            self.__el_juego_esta_funcionando = False

    # Actualiza este método dentro de tu clase Game en engine.py
    def __revisar_si_hay_colisiones(self):
        """Revisa choques de balas y también si los enemigos tocan la nave."""
        
        # 1. Colisiones: Balas contra Enemigos
        for proyectil in self.__lista_de_proyectiles_en_vuelo:
            for enemigo in self.__lista_de_enemigos_activos:
                if proyectil.x == enemigo.x and proyectil.y == enemigo.y:
                    proyectil.morir()
                    enemigo.recibir_impacto()
                    if enemigo.esta_viva == False:
                        self.__puntuacion_acumulada = self.__puntuacion_acumulada + 100

        # 2. NUEVA LÓGICA: Colisiones: Enemigos contra la Nave
        for enemigo in self.__lista_de_enemigos_activos:
            # Si el enemigo pisa la misma coordenada que la nave
            if enemigo.x == self.__mi_nave_espacial.x and enemigo.y == self.__mi_nave_espacial.y:
                # El jugador recibe mucho daño y el enemigo muere al chocar
                self.__mi_nave_espacial.recibir_danio(25) 
                enemigo.morir()
                print("¡ALERTA! ¡Impacto directo en el casco!")

    def __gestionar_limpieza_de_memoria(self):
        """Bucle tradicional para filtrar solo los objetos que siguen vivos."""
        
        # Filtrado manual de enemigos
        lista_temporal_de_enemigos = []
        for enemigo in self.__lista_de_enemigos_activos:
            if enemigo.esta_viva == True:
                lista_temporal_de_enemigos.append(enemigo)
        self.__lista_de_enemigos_activos = lista_temporal_de_enemigos

        # Filtrado manual de proyectiles
        lista_temporal_de_proyectiles = []
        for proyectil in self.__lista_de_proyectiles_en_vuelo:
            if proyectil.esta_viva == True:
                lista_temporal_de_proyectiles.append(proyectil)
        self.__lista_de_proyectiles_en_vuelo = lista_temporal_de_proyectiles