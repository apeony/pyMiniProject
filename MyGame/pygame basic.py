import pygame

#크기
SCREEN_WIDTH =800
SCREEN_HEIGHT =800

BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(94,32,42)
GREEN=(47,73,44)
BLUE=(45,76,82)


#초기화
pygame.init()

#윈도우제목
pygame.display.set_caption("minigame palette")

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

   #화면 업데이트
   pygame.display.flip()

   #화면 업데이트 60/초
   clock.tick(60)


pygame.quit() 
         
         