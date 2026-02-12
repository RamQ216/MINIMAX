fila=5
columna=5
pos_gato=(0,0)
pos_raton=(4,4)
def crear_tablero():
        return [["_" for _ in range(columna)] for _ in range(fila)]

def mostrar_tablero(laboratorio):
    laboratorio[pos_gato[0]][pos_gato[1]] = "G"
    laboratorio[pos_raton[0]][pos_raton[1]] = "R"
    for f in laboratorio:
        print(" ".join(f))

m=crear_tablero()
mostrar_tablero(m)

def movimientos(fila,columna):
    mov=[(-1,0),(1,0),(0,-1),(0,1)]
    mov_validos=[m for m in mov if 0<mov[0]<fila and 0<mov[1]<columna]
    return mov_validos



