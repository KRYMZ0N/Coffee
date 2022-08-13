import pygame as pg, sys

pg.init()

size = width, height = 400, 400

screen = pg.display.set_mode(size, pg.RESIZABLE)
img = pg.image.load("cup.png")
rect = img.get_rect()
white = 80, 80, 80
black = 0, 0, 0


def drawRect():
    blocksize = 5
    for x in range(0, width, blocksize):
        for y in range(0, height, blocksize):
            rect1 = pg.Rect(x, y, blocksize, blocksize)
            pg.draw.rect(screen, black, rect1, 1)


while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()

    rect.centerx = screen.get_width() / 2
    rect.centery = screen.get_height() / 2

    screen.fill(white)
    drawRect()
    screen.blit(img, rect)

    pg.display.flip()
