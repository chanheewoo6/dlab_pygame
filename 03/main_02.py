import pygame, sys
from pygame.locals import *
import random

pygame.init()

width = 500
height = 500

screen = pygame.display.set_mode((width, height))

# rect 생성 (가로크기, 세로크기)
rect_width = 100
rect_height = 100
r1 = pygame.Rect(0, 0, rect_width, rect_height)
r1.center = (width // 2, height // 2)  # 중앙에 정렬

# rect2 생성 (가로크기, 세로크기)
rect_width = 100
rect_height = 100
r2 = pygame.Rect(0, 0, rect_width, rect_height)
r2.center = (width // 2, height // 2)  # 중앙에 정렬

# 이미지 가져오기 
img1 = pygame.image.load("03\\image\\dcon.png")

#이미지 크기 조정
img1 = pygame.transform.scale(img1, (100, 100))

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    # 마우스 버튼 눌렀는가 감지
    if event.type == MOUSEBUTTONDOWN:
      #이벤트가 발생한 좌표 출력
      print(event.pos)
    
    if event.type == KEYDOWN:
      if event.key == K_SPACE:
        r1.centerx = random.randint(0, width - rect_width)
        r1.centery = random.randint(0, height - rect_height)
    
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
  if keys[K_d] and r2.right < width:
    r2.x += 1
  if keys[K_a] and r2.left > 0:
    r2.x -= 1
  if keys[K_s] and r2.bottom < height:
    r2.y += 1
  if keys[K_w] and r2.top > 0:
    r2.y -= 1
    
  

  screen.fill((0, 0, 0))

  # 사각형 그리기 (그려줄 곳, 색깔, 그려줄 사각형)
  pygame.draw.rect(screen, (255, 255, 255), r2, 0 )
  
  # 이미지 그려주기(그려줄곳, blit(이미지, 좌표))
  screen.blit(img1, (r1.x, r1.y))

  pygame.display.update()