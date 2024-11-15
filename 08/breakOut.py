import pygame, sys
from pygame.locals import *
import random
import time
  
pygame.init()

width = 800
height = 500
screen = pygame.display.set_mode((width, height))

font = pygame.font.SysFont("malgungothic", 13)
stick = pygame.Rect(400, 470, 120, 20)

clock = pygame.time.Clock()
score = 0
level = 1

ball_img = pygame.image.load("08/tiles/ball.png")
ball_img = pygame.transform.scale(ball_img, (20, 20))
stick_img = pygame.image.load("08/tiles/stick.png")
stick_img = pygame.transform.scale(stick_img, (120, 20))

def render_level():
  return font.render(f"레벨: {level}", True, (255, 255, 255))

level_text = render_level()

def show_restart_screen(message):
  global score
  global balls
  global ball_velocities
  global level
  global level_text
  score_text = font.render(f"점수: {score}", True, (255, 255, 255))
  screen.blit(score_text, (10, 10))
  restart_font = pygame.font.SysFont("malgungothic", 30)
  restart_text = restart_font.render(message, True, (255, 255, 0))
  screen.blit(restart_text, (width/4 - restart_text.get_width()/4, height/2 - restart_text.get_height()/2))
  button = pygame.Rect(width/2 - 100, height/2 - 50, 200, 100)
  pygame.draw.rect(screen, (255, 0, 255), button)
  if message == "게임 오버":
    button_text = restart_font.render("다시 시작", True, (127, 255, 212))
    level = 1
    level_text = render_level()
    pygame.display.update()
  else:
    button_text = restart_font.render("다음 레벨", True, (127, 255, 212))
    level += 1
    level_text = render_level()
    screen.blit(level_text, (10, 40))
    pygame.display.update()
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
          reset_game()

def reset_game():
  global score
  global balls
  global ball_velocities
  score = 0
  balls = [pygame.Rect(width/2, height/2, 20, 20)]
  ball_velocities = [[-1, -1]]
  create_bricks()

# 벽돌 생성 (메인 루프 밖으로 이동)
bricks = []
brick_images = []

def show_done_screen(message):
  global score
  global balls
  global ball_velocities
  global level
  global level_text
  score_text = font.render(f"점수: {score}", True, (255, 255, 255))
  screen.blit(score_text, (10, 10))
  restart_font = pygame.font.SysFont("malgungothic", 30)
  restart_text = restart_font.render(message, True, (255, 255, 0))
  screen.blit(restart_text, (width/4 - restart_text.get_width()/2, height/2 - restart_text.get_height()/2))
  button = pygame.Rect(width/2 - 100, height/2 - 50, 200, 100)
  pygame.draw.rect(screen, (255, 0, 255), button)
  if message == "게임 클리어":
    button_text = restart_font.render("다시 시작", True, (127, 255, 212))
    level = 1
    level_text = render_level()
    pygame.display.update()
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
          reset_game()

def create_bricks():
  bricks.clear()
  brick_images.clear()
  for j in range(8):
    for i in range(12):
      brick = pygame.Rect((i+1)*60, j*20+50, 15, 5)
      bricks.append(brick)
      num = random.randint(1, 16)
      if 1 <= num <= 9:
        brick_img = pygame.image.load(f"08/tiles/0{num}-Breakout-Tiles.png")
      elif 10 <= num <= 16:
        brick_img = pygame.image.load(f"08/tiles/{num}-Breakout-Tiles.png")
      brick_img = pygame.transform.scale(brick_img, (25, 10))
      brick_images.append(brick_img)
  return bricks, brick_images
    
create_bricks()

# 공 리스트 초기화 (파일 상단에 추가)
balls = [pygame.Rect(width/2, height/2, 20, 20)]
ball_velocities = [[-1, -1]]  # 각 공의 속도를 저장

last_space_press_time = 0  # 마지막 스페이스바 누른 시간

for i in range(3):
  start_font = pygame.font.SysFont("malgungothic", 50)
  start_text = start_font.render(f"{3-i}", True, (255, 255, 255))
  screen.blit(start_text, (width/2 - start_text.get_width()/2, height/2 - start_text.get_height()/2))
  pygame.display.update()
  pygame.time.delay(1000)
  screen.fill((0, 0, 0))  # 마지막에 텍스트 지우기
  pygame.display.update()

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  if level > 3:
    show_done_screen("게임 클리어")
  
  # 스페이스바로 공 복사
  keys = pygame.key.get_pressed()
  current_time = time.time()
  if keys[K_SPACE] and current_time - last_space_press_time > 2:
    last_space_press_time = current_time
    new_balls = []
    new_velocities = []
    for ball, vel in zip(balls[:], ball_velocities[:]):
      new_ball = pygame.Rect(ball.x, ball.y, 20, 20)
      new_velocity = [vel[0], -vel[1]]
      new_balls.append(new_ball)
      new_velocities.append(new_velocity)
    balls.extend(new_balls)
    ball_velocities.extend(new_velocities)

  # 스틱 이동 (기존 코드 유지)
  if keys[K_LEFT]:
    stick.x -= 6
  if keys[K_RIGHT]:
    stick.x += 6
  if stick.left < 0:
    stick.left = 0
  if stick.right > width:
    stick.right = width

  # 모든 공 업데이트
  balls_to_remove = []  # 제거할 공들의 인덱스를 저장할 리스트
  for i, (ball, vel) in enumerate(zip(balls[:], ball_velocities[:])):
    ball.x += level * vel[0]
    ball.y += level * vel[1]
    
    # 벽과 충돌
    if ball.left <= 0 or ball.right >= width:
      vel[0] *= -1
    if ball.top <= 0:
      vel[1] *= -1
    if ball.top >= height:
      balls_to_remove.append(i)  # 제거할 공의 인덱스 저장
      continue
      
    ball_num = 0
    # 막대기와 충돌
    if ball.colliderect(stick):
      vel[1] *= -1
      # 버그 수정
      ball.bottom = stick.top - 1
      
    # 벽돌과 충돌 (기존 코드 유지)
    for brick, brick_img in zip(bricks, brick_images):
      if ball.colliderect(brick):
        vel[1] *= -1
        bricks.remove(brick)
        score += 1
        break
        
  # 루프가 끝난 후 공들을 제거
  for i in reversed(balls_to_remove):  # 큰 인덱스부터 제거
    balls.pop(i)
    ball_velocities.pop(i)
    if len(balls) == 0:
      show_restart_screen("게임 오버")
    elif score == 96:
      show_restart_screen("게임 성공")

  # 화면 그리기
  screen.fill((0, 0, 0))
  screen.blit(stick_img, stick)
  for ball in balls:
    screen.blit(ball_img, ball)
  for brick, brick_img in zip(bricks, brick_images):
    screen.blit(brick_img, brick)
  screen.blit(level_text, (10, 40))
  
  score_image = font.render(f"점수: {score}", True, (255, 255, 255))
  screen.blit(score_image, (10, 10))
  pygame.display.update()
  pygame.time.delay(3)