import random
import math
import time


# --- TUS FUNCIONES DE BASE ---
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
    # Dibujamos al gato y al ratón
    if pos_validas(fila, columna, ubi_gato):
        tablero[ubi_gato[0]][ubi_gato[1]] = "G"
    if pos_validas(fila, columna, ubi_raton):
        tablero[ubi_raton[0]][ubi_raton[1]] = "R"
    return tablero


def movimientos(fila, columna, pos_actual):
    f, c = pos_actual
    posibilidades = [(f - 1, c), (f + 1, c), (f, c - 1), (f, c + 1)]
    validos = [mov for mov in posibilidades if 0 <= mov[0] < fila and 0 <= mov[1] < columna]#1
    return validos


# --- EL CORAZÓN DEL RETO: ALGORITMO MINIMAX ---
def minimax(pos_gato, pos_raton, profundidad, es_maximizando, f, c):
    # Caso base: El gato atrapa al ratón
    if pos_gato == pos_raton:
        return -100 if es_maximizando else 100#2

    # Caso base: Límite de "visión" del futuro
    if profundidad == 0:
        # Puntuación basada en Distancia Manhattan
        return abs(pos_gato[0] - pos_raton[0]) + abs(pos_gato[1] - pos_raton[1])#3

    if es_maximizando:
        # Turno del RATÓN: Quiere ALEJARSE (Maximizar distancia)
        mejor_valor = -math.inf#4
        for mov in movimientos(f, c, pos_raton):
            valor = minimax(pos_gato, mov, profundidad - 1, False, f, c)#5
            mejor_valor = max(mejor_valor, valor)#4
        return mejor_valor
    else:
        # Turno del GATO: Quiere ACERCARSE (Minimizar distancia)
        mejor_valor = math.inf
        for mov in movimientos(f, c, pos_gato):
            valor = minimax(mov, pos_raton, profundidad - 1, True, f, c)#5.1
            mejor_valor = min(mejor_valor, valor)#4.1
        return mejor_valor


def mov_inteligente_gato(ubi_gato, ubi_raton, f, c):
    opciones = movimientos(f, c, ubi_gato)
    mejor_mov = ubi_gato
    mejor_valor = math.inf
    for mov in opciones:
        # El gato simula qué hará el ratón después
        valor = minimax(mov, ubi_raton, 3, True, f, c)
        if valor < mejor_valor:
            mejor_valor = valor
            mejor_mov = mov
    return mejor_mov


def mov_inteligente_raton(ubi_raton, ubi_gato, f, c):
    opciones = movimientos(f, c, ubi_raton)
    mejor_mov = ubi_raton
    mejor_valor = -math.inf
    for mov in opciones:
        # El ratón simula qué hará el gato después
        valor = minimax(ubi_gato, mov, 3, False, f, c)
        if valor > mejor_valor:
            mejor_valor = valor
            mejor_mov = mov
    return mejor_mov


def juego_terminado(ubi_gato, ubi_raton, turno_actual, max_turnos):
    if ubi_gato == ubi_raton:
        return True
    if turno_actual >= max_turnos:
        return True
    return False


# --- CONFIGURACIÓN E INICIO ---
print("--- BIENVENIDO AL MINIMAX LAB ---")
f = int(input("Filas: "))
c = int(input("Columnas: "))

gato_pos = (random.randint(0, f - 1), random.randint(0, c - 1))
raton_pos = (random.randint(0, f - 1), random.randint(0, c - 1))
while gato_pos == raton_pos:
    raton_pos = (random.randint(0, f - 1), random.randint(0, c - 1))

max_turnos = 30
turno = 0

# --- BUCLE DE JUEGO (IA vs IA) ---
while not juego_terminado(gato_pos, raton_pos, turno, max_turnos):
    tablero_actual = actualizar_laboratorio(f, c, gato_pos, raton_pos)
    print(f"\nTurno {turno}/{max_turnos}")
    mostrar_laboratorio(tablero_actual)

    # 1. Movimiento del Gato (IA)
    gato_pos = mov_inteligente_gato(gato_pos, raton_pos, f, c)
    if gato_pos == raton_pos: break

    # 2. Movimiento del Ratón (IA)
    raton_pos = mov_inteligente_raton(raton_pos, gato_pos, f, c)

    turno += 1
    time.sleep(0.55)  # Para poder ver el movimiento

# Resultado final
tablero_final = actualizar_laboratorio(f, c, gato_pos, raton_pos)
mostrar_laboratorio(tablero_final)
if gato_pos == raton_pos:
    print("\n¡Miau! El gato atrapó al ratón mediante cálculo Minimax.")
else:
    print("\n¡El ratón escapó! Su estrategia fue superior.")
