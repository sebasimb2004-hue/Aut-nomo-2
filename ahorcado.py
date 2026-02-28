import random
import time
import os

# ==========================================
# BASE DE DATOS ORGANIZADA POR CATEGORÍAS
# ==========================================
PALABRAS = {
    "Programación": {
        "python": "Lenguaje de programación popular",
        "java": "Lenguaje orientado a objetos",
        "variable": "Espacio en memoria que almacena un valor",
        "funcion": "Bloque de código que realiza una tarea",
        "algoritmo": "Conjunto de pasos para resolver un problema",
        "clase": "Molde para crear objetos",
        "objeto": "Instancia de una clase",
        "metodo": "Función dentro de una clase",
        "parametro": "Dato que recibe una función",
        "diccionario": "Estructura de datos clave-valor",
        "lista": "Estructura de datos ordenada y mutable",
        "booleano": "Tipo de dato verdadero o falso"
    },
    "Informática": {
        "computadora": "Máquina que procesa información",
        "hardware": "Componentes físicos",
        "software": "Programas del sistema",
        "memoria": "Almacena información temporal",
        "procesador": "Cerebro de la computadora",
        "archivo": "Documento almacenado",
        "servidor": "Equipo que ofrece servicios",
        "cliente": "Equipo que solicita servicios",
        "sistema": "Conjunto de elementos organizados",
        "red": "Conjunto de dispositivos conectados"
    },
    "Tecnología": {
        "internet": "Red global de comunicación",
        "digital": "Relacionado con tecnología electrónica",
        "innovacion": "Creación de algo nuevo",
        "tecnologia": "Aplicación del conocimiento científico",
        "datos": "Información procesable",
        "seguridad": "Protección contra amenazas",
        "usuario": "Persona que usa un sistema",
        "repositorio": "Lugar donde se almacena código",
        "actualizacion": "Mejora de software",
        "proyecto": "Conjunto de tareas planificadas"
    }
}

AHORCADO = [
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
     O   |
         |
         |
         |
    =======""",
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =======""",
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =======""",
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =======""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =======""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ======="""
]

# ==========================================
# FUNCIONES
# ==========================================
def elegir_categoria():
    print("\nCategorías disponibles:")
    categorias = list(PALABRAS.keys())
    for i, cat in enumerate(categorias, 1):
        print(f"{i}. {cat}")

    opcion = input("Selecciona categoría: ")
    if opcion.isdigit() and 1 <= int(opcion) <= len(categorias):
        return categorias[int(opcion) - 1]
    else:
        print("Opción inválida. Se selecciona Programación.")
        return categorias[0]

def elegir_dificultad():
    print("\nDificultad:")
    print("1. Fácil (8 intentos)")
    print("2. Medio (6 intentos)")
    print("3. Difícil (4 intentos)")
    opcion = input("Opción: ")
    return {"1": 8, "2": 6, "3": 4}.get(opcion, 6)

def seleccionar_palabra(categoria, usadas):
    disponibles = list(set(PALABRAS[categoria].keys()) - usadas)
    if not disponibles:
        return None, None
    palabra = random.choice(disponibles)
    pista = PALABRAS[categoria][palabra]
    usadas.add(palabra)
    return palabra, pista

def actualizar_palabra(palabra, letras_usadas):
    return list(map(lambda x: x if x in letras_usadas else "_", palabra))

def mostrar_estado(intentos_restantes, letras_mostradas, letras_usadas, intentos_base):
    # Calcular índice del dibujo del ahorcado
    usado = intentos_base - intentos_restantes
    usado = min(usado, len(AHORCADO) - 1)
    print(AHORCADO[usado])
    print("\nPalabra:", " ".join(letras_mostradas))
    print("Letras usadas:", ", ".join(sorted(letras_usadas)))

def guardar_ranking(nombre, puntaje):
    archivo = "ranking.txt"
    registros = []
    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            for linea in f:
                nombre_r, puntos = linea.strip().split(",")
                registros.append((nombre_r, int(puntos)))

    registros.append((nombre, puntaje))
    registros = sorted(registros, key=lambda x: x[1], reverse=True)[:5]

    with open(archivo, "w", encoding="utf-8") as f:
        for n, p in registros:
            f.write(f"{n},{p}\n")

def mostrar_ranking():
    archivo = "ranking.txt"
    print("\n===== TOP 5 JUGADORES =====")
    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            for i, linea in enumerate(f, 1):
                nombre, puntos = linea.strip().split(",")
                print(f"{i}. {nombre} - {puntos} puntos")
    else:
        print("Aún no hay registros.")

def reiniciar_ranking():
    archivo = "ranking.txt"
    if os.path.exists(archivo):
        with open(archivo, "w", encoding="utf-8") as f:
            f.write("")

def jugar():
    nombre = input("\nIngresa tu nombre: ")
    categoria = elegir_categoria()
    intentos_base = elegir_dificultad()
    palabras_usadas = set()
    puntaje_total = 0

    while True:
        palabra, pista = seleccionar_palabra(categoria, palabras_usadas)
        if palabra is None:
            print("No quedan más palabras en esta categoría.")
            break

        letras_usadas = []
        intentos_actuales = intentos_base
        inicio = time.time()
        print(f"\nPista: {pista}")

        while intentos_actuales > 0:
            letras_mostradas = actualizar_palabra(palabra, letras_usadas)
            mostrar_estado(intentos_actuales, letras_mostradas, letras_usadas, intentos_base)

            if "_" not in letras_mostradas:
                tiempo = round(time.time() - inicio, 2)
                puntaje_total += 50
                print(f"\n🎉 ¡Ganaste! Palabra: {palabra}")
                print(f"Tiempo: {tiempo}s")
                break

            letra = input("Ingresa una letra: ").lower()
            if len(letra) != 1 or not letra.isalpha():
                print("Letra inválida.")
                continue
            if letra in letras_usadas:
                print("Ya usaste esa letra.")
                continue

            letras_usadas.append(letra)
            if letra in palabra:
                print("Correcto!")
                puntaje_total += 10
            else:
                print("Incorrecto.")
                intentos_actuales -= 1
                puntaje_total -= 5

        if intentos_actuales == 0:
            print(AHORCADO[-1])
            print(f"\n💀 Perdiste. Palabra: {palabra}")
            break

        otra = input("¿Jugar otra palabra? (s/n): ").lower()
        if otra != "s":
            break

    print(f"\nPuntaje total: {puntaje_total}")
    guardar_ranking(nombre, puntaje_total)

def menu():
    while True:
        print("\n===== JUEGO DEL AHORCADO =====")
        print("1. Jugar")
        print("2. Ver Ranking")
        print("3. Salir")
        opcion = input("Selecciona opción: ")
        if opcion == "1":
            jugar()
        elif opcion == "2":
            mostrar_ranking()
        elif opcion == "3":
            print("Gracias por jugar.")
            reiniciar_ranking()  # Reinicia ranking al salir
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()