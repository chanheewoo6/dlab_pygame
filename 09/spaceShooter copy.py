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
  'speed' : 1
}

# 총알
bulletImg = pygame.image.load("09/bullet1.png")
bulletImg = pygame.transform.scale(bulletImg, (20, 10))
bullet = {
  'rect' : pygame.Rect(0, 215, 30, 60),
  'image' : bulletImg,
  'speed' : 18
}

spaceship_velocity = {'x': 0, 'y': 0}

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
    spaceship_velocity['x'] -= 1
  else:
    if spaceship_velocity['x'] < 0:
      spaceship_velocity['x'] += 1
  if keyInput[K_RIGHT]:
    spaceship_velocity['x'] += 1
  else:
    if spaceship_velocity['x'] > 0:
      spaceship_velocity['x'] -= 1
  if keyInput[K_UP]:
    spaceship_velocity['y'] -= 1
  else:
    if spaceship_velocity['y'] < 0:
      spaceship_velocity['y'] += 1
  if keyInput[K_DOWN]:
    spaceship_velocity['y'] += 1
  else:
    if spaceship_velocity['y'] > 0:
      spaceship_velocity['y'] -= 1
      
  # 배경 X 좌표 이동
  backX += -spaceship_velocity['x']
  backX2 += -spaceship_velocity['x']
  
  if spaceship_velocity['x'] < 0 and spaceship['rect'].left >= 0:
    spaceship['rect'].left += spaceship_velocity['x']
  elif spaceship_velocity['x'] > 0 and spaceship['rect'].right <= width:
    spaceship['rect'].right += spaceship_velocity['x']
  if spaceship_velocity['y'] < 0 and spaceship['rect'].top >= 0:
    spaceship['rect'].top += spaceship_velocity['y']
  elif spaceship_velocity['y'] > 0 and spaceship['rect'].bottom <= height:
    spaceship['rect'].bottom += spaceship_velocity['y']
  
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
    bu.x += bullet['speed']
    screen.blit(bullet['image'], bu)
    if bu.left > width:
      bullets.remove(bu)
  pygame.display.update()
  pygame.time.delay(50)