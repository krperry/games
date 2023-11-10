"""
Rebound
A simple breakout style game
Written by Blindgoofball from Nibble Nerds
https://nibblenerds.com
"""
import openal
import accessible_output2.outputs.auto
from random import randint
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

o=accessible_output2.outputs.auto.Auto()
pygame.init()
pygame.mixer.init()

width=800
height=600

paddle_position=[width/2-20, height-40]
ball_position=[width/2, height-70]
ball_velocity=[0, 0]

listener=openal.Listener()
listener.distance_model=5
listener.position=(width/2, height-40, 0)

front_sound=pygame.mixer.Sound('sounds/beep.wav')
ball_sound=openal.LoadSound('sounds/ball.wav')
ball_source=openal.Player()
ball_source.add(ball_sound)
ball_source.position=(width/2, height-50, 0)
ball_source.loop=True
ball_source.rolloff=0.1
ball_source.reference_distance=0.1

paddle=pygame.rect.Rect(paddle_position[0], paddle_position[1], 40, 40)
ball=pygame.rect.Rect(0, 0, 10, 10)
ball.center=ball_position

blocks=[]
for i in range(width//40):
  for j in range((height-200)//40):
    blocks.append(pygame.rect.Rect(i*40, j*40, 40, 40))

def get_pitch(y):
  return 1.0+((height-y)/height)*(2.0)

def move_ball():
  ball_position[0]+=ball_velocity[0]*delta_time
  ball_position[1]-=ball_velocity[1]*delta_time
  ball.center=ball_position
  if ball.left < 0 or ball.right > width:
    bounce=pygame.mixer.Sound('sounds/bounce.wav')
    channel=pygame.mixer.find_channel()
    if ball.left < 0:
      channel.set_volume(1.0, 0.0)
    else:
      channel.set_volume(0.0, 1.0)
    channel.play(bounce)
    ball_velocity[0]*=-1
    ball_position[0]+=ball_velocity[0]*delta_time
  if ball.top < 0 or ball.bottom > height:
    ball_velocity[1]*=-1
    ball_position[1]-=ball_velocity[1]*delta_time
    pygame.mixer.Sound('sounds/bounce.wav').play()
  ball_source.position=(ball_position[0], ball_position[1], 0)
  ball_source.pitch=get_pitch(ball_position[1])

screen=pygame.display.set_mode((width, height))
pygame.display.set_caption('Rebound')
started=False
clock=pygame.time.Clock()
delta_time=0
ball_source.play()
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      break
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_b:
        o.speak(f"{len(blocks)} blocks remaining.")
      elif event.key == pygame.K_c:
        o.speak(str(len(in_front)))
  keys=pygame.key.get_pressed()
  if keys[pygame.K_SPACE] and not started:
    ball_position=[paddle_position[0]+20, paddle_position[1]-30]
    ball_velocity=[0, 150]
  if keys[pygame.K_LEFT] and paddle.left >= 5:
    paddle_position[0]-=5
    listener.position=(paddle_position[0], paddle_position[1], 0)
  if keys[pygame.K_RIGHT] and paddle.right <= width-5:
    paddle_position[0]+=5
    listener.position=(paddle_position[0], paddle_position[1], 0)
  move_ball()
  paddle.center=paddle_position
  screen.fill((0, 0, 0))
  for block in blocks:
    pygame.draw.rect(screen, (255, 255, 255), block, 1)
  pygame.draw.rect(screen, (0, 255, 0), paddle)
  pygame.draw.rect(screen, (0, 0, 255), ball)
  pygame.display.update()
  if pygame.Rect.colliderect(ball, paddle) and ball_position[0] <= paddle_position[0]:
    ball_velocity[1]*=-1
    ball_velocity[0]=randint(-75, 0)
    pygame.mixer.Sound('sounds/deflect.wav').play()
  elif pygame.Rect.colliderect(ball, paddle) and ball_position[0] > paddle_position[0]:
    ball_velocity[1]*=-1
    ball_velocity[0]=randint(0, 75)
    pygame.mixer.Sound('sounds/deflect.wav').play()
  for block in range(len(blocks)):
    if pygame.Rect.colliderect(ball, blocks[block]):
      del blocks[block]
      pygame.mixer.Sound('sounds/collide.wav').play()
      break
  in_front=[block for block in blocks if block.left >= paddle.left and block.right <= paddle.right]
  if in_front:
    if not front_sound.get_num_channels():
      front_sound.play(-1)
  else:
    front_sound.stop()
  delta_time=clock.tick(60)/1000
ball_source.delete()
ball_sound.delete()
listener.delete()