import pygame, sys
from pygame.locals import *

pygame.init()

width = 600
height = 400
screen = pygame.display.set_mode((width, height))

r1 = pygame.Rect(270, 170, 60, 60)
image1 = pygame.image.load('08\soccerBall.png')
image1 = pygame.transform.scale(image1, (60, 60))

# 공의 방향에 대한 수치를 지니는 리스트
vel = [-1, -1]

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

  # 공의 방향 값 적용
  r1.x += vel[0]
  r1.y += vel[1]
  
  # 튕김 기능 구현
  if r1.left <= 0 or r1.right >= width:  # x축 충돌 처리
    vel[0] *= -1
  if r1.top <= 0 or r1.bottom >= height:  # y축 충돌 처리
    vel[1] *= -1

  screen.fill((83, 193, 75))
  screen.blit(image1, r1)
  pygame.display.update()
  
  pygame.time.delay(4)