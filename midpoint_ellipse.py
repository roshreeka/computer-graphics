import pygame
import sys

rx = int(input("Enter major axis (rx): "))
ry = int(input("Enter minor axis (ry): "))
xc = int(input("Enter x-axis center: "))
yc = int(input("Enter y-axis center: "))

pygame.init()


WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Midpoint Ellipse Drawing Algorithm")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def flip_y(y):
    return HEIGHT - y

def plot_ellipse_points(xc, yc, x, y):
    points = [
        (xc + x, flip_y(yc + y)),
        (xc - x, flip_y(yc + y)),
        (xc + x, flip_y(yc - y)),
        (xc - x, flip_y(yc - y)),
    ]
    for px, py in points:
        if 0 <= px < WIDTH and 0 <= py < HEIGHT:
            screen.set_at((int(px), int(py)), BLACK)

def midpoint_ellipse(rx, ry, xc, yc):
    x = 0
    y = ry

    
    p1 = (ry * ry) - (rx * rx * ry) + (0.25 * rx * rx)
    dx = 2 * ry * ry * x
    dy = 2 * rx * rx * y

    
    while dx < dy:
        plot_ellipse_points(xc, yc, x, y)
        x += 1
        dx = 2 * ry * ry * x
        if p1 < 0:
            p1 = p1 + dx + (ry * ry)
        else:
            y -= 1
            dy = 2 * rx * rx * y
            p1 = p1 + dx - dy + (ry * ry)

    p2 = ((ry * ry) * ((x + 0.5) ** 2)) + ((rx * rx) * ((y - 1) ** 2)) - (rx * rx * ry * ry)

   
    while y >= 0:
        plot_ellipse_points(xc, yc, x, y)
        y -= 1
        dy = 2 * rx * rx * y
        if p2 > 0:
            p2 = p2 - dy + (rx * rx)
        else:
            x += 1
            dx = 2 * ry * ry * x
            p2 = p2 + dx - dy + (rx * rx)

def main():
    screen.fill(WHITE)
    midpoint_ellipse(rx, ry, xc, yc)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()