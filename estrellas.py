"""
Este programa utiliza el módulo turtle para dibujar estrellas regulares con un número y longitud de puntas a escoger.

Funciones:
- choose_number_arms(): Permite al usuario elegir el número de puntas para la estrella (5, 7 o 9).
- choose_length_arms(): Solicita al usuario introducir la longitud de las puntas de la estrella.
- main(): Dibuja la estrella con el número y longitud de puntas especificados.

Instrucciones:
1. Ejecutar el programa.
2. Seleccionar el número de puntas y la longitud deseada siguiendo las instrucciones en consola.
3. Una vez completada la configuración, la estrella se dibujará utilizando el módulo turtle.
4. La ventana de turtle se cerrará al hacer clic en ella.

Autor: Álvaro Santamaría Antón
"""

import turtle

def choose_number_arms():
    # Función para elegir un número de puntas

    print("""\nElige una opción para tu estrella:
A - 5 puntas
B - 7 puntas
C - 9 puntas""")

    # Solicitar al usuario la entrada
    while True:
        eleccion_1 = input("\nIntroduce el número de puntas que desees: ").upper()

        if eleccion_1 == "A":
            eleccion_1 = 5
            break
        elif eleccion_1 == "B":
            eleccion_1 = 7
            break
        elif eleccion_1 == "C":
            eleccion_1 = 9
            break
        else:
            print("Por favor, elige una opción válida (Introduce A, B o C).")
        
    return eleccion_1


def choose_length_arms():
    # Función para determinar la longitud de las puntas

    # Solicitar al usuario la entrada
    while True:
        try:
            eleccion_2 = float(input("\nIntroduce la longitud de las puntas: "))
            break
        except ValueError:
            print("Por favor, introduce una longitud válida.")
    
    return eleccion_2


def main():
    # Función principal para dibujar la estrella

    # Mostrar título por consola
    titulo = "LAS ESTRELLAS REGULARES"
    print("\n" + titulo + "\n" + "-" * len(titulo))

    # Llamar a las funciones para determinar el número y la longitud de las puntas
    numero_puntas = choose_number_arms()
    longitud_puntas = choose_length_arms()

    # Mensaje de feedback
    print("\n¡Tu estrella está lista!")

    # Configurar la tortuga
    t = turtle.Turtle()
    t.speed(2)  # Velocidad de la tortuga

    # Dibujar la estrella
    for _ in range(numero_puntas):
        t.forward(longitud_puntas)
        angle = 180 - (180 / numero_puntas)
        t.right(angle)

    # Cerrar la ventana al hacer clic
    turtle.exitonclick()


if __name__ == "__main__":
    main()