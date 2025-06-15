import pygame
import sys

pygame.init()
xc=(int(input("enter the x cordinate center point")))
yc=(int(input("enter the y cordinate center point")))
r=(int(input("enter the radius")))

WIDTH, HEIGHT = 800,1200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("midpoint circle  Algorithm")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def midpointcircle(xc,yc,r):
    d=1-r
    x=0
    screen.set_at((x+xc,y+yc),BLACK)
    screen.set_at((x+xc,y+yc),BLACK)
    screen.set_at((x+xc,y+yc),BLACK)
    screen.set_at((x+xc,y+yc),BLACK)
    screen.set_at((x+xc,y+yc),BLACK)
    screen.set_at((x+xc,y+yc),BLACK)
    screen.set_at((x+xc,y+yc),BLACK)
    screen.set_at((x+xc,y+yc),BLACK)
    while (x<=y):
        if (d<0):
            x+=1
            d+=2*x+1
        else:
            x+=1
            y-=1
            d+=2*x-2*y+1
        screen.set_at((x+xc,y+yc),BLACK)
        screen.set_at((-x+xc,y+yc),BLACK)
        screen.set_at((x+xc,-y+yc),BLACK)
        screen.set_at((-x+xc,-y+yc),BLACK)
        screen.set_at((y+yc,x+xc),BLACK)
        screen.set_at((-y+yc,x+xc),BLACK)
        screen.set_at((y+yc,-x+xc),BLACK)
        screen.set_at((-y+yc,-x+xc),BLACK)



def main():
    screen.fill(WHITE) 
    
    midpointcircle(xc,yc,r)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
        main()
