from pygame import *
from random import *
from tkinter import *
from tkinter import filedialog
from tkinter.colorchooser import askcolor

init()  # Initialization
root = Tk()
root.withdraw()

width, height = 1400, 800
screen = display.set_mode((width, height))

RED = (255, 0, 0)  # Constant colour RGB values
GREY = (127, 127, 127)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
L_BLUE = (173, 216, 230)
L_GREEN = (157, 255, 176)

back = image.load("images/background0.jpeg").convert_alpha(screen)
colour_wheel = image.load("images/wheel.png").convert_alpha(screen)
black_white = image.load("images/blackwhite.jpg").convert_alpha(screen)
frame = image.load("images/frame.png").convert_alpha(screen)

logo = image.load("images/logo.png").convert_alpha(screen)
tool_0 = image.load("images/brush.png").convert_alpha(screen)
tool_1 = image.load("images/line.png").convert_alpha(screen)
tool_2 = image.load("images/eraser.png").convert_alpha(screen)
tool_3 = image.load("images/spray-paint.png").convert_alpha(screen)
tool_4 = image.load("images/pencil.png").convert_alpha(screen)
tool_5 = image.load("images/save.png").convert_alpha(screen)
tool_6 = image.load("images/load.png").convert_alpha(screen)
tool_7 = image.load("images/undo.png").convert_alpha(screen)
tool_8 = image.load("images/redo.png").convert_alpha(screen)
tool_9 = image.load("images/delete.png").convert_alpha(screen)

tool_10 = image.load("images/dropper.png").convert_alpha(screen)
tool_11 = image.load("images/text.png").convert_alpha(screen)
tool_12 = image.load("images/polygon.png").convert_alpha(screen)
tool_13 = image.load("images/rectangle.png").convert_alpha(screen)
tool_14 = image.load("images/circle.png").convert_alpha(screen)
tool_15 = image.load("images/rectangle_f.png").convert_alpha(screen)
tool_16 = image.load("images/circle_f.png").convert_alpha(screen)

tool_17 = image.load("images/apple.png").convert_alpha(screen)
tool_18 = image.load("images/bell_bag.png").convert_alpha(screen)
tool_19 = image.load("images/symbol.png").convert_alpha(screen)
tool_20 = image.load("images/fossil.png").convert_alpha(screen)
tool_21 = image.load("images/blathers.png").convert_alpha(screen)
tool_22 = image.load("images/isabelle.png").convert_alpha(screen)
tool_23 = image.load("images/kk_slider.png").convert_alpha(screen)

pause_button = image.load("images/pause.png").convert_alpha(screen)
play_button = image.load("images/play.png").convert_alpha(screen)
skip_button = image.load("images/skip.png").convert_alpha(screen)

tool_24 = image.load("images/slide.png")

main_font = font.Font("Fink Heavy.ttf", 32)  # Loading the Animal Crossing Font

size_heading = main_font.render("Size", True, BLACK)  # The size buttons and menu
add_size = main_font.render("+", True, BLACK)
sub_size = main_font.render("-", True, BLACK)

icon = image.load("images/paint.png")  # Program Icon and heading
display.set_icon(icon)
display.set_caption("Paint Project")

running = True

canvas = Rect(285, 90, 1030, 530)  # Main canvas and frame
draw.rect(screen, WHITE, canvas, 0)
capture = screen.subsurface(canvas).copy()

tool = 0  # Setting the default values
colour = BLACK
size = 5
oldX = oldY = 0
mx = my = 0

c = time.Clock()

Tool_0 = Rect(10, 50, 85, 85)  # Rectangle boundary box for each tool
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
Tool_15 = Rect(825, 685, 85, 85)
Tool_16 = Rect(910, 685, 85, 85)

Tool_17 = Rect(400, 685, 85, 85)
Tool_18 = Rect(485, 685, 85, 85)
Tool_19 = Rect(570, 685, 85, 85)
Tool_20 = Rect(655, 685, 85, 85)
Tool_21 = Rect(740, 685, 85, 85)
Tool_22 = Rect(825, 685, 85, 85)
Tool_23 = Rect(910, 685, 85, 85)

Tool_24 = Rect(1010, 685, 85, 85)

size_display = Rect(260, 740, 50, 50)
add_rect = Rect(330, 685, 30, 30)
sub_rect = Rect(330, 725, 30, 30)

pause_play_rect = Rect(700, 5, 40, 40)
skip_rect = Rect(740, 5, 40, 40)

user_input = ""

undo = [screen.subsurface(canvas).copy()]
pointer = 0

points = []

draw_rect = Rect(0, 0, 0, 0)

songs = ["2 AM Snow.mp3", "ACNH Main Theme.mp3", "ACNH Town Hall.mp3", "ACNL Main Theme.mp3",
         "ACNL Town Hall.mp3"]
# SONG_END event from https://nerdparadise.com/programming/pygame/part3, all other music programming was original
SONG_END = USEREVENT + 1
mixer.music.set_endevent(SONG_END)
mixer.music.load(songs[0])
mixer.music.play()

slide = 0

while running:
    screen.blit(back, (0, 0))  # Refreshing the screen
    draw.rect(screen, WHITE, canvas, 0)
    screen.blit(capture, canvas)
    screen.blit(logo, (1120, 670))

    mx, my = mouse.get_pos()
    mb = mouse.get_pressed(3)
    for evt in event.get():  # Main event loop
        if evt.type == QUIT:
            running = False
        if evt.type == MOUSEBUTTONDOWN:
            print(undo, pointer)

            oldX, oldY = evt.pos

            if evt.button == 4 and size < 100:  # Mousewheel to add/decrease size
                size += 1
            if evt.button == 5 and size > 1:
                size -= 1
            if evt.button == 1:

                if add_rect.collidepoint(mx, my) and size < 100:  # Clicking on the buttons to add/decrease size
                    size += 1
                elif sub_rect.collidepoint(mx, my) and size > 1:
                    size -= 1

                if tool == 11 and canvas.collidepoint(mx, my):  # User inputted text
                    user_font = font.Font("Fink Heavy.ttf", size)  # Loading the Animal Crossing Font
                    display_input = user_font.render(user_input, True, colour)  # Rendering the input in the colour
                    input_box = Rect(mx, my, width - mx,
                                     height - my)  # A boundary box between the width and height and pos
                    screen.blit(display_input, input_box)

                if Tool_5.collidepoint(mx, my):
                    tool = -1
                    file_name = filedialog.asksaveasfilename(defaultextension=".png",
                                                             filetypes=(("PNG", "*.png"), ("All Files", "*.*")))
                    if len(file_name) > 0:
                        if "." in file_name:
                            image.save(screen.subsurface(canvas), file_name)
                        else:
                            image.save(screen.subsurface(canvas), file_name + ".png")

                elif Tool_6.collidepoint(mx, my):
                    try:
                        file_name = filedialog.askopenfilename()
                        imported = image.load(file_name)
                        screen.blit(imported, canvas)
                        capture = screen.subsurface(canvas).copy()
                        screen.blit(capture, canvas)
                    except error:
                        pass
                    tool = -1

                elif Tool_7.collidepoint(mx, my):
                    if pointer < 0:
                        pointer = 0
                        print("Error 3", pointer)
                    elif pointer > len(undo):
                        pointer = len(undo)
                    try:
                        if pointer >= 1:
                            pointer -= 1
                        screen.blit(undo[pointer], canvas)
                        capture = screen.subsurface(canvas).copy()
                    except IndexError:
                        print("Error")
                        pointer += 1

                elif Tool_8.collidepoint(mx, my):
                    if pointer < 0:
                        pointer = 0
                        print("Error 3", pointer)
                    elif pointer > len(undo):
                        pointer = len(undo)

                    try:
                        pointer += 1
                        screen.blit(undo[pointer], canvas)
                        capture = screen.subsurface(canvas).copy()
                    except IndexError:
                        print("Error")
                        pointer -= 1

                elif Tool_9.collidepoint(mx, my):
                    pointer += 1
                    draw.rect(screen, WHITE, canvas)
                    screen.blit(frame, (200, 20))
                    tool = -1

                elif tool == 12 and canvas.collidepoint(mx, my):
                    points.append((mx, my))
                    if len(points) >= 3:
                        draw.polygon(screen, colour, points, 0)

                elif tool == 14 and canvas.collidepoint(mx, my):
                    oldX, oldY = mx, my

                elif Tool_24.collidepoint(mx, my):
                    if slide == 0:
                        slide = 1
                    elif slide == 1:
                        slide = 0
                    tool = -1

                if pause_play_rect.collidepoint(mx, my):
                    if mixer.music.get_busy():
                        mixer.music.pause()
                    else:
                        mixer.music.unpause()

                if skip_rect.collidepoint(mx, my):
                    mixer.music.unload()
                    songs.append(songs[0])
                    del songs[0]
                    mixer.music.load(songs[0])
                    mixer.music.play()

        if evt.type == MOUSEBUTTONUP:
            print(undo, pointer)
            if evt.button == 1:


                screen.blit(capture, canvas)

                if tool == 1:
                    draw.line(screen, colour, (oldX, oldY), (mx, my), size)

                elif tool == 13:
                    draw.rect(screen, colour, draw_rect, size)

                    if (mx - oldX) > 0 and (my - oldY) > 0 or (my - oldY) < 0 < (mx - oldX):  # 4th Quadrant or 1st
                        if size % 2 == 1:
                            draw.line(screen, colour, (mx + size // 2 - 1, oldY), (oldX - size // 2, oldY), size)
                            draw.line(screen, colour, (mx + size // 2 - 1, my), (oldX - size // 2, my), size)
                        else:
                            draw.line(screen, colour, (mx + size // 2 - 1, oldY), (oldX - size // 2 + 1, oldY), size)
                            draw.line(screen, colour, (mx + size // 2 - 1, my), (oldX - size // 2 + 1, my), size)

                    elif (mx - oldX) < 0 and (my - oldY) < 0 or (mx - oldX) < 0 < (my - oldY):  # 2nd Quadrant or 3rd
                        if size % 2 == 1:
                            draw.line(screen, colour, (mx - size // 2, oldY), (oldX + size // 2 - 1, oldY), size)
                            draw.line(screen, colour, (mx - size // 2, my), (oldX + size // 2 - 1, my), size)
                        else:
                            draw.line(screen, colour, (mx - size // 2 + 1, oldY), (oldX + size // 2 - 1, oldY), size)
                            draw.line(screen, colour, (mx - size // 2 + 1, my), (oldX + size // 2 - 1, my), size)

                elif tool == 14:
                    if (mx - oldX) > 0 and (my - oldY) > 0:  # 4th Quadrant
                        draw.ellipse(screen, colour, (oldX, oldY, mx - oldX, my - oldY), size)
                    elif (my - oldY) < 0 < (mx - oldX):  # 1st Quadrant
                        draw.ellipse(screen, colour, (oldX, my, mx - oldX, oldY - my), size)
                    elif (mx - oldX) < 0 and (my - oldY) < 0:  # 2nd Quadrant
                        draw.ellipse(screen, colour, (mx, my, oldX - mx, oldY - my), size)
                    elif (mx - oldX) < 0 < (my - oldY):  # 3rd Quadrant
                        draw.ellipse(screen, colour, (mx, oldY, oldX - mx, my - oldY), size)

                elif tool == 15:
                    draw.rect(screen, colour, draw_rect, 0)

                elif tool == 16:
                    if (mx - oldX) > 0 and (my - oldY) > 0:  # 4th Quadrant
                        draw.ellipse(screen, colour, (oldX, oldY, mx - oldX, my - oldY), 0)
                    elif (my - oldY) < 0 < (mx - oldX):  # 1st Quadrant
                        draw.ellipse(screen, colour, (oldX, my, mx - oldX, oldY - my), 0)
                    elif (mx - oldX) < 0 and (my - oldY) < 0:  # 2nd Quadrant
                        draw.ellipse(screen, colour, (mx, my, oldX - mx, oldY - my), 0)
                    elif (mx - oldX) < 0 < (my - oldY):  # 3rd Quadrant
                        draw.ellipse(screen, colour, (mx, oldY, oldX - mx, my - oldY), 0)

                elif 17 <= tool <= 23:
                    screen.blit(current_stamp, stamp_size)

                if tool not in range(5, 9) and canvas.collidepoint(mx, my):
                    capture = screen.subsurface(canvas).copy()
                    undo = undo[:pointer + 1] + [screen.subsurface(canvas).copy()]
                    pointer += 1

                capture = screen.subsurface(canvas).copy()

        if evt.type == KEYDOWN:
            if tool == 11:
                if evt.key == K_RETURN:
                    user_input = ""
                if evt.key == K_BACKSPACE:
                    user_input = user_input[:-1]
                else:
                    user_input += evt.unicode
            elif tool == 12:
                if evt.key == K_RETURN:
                    points = []

        if evt.type == SONG_END:
            mixer.music.unload()
            songs.append(songs[0])
            del songs[0]
            mixer.music.load(songs[0])
            mixer.music.play()

    for i in range(5):
        draw.rect(screen, BLACK, (10, 50 + 85 * i, 85, 85), 2)
        draw.rect(screen, BLACK, (115, 50 + 85 * i, 85, 85), 2)
    for i in range(7):
        draw.rect(screen, BLACK, (400 + 85 * i, 685, 85, 85), 2)
    draw.rect(screen, BLACK, Tool_24, 2)

    for i in range(5):
        draw.rect(screen, RED, (11, 51 + 85 * i, 83, 83))
        screen.blit(eval("tool_" + str(i)), (10, 50 + 85 * i))
        draw.rect(screen, RED, (116, 51 + 85 * i, 83, 83))
        screen.blit(eval("tool_" + str(i + 5)), (115, 50 + 85 * i))

    for i in range(7):
        draw.rect(screen, RED, (401 + 85 * i, 686, 83, 83))
        if slide == 0:
            screen.blit(eval("tool_" + str(i + 10)), (400 + 85 * i, 685))
        elif slide == 1:
            resized_stamp = transform.scale(eval("tool_" + str(i + 17)), (85, 85))
            screen.blit(resized_stamp, (400 + 85 * i, 685))

    draw.rect(screen, RED, (Tool_24[0] + 1, Tool_24[1] + 1, 83, 83))
    screen.blit(tool_24, Tool_24)

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
    screen.blit(size_heading, (250, 700))
    current_size = main_font.render(str(size), True, BLACK)
    screen.blit(current_size, size_display)

    screen.blit(add_size, (339, 686, 30, 30))
    screen.blit(sub_size, (340, 725, 30, 30))

    if mb[0] == 1 and my >= 485:
        if ((mx - 110) ** 2 + (my - 585) ** 2) ** 0.5 <= 90:
            colour = screen.get_at((mx, my))
        elif 215 >= mx >= 15 and 765 >= my >= 685:
            colour = screen.get_at((mx, my))

    if mb[0] == 1:
        screen.set_clip(canvas)
        if tool == 0 or tool == 2:
            distX = mx - oldX
            distY = my - oldY
            dist = int(((my - oldY) ** 2 + (mx - oldX) ** 2) ** 0.5)
            for i in range(dist):
                dotX = distX * i / dist + oldX
                dotY = distY * i / dist + oldY
                if tool == 0:
                    draw.circle(screen, colour, (int(dotX), int(dotY)), size)
                else:
                    draw.circle(screen, WHITE, (int(dotX), int(dotY)), size)

        elif tool == 1:
            screen.blit(capture, canvas)
            draw.line(screen, colour, (mx, my), (oldX, oldY), size)

        elif tool == 3:
            for i in range(size // 3):
                rand_y = randint(my - size, my + size)
                rand_x = randint(int(mx - (1 * size ** 2 - (my - rand_y) ** 2) ** 0.5),
                                 int(mx + (1 * size ** 2 - (my - rand_y) ** 2) ** 0.5))
                draw.circle(screen, colour, (rand_x, rand_y), 2)

        elif tool == 4:
            draw.line(screen, colour, (mx, my), (oldX, oldY), min(5, size))

        elif tool == 10 and canvas.collidepoint(mx, my):
            colour = screen.get_at((mx, my))

        elif tool == 13:
            screen.blit(capture, canvas)
            draw_rect = Rect(oldX, oldY, mx - oldX, my - oldY)
            draw_rect.normalize()
            draw.rect(screen, colour, draw_rect, size)
            if (mx - oldX) > 0 and (my - oldY) > 0 or (my - oldY) < 0 < (mx - oldX):  # 4th Quadrant or 1st
                if size % 2 == 1:
                    draw.line(screen, colour, (mx + size // 2 - 1, oldY), (oldX - size // 2, oldY), size)
                    draw.line(screen, colour, (mx + size // 2 - 1, my), (oldX - size // 2, my), size)
                else:
                    draw.line(screen, colour, (mx + size // 2 - 1, oldY), (oldX - size // 2 + 1, oldY), size)
                    draw.line(screen, colour, (mx + size // 2 - 1, my), (oldX - size // 2 + 1, my), size)

            elif (mx - oldX) < 0 and (my - oldY) < 0 or (mx - oldX) < 0 < (my - oldY):  # 2nd Quadrant or 3rd
                if size % 2 == 1:
                    draw.line(screen, colour, (mx - size // 2, oldY), (oldX + size // 2 - 1, oldY), size)
                    draw.line(screen, colour, (mx - size // 2, my), (oldX + size // 2 - 1, my), size)
                else:
                    draw.line(screen, colour, (mx - size // 2 + 1, oldY), (oldX + size // 2 - 1, oldY), size)
                    draw.line(screen, colour, (mx - size // 2 + 1, my), (oldX + size // 2 - 1, my), size)

        elif tool == 14:
            screen.blit(capture, canvas)
            if (mx - oldX) > 0 and (my - oldY) > 0:  # 4th Quadrant
                draw.ellipse(screen, colour, (oldX, oldY, mx - oldX, my - oldY), size)
            elif (my - oldY) < 0 < (mx - oldX):  # 1st Quadrant
                draw.ellipse(screen, colour, (oldX, my, mx - oldX, oldY - my), size)
            elif (mx - oldX) < 0 and (my - oldY) < 0:  # 2nd Quadrant
                draw.ellipse(screen, colour, (mx, my, oldX - mx, oldY - my), size)
            elif (mx - oldX) < 0 < (my - oldY):  # 3rd Quadrant
                draw.ellipse(screen, colour, (mx, oldY, oldX - mx, my - oldY), size)

        elif tool == 15:
            screen.blit(capture, canvas)
            draw_rect = Rect(oldX, oldY, mx - oldX, my - oldY)
            draw_rect.normalize()
            draw.rect(screen, colour, draw_rect, 0)

        elif tool == 16:
            screen.blit(capture, canvas)
            if (mx - oldX) > 0 and (my - oldY) > 0:  # 4th Quadrant
                draw.ellipse(screen, colour, (oldX, oldY, mx - oldX, my - oldY), 0)
            elif (my - oldY) < 0 < (mx - oldX):  # 1st Quadrant
                draw.ellipse(screen, colour, (oldX, my, mx - oldX, oldY - my), 0)
            elif (mx - oldX) < 0 and (my - oldY) < 0:  # 2nd Quadrant
                draw.ellipse(screen, colour, (mx, my, oldX - mx, oldY - my), 0)
            elif (mx - oldX) < 0 < (my - oldY):  # 3rd Quadrant
                draw.ellipse(screen, colour, (mx, oldY, oldX - mx, my - oldY), 0)

        elif 17 <= tool <= 23:
            screen.blit(capture, canvas)
            current_stamp = eval("tool_" + str(tool))
            stamp_size = Rect(oldX, oldY, mx - oldX, my - oldY)
            stamp_size.normalize()
            current_stamp = transform.scale(current_stamp, (stamp_size[2], stamp_size[3]))
            if (mx - oldX) > 0 and (my - oldY) > 0:  # 4th Quadrant
                screen.blit(current_stamp, stamp_size)
            elif (my - oldY) < 0 < (mx - oldX):  # 1st Quadrant
                current_stamp = transform.flip(current_stamp, False, True)
            elif (mx - oldX) < 0 and (my - oldY) < 0:  # 2nd Quadrant
                current_stamp = transform.flip(current_stamp, True, True)
            elif (mx - oldX) < 0 < (my - oldY):  # 3rd Quadrant
                current_stamp = transform.flip(current_stamp, True, False)
            screen.blit(current_stamp, stamp_size)

        screen.set_clip(None)

    for i in range(25):
        if slide == 0 and i > 16:
            continue
        if eval("Tool_" + str(i)).collidepoint(mx, my):
            draw.rect(screen, L_BLUE, eval("Tool_" + str(i)))
            if i < 5:
                screen.blit(eval("tool_" + str(i)), (10, 50 + 85 * i))
            elif i < 10:
                screen.blit(eval("tool_" + str(i)), (115, 50 + 85 * (i - 5)))
            elif i < 17 and slide == 0:
                screen.blit(eval("tool_" + str(i)), (400 + 85 * (i - 10), 685))
            elif i < 24 and slide == 1:
                resized_stamp = transform.scale(eval("tool_" + str(i)), (85, 85))
                screen.blit(resized_stamp, eval("Tool_" + str(i)))

            if mb[0] == 1:
                tool = i
                if tool >= 17 and slide == 0:
                    tool -= 7
                points = []

    if Tool_24.collidepoint(mx, my):
        draw.rect(screen, L_BLUE, Tool_24)
        screen.blit(tool_24, Tool_24)
        if mb[0] == 1:
            tool = 24
            points = []

    for i in range(24):
        if tool == i:
            draw.rect(screen, L_GREEN, eval("Tool_" + str(i)))
            if tool < 5:
                screen.blit(eval("tool_" + str(i)), (10, 50 + 85 * i))
            elif i < 10:
                screen.blit(eval("tool_" + str(i)), (115, 50 + 85 * (i - 5)))
            elif i < 17 and slide == 0:
                screen.blit(eval("tool_" + str(i)), (400 + 85 * (i - 10), 685))
            elif i < 24 and slide == 1:
                resized_stamp = transform.scale(eval("tool_" + str(i)), (85, 85))
                screen.blit(resized_stamp, (400 + 85 * (i - 17), 685))

    if canvas.collidepoint(mx, my):
        coordinates = main_font.render("(%d, %d)" % (mx - 300, my - 100), True, BLACK)
    else:
        coordinates = main_font.render("(-1, -1)", True, BLACK)

    screen.blit(coordinates, (1100, 0))

    track = songs[0]
    track = track[0: track.rfind('.')]
    currently_playing = main_font.render("Playing: " + track, True, BLACK)
    screen.blit(currently_playing, (300, 0))
    draw.rect(screen, RED, pause_play_rect)
    draw.rect(screen, RED, skip_rect)

    draw.rect(screen, BLACK, (700, 5, 40, 40), 2)
    draw.rect(screen, BLACK, (740, 5, 40, 40), 2)

    if pause_play_rect.collidepoint(mx, my):
        draw.rect(screen, L_BLUE, pause_play_rect)
        if mixer.music.get_busy():
            screen.blit(pause_button, pause_play_rect)
        else:
            screen.blit(play_button, pause_play_rect)

    if skip_rect.collidepoint(mx, my):
        draw.rect(screen, L_BLUE, skip_rect)
        screen.blit(skip_button, skip_rect)

    if mixer.music.get_busy():  # Note: needs pygame v2.0.1 to work properly, otherwise can not be unpaused
        screen.blit(pause_button, pause_play_rect)
    else:
        screen.blit(play_button, pause_play_rect)

    screen.blit(skip_button, skip_rect)

    if tool != 1 and tool < 13:
        oldX, oldY = mx, my

    if tool != 1 and tool < 13:
        capture = screen.subsurface(canvas).copy()

    if (0 <= tool < 5 or 10 <= tool <= 16) and canvas.collidepoint(mx, my):
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

    screen.blit(frame, (200, 20))
    display.flip()
    c.tick(144)
quit()
