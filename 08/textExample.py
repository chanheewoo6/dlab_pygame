import pygame, sys
from pygame.locals import *

pygame.init()

width = 500
height = 500
screen = pygame.display.set_mode((width, height))

# 폰트 설정
font = pygame.font.SysFont(pygame.font.get_default_font(), 50, bold=False, italic=False)

# 폰트 렌더링
my_text1 = font.render("Hello Pygame", True, (255, 255, 255))
my_text2 = font.render("Hello Pygame", False, (255, 255, 255))
my_text3 = font.render("Hello Pygame", False, (255, 255, 255), (50, 70, 0))

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

  screen.fill((0, 0, 0))
  screen.blit(my_text1, (width/2 - my_text1.get_width()/2, height/2 - my_text1.get_height()/2))
  screen.blit(my_text2, (width/2 - my_text2.get_width()/2, height/2 - my_text2.get_height()/2 + 50))
  screen.blit(my_text3, (width/2 - my_text3.get_width()/2, height/2 - my_text3.get_height()/2 + 100))
  pygame.display.update()