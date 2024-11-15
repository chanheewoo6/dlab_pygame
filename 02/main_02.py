import pygame, sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((300, 300))

rgb = 255

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      # 파이썬 프로그램 종료
      sys.exit()
    if event.type == KEYUP:
      if event.key == K_DOWN:
        rgb -= 20
        if rgb < 0:
          rgb = 255
      if event.key == K_UP:
        rgb += 20
        if rgb > 255:
          rgb = 0
      if event.key == K_SPACE:
        rgb = 255
      if event.key == K_ESCAPE:
        pygame.quit()
        sys.exit()

  screen.fill((rgb, 0, 0))
  pygame.display.update()