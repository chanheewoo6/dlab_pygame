import pygame, sys
from pygame.locals import *

pygame.init()

width = 700
height = 500
screen = pygame.display.set_mode((width, height))

# 배경 이미지
bgImage = pygame.image.load("09/background.jpg")
bgImage = pygame.transform.scale(bgImage, (width, height))

backX = 0
backX2 = width

# 배경 이미지 속도
backSpeed = 2

# 주인공
img = pygame.image.load("09/spaceship.png")
img = pygame.transform.scale(img, (70, 70))
spaceship = {
  'rect' : pygame.Rect(0, 215, 70, 70),
  'image' : img,
  'speed' : 3
}

# 총알
bulletImg = pygame.image.load("09/bullet1.png")
bulletImg = pygame.transform.scale(bulletImg, (20, 10))
bullet = {
  'rect' : pygame.Rect(0, 215, 30, 60),
  'image' : bulletImg,
  'speed' : 10
}

bullets = []

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    if event.type == KEYDOWN and event.key == K_SPACE:
      b = pygame.Rect(-10, -10, 10, 20)
      b.center = spaceship['rect'].center  
      bullets.append(b)
  
  keyInput = pygame.key.get_pressed()
  if keyInput[K_LEFT]:
    spaceship['rect'].x -= spaceship['speed']
    if spaceship['rect'].x < 0:
      spaceship['rect'].x = 0
  if keyInput[K_RIGHT]:
    spaceship['rect'].x += spaceship['speed']
    if spaceship['rect'].x > width - spaceship['rect'].width:
      spaceship['rect'].x = width - spaceship['rect'].width
  if keyInput[K_UP]:
    spaceship['rect'].y -= spaceship['speed']
    if spaceship['rect'].y < 0:
      spaceship['rect'].y = 0
  if keyInput[K_DOWN]:
    spaceship['rect'].y += spaceship['speed']
    if spaceship['rect'].y > height - spaceship['rect'].height:
      spaceship['rect'].y = height - spaceship['rect'].height
  
  # 배경 X 좌표 이동
  # backX -= backSpeed
  # backX2 -= backSpeed
  
  # 스크롤링
  if backX < -width:
    backX = width
  if backX2 < -width:
    backX2 = width
  if backX > width:
    backX = -width
  if backX2 > width:
    backX2 = -width
  
  # 배경 그리기
  screen.blit(bgImage, (backX, 0))
  screen.blit(bgImage, (backX2, 0))
  # 주인공 그리기
  screen.blit(spaceship['image'], spaceship['rect'])
  for bu in bullets:
    bu.x += 3
    screen.blit(bullet['image'], bu)
    if bu.left > width:
      bullets.remove(bu)
  pygame.display.update()
  pygame.time.delay(3)