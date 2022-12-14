#-*- coding: utf-8 -*-
import pygame


#크기
SCREEN_WIDTH =800
SCREEN_HEIGHT =600

BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(239,82,108)
GREEN=(119,185,113)
BLUE=(116,194,208)
YELLOW=(239,226,68)



#초기화
pygame.init()

#윈도우제목
pygame.display.set_caption("boomboom ball")

#스크린 정의
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#게임화면 업데이트 속도
clock = pygame.time.Clock()



#공 초기 위치/크기/속도
ball_x=int(SCREEN_WIDTH/2)
ball_y=int(SCREEN_HEIGHT/2)
ball_dx=4
ball_dy=4
ball_size=40
   
   
# 게임 종료 전까지 반복
done=False

# 게임 반복 구간
while not done:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
      # QUIT는 윈도우 창을 닫을 때 발생하는 이벤트
      # 창이 닫히는 이벤트가 발생했다면
      
         done = True #반복 중단으로 게임 종료
         
         
   # 게임 로직 구간
   #속도에 따라 위치변경
   ball_x +=ball_dx
   ball_y +=ball_dy
   
   #스크린 벗어날 경우
   if (ball_x+ball_size)>SCREEN_WIDTH or (ball_x - ball_size)<0:
      ball_dx = ball_dx *-1
   if (ball_y +ball_size)>SCREEN_HEIGHT or(ball_y- ball_size)<0:
      ball_dy=ball_dy*-1

   # 화면 삭제 구간  
          
         
   #스크린채우기
   screen.fill(RED)

   #화면그리기
   #공   
   pygame.draw.circle(screen,YELLOW,[ball_x,ball_y],ball_size,0)

  
   
   #화면 업데이트
   pygame.display.flip()

   #화면 업데이트 60/초
   clock.tick(60)


""" for i in pygame.font.get_fonts():
    print(i)
    
     """
pygame.quit() 
         
         