import pygame, sys
from pygame.locals import *

pygame.init()

width = 700
height = 400
screen = pygame.display.set_mode((width, height))

bgImage = pygame.image.load('05/background.jpg')
bgImage = pygame.transform.scale(bgImage, (width, height))

r1 = pygame.Rect(0, 223, 50, 80)

image1 = pygame.image.load('05/walk.png')
image1 = pygame.transform.scale(image1, (50, 80))
image2 = pygame.image.load('05/jump.png')
image2 = pygame.transform.scale(image2, (50, 80))

bear = image1

# 점프 상태 및 물리 변수 저장
is_jump = False
jump_velocity = 0
gravity = 0.5
jump_strength = 10

while True:
  pygame.time.delay(5)

  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

  keyInput = pygame.key.get_pressed()
  if keyInput[K_LEFT] and r1.left >= 0:
    r1.left -= 1
  if keyInput[K_RIGHT] and r1.right <= width:
    r1.right += 1

  # 점프기능
  if not is_jump:
    if keyInput[K_SPACE]:
      is_jump = True
      jump_velocity = jump_strength
      bear = image2  # 점프 이미지로 변경
  else:
    r1.y -= jump_velocity
    jump_velocity -= gravity

    if jump_velocity < -jump_strength:
      is_jump = False
      bear = image1  # 걷는 이미지로 변경
      r1.y = 223  # 초기 위치로 복귀

  screen.blit(bgImage, (0, 0))    # 배경이미지
  screen.blit(bear, r1)
  pygame.display.update()
  pygame.time.delay(3)