import os

class UIConsola:
    def __init__(self, motor_juego):
        self.__juego = motor_juego 

    def iniciar_loop(self):
        while self.__juego.jugando:
            self.dibujar_pantalla()
            
            tecla = input("Mover (a/d) o Disparar (f): ")
            
            self.__juego.procesar_entrada_del_usuario(tecla)
            self.__juego.generar_aparicion_de_enemigos()
            self.__juego.actualizar_todo_el_mundo()
            
        print("¡Juego Terminado! Puntaje final:", self.__juego.puntaje)

    def dibujar_pantalla(self):
        # Limpia la consola en cada turno para crear el efecto de movimiento
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Muestra el HUD (Puntaje y Vida)
        print(f"--- PUNTUACIÓN: {self.__juego.puntaje} | ESCUDOS: {self.__juego.nave.energia} ---")

        # Dibuja el tablero 2D
        for y in range(self.__juego.alto):
            fila_actual = ""
            for x in range(self.__juego.ancho):
                dibujado = False

                # 1. Dibujar la nave
                if self.__juego.nave.x == x and self.__juego.nave.y == y:
                    fila_actual += self.__juego.nave.icono
                    dibujado = True

                # 2. Dibujar enemigos si no hay nave en esta coordenada
                if not dibujado:
                    for enemigo in self.__juego.lista_de_enemigos:
                        if enemigo.x == x and enemigo.y == y:
                            fila_actual += enemigo.icono
                            dibujado = True
                            break # Detiene el bucle si ya encontró un enemigo aquí

                # 3. Dibujar proyectiles si el espacio sigue libre
                if not dibujado:
                    for bala in self.__juego.lista_de_proyectiles:
                        if bala.x == x and bala.y == y:
                            fila_actual += bala.icono
                            dibujado = True
                            break

                # 4. Dibujar espacio vacío si no hay ninguna entidad
                if not dibujado:
                    fila_actual += "  "

            # Imprime la fila completa antes de pasar a la siguiente (y)
            print(fila_actual)