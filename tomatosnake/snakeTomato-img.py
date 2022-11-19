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
   
   screen.blit(tomatohead,[100,80])
   screen.blit(tomatobody,[100,100])
   screen.blit(tomatotail,[100,120])
   #화면 업데이트
   pygame.display.flip()

   #화면 업데이트 60/초
   clock.tick(60)


""" for i in pygame.font.get_fonts():
    print(i)
    
     """
pygame.quit() 
         
         