import pygame, sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((500, 500))

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    if event.type == MOUSEBUTTONDOWN:
      #이벤트가 발생한 좌표 출력
      print(event.pos)

  screen.fill((0, 0, 0))
  pygame.display.update()