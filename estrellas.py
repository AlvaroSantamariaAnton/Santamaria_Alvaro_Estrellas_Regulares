"""
Este programa utiliza el módulo turtle para dibujar estrellas regulares 
con un número y longitud de puntas a decidir por el usuario.

Funciones:
- choose_number_arms(): 
Permite al usuario elegir la cantidad de puntas para la estrella. Siempre y cuando sean al 
menos 5 puntas y dicho número sea impar.
- choose_length_arms(): Solicita al usuario introducir la longitud de las puntas de la estrella.
- main(): Dibuja la estrella con el número y longitud de puntas especificados.

Instrucciones:
1. Ejecutar el programa.
2. Introducir el número de puntas y la longitud deseada siguiendo las instrucciones en consola.
3. Una vez completada la configuración, la estrella se dibujará utilizando el módulo turtle.
4. La ventana de turtle se cerrará al hacer clic en ella.

Autor: Álvaro Santamaría Antón
"""

import turtle

def choose_number_arms():
    # Función para determinar el número de puntas

    # Solicitar al usuario la entrada
    while True:
        try:
            eleccion_1 = int(input(
                "\nIngresa la cantidad de puntas deseada para la estrella. " 
                "\nRecuerda que debe tener al menos 5 puntas y ser un número impar: "
            ))
            
            if eleccion_1 % 2 == 1 and eleccion_1 >= 5:
                break
            else:
                print("\nPor favor, elige una opción válida (Revisa las instrucciones).")
        except ValueError:
            print("\nPor favor, introduce un número entero válido.")

    return eleccion_1


def choose_length_arms():
    # Función para determinar la longitud de las puntas

    # Solicitar al usuario la entrada
    while True:
        try:
            eleccion_2 = float(input("\nIntroduce la longitud de las puntas: "))
            break
        except ValueError:
            print("\nPor favor, introduce una longitud válida.")
    
    return eleccion_2


def main():
    # Función principal para dibujar la estrella

    # Mostrar título por consola
    titulo = "ESTRELLAS REGULARES"
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