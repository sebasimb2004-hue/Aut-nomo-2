import random 
palabras_con_pista = {
    "python": "Lenguaje de programacion popular",
    "programa": "Conjunto de instrucciones para la computadora",
    "ahorcado": "juego de adivinanza con letras",
    "computadora": "Máquina para procesar información",
    "juego": "Actividad de entretenimiento",
    "algoritmo": "Conjunto de pasos para resolver un problema",
    "variable": "Espacio en memoria que almacena un valor",
    "funcion": "Bloque de código que realiza uan tarea",
    "condicion": "Se usa para decidir entre opciones",
    "bucle": "Repite instrucciones varias veces",
    "archivo": "Documento almacenado en la computadora",
    "proyecto": "Conjunto de tareas planificadas",
    "desarrollo": "Proceso de crear software",
    "teclado": "Dispositivo para escribir",
    "monitor": "Pantalla de la computadora",
    "memoria": "Almacena información temporalmente",
    "internet": "Red global de comunicacion",
    "software": "Programas que usa la computadora",
    "hardware": "Componentes físicos de la computadora",
    "codifiacion": "Escribir instrucciones en un lenguaje de programacion"
}
palabra, pista = random.choice(list(palabras_con_pista.items()))

letras_acertadas = ["_"] * len(palabra)
intentos = 6 
letras_usadas = []

ahorcado = [
   """
    +---+
    |   |
        |
        |
        |
        |
   =======""",
   """
    +---+
    |   |
    o   |
        |
        |
        |
   =======""",
   """
    +---+
    |   |
    o   |
    |   |
        |
        |
   =======""",
   """
    +---+
    |   |
    o   |
   /|   |
        |
        |
   =======""",
   """
    +---+
    |   |
    o   |
   /|\\  |
        |
        |
   =======""",
   """
    +---+
    |   |
    o   |
   /|\\  |
   /    |
        |
   =======""",
   """
    +---+
    |   |
    o   |
   /|\\  |
   / \\  |
        |
   ======="""        
]
print(f"pista:  {pista}")
while True:
    #Mostrar estado actual del ahorcado
    print("\n" + ahorcado[6 - intentos])
    print(" ".join(letras_acertadas))

    #Solicitar letra al usuario
    letra = input("Ingresa una letra: ").lower()
    #CONDICIONAL: Validacion de entrada, Verifica que el jugador ingrese una letra valida
    if len (letra) != 1 or not letra.isalpha():
        print("Por favor ingresa solo una letra valida.")
        continue
    #CONDICIONAL: Verificar si la letra ya fue usada
    if letra in letras_usadas:
        print("Ya ingresaste esa letra. Intenta con otra.")
        continue
    #Guardar la letra en la lista de usadas
    letras_usadas.append(letra)
    #CONDICIONAL: Verificar si la letra esta en la palabra
    if letra in palabra: 
        #BUCLE: Recorrer la palabra para actualizar las posiciones correctas
        for i,l in enumerate(palabra):
            if l == letra:
                letras_acertadas[i] = letra
        print("¡Acertaste!")
    else:
        #Si la letra no esta, se reduce el numero de intentos disponibles
        intentos -= 1
        print(f"Incorrecto. Te quedan {intentos} intentos.")
    #CONDICIONAL: Verificar si gano
    if "_" not in letras_acertadas:
        print("\n" + ahorcado[6 - intentos])
        print(f"¡Felicidades! Ganaste. La palabra era '{palabra}'")
        break
    #CONDICIONAL: Verificar si perdio
    if intentos == 0:
        print("\n" + ahorcado[6 - intentos])
        print(f"Perdiste. La palabra era '{palabra}'")
        break 