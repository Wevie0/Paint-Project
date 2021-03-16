from pygame import *
from math import *
from random import *
from tkinter import *
from tkinter import filedialog

init()
root = Tk()
root.withdraw()

colour_wheel = image.load("images/wheel.png")
black_white = image.load("images/blackwhite.jpg")
tool_0 = image.load("images/brush.png")
tool_1 = image.load("images/line.png")
tool_2 = image.load("images/eraser.png")
tool_3 = image.load("images/spray-paint.png")
tool_4 = image.load("images/pencil.png")

icon = image.load("images/paint.png")
display.set_icon(icon)
display.set_caption("Paint Project")

width, height = 1400, 800
screen = display.set_mode((width, height))

RED = (255, 0, 0)
GREY = (127, 127, 127)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
L_BLUE = (173, 216, 230)

running = True
screen.fill(RED)

canvas = Rect(250, 50, 1100, 600)
draw.rect(screen, BLACK, (245, 45, 1110, 610), 10)
draw.rect(screen, WHITE, canvas, 0)
capture = screen.subsurface(canvas).copy()

tool = 0
colour = BLACK
thickness = 5

c = time.Clock()

Tool_0 = Rect(10, 50, 85, 85)
Tool_1 = Rect(10, 135, 85, 85)
Tool_2 = Rect(10, 220, 85, 85)
Tool_3 = Rect(10, 305, 85, 85)
Tool_4 = Rect(10, 390, 85, 85)
while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False
        if evt.type == MOUSEBUTTONDOWN:
            oldX, oldY = evt.pos
        if evt.type == MOUSEBUTTONUP:
            capture = screen.subsurface(canvas).copy()
            screen.blit(capture, (250, 50))

    mx, my = mouse.get_pos()
    mb = mouse.get_pressed(3)

    for i in range(5):
        draw.rect(screen, BLACK, (10, 50 + 85 * i, 85, 85), 2)
        draw.rect(screen, BLACK, (115, 50 + 85 * i, 85, 85), 2)
    for i in range(5):
        draw.rect(screen, RED, (11, 51 + 85 * i, 83, 83))
        screen.blit(eval("tool_" + str(i)), (10, 50 + 85 * i))

    screen.blit(colour_wheel, (10, 485))
    screen.blit(black_white, (15, 685))

    if mb[0] == 1 and my >= 485:
        if ((mx - 110) ** 2 + (my - 585) ** 2) ** 0.5 <= 90:
            colour = screen.get_at((mx, my))
        elif 215 >= mx >= 15 and 765 >= my >= 685:
            colour = screen.get_at((mx, my))

    if mb[0] == 1 and canvas.collidepoint(mx, my):
        if tool == 0:
            draw.circle(screen, colour, (mx, my), thickness)
        elif tool == 1:
            screen.set_clip(canvas)
            screen.blit(capture, (250, 50))
            draw.line(screen, colour, (mx, my), (oldX, oldY), thickness)
            screen.set_clip(None)
        elif tool == 2:
            draw.circle(screen, WHITE, (mx, my), thickness)
        elif tool == 3:
            for i in range(thickness // 2):
                rand_y = randint(my - thickness * 5, my + thickness * 5)
                rand_x = randint(int(mx - ((5 * thickness) ** 2 - abs(my - rand_y) ** 2) ** 0.5),
                                 int(mx + ((5 * thickness) ** 2 - abs(my - rand_y) ** 2) ** 0.5))
                draw.circle(screen, colour, (rand_x, rand_y), 2)
        elif tool == 4:
            draw.circle(screen, BLACK, (mx, my), 1)

    if mx < 250:
        for i in range(5):
            if eval("Tool_" + str(i)).collidepoint(mx, my):
                draw.rect(screen, L_BLUE, eval("Tool_" + str(i)))
                screen.blit(eval("tool_" + str(i)), (10, 50 + 85 * i))
                if mb[0] == 1:
                    tool = i

    if tool == 0:
        draw.rect(screen, BLUE, Tool_0)
        screen.blit(tool_0, (10, 50))
    elif tool == 1:
        draw.rect(screen, BLUE, Tool_1)
        screen.blit(tool_1, (10, 135))
    elif tool == 2:
        draw.rect(screen, BLUE, Tool_2)
        screen.blit(tool_2, (10, 220))
    elif tool == 3:
        draw.rect(screen, BLUE, Tool_3)
        screen.blit(tool_3, (10, 305))

    display.flip()
    c.tick(120)

quit()

quit()
