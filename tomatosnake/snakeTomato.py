#-*- coding: utf-8 -*-
import pygame
import os
import sys
import random
from time import sleep



#크기
SCREEN_WIDTH =800
SCREEN_HEIGHT =600

#게임화면 전역변수
GRID_SIZE = 20
GRID_WIDTH =SCREEN_WIDTH/GRID_SIZE
GRID_HEIGHT =SCREEN_HEIGHT/GRID_SIZE

#방향 전역변수
UP=(0,-1)
DOWN=(0,1)
LEFT=(-1,0)
RIGHT=(1,0)

#색상전역변수
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(239,82,108)
GREEN=(119,185,113)
BLUE=(116,194,208)
YELLOW=(239,226,68)
PINK=(231,165,199)
TILBLUE=(141,219,211)

#토마토뱀 정의
class Tomato():
   def __init__(self):
      self.creat()
      
   def create(self):
      self.length=2
      self.position=[(int(SCREEN_WIDTH/2),int(SCREEN_HEIGHT/2))]
      self.direction=random.choice([UP,DOWN,LEFT,RIGHT])
   
   def control(self,xy):
      if(xy[0]*-1,xy[1]*-1)==self.direction:
         return
      else:
         self.direction=xy
         
   def move(self):
      cur = self.position[0]
      x,y=self.direction
      new=(cur[0]+(x* GRID_SIZE)),(cur[1]+(y* GRID_SIZE))
      
      if new in self.position[2:]: #몸에 닿았을때
         sleep(1)
         self.create()
         
      #화면을 넘어갈때 
      elif new[0]<0 or new[0]>= SCREEN_WIDTH or new[1]<0 or new[1]>= SCREEN_HEIGHT:
         sleep(1)
         self.create()
         
      else: #정상이동
         self.position.insert(0,new)
         if len(self.position)>self.length:
            self.position.pop()
   
   def eat(self):
      self.length += 1
      
   def draw(self,screen):
      tomatohead,tomatobody,tomatotail=50/(self.length -1),150,150 /(self.length -1)
      for i, p in enumerate(self.position):
               
      
class Feed():
   def __init__(self):
      self.position =(0,0)
      self.color=YELLOW
      self.create()
         
#초기화
pygame.init()

#윈도우제목
pygame.display.set_caption("Tomato Snakes!")

#스크린 정의
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#게임화면 업데이트 속도
clock = pygame.time.Clock()


#assets 경로 구간
current_path=os.path.dirname(__file__)
assets_path=os.path.join(current_path,'assets')

#이미지 로드
background_image=pygame.image.load(os.path.join(assets_path,'bg.png'))
tomatohead=pygame.image.load(os.path.join(assets_path,'head.png'))
tomatobody=pygame.image.load(os.path.join(assets_path,'body.png'))
tomatotail=pygame.image.load(os.path.join(assets_path,'tail.png'))

#배경음악 로드
pygame.mixer.music.load(os.path.join(assets_path, 'elbgm.wav'))
pygame.mixer.music.play(-1) #무한재생

#효과음 로드
#boomsound=pygame.mixer.Sound(os.path.join(assets_path,'boom.wav'))
#eatsound=pygame.mixer.Sound(os.path.join(assets_path,'eatting.wav'))

# 게임 종료 전까지 반복
done=False

# 게임 반복 구간
while not done:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
      # QUIT는 윈도우 창을 닫을 때 발생하는 이벤트
      # 창이 닫히는 이벤트가 발생했다면
      
         done = True #반복 중단으로 게임 종료
      #if event.type == pygame.MOUSEBUTTONDOWN:
      #   sound.play()
         
   # 게임 로직 구간
   

   
   # 화면 삭제 구간         
         
   #스크린채우기
   screen.fill(TILBLUE)


   #화면 그리기 구간
   #배경이미지 그리기
   screen.blit(background_image, background_image.get_rect())

   #화면 업데이트
   pygame.display.flip()

   #화면 업데이트 60/초
   clock.tick(60)


""" for i in pygame.font.get_fonts():
    print(i)
    
     """
pygame.quit() 
         
         