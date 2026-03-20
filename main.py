from consola import UIConsola
from motor.engine import Game

if __name__ == "__main__":
    # 1. Instanciamos el motor
    juego = Game()
    
    # 2. Instanciamos la UI y le pasamos el motor
    interfaz = UIConsola(juego)
    
    # 3. Arrancamos el loop (cero lógica flotando)
    interfaz.iniciar_loop()