# Juego del Ahorcado

## Datos del Creador
- **Alumno:** Sebastián  
- **Asignatura:** [Logica de Programacion]  
- **Fecha de entrega:** 01/03/2026  

---

## Objetivo del programa
El objetivo de este proyecto es desarrollar un juego del **Ahorcado** en Python que integre los conocimientos adquiridos durante las 8 semanas de la asignatura.  
El juego permite al usuario adivinar palabras de diferentes categorías, mostrando un muñeco que se completa con cada error, incorporando dificultad, ranking y puntuación.

---

## Principales funcionalidades
- Elección de **categorías**: Tecnología, Programación, Informática.  
- Palabras aleatorias con **pistas**.  
- Sistema de **dificultad** (Fácil, Medio, Difícil) ajustando los intentos.  
- **Ranking de puntajes** con top 5 jugadores, guardado en `ranking.txt`.  
- **Puntuación** por palabra y por juego completo.  
- **No repetición de palabras** dentro de la misma sesión.  
- **Opciones de jugar múltiples rondas**.  
- Integración de **programación funcional** usando `map()` y `lambda` para actualizar las letras acertadas.  
- **Muñeco del ahorcado** que se reinicia correctamente entre palabras y partidas.

---

## Introducción al proyecto
Este proyecto integra los temas de la asignatura revisados durante las 8 semanas:

1. **Unidad 1: Introducción y entorno de programación** – Resolución de problemas y configuración del entorno de desarrollo.  
2. **Unidad 2: Manejo de datos y algoritmos** – Estructuras de datos, diccionarios, sets y diagramas de flujo para organizar la lógica.  
3. **Unidad 3: Condicionales y bucles** – Control de flujo para validar letras, calcular intentos y puntajes.  
4. **Unidad 4: Estructuras de datos y funciones** – Organización del código en funciones y uso de programación funcional (`map`, `lambda`).  

Se complementa con **programación funcional** para mejorar la actualización de las letras en la palabra.

---

## Cómo ejecutar el juego

Sigue estos pasos en la terminal para ejecutar el juego:

```bash
# 1 Clonar el repositorio
git clone https://github.com/sebasimb2004-hue/Aut-nomo-2.git

# 2 Entrar a la carpeta del juego
cd Aut-nomo-2/SOFTWARE

# 3 Verificar que Python esté instalado
python --version
# Debe mostrar algo como Python 3.x
# Si no lo tienes, descárgalo desde https://www.python.org/downloads/

# 4 Ejecutar el juego
python ahorcado.py

# 5 Cómo jugar
# - Ingresa tu nombre
# - Selecciona la categoría (Tecnología, Programación, Informática)
# - Escoge la dificultad: Fácil, Medio o Difícil
# - Adivina las letras de la palabra
# - Revisa tu puntaje y el ranking al final
# - Puedes jugar otra palabra o salir del juego

# 6 Cerrar el juego
# Cierra la terminal. El ranking se guarda en ranking.txt para la sesión actual,
# pero se reinicia si así lo deseas.

## Consideraciones
- Cada partida reinicia correctamente el muñeco y las letras usadas.  
- El ranking se guarda solo durante la sesión y se reinicia al cerrar el juego si se desea.  
- Recomendado usar Python 3.x.  
- No se repiten palabras en la misma sesión.  
- Se pueden jugar múltiples rondas sin reiniciar el programa.  
- Buenas prácticas de programación y control de versiones implementadas usando GitHub.  
- Todas las funcionalidades cumplen con las 4 unidades de la asignatura.

## Créditos
Desarrollado por **Sebastián Simbaña** como proyecto final integrador de la asignatura logica de programacion, implementando buenas prácticas de programación y control de versiones con GitHub.