from pygame import *
from math import *
from random import *
from tkinter import *
from tkinter import filedialog

init()  # Initialization
root = Tk()
root.withdraw()

RED = (255, 0, 0)  # Constant colour RGB values
GREY = (127, 127, 127)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
L_BLUE = (173, 216, 230)
L_GREEN = (157, 255, 176)

colour_wheel = image.load("images/wheel.png")  # Loading images
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
tool_10 = image.load("images/dropper.png")
tool_11 = image.load("images/text.png")
tool_12 = image.load("images/triangle.png")
tool_13 = image.load("images/rectangle.png")
tool_14 = image.load("images/circle.png")

main_font = font.Font("Fink Heavy.ttf", 32)  # Loading the Animal Crossing Font

size_heading = main_font.render("Size", True, BLACK)  # The size buttons and menu
add_size = main_font.render("+", True, BLACK)
sub_size = main_font.render("-", True, BLACK)

icon = image.load("images/paint.png") # Program Icon and heading
display.set_icon(icon)
display.set_caption("Paint Project")

width, height = 1400, 800
screen = display.set_mode((width, height))

running = True

canvas = Rect(250, 50, 1100, 600)  # Main canvas and frame
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
Tool_10 = Rect(400, 685, 85, 85)
Tool_11 = Rect(485, 685, 85, 85)
Tool_12 = Rect(570, 685, 85, 85)
Tool_13 = Rect(655, 685, 85, 85)
Tool_14 = Rect(740, 685, 85, 85)

size_display = Rect(260, 720, 50, 50)
add_rect = Rect(330, 685, 30, 30)
sub_rect = Rect(330, 725, 30, 30)

user_input = ""

undo = []
redo = []


def save():
    global tool
    tool = -1
    file_name = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=(("PNG", "*.png"), ("All Files", "*.*")))
    if len(file_name) > 0:
        if "." in file_name:
            image.save(screen.subsurface(canvas), file_name)
        else:
            image.save(screen.subsurface(canvas), file_name + ".png")


while running:
    screen.fill(RED)
    draw.rect(screen, WHITE, canvas, 0)
    draw.rect(screen, BLACK, (245, 45, 1110, 610), 10)
    screen.blit(capture, (250, 50))

    for evt in event.get():
        if evt.type == QUIT:
            running = False
        if evt.type == MOUSEBUTTONDOWN:
            oldX, oldY = evt.pos
            if evt.button == 4 and size < 100:
                size += 1
            if evt.button == 5 and size > 1:
                size -= 1
            if add_rect.collidepoint(mx, my) and size < 100:
                size += 1
            if sub_rect.collidepoint(mx, my) and size > 1:
                size -= 1
            if tool == 11 and canvas.collidepoint(mx, my):
                display_input = main_font.render(user_input, True, colour)
                input_box = Rect(mx, my, width - mx, height - my)
                screen.blit(display_input, input_box)

        if evt.type == MOUSEBUTTONUP:
            screen.blit(capture, (250, 50))
            if tool == 1:
                draw.line(screen, colour, (oldX, oldY), (mx, my), size)
            elif tool == 5:
                save()
            capture = screen.subsurface(canvas).copy()
        if evt.type == KEYDOWN:
            if tool == 11:
                if evt.key == K_RETURN:
                    user_input = ""
                if evt.key == K_BACKSPACE:
                    user_input = user_input[:-1]
                else:
                    user_input += evt.unicode
    mx, my = mouse.get_pos()
    mb = mouse.get_pressed(3)

    for i in range(5):
        draw.rect(screen, BLACK, (10, 50 + 85 * i, 85, 85), 2)
        draw.rect(screen, BLACK, (115, 50 + 85 * i, 85, 85), 2)
        draw.rect(screen, BLACK, (400 + 85 * i, 685, 85, 85), 2)

    for i in range(5):
        draw.rect(screen, RED, (11, 51 + 85 * i, 83, 83))
        screen.blit(eval("tool_" + str(i)), (10, 50 + 85 * i))
        draw.rect(screen, RED, (116, 51 + 85 * i, 83, 83))
        screen.blit(eval("tool_" + str(i + 5)), (115, 50 + 85 * i))
        draw.rect(screen, RED, (401 + 85 * i, 686, 83, 83))
        screen.blit(eval("tool_" + str(i + 10)), (400 + 85 * i, 685))

    draw.rect(screen, WHITE, sub_rect)
    draw.rect(screen, WHITE, add_rect)
    if sub_rect.collidepoint(mx, my) and size > 1:
        draw.rect(screen, L_BLUE, sub_rect)
    elif sub_rect.collidepoint(mx, my):
        draw.rect(screen, RED, sub_rect)
    elif add_rect.collidepoint(mx, my) and size < 100:
        draw.rect(screen, L_BLUE, add_rect)
    elif add_rect.collidepoint(mx, my):
        draw.rect(screen, RED, add_rect)
    screen.blit(colour_wheel, (10, 485))
    screen.blit(black_white, (15, 685))
    draw.rect(screen, colour, (10, 485, 30, 30))
    screen.blit(size_heading, (250, 685))
    current_size = main_font.render(str(size), True, BLACK)
    screen.blit(current_size, size_display)

    screen.blit(add_size, (339, 686, 30, 30))
    screen.blit(sub_size, (340, 725, 30, 30))

    if mb[0] == 1 and my >= 485:
        if ((mx - 110) ** 2 + (my - 585) ** 2) ** 0.5 <= 90:
            colour = screen.get_at((mx, my))
        elif 215 >= mx >= 15 and 765 >= my >= 685:
            colour = screen.get_at((mx, my))

    if mb[0] == 1 and canvas.collidepoint(mx, my):
        if tool == 0:
            distX = mx - oldX
            distY = my - oldY
            dist = int(((my - oldY) ** 2 + (mx - oldX) ** 2) ** 0.5)
            for i in range(dist):
                dotX = distX * i / dist + oldX
                dotY = distY * i / dist + oldY
                draw.circle(screen, colour, (int(dotX), int(dotY)), size)
            capture = screen.subsurface(canvas).copy()

        elif tool == 1:
            screen.set_clip(canvas)
            screen.blit(capture, canvas)
            draw.line(screen, colour, (mx, my), (oldX, oldY), size)
            screen.set_clip(None)

        elif tool == 2:
            draw.circle(screen, WHITE, (mx, my), size)

        elif tool == 3:
            for i in range(size // 3):
                rand_y = randint(my - size, my + size)
                rand_x = randint(int(mx - (1 * size ** 2 - (my - rand_y) ** 2) ** 0.5),
                                 int(mx + (1 * size ** 2 - (my - rand_y) ** 2) ** 0.5))
                draw.circle(screen, colour, (rand_x, rand_y), 2)

        elif tool == 4:
            draw.line(screen, colour, (mx, my), (oldX, oldY), min(5, size))
        elif tool == 10:
            colour = screen.get_at((mx, my))

    if tool == 6:
        try:
            file_name = filedialog.askopenfilename()
            imported = image.load(file_name)
            screen.blit(imported, (250, 50))
            capture = screen.subsurface(canvas).copy()
            screen.blit(capture, (250, 50))
        except error:
            pass
        tool = -1
        continue

    elif tool == 9:
        draw.rect(screen, WHITE, canvas)

    for i in range(15):
        if eval("Tool_" + str(i)).collidepoint(mx, my):
            draw.rect(screen, L_BLUE, eval("Tool_" + str(i)))
            if i < 5:
                screen.blit(eval("tool_" + str(i)), (10, 50 + 85 * i))
            elif i < 10:
                screen.blit(eval("tool_" + str(i)), (115, 50 + 85 * (i - 5)))
            elif i < 15:
                screen.blit(eval("tool_" + str(i)), (400 + 85 * (i - 10), 685))
            if mb[0] == 1:
                tool = i

    for i in range(15):
        if tool == i:
            draw.rect(screen, L_GREEN, eval("Tool_" + str(i)))
            if tool < 5:
                screen.blit(eval("tool_" + str(i)), (10, 50 + 85 * i))
            elif i < 10:
                screen.blit(eval("tool_" + str(i)), (115, 50 + 85 * (i - 5)))
            elif i < 15:
                screen.blit(eval("tool_" + str(i)), (400 + 85 * (i - 10), 685))
    if canvas.collidepoint(mx, my):
        coordinates = main_font.render("(%d, %d)" % (mx - 250, my - 50), True, BLACK)
    else:
        coordinates = main_font.render("(-1, -1)", True, BLACK)
    screen.blit(coordinates, (1200, 0))

    if tool != 1:
        oldX, oldY = mx, my

    if tool != 1:
        capture = screen.subsurface(canvas).copy()

    if 0 <= tool < 5 and canvas.collidepoint(mx, my):
        try:
            mouse.set_visible(False)
            cursor_image = transform.scale(eval("tool_" + str(tool)), (16, 16))
            screen.blit(cursor_image, (mx - 8, my - 8, 16, 16))
        except NameError:
            # This code shouldn't reach the except, because the NameError was caused by the tool being -1
            mouse.set_visible(True)
            print("NameError")
    else:
        mouse.set_visible(True)

    display.flip()
    c.tick(144)
quit()
