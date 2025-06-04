import pygame
import sys

pygame.init()
width , height = 800,600
screen = pygame.display.set_mode(width ,height)
pygame.display.set_caption("dda line algoithm")
white=(25,255,255)
black=(0,0,0)

def draw_line_dda(x1,y1,x2,y2):
    dx=abs(x2-x1)
    dy=abs(y2-y1)
    if dx>dy:
        steps =dx
    else:
        steps =dy
    
    xinc = dx/steps        
    yinc = dy/steps
    x=x1
    y=y1
for i in range (steps +1):
    print(x,",",y)
    x = x+ xinc        
    y += yinc
screen.set_at((round(x),round(y)),white)            

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(black)
        draw_line_dda(100,100,1000,900)
        pygame.display.flip
        if __name__=="--main--":
            main()
       
                    