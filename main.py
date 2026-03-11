import os

# Importamos la clase Game desde nuestro motor
from motor.engine import Game

def limpiar_pantalla():
    """Borra el texto anterior de la consola para redibujar el juego."""
    # 'cls' para Windows, 'clear' para Linux/Mac
    os.system('cls' if os.name == 'nt' else 'clear')

def dibujar_interfaz_del_juego(juego_actual: Game):
    limpiar_pantalla()
    # Añadimos el indicador de ENERGÍA
    print(f"--- SPACE SHOOTER --- | PUNTAJE: {juego_actual.puntaje} | ENERGÍA: {juego_actual.nave.energia}%")
    print("-" * (juego_actual.ancho * 2 + 3))

    # Recorremos cada fila del mapa (coordenada vertical Y)
    for fila_y in range(juego_actual.alto):
        linea_render = "|"
        
        # Recorremos cada columna de la fila (coordenada horizontal X)
        for columna_x in range(juego_actual.ancho):
            caracter_a_mostrar = "  " # Por defecto, mostramos dos espacios vacios

            # 1. ¿Hay algun proyectil en esta coordenada?
            for proyectil in juego_actual.lista_de_proyectiles:
                if proyectil.x == columna_x and proyectil.y == fila_y:
                    caracter_a_mostrar = proyectil.icono + " "

            # 2. ¿Hay algun enemigo en esta coordenada?
            for enemigo in juego_actual.lista_de_enemigos:
                if enemigo.x == columna_x and enemigo.y == fila_y:
                    caracter_a_mostrar = enemigo.icono + " "

            # 3. ¿Esta la nave del jugador aqui?
            if juego_actual.nave.x == columna_x and juego_actual.nave.y == fila_y:
                caracter_a_mostrar = juego_actual.nave.icono + " "

            linea_render = linea_render + caracter_a_mostrar
        
        linea_render = linea_render + "|"
        print(linea_render)

    # Dibujamos el suelo del mapa
    print("-" * (juego_actual.ancho * 2 + 3))
    print("CONTROLES: [A] Izq | [D] Der | [W] Arriba | [S] Abajo | [F] Disparar")

def iniciar_programa():
    """Bucle principal que mantiene el juego corriendo."""
    # Creamos la instancia del juego
    mi_partida = Game()

    while mi_partida.jugando == True:
        # 1. Mostramos visualmente el estado de la partida
        dibujar_interfaz_del_juego(mi_partida)

        # 2. Capturamos la tecla del usuario
        entrada = input("Tu próximo movimiento: ").lower()
        
        # 3. Enviamos la orden al motor (CON LOS NOMBRES NUEVOS)
        mi_partida.procesar_entrada_del_usuario(entrada)
        
        # 4. El motor decide si aparecen nuevos villanos
        mi_partida.generar_aparicion_de_enemigos()
        
        # 5. El motor mueve todo y revisa choques
        mi_partida.actualizar_todo_el_mundo()

    # Si salimos del bucle, el jugador perdio
    limpiar_pantalla()
    print("¡FIN DE LA PARTIDA, PILOTO!")
    print(f"Tu puntuación final fue de: {mi_partida.puntaje} puntos.")

# Punto de entrada oficial de Python
if __name__ == "__main__":
    iniciar_programa()