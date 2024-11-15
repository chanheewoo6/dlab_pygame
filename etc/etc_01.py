import pygame, sys
from pygame.locals import *

pygame.init()

width = 500
height = 500

screen = pygame.display.set_mode((width, height))

# rect 생성 (가로크기, 세로크기)
r1 = pygame.Rect(100, 100, 100, 100)
r2 = pygame.Rect(300, 100, 50, 100)
r3 = pygame.Rect(100, 300, 50, 70)
r4 = pygame.Rect(300, 300, 100, 100)

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    # 마우스 버튼 눌렀는가 감지
    if event.type == MOUSEBUTTONDOWN:
      #이벤트가 발생한 좌표 출력
      print(event.pos)
    
    
  # 키보드 감지 & 움직임 확인 & 움직임 제한
  keys = pygame.key.get_pressed()
  if keys[K_RIGHT] and r1.right < width:
    r1.x += 1
  if keys[K_LEFT] and r1.left > 0:
    r1.x -= 1
  if keys[K_DOWN] and r1.bottom < height:
    r1.y += 1
  if keys[K_UP] and r1.top > 0:
    r1.y -= 1
    
  screen.fill((255, 255, 255))

  # 사각형 그리기 (그려줄 곳, 색깔, 그려줄 사각형)
  pygame.draw.rect(screen, (255, 0, 0), r1, 5)
  pygame.draw.rect(screen, (0, 255, 0), r2)
  pygame.draw.rect(screen, (0, 0, 255), r3)
  pygame.draw.rect(screen, (0, 0, 0), r4, 5)

  pygame.display.update()