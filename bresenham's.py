import pygame
import sys

x1 = int(input("enter value"))
x2 = int(input("enter value"))
y1 = int(input("enter value"))
y2 = int(input("enter value"))

pygame.init()
WIDTH,HEIGHT=600,600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("bresenham's line algo")
white=(25,255,255)
black=(0,0,0)


def draw_line(x1,y1,x2,y2):
    dx=abs(x2-x1)
    dy=abs(y2-y1)
    
    x= x1
    y= y1

    if x2>x1:
        lx=1
    else :
        lx=-1

    if y2>y1:
        ly=1
    else:
        ly=-1

    if dx>dy:
            p = 2 * dy - dx
            for _ in range(dx):
                if p < 0:
                    x += lx
                    p += 2 * dy
            else:
                x += lx
                y += ly 
                p += 2 * dy - 2 * dx
            screen.set_at((round(x), HEIGHT - round(y)), black)
    else:
        p = 2 * dx - dy
        for _ in range(dy):
            if p < 0:
                y += ly
                p += 2 * dx
            else:
                x += lx
                y += ly
                p += 2 * dx - 2 * dy
            screen.set_at((round(x), HEIGHT - round(y)), black)
        
def main():
    screen.fill(white)
    draw_line(x1, y1, x2, y2)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


				

if __name__ == "__main__":
    main()
