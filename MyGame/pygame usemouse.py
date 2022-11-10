#-*- coding: utf-8 -*-
import pygame
import os

#크기
SCREEN_WIDTH =800
SCREEN_HEIGHT =800


YELLOW=(243,220,45)


#초기화
pygame.init()

#윈도우제목
pygame.display.set_caption("KEYBOARD USING")

#스크린 정의
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#게임화면 업데이트 속도
clock = pygame.time.Clock()


#assets 경로 구간
current_path=os.path.dirname(__file__)
assets_path=os.path.join(current_path,'assets')

#이미지 로드
keyboard_image=pygame.image.load(os.path.join(assets_path,'blueberrypet.png'))
keyboard_x=int(SCREEN_WIDTH/2)
keyboard_y=int(SCREEN_HEIGHT/2)
keyboard_dx=0
keyboard_dy=0

# 게임 종료 전까지 반복
done=False

# 게임 반복 구간
while not done:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
      # QUIT는 윈도우 창을 닫을 때 발생하는 이벤트
      # 창이 닫히는 이벤트가 발생했다면
      
         done = True #반복 중단으로 게임 종료
         
      #키보드 조작
      #키보드 눌릴 경우
      elif event.type == pygame.KEYDOWN:
         if event.key==pygame.K_LEFT:
            keyboard_dx=-3
         elif event.key==pygame.K_RIGHT:
            keyboard_dx=5
         elif event.key==pygame.K_UP:
            keyboard_dy=-3
         elif event.key==pygame.K_DOWN:
            keyboard_dy=3
      #키보드 놓일 경우
      elif event.type==pygame.KEYUP:
         if event.key==pygame.K_LEFT or event.key== pygame.K_RIGHT:
            keyboard_dx=0
         elif event.key==pygame.K_UP or event.key== pygame.K_DOWN:
            keyboard_dy=0
            
            
         
   # 게임 로직 구간
   #이미지 위치변경
   keyboard_x +=keyboard_dx
   keyboard_y +=keyboard_dy
   # 화면 삭제 구간         
         
   #스크린채우기
   screen.fill(YELLOW)


   #화면 그리기 구간
   #키보드 이미지 그리기 
   screen.blit(keyboard_image,[keyboard_x,keyboard_y])
   
   #화면 업데이트
   pygame.display.flip()

   #화면 업데이트 60/초
   clock.tick(60)


""" for i in pygame.font.get_fonts():
    print(i)
    
     """
pygame.quit() 
         
         