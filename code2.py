import time

FILA=5
COLUMNA=5
gato=[0,0]
raton=[FILA-1,COLUMNA-1]

def crear():
    return[["_" for _ in range(COLUMNA)]for _ in range(FILA)]

def imprimir(p):
    for i in p:
        print(" ".join(i))

def update():
    matriz=crear()
    if 0<=gato[0]<FILA and 0<=gato[1]<COLUMNA:
        matriz[gato[0]][gato[1]]= "G"
    if 0<=raton[0]<FILA and 0<=raton[1]<COLUMNA:
        matriz[raton[0]][raton[1]]= "R"
    return matriz

def movimientos_p(pos):
    f=pos[0]
    c=pos[1]
    movi=[(f-1,c),(f+1,c),(f,c-1),(f,c+1)]
    valido=[]
    for m in movi:
        if 0<=m[0]<FILA and 0<=m[1]<COLUMNA:
            valido.append(m)
    return valido

def minimax(p_gato,p_raton,profundidad,t_r):
    if p_gato==p_raton:
        return -999
    if profundidad==0:
        return abs(p_gato[0]-p_raton[0])+abs(p_gato[1]-p_raton[1])
    if t_r==True:
        mejor_v=-1000000000
        mov=movimientos_p(p_raton)
        for m in mov:
            valor=minimax(p_gato, m, profundidad-1, False)
            mejor_v=max(mejor_v, valor)
        return mejor_v
    else:
        mejor_v=1000000000
        mov=movimientos_p(p_gato)
        for m in mov:
            valor=minimax(m, p_raton, profundidad-1, True)
            mejor_v=min(mejor_v, valor)
        return mejor_v
    
def IA_GATO():
    global gato
    mejor_v=100000000
    mejor_mov=gato
    mov=movimientos_p(gato)
    for m in  mov:
        valor=minimax(m, raton, 5, True)
        if valor<mejor_v:
            mejor_v=valor
            mejor_mov=m
    gato=mejor_mov

def IA_RATON():
    global raton
    mejor_v=-100000000
    mejor_mov=raton
    mov=movimientos_p(raton)
    for m in  mov:
        valor=minimax(gato, m, 2, False)
        if valor>mejor_v:
            mejor_v=valor
            mejor_mov=m
    raton=mejor_mov

turnos=10
for i in range(turnos):
    print(f"\nTURNOS {i+1}")
    IA_GATO()
    if gato==raton:
        print("el gato comio raton")
        break
    IA_RATON()
    mi_entorno=update()
    imprimir(mi_entorno)
    time.sleep(0.5)
if i==turnos-1:
    print("el raton escapo")

