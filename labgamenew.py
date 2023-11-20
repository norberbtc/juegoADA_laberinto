import os
import random

nombre_jugador = input("Por favor, introduce tu nombre: ")

ascii_art = """
### ##     ####   ### ###  ###  ##  ### ###  ### ###  ###  ##    ####   ### ##    ## ##
##  ##     ##     ##  ##    ## ##   ##  ##   ##  ##    ## ##     ##     ##  ##  ##   ##
##  ##     ##     ##       # ## #   ##  ##   ##       # ## #     ##     ##  ##  ##   ##
## ##      ##     ## ##    ## ##    ##  ##   ## ##    ## ##      ##     ##  ##  ##   ##
##  ##     ##     ##       ##  ##   ### ##   ##       ##  ##     ##     ##  ##  ##   ##
##  ##     ##     ##  ##   ##  ##    ###     ##  ##   ##  ##     ##     ##  ##  ##   ##
### ##     ####   ### ###  ###  ##     ##    ### ###  ###  ##    ####   ### ##    ## ##
"""

print(ascii_art)
print(f"Bienvenido, {nombre_jugador}!")



import os
import random

class Juego:
    def __init__(self, mapa, posicion_inicial, posicion_final):
        self.mapa = mapa
        self.posicion_inicial = posicion_inicial
        self.posicion_final = posicion_final

    def crear_laberinto(self):
        filas = self.mapa.split("\n")
        matriz = [list(fila) for fila in filas]
        return matriz

    def mostrar_laberinto(self, laberinto_matriz):
        os.system('cls' if os.name == 'nt' else 'clear')
        for fila in laberinto_matriz:
            print("".join(fila))

    def main_loop(self):
        laberinto_matriz = self.crear_laberinto()
        px, py = self.posicion_inicial
        filas = len(laberinto_matriz)
        columnas = len(laberinto_matriz[0])

        while (px, py) != self.posicion_final:
            self.mostrar_laberinto(laberinto_matriz)
            if 0 <= py < filas and 0 <= px < columnas:  # Verificar que las coordenadas sean válidas
                laberinto_matriz[py][px] = 'P'
            else:
                print("Coordenadas del jugador fuera de límites.")
                break

            movimiento = input("Presiona una tecla de flecha para mover al jugador (q para salir): ")

            if movimiento == "q":
                break
            elif movimiento == "w":
                if py - 1 >= 0 and laberinto_matriz[py - 1][px] != '#':
                    laberinto_matriz[py][px] = '.'
                    py -= 1
            elif movimiento == "s":
                if py + 1 < filas and laberinto_matriz[py + 1][px] != '#':
                    laberinto_matriz[py][px] = '.'
                    py += 1
            elif movimiento == "a":
                if px - 1 >= 0 and laberinto_matriz[py][px - 1] != '#':
                    laberinto_matriz[py][px] = '.'
                    px -= 1
            elif movimiento == "d":
                if px + 1 < columnas and laberinto_matriz[py][px + 1] != '#':
                    laberinto_matriz[py][px] = '.'
                    px += 1

        self.mostrar_laberinto(laberinto_matriz)

        if (px, py) == self.posicion_final:
            print("\n¡Felicidades! Has superado el juego del laberinto.\n")

class JuegoArchivo(Juego):
    def __init__(self, path_a_mapas):
        self.path_a_mapas = path_a_mapas
        self.mapa, self.posicion_inicial, self.posicion_final = self.leer_mapa_aleatorio()

    def leer_mapa_aleatorio(self):
        archivos = os.listdir(self.path_a_mapas)
        nombre_archivo = random.choice(archivos)
        path_completo = os.path.join(self.path_a_mapas, nombre_archivo)

        with open(path_completo, 'r') as archivo:
            lineas = archivo.readlines()
            dimensiones = lineas[0].split()
            filas = int(dimensiones[0])
            columnas = int(dimensiones[1])
            mapa = ''.join(lineas[1:])

            posicion_inicial = (0, 0)  
            posicion_final = (columnas - 1, filas - 1)  

        return mapa, posicion_inicial, posicion_final

if __name__ == "__main__":
    mapa = """
    ..###################
    ....#...............#
    #.#.#####.#########.#
    #.#...........#.#.#.#
    #.#####.#.###.#.#.#.#
    #...#.#.#.#.....#...#
    #.#.#.#######.#.#####
    #.#...#.....#.#...#.#
    #####.#####.#.#.###.#
    #.#.#.#.......#...#.#
    #.#.#.#######.#####.#
    #...#...#...#.#.#...#
    ###.#.#####.#.#.###.#
    #.#...#.......#.....#
    #.#.#.###.#.#.###.#.#
    #...#.#...#.#.....#.#
    ###.#######.###.###.#
    #.#.#.#.#.#...#.#...#
    #.#.#.#.#.#.#.#.#.#.#
    #.....#.....#.#.#.#.#
    ###################..
    """
    pos_ini = (0, 0)
    pos_fin = (20, 20)

    pos_2ini = (0, 0)
    pos_2fin = (19, 20)
    juego = Juego(mapa, pos_ini, pos_fin)
    juego.main_loop()

    # direccion
    juego_archivo = JuegoArchivo('Direccion de archivos')
    juego_archivo.main_loop()

