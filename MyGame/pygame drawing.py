#-*- coding: utf-8 -*-
import pygame

#크기
SCREEN_WIDTH =800
SCREEN_HEIGHT =800

BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(239,82,108)
GREEN=(119,185,113)
BLUE=(116,194,208)


#초기화
pygame.init()

#윈도우제목
pygame.display.set_caption("drawing somthing")

#스크린 정의
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#게임화면 업데이트 속도
clock = pygame.time.Clock()

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

   # 화면 삭제 구간         
         
   #스크린채우기
   screen.fill(WHITE)

   # 화면 그리기 구간
   ##선
   pygame.draw.line(screen,RED,[50,50],[500,50],10)
   #시작위치 50,50 / 끝날위치 500,50 / 선의 두께 10 
   pygame.draw.line(screen,BLUE,[50,100],[500,100],4)
   pygame.draw.line(screen,GREEN,[50,150],[500,150],8)   
 
   ##도형
   pygame.draw.rect(screen,RED,[50,200,150,150],20)
   pygame.draw.polygon(screen,BLUE,[[350,200],[250,350],[450,350]],2)
   pygame.draw.circle(screen,GREEN,[150,450],60,20)
   pygame.draw.ellipse(screen,BLUE,[250,400,200,100],0)
   
   ##글자
   font=pygame.font.SysFont('nanummyeongjo',40,True,False)
   text =font.render("cute my game",True,BLACK)
   screen.blit(text,[200,600])
   #화면 업데이트
   pygame.display.flip()

   #화면 업데이트 60/초
   clock.tick(60)


""" for i in pygame.font.get_fonts():
    print(i)
    
     """
pygame.quit() 
         
         