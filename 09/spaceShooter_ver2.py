import pygame, sys
from pygame.locals import *
import random as rd

start = False

def reset():
  global start, hp, score
  start = False
  hp = 200
  hp_rect.width = hp
  score = 0
  text = font.render(str(score), True, (255, 255, 255))
  enemies.clear()  # 운석 초기화
  bullets.clear()  # 총알 초기화
  spaceship["rect"].topleft = (30, 215)  # 우주선 위치 초기화

def drawEnemies():
  # 운석 이동
  for e in enemies:
    e["rect"].x -= 2
    screen.blit(e["image"], e["rect"])
    if e["rect"].right <= 0:
      enemies.remove(e)

def loading():
  global start
  main_img = pygame.image.load("09/start.jpg")
  main_img = pygame.transform.scale(main_img, (width, height))
  screen.blit(main_img, (0, 0))
  pygame.display.update()
  keyInput = pygame.key.get_pressed()
  if keyInput[K_SPACE]:
    start = True
    reset()

def gameOver():
  global start
  start = False
  main_img = pygame.image.load("09/gameover.jpg")
  main_img = pygame.transform.scale(main_img, (width, height))
  screen.blit(main_img, (0, 0))
  pygame.display.update()
  keyInput = pygame.key.get_pressed()
  if keyInput[K_r]:
    reset()

pygame.init()

width = 700
height = 500
screen = pygame.display.set_mode((width, height))

# 배경
bgImage = pygame.image.load("09/background.jpg")
bgImage = pygame.transform.scale(bgImage, (width, height))
backX = 0
backX2 = width - 10

# 주인공
img = pygame.image.load("09/spaceship.png")
spaceship = {
  "rect": pygame.Rect(30, 215, 70, 70),
  "image": pygame.transform.scale(img, (70, 70)),
}

# 총알
bullets = []
bulletImage = pygame.image.load("09/bullet1.png")
bulletImage = pygame.transform.scale(bulletImage, (20, 10))

# 운석
enemies = []
cnt = 0 # 운선 소환 시간 체크 기능
imgList = [
  pygame.image.load("09/stone1.png"),
  pygame.image.load("09/stone2.png")
]

# HP
hp = 200
hp_rect = pygame.Rect(10, 10, hp, 20)

# 점수
score = 0
font = pygame.font.SysFont("malgungothic", 30, bold=True)
text = font.render(str(score), True, (255, 255, 255))

while True:
  
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    if event.type == KEYDOWN:
      if event.key == K_SPACE and not start:
        start = True
      elif event.key == K_SPACE and start:
        bullet = pygame.Rect(
          spaceship["rect"].centerx - 10, spaceship["rect"].centery - 5, 20, 10
        )
        bullets.append(bullet)
      elif event.key == K_r and not start:  # R 키로 재시작
        reset()
        start = True

  if not start:
    if hp <= 0:
      gameOver()
    else:
      loading()
    continue
    
  # 키보드 이벤트
  keyInput = pygame.key.get_pressed()
  if keyInput[K_RIGHT]:
    backX -= 3
    backX2 -= 3

  if keyInput[K_UP] and spaceship["rect"].top > 0:
    spaceship["rect"].top -= 3
  elif keyInput[K_DOWN] and spaceship["rect"].bottom < height:
    spaceship["rect"].bottom += 3

  # 배경 움직임
  if backX <= width * -1:
    backX = width - 10

  if backX2 <= width * -1:
    backX2 = width - 10

  if backX >= 0:
    backX -= width - 10
    backX2 -= width - 10
  
  # 운석 생성
  cnt += 1
  if cnt >= 200:
    cnt = 0
    size = rd.randint(20, 60)
    enemy = {
      "rect": pygame.Rect(width, rd.randint(size, height - size), size, size),
      "image": pygame.transform.scale(rd.choice(imgList), (size, size)),
    }
    enemies.append(enemy)
    
  screen.blit(bgImage, (backX, 0))
  screen.blit(bgImage, (backX2, 0))

  for bullet in bullets:
    bullet.x += 5
    screen.blit(bulletImage, bullet)
    if bullet.right >= width:
      bullets.remove(bullet)

  # 충돌 체크
  for b in bullets:
    for e in enemies:
      if b.colliderect(e["rect"]):
        score += 1
        bullets.remove(b)
        enemies.remove(e)
        text = font.render(str(score), True, (255, 255, 255))
  
  # HP 체크
  for e in enemies:
    if spaceship["rect"].colliderect(e["rect"]):
      hp -= 20
      hp_rect.width = hp
      print(hp)
      enemies.remove(e)
      if hp <= 0:
        gameOver()  # 게임오버 화면 표시

  drawEnemies()
  
  pygame.draw.rect(screen, (255, 69, 0), hp_rect)
  pygame.draw.rect(screen, (255, 255, 255), (10, 10, 200, 20), 3)

  screen.blit(spaceship["image"], spaceship["rect"])
  screen.blit(text, (width/2, 10))
  pygame.display.update()
  pygame.time.delay(4)
