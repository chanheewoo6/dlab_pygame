import pygame
import sys
import random

pygame.init()

width = 600
height = 700

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Avoid poop!")

total_time = 100
done = False
life = 100  # 초기 점수 설정
level = 1

font = pygame.font.SysFont("malgungothic", 13)

player_mode = None
ground_y = height - 400

# 플레이어 이미지
player = pygame.image.load("etc/myproject/images/player.png")
player = pygame.transform.scale(player, (70, 70))
player2 = pygame.transform.flip(player, True, False)

#배경 화면
background = pygame.image.load("etc/myproject/images/background.png")
background = pygame.transform.scale(background, (width, height))
ground = pygame.image.load("etc/myproject/images/ground.png")
ground = pygame.transform.scale(ground, (width, 400))

# 똥 이미지
poop = pygame.image.load("etc/myproject/images/poop.png")
poop = pygame.transform.scale(poop, (30, 30))
poop_die = pygame.image.load("etc/myproject/images/poop_die.png")
poop_die = pygame.transform.scale(poop_die, (30, 30))

player_rect = pygame.Rect(width/2, height-175, 70, 70)

x = 15
y = 15
clock = pygame.time.Clock()

# 하나의 이벤트만 설정
DROP_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(DROP_EVENT, 1000)

poop_rect = []
start_ticks = pygame.time.get_ticks() # 시작 시간 기록

def show_restart_screen(message):
  global level
  restart_font = pygame.font.SysFont("malgungothic", 30)
  restart_text = restart_font.render(message, True, (255, 255, 0))
  screen.blit(restart_text, (width/4 - restart_text.get_width()/4, height/2 - restart_text.get_height()/2))
  button = pygame.Rect(width/2 - 100, height/2 - 50, 200, 100)
  pygame.draw.rect(screen, (255, 0, 255), button)
  button_text = restart_font.render("다시 시작", True, (127, 255, 212))
  screen.blit(button_text, (button.x + (button.width - button_text.get_width()) / 2, button.y + (button.height - button_text.get_height()) / 2))
  pygame.display.update()
  
  waiting = True
  while waiting:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()
        if button.collidepoint(mouse_pos):
          waiting = False
          level += 1

paused = False  # 일시 정지 상태를 나타내는 변수

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    elif event.type == DROP_EVENT and not paused:
      x = random.randint(0, width - 50)
      # 똥 크기를 고정된 값으로 수정
      poop_rect.append(pygame.Rect(x, y, 30, 30))
      
  # 경과 시간 계산
  seconds = (pygame.time.get_ticks() - start_ticks) / 1000
  if seconds >= total_time:
    show_restart_screen("클리어!")
    life = 100
    poop_rect = []
    start_ticks = pygame.time.get_ticks()
    
    
  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT] and player_rect.x > 0 and not paused:
    player_rect.x -= 10
    player_mode = player2
  if keys[pygame.K_RIGHT] and player_rect.x < width - 100 and not paused:
    player_rect.x += 10
    player_mode = player
  if keys[pygame.K_SPACE]:
    paused = not paused  # space바를 누르면 일시 정지 상태를 토글
    if paused:
      stop_text = font.render("일시 정지", True, (255, 255, 255))
      screen.blit(stop_text, (width/2 - stop_text.get_width()/2, height/2 - stop_text.get_height()/2))
      pygame.display.update()
    else:
      screen.fill((30, 30, 30))
      pygame.display.update()
    
  if not paused:
    my_text = font.render(f"시간: {int(seconds)}", True, (86, 105, 225))
    life_text = font.render(f"생명: {life}", True, (255, 69, 0))
    
    screen.fill((30, 30, 30))
    screen.blit(background, (0, 0))
    screen.blit(ground, (0, ground_y))
    
    if player_mode:
      screen.blit(player_mode, player_rect)
    else:
      screen.blit(player, player_rect)
    for rect in poop_rect:
      screen.blit(poop, rect)
      rect.y += level * 2
      if player_rect.colliderect(rect):
        life -= 10  # 충돌 시 점수 10점 감소
        poop_rect.remove(rect)  # 충돌한 똥 제거
        if life <= 0:  # 점수가 0 이하가 되면 게임 종료
          show_restart_screen("게임 오버!")
          life = 100
          poop_rect = []
          start_ticks = pygame.time.get_ticks()
          
      elif rect.y > height - 175:
        screen.blit(poop_die, rect)
        clock.tick(100)
        poop_rect.remove(rect)
        
    # 점수 표시 위치 설정
    screen.blit(my_text, (width/2-10, 10))
    screen.blit(life_text, (width/2-10, 20))  # 시간 표시 아래에 점수 표시
    pygame.display.update()
  clock.tick(60)
