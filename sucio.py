import random


# --- TUS FUNCIONES DE BASE (SIN CAMBIOS) ---
def crear_laboratorio(fila, columna):
    return [["_" for _ in range(columna)] for _ in range(fila)]


def mostrar_laboratorio(tablero_a_imprimir):
    for fila in tablero_a_imprimir:
        print(" ".join(fila))


def pos_validas(fila, columna, pos):
    f, c = pos
    return 0 <= f < fila and 0 <= c < columna


def actualizar_laboratorio(fila, columna, ubi_gato, ubi_raton):
    tablero = [["_" for _ in range(columna)] for _ in range(fila)]
    for p, s in [(ubi_gato, "G"), (ubi_raton, "R")]:
        if pos_validas(fila, columna, p):
            tablero[p[0]][p[1]] = s
    return tablero


def movimientos(fila, columna, pos_actual):
    f, c = pos_actual
    posibilidades = [(f - 1, c), (f + 1, c), (f, c - 1), (f, c + 1)]
    validos = [mov for mov in posibilidades if 0 <= mov[0] < fila and 0 <= mov[1] < columna]
    return validos


# --- EL CAMBIO LÓGICO: EL RATÓN AHORA ESCAPA ---
def mov_raton(ubi_raton, ubi_gato, fila, columna):
    opciones = movimientos(fila, columna, ubi_raton)

    # El ratón evalúa cada opción y elige la que lo aleje más del gato
    mejor_opcion = ubi_raton
    distancia_maxima = -1

    for opt in opciones:
        # Distancia de Manhattan entre la opción y el gato
        dist = abs(opt[0] - ubi_gato[0]) + abs(opt[1] - ubi_gato[1])
        if dist > distancia_maxima:
            distancia_maxima = dist
            mejor_opcion = opt

    return mejor_opcion


def juego_terminado(ubi_gato, ubi_raton, turno_actual, max_turnos):
    if ubi_gato == ubi_raton:
        print("\n¡Miau! El gato atrapó al ratón.")
        return True
    if turno_actual >= max_turnos:
        print("\n¡El ratón escapó del laboratorio!")
        return True
    return False


# --- CONFIGURACIÓN E INICIO ---
f = int(input("Filas: "))
c = int(input("Columnas: "))

gato_pos = (random.randint(0, f - 1), random.randint(0, c - 1))
raton_pos = (random.randint(0, f - 1), random.randint(0, c - 1))
while gato_pos == raton_pos:
    raton_pos = (random.randint(0, f - 1), random.randint(0, c - 1))

max_turnos = 20
turno = 0

# --- BUCLE DE JUEGO ---
while not juego_terminado(gato_pos, raton_pos, turno, max_turnos):
    tablero_actual = actualizar_laboratorio(f, c, gato_pos, raton_pos)
    print(f"\nTurno {turno}/{max_turnos}")
    mostrar_laboratorio(tablero_actual)

    # MOVIMIENTO DEL GATO (CONTROLADO POR TI)
    print("Mueve al Gato: W(arriba), A(izquierda), S(abajo), D(derecha)")
    jugada = input(">> ").upper()

    f_g, c_g = gato_pos
    nueva_p = gato_pos
    if jugada == "W" or "w":
        nueva_p = (f_g - 1, c_g)
    elif jugada == "S" or "s":
        nueva_p = (f_g + 1, c_g)
    elif jugada == "A" or "a":
        nueva_p = (f_g, c_g - 1)
    elif jugada == "D" or "d":
        nueva_p = (f_g, c_g + 1)

    if pos_validas(f, c, nueva_p):
        gato_pos = nueva_p
    else:
        print("¡Te chocaste con la pared!")

    # MOVIMIENTO DEL RATÓN (IA QUE HUYE)
    if gato_pos != raton_pos:
        raton_pos = mov_raton(raton_pos, gato_pos, f, c)

    turno += 1

mostrar_laboratorio(actualizar_laboratorio(f, c, gato_pos, raton_pos))