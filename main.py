def crear_tablero(filas, columnas):
    # Creamos una matriz llena de puntos '.' que representan espacios vacíos
    tablero = [["__"  for _ in range(columnas)] for _ in range(filas)]

    return tablero


def limite(filas, columnas): #creamos los limites del tablero
    if filas < 0 or columnas < 0:
        return False
    else:
        return True


def es_valida(pos, filas, columnas):
    r, c = pos
    # Ahora funciona para cualquier tamaño de tablero
    return 0 <= r < filas and 0 <= c < columnas


def actualizar_tablero(filas, columnas, pos_gato, pos_raton):
    # Creamos un tablero limpio en cada renderizado
    tablero = [["__" for _ in range(columnas)] for _ in range(filas)]

    # Validamos antes de colocar para evitar errores de índice
    if es_valida(pos_gato, filas, columnas):
        tablero[pos_gato[0]][pos_gato[1]] = " G"  # Espacio para alinear
    if es_valida(pos_raton, filas, columnas):
        tablero[pos_raton[0]][pos_raton[1]] = " R"
    return tablero
def colocar_personajes(tablero, pos_gato, pos_raton):
    # Marcamos la posición del Gato con 'G' y del Ratón con 'R'
    tablero[pos_raton[0]][pos_raton[1]] = "G"
    tablero[pos_gato[0]][pos_gato[1]] = "R"





def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))

# Uso sencillo:
mi_tablero = crear_tablero(5, 4)
colocar_personajes(mi_tablero, (0, 0), (4, 3))
actualizar_tablero(5, 4, (0,0), (4,3))
mostrar_tablero(mi_tablero)


import random


def obtener_movimientos_validos(pos_actual, filas, columnas):
    r, c = pos_actual
    # El ratón puede ser ágil y moverse en 4 direcciones [cite: 21]
    arriba=(r - 1, c)
    abajo=(r + 1, c)
    izquierda=(r, c - 1)
    derecha=(r, c + 1)

    candidatos = [arriba, abajo, izquierda, derecha]

    validos = []
    for mov in candidatos:
        # Usamos tu lógica de límites mejorada
        if 0 <= mov[0] < filas and 0 <= mov[1] < columnas:
            validos.append(mov)
    return validos
def mover_raton_azar(pos_raton, filas, columnas):
    opciones = obtener_movimientos_validos(pos_raton, filas, columnas)
    # Elegimos una opción al azar de la lista
    nueva_posicion = random.choice(opciones)
    return nueva_posicion


def juego_terminado(pos_gato, pos_raton, turno_actual, max_turnos):
    # Condición 1: El gato atrapó al ratón
    if pos_gato == pos_raton:
        print("¡El gato atrapó al ratón!")
        return True

    # Condición 2: El ratón escapó tras X turnos
    if turno_actual >= max_turnos:
        print("¡El ratón logró escapar!")
        return True

    return False


def simular_persecucion(filas, columnas, max_turnos=10):
    # Definimos posiciones iniciales [cite: 20]
    pos_gato = (0, 0)
    pos_raton = (filas - 1, columnas - 1)

    print("¡Empieza el duelo cerebral!")

    for turno in range(1, max_turnos + 1):
        print(f"\n--- Turno {turno} ---")

        # 1. Turno del Ratón (Mueve al azar por ahora) [cite: 23]
        pos_raton = mover_raton_azar(pos_raton, filas, columnas)

        # 2. Verificar si el ratón se movió a la casilla del gato
        if pos_raton == pos_gato:
            tablero_final = actualizar_tablero(filas, columnas, pos_gato, pos_raton)
            mostrar_tablero(tablero_final)
            print("¡Increíble! El ratón se entregó solo. Gato gana.")
            return

        # 3. Turno del Gato (Mueve al azar por ahora, luego será Minimax) [cite: 25]
        # Usamos la misma lógica de azar para probar el tablero
        pos_gato = mover_raton_azar(pos_gato, filas, columnas)

        # 4. Mostrar el estado actual
        tablero_actual = actualizar_tablero(filas, columnas, pos_gato, pos_raton)
        mostrar_tablero(tablero_actual)

        # 5. Condición de finalización: Gato atrapa ratón
        if pos_gato == pos_raton:
            print("¡Miau! El gato ha atrapado al ratón.")
            return

    print("¡El tiempo se acabó! El ratón logró escapar del laboratorio.")


# Para probarlo:
simular_persecucion(5, 4, max_turnos=5)