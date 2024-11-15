import pygame, sys
from pygame.locals import *
import random

width = 800
height = 600

pygame.init()
screen = pygame.display.set_mode((width, height))

# 바탕이미지 설정
background_image = pygame.image.load('04/image/background.png')
background_image = pygame.transform.scale(background_image, (width, height))

#히트박스 설정
r1 = pygame.Rect(width/2-30, height/2-30, 60, 100)

# 코인 리스트 생성
coins = []

# 코인 생성
for i in range(random.randint(1, 30)):
  coin_image = pygame.image.load('04/image/coin.png')
  coin_image = pygame.transform.scale(coin_image, (40, 40))
  coin_rect = coin_image.get_rect()
  coin_rect.x = random.randint(0, width-30)
  coin_rect.y = random.randint(0, height-110)
  coins.append(coin_rect)

# 이미지 설정
mario_image_left = pygame.image.load('04/image/mario.png')
mario_image_left = pygame.transform.scale(mario_image_left, (60, 100))
mario_image_right = pygame.transform.flip(mario_image_left, True, False)

mario = mario_image_left

# 메인 bgm 한개의 음악과 큰 크기의 음악
bgm = pygame.mixer.music.load('04/sound/bgm.ogg')
pygame.mixer.music.play(-1)

#메인 bgm 여러개의 음악과 작은 크기의 음악
# bgm = pygmae.mixer.Sound(04/sound/bgm.ogg)
# bgm.play

while True:
  
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

  # 마리오 움직임
  keyInput = pygame.key.get_pressed()
  
  if keyInput[K_LEFT] and r1.left >= 0:
    r1.left -= 1
    mario = mario_image_left # 왼쪽 보기
  elif keyInput[K_RIGHT] and r1.right <= width:
    r1.right += 1
    mario = mario_image_right # 오른쪽 보기
  elif keyInput[K_UP] and r1.top >= 0:
    r1.top -= 1
  elif keyInput[K_DOWN] and r1.bottom <=510:   # 땅 충돌 처리
    r1.bottom += 1
    
  if len(coins) == 0 :
    print("끝")
    pygame.quit()
    sys.exit()
    
  # 마리오 코인 충돌 처리
  for coin_rect in coins:
    if r1.colliderect(coin_rect):
      coins.remove(coin_rect)
      
  
  #배경 이미지 그리기
  screen.blit(background_image, (0, 0))

  # 코인 이미지 그리기
  for coin in coins:
    screen.blit(coin_image, coin)

  # 마리오 이미지 그리기
  screen.blit(mario, r1)
  
  pygame.display.update()