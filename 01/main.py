import pygame

# 파이게임을 사용할 수 있게 초기화
pygame.init()

# 창을 만들기
# set_mode((가로, 세로))
screen = pygame.display.set_mode((300, 300))
R = 255
G = 51
B = 51

pygame.display.flip()

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      break
  screen.fill((R, G, B))
  
  R += 1
  G += 1
  B += 1
  
  R %= 256
  G %= 256
  B %= 256
  
  pygame.display.update()
  pygame.time.delay(10)