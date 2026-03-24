# 🚀 Space Shooter - Penguin Academy Challenge

Este proyecto es un simulador de combate espacial desarrollado en Python, diseñado bajo los estándares de la Programación Orientada a Objetos (POO). El sistema no solo es funcional, sino que demuestra una arquitectura robusta, jerárquica y extensible.

## 🎯 El Reto
Modelar un sistema complejo donde la lógica no dependa de funciones sueltas, sino de una estructura de clases con responsabilidades claras.

## 🏗️ Arquitectura del Sistema
El código está estrictamente separado en tres zonas lógicas para garantizar la modularización:

1. **Dominio**: Contiene las entidades base y las reglas del mundo (clases abstractas y concretas).
2. **Motor (Engine)**: La clase `Game` actúa como el orquestador, controlando el ciclo de vida de los objetos y la mecánica del juego.
3. **UI Consola**: Responsable exclusiva de la renderización visual y la captura de entradas del usuario.

## 🧱 Pilares POO Aplicados
El núcleo del proyecto gira en torno a los cuatro pilares fundamentales:

### 1. Abstracción y Clase Base
Se implementó una clase base abstracta `EntidadEspacial` que define el "contrato" para cualquier objeto que exista en el mapa.
* **Contrato Estricto**: Define métodos abstractos como `actualizar()`, obligando a las clases hijas a implementar su propia lógica.
* **Restricción**: La clase base no puede instanciarse directamente.

### 2. Herencia y Polimorfismo
Se crearon tres clases hijas que heredan de `EntidadEspacial`, reutilizando la lógica de posicionamiento y modificando comportamientos específicos:
* **NaveJugador**: Gestiona la energía y el disparo.
* **Enemigo**: Implementa patrones de movimiento descendente y resistencia aleatoria.
* **Proyectil**: Posee una lógica de movimiento lineal y autodestrucción fuera de límites.
* **Mensajería Polimórfica**: El motor del juego (`Game`) actualiza todas las entidades enviando el mismo mensaje `.actualizar()`, sin preocuparse por el tipo de objeto.

### 3. Encapsulamiento Real
* **Atributos Privados**: Los estados críticos (salud, coordenadas, puntuación) están protegidos mediante el uso de doble guion bajo (`__`).
* **Getters y Setters**: Se utilizan decoradores `@property` para permitir la lectura segura desde la UI sin permitir la escritura directa desde fuera de la clase.

### 4. Control del Game Loop
La clase `Game` es la única responsable de coordinar las interacciones y determinar el fin de la partida.
* **Main Limpio**: El archivo `main.py` no contiene lógica de juego ni condicionales sueltos; solo inicializa los componentes principales.

## 🛠️ Extensibilidad
El diseño permite que el código crezca sin romperse. Es posible añadir nuevos tipos de enemigos o ítems simplemente creando una nueva clase que herede de `EntidadEspacial` e implemente su propio método `actualizar()`.