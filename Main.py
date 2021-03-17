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
tool_5 = image.load("images/save.png")
tool_6 = image.load("images/load.png")
tool_7 = image.load("images/undo.png")
tool_8 = image.load("images/redo.png")
tool_9 = image.load("images/delete.png")

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

canvas = Rect(250, 50, 1100, 600)
draw.rect(screen, BLACK, (245, 45, 1110, 610), 10)
draw.rect(screen, WHITE, canvas, 0)
capture = screen.subsurface(canvas).copy()


tool = 0
colour = BLACK
size = 5
oldX = oldY = 0

c = time.Clock()

Tool_0 = Rect(10, 50, 85, 85)
Tool_1 = Rect(10, 135, 85, 85)
Tool_2 = Rect(10, 220, 85, 85)
Tool_3 = Rect(10, 305, 85, 85)
Tool_4 = Rect(10, 390, 85, 85)
Tool_5 = Rect(115, 50, 85, 85)
Tool_6 = Rect(115, 135, 85, 85)
Tool_7 = Rect(115, 220, 85, 85)
Tool_8 = Rect(115, 305, 85, 85)
Tool_9 = Rect(115, 390, 85, 85)

while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False
        if evt.type == MOUSEBUTTONDOWN:
            oldX, oldY = evt.pos
            if evt.button == 4 and size < 100:
                size += 1
            if evt.button == 5 and size > 1:
                size -= 1
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
        draw.rect(screen, RED, (116, 51 + 85 * i, 83, 83))
        screen.blit(eval("tool_" + str(i + 5)), (115, 50 + 85 * i))

    screen.blit(colour_wheel, (10, 485))
    screen.blit(black_white, (15, 685))

    if mb[0] == 1 and my >= 485:
        if ((mx - 110) ** 2 + (my - 585) ** 2) ** 0.5 <= 90:
            colour = screen.get_at((mx, my))
        elif 215 >= mx >= 15 and 765 >= my >= 685:
            colour = screen.get_at((mx, my))

    if mb[0] == 1 and canvas.collidepoint(mx, my):
        if tool == 0:
            draw.circle(screen, colour, (mx, my), size)
        elif tool == 1:
            screen.set_clip(canvas)
            screen.blit(capture, (250, 50))
            draw.line(screen, colour, (mx, my), (oldX, oldY), size)
            screen.set_clip(None)
        elif tool == 2:
            draw.circle(screen, WHITE, (mx, my), size)
        elif tool == 3:
            for i in range(size // 2):
                rand_y = randint(my - size * 5, my + size * 5)
                rand_x = randint(int(mx - ((5 * size) ** 2 - abs(my - rand_y) ** 2) ** 0.5),
                                 int(mx + ((5 * size) ** 2 - abs(my - rand_y) ** 2) ** 0.5))
                draw.circle(screen, colour, (rand_x, rand_y), 2)
        elif tool == 4:
            draw.line(screen, colour, (mx, my), (pencilX, pencilY), 5)

    if tool == 5:
        tool = 1
        file_name = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=(("PNG", "*.png"), ("All Files", "*.*")))
        if len(file_name) > 0:
            if "." in file_name:
                image.save(screen.subsurface(canvas), file_name)
            else:
                image.save(screen.subsurface(canvas), file_name + ".png")
        continue
    if tool == 9:
        draw.rect(screen, WHITE, canvas)

    if mx < 250:
        for i in range(10):
            if eval("Tool_" + str(i)).collidepoint(mx, my):
                draw.rect(screen, L_BLUE, eval("Tool_" + str(i)))
                if i < 5:
                    screen.blit(eval("tool_" + str(i)), (10, 50 + 85 * i))
                else:
                    screen.blit(eval("tool_" + str(i)), (115, 50 + 85 * (i - 5)))
                if mb[0] == 1:
                    tool = i

    for i in range(10):
        if tool == i:
            draw.rect(screen, BLUE, eval("Tool_" + str(i)))
            if tool < 5:
                screen.blit(eval("tool_" + str(i)), (10, 50 + 85 * i))
            else:
                screen.blit(eval("tool_" + str(i)), (115, 50 + 85 * (i - 5)))

    pencilX, pencilY = mx, my
    display.flip()
    capture = screen.subsurface(canvas).copy()
    screen.fill(RED)
    draw.rect(screen, WHITE, canvas, 0)
    draw.rect(screen, BLACK, (245, 45, 1110, 610), 10)
    screen.blit(capture, (250, 50))
    c.tick(144)
quit()

