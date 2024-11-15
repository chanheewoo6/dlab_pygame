import pygame, sys
from pygame.locals import *

# 색상 상수
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

width = 500
height = 500

pygame.init()
screen = pygame.display.set_mode((width, height))

# Rect 객체 생성
r1 = pygame.Rect(100, 100, 100, 100)
r2 = pygame.Rect(100, 300, 50, 100)
r3 = pygame.Rect(300, 100, 50, 70)
r4 = pygame.Rect(300, 300, 100, 100)

color = RED

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

  # 키보드 이벤트 처리
  keys = pygame.key.get_pressed()
  if keys[K_RIGHT] and r1.right < width:
    r1.x += 1
  if keys[K_LEFT] and r1.left > 0:
    r1.x -= 1
  if keys[K_DOWN] and r1.bottom < height:
    r1.y += 1
  if keys[K_UP] and r1.top > 0:
    r1.y -= 1
    
  # 충돌 감지
  if r1.colliderect(r2):
    color = GREEN
  elif r1.colliderect(r3):
    color = BLUE
  elif r1.colliderect(r4):
    color = BLACK
  
  screen.fill(WHITE)
  
  # 사각형 그리기 (그려줄 곳, 색깔, 그려줄 사각형)
  pygame.draw.rect(screen, color, r1, 5)
  pygame.draw.rect(screen, GREEN, r2)
  pygame.draw.rect(screen, BLUE, r3)
  pygame.draw.rect(screen, BLACK, r4, 5)
  
  pygame.display.update()