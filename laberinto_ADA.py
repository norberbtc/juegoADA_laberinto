import pygame

WIDTH = 800
HEIGHT = 600

def generar_laberinto(tamaño):
  """Genera un laberinto de tamaño especificado."""
  laberinto = []
  for fila in range(tamaño):
    laberinto.append([random.randint(0, 1) for _ in range(tamaño)])
  for fila in range(tamaño):
    for columna in range(tamaño):
      if random.randint(0, 10) == 0:
        laberinto[fila][columna] = 2
  return laberinto

def mostrar_laberinto(laberinto):
  """Muestra el laberinto en la pantalla."""
  for fila in laberinto:
    for celda in fila:
      if celda == 0:
        color = (255, 255, 255)
      elif celda == 2:
        color = (0, 0, 0)
      else:
        color = (128, 128, 128)
      pygame.draw.rect(pantalla, color, (fila * 100, columna * 100, 100, 100))

def mover_jugador(laberinto, jugador, tecla):
  """Mueve al jugador por el laberinto."""
  if tecla == pygame.K_w:
    jugador.fila -= 1
  elif tecla == pygame.K_s:
    jugador.fila += 1
  elif tecla == pygame.K_a:
    jugador.columna -= 1
  elif tecla == pygame.K_d:
    jugador.columna += 1
  return jugador

def ha_ganado_jugador(laberinto, jugador):
  """Determina si el jugador ha ganado."""
  return jugador.fila == laberinto.shape[0] - 1 and jugador.columna == laberinto.shape[1] - 1

def main():
  """Juego principal."""
  pygame.init()
  pantalla = pygame.display.set_mode((WIDTH, HEIGHT))
  laberinto = generar_laberinto(10)
  jugador = Jugador(0, 0)
  while True:
    for evento in pygame.event.get():
      if evento.type == pygame.QUIT:
        pygame.quit()
        exit()
    mostrar_laberinto(laberinto)
    tecla = pygame.key.get_pressed()
    jugador = mover_jugador(laberinto, jugador, tecla)
    if ha_ganado_jugador(laberinto, jugador):
      print("¡Felicidades, has ganado el juego!")
      pygame.quit()
      exit()
    pygame.display.update()

class Jugador:
  """Representa al jugador."""

  def __init__(self, fila, columna):
    self.fila = fila
    self.columna = columna

