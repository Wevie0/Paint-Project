from pygame import *
from random import *
from tkinter import *
from tkinter import filedialog

init()  # Initialization
root = Tk()
root.withdraw()
running = True
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
PINK = (255, 147, 145)

# Setting the default values
canvas = Rect(285, 90, 1030, 530)  # Location of the canvas
draw.rect(screen, WHITE, canvas, 0)
capture = screen.subsurface(canvas).copy()  # Capture is the screen capture of the canvas

colour = BLACK
tool = 0  # Which tool is currently selected
size = 5  # The radius and size of the shapes/brushes
oldX = oldY = 0  # The current location of the mouse
user_input = ""  # User keyboard text
vertices = []  # The locations of each vertex of a custom polygon

undo = [screen.subsurface(canvas).copy()]  # The undo queue, i.e. all the previous states of the canvas
pointer = 0  # The 'pointer', indicating what index of the undo list is wanted

draw_rect = Rect(0, 0, 0, 0)  # Rect objects for the rectangles and stamps

slide = 0
c = time.Clock()

# Loading images, the convert_alpha method makes the images less resource intensive
back = image.load("images/background0.jpeg").convert_alpha(screen)  # Background
colour_wheel = image.load("images/wheel.png").convert_alpha(screen)  # Colour Selection
black_white = image.load("images/blackwhite.jpg").convert_alpha(screen)
frame = image.load("images/frame.png").convert_alpha(screen)  # Border canvas frame

logo = image.load("images/logo.png").convert_alpha(screen)
tool_0 = image.load("images/brush.png").convert_alpha(screen)  # Brush
tool_1 = image.load("images/line.png").convert_alpha(screen)  # Line
tool_2 = image.load("images/eraser.png").convert_alpha(screen)  # Eraser
tool_3 = image.load("images/spray-paint.png").convert_alpha(screen)  # Spray
tool_4 = image.load("images/pencil.png").convert_alpha(screen)  # Pencil
tool_5 = image.load("images/save.png").convert_alpha(screen)  # Save
tool_6 = image.load("images/load.png").convert_alpha(screen)  # Load
tool_7 = image.load("images/undo.png").convert_alpha(screen)  # Undo
tool_8 = image.load("images/redo.png").convert_alpha(screen)  # Redo
tool_9 = image.load("images/delete.png").convert_alpha(screen)  # Clear Screen

tool_10 = image.load("images/dropper.png").convert_alpha(screen)  # Dropper
tool_11 = image.load("images/text.png").convert_alpha(screen)  # Text
tool_12 = image.load("images/polygon.png").convert_alpha(screen)  # Filled Polygon
tool_13 = image.load("images/rectangle.png").convert_alpha(screen)  # Unfilled Rectangle
tool_14 = image.load("images/circle.png").convert_alpha(screen)  # Unfilled Ellipse
tool_15 = image.load("images/rectangle_f.png").convert_alpha(screen)  # Filled Rectangle
tool_16 = image.load("images/circle_f.png").convert_alpha(screen)  # Filled Ellipse

tool_17 = image.load("images/apple.png").convert_alpha(screen)  # Apple Stamp
tool_18 = image.load("images/bell_bag.png").convert_alpha(screen)  # Money Stamp
tool_19 = image.load("images/symbol.png").convert_alpha(screen)  # Animal Crossing Leaf Stamp
tool_20 = image.load("images/fossil.png").convert_alpha(screen)  # Fossil Stamp
tool_21 = image.load("images/blathers.png").convert_alpha(screen)  # Blathers (Owl) Stamp
tool_22 = image.load("images/isabelle.png").convert_alpha(screen)  # Isabelle (Yellow Dog) Stamp
tool_23 = image.load("images/kk_slider.png").convert_alpha(screen)  # KK (B&W Dog) Stamp

pause_button = image.load("images/pause.png").convert_alpha(screen)  # Music buttons
play_button = image.load("images/play.png").convert_alpha(screen)
skip_button = image.load("images/skip.png").convert_alpha(screen)

tool_24 = image.load("images/slide.png")  # Switch between stamps and shapes

main_font = font.Font("Fink Heavy.ttf", 32)  # Loading the Animal Crossing Font

size_heading = main_font.render("Size", True, BLACK)  # The size buttons and menu
add_size = main_font.render("+", True, BLACK)
sub_size = main_font.render("-", True, BLACK)

icon = image.load("images/paint.png")  # Program Icon and heading
display.set_icon(icon)
display.set_caption("Paint Project")  # Sets the icon and name

# Rectangle boundary boxes for each tool
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

size_display = Rect(260, 740, 50, 50)  # Rectangles for the manual size changes
add_rect = Rect(330, 685, 30, 30)
sub_rect = Rect(330, 725, 30, 30)

pause_play_rect = Rect(700, 5, 40, 40)  # Song menu
skip_rect = Rect(740, 5, 40, 40)
songs = ["2 AM Snow.mp3", "ACNH Main Theme.mp3", "ACNH Town Hall.mp3", "ACNL Main Theme.mp3",
         "ACNL Town Hall.mp3"]

# SONG_END event from https://nerdparadise.com/programming/pygame/part3, all other music programming was original
SONG_END = USEREVENT + 1  # SONG_END creates an event, so we can access it
mixer.music.set_endevent(SONG_END)
mixer.music.load(songs[0])  # Loads and plays song #1
mixer.music.play()
# Note: needs pygame v2.0.1 to work properly, otherwise can not be unpaused


while running:
    screen.blit(back, (0, 0))  # Refreshing the screen
    draw.rect(screen, WHITE, canvas, 0)  # Drawing the canvas and the user drawings
    screen.blit(capture, canvas)
    screen.blit(logo, (1120, 670))

    mx, my = mouse.get_pos()
    mb = mouse.get_pressed(3)

    for evt in event.get():  # Main event loop
        if evt.type == QUIT:
            running = False

        if evt.type == MOUSEBUTTONDOWN:
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

                if Tool_5.collidepoint(mx, my):  # Saving is selected
                    tool = -1  # Tool "resets" to -1
                    file_name = filedialog.asksaveasfilename(defaultextension=".png",
                                                             filetypes=(("PNG", "*.png"), ("All Files", "*.*")))
                    # File name is the user selected filename, defaults to .png extension
                    if len(file_name) > 0:
                        if "." in file_name:  # If the user already has an extension, it lets the user decide
                            image.save(screen.subsurface(canvas), file_name)
                        else:  # Defaults to .png
                            image.save(screen.subsurface(canvas), file_name + ".png")

                elif Tool_6.collidepoint(mx, my):  # Load custom image
                    try:
                        screen.blit(capture, canvas)
                        file_name = filedialog.askopenfilename()
                        imported = image.load(file_name).convert_alpha(screen)  # Imported is the user selected file
                        screen.blit(imported, (canvas[0], canvas[1]))
                    except error:
                        pass

                elif Tool_7.collidepoint(mx, my):  # Undo is selected
                    if pointer < 0:  # If the pointer is out of bounds, it resets to the closest position
                        pointer = 0
                    elif pointer > len(undo):
                        pointer = len(undo)

                    try:
                        if pointer >= 1:  # Moves the pointer closer to the 0th index (i.e. empty canvas)
                            pointer -= 1
                        screen.blit(undo[pointer], canvas)  # Blits the previous canvas to the screen
                        capture = screen.subsurface(canvas).copy()  # Overwrites the capture
                    except IndexError:  # If out of bounds (-), moves the pointer to a valid index
                        pointer += 1

                elif Tool_8.collidepoint(mx, my):  # Redo is selected
                    if pointer < 0:
                        pointer = 0
                    elif pointer > len(undo):
                        pointer = len(undo)

                    try:
                        pointer += 1  # Moves the pointer closer to the end of the list (more recent)
                        screen.blit(undo[pointer], canvas)
                        capture = screen.subsurface(canvas).copy()
                    except IndexError:  # If out of bounds (+), moves the pointer to a valid index
                        pointer -= 1

                elif Tool_9.collidepoint(mx, my):  # Clear screen is selected
                    draw.rect(screen, WHITE, canvas)  # Draws a blank white canvas and the frame, resets tool to -1
                    screen.blit(frame, (200, 20))
                    tool = -1

                elif tool == 11 and canvas.collidepoint(mx, my):  # User inputted text
                    user_font = font.Font("Fink Heavy.ttf", size)  # Loading the Animal Crossing Font
                    display_input = user_font.render(user_input, True, colour)  # Rendering the input in the colour
                    input_box = Rect(mx, my, width - mx,
                                     height - my)  # A boundary box between the width and height and mouse position
                    screen.blit(display_input, input_box)
                    capture = screen.subsurface(canvas).copy()

                elif tool == 12 and canvas.collidepoint(mx, my):  # Filled polygon is selected
                    vertices.append((mx, my))  # A new vertex is created at (mx, my)
                    if len(vertices) >= 3:  # A polygon has to have 3 or more vertices, then draws the vertices
                        draw.polygon(screen, colour, vertices, 0)

                elif Tool_24.collidepoint(mx, my):  # Slide change is selected
                    if slide == 0:  # 0 -> 1 and 1 -> 0, flips the slide
                        slide = 1
                    elif slide == 1:
                        slide = 0
                    tool = -1

                if pause_play_rect.collidepoint(mx, my):  # Pause/Play is selected
                    if mixer.music.get_busy():  # 1 -> Playing, 0 -> Paused, and this code inverts that
                        # This pause and play feature only works on pygame v2.0.1 because
                        # mixer.music.get_busy() returns 0 if music is paused on this version, where before it was 1
                        mixer.music.pause()
                    else:
                        mixer.music.unpause()

                if skip_rect.collidepoint(mx, my):  # Skip song is selected
                    mixer.music.unload()  # Unloads the current song
                    songs.append(songs[0])  # Moves the current song from the beginning to the end of the list
                    del songs[0]
                    mixer.music.load(songs[0])  # Loads the new song and plays it
                    mixer.music.play()

        if evt.type == MOUSEBUTTONUP:
            if evt.button == 1:
                screen.blit(capture, canvas)  # Updates the canvas

                if tool == 1:  # Line is selected
                    draw.line(screen, colour, (oldX, oldY), (mx, my), size)  # Draws a line from old pos to current pos

                elif tool == 13:  # Unfilled Rect is selected
                    draw_rect = Rect(oldX, oldY, mx - oldX, my - oldY)
                    # Draw rect is a rectangle from when you first pressed the mouse to when you let go
                    draw_rect.normalize()
                    draw.rect(screen, colour, draw_rect, size)  # Draws the rectangle to the screen
                    # 1st and 4th Quadrant on the Cartesian Plane work the same way regarding rectangles
                    # 2nd and 3rd Quadrant also work the same way
                    # 4th Quadrant -> mx > oldX, and my > oldY
                    # 1st Quadrant -> mx > oldX, and my < oldY
                    # 2nd Quadrant -> mx < oldX, and my < oldY
                    # 3rd Quadrant -> mx < oldX, and my > oldY
                    if (mx - oldX) > 0 and (my - oldY) > 0 or (my - oldY) < 0 < (mx - oldX):  # 4th Quadrant or 1st
                        # Draws lines to remove the 4 gaps in the corner of the rectangle, depending on the size and
                        # quadrant, the gaps have a different location
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

                elif tool == 14:  # Unfilled Ellipse is selected
                    if (mx - oldX) > 0 and (my - oldY) > 0:  # 4th Quadrant
                        # This code changes the mx and my, and subtraction to ensure all values are positive
                        # E.g. in the 4th quadrant, mx > oldX, and so all values will be positive
                        draw.ellipse(screen, colour, (oldX, oldY, mx - oldX, my - oldY), size)
                    elif (my - oldY) < 0 < (mx - oldX):  # 1st Quadrant
                        draw.ellipse(screen, colour, (oldX, my, mx - oldX, oldY - my), size)
                    elif (mx - oldX) < 0 and (my - oldY) < 0:  # 2nd Quadrant
                        draw.ellipse(screen, colour, (mx, my, oldX - mx, oldY - my), size)
                    elif (mx - oldX) < 0 < (my - oldY):  # 3rd Quadrant
                        draw.ellipse(screen, colour, (mx, oldY, oldX - mx, my - oldY), size)

                elif tool == 15:  # Filled Rect is selected
                    # Draws the filled rect on the screen
                    draw.rect(screen, colour, draw_rect, 0)

                elif tool == 16:  # Filled Ellipse is selected
                    if (mx - oldX) > 0 and (my - oldY) > 0:  # 4th Quadrant
                        draw.ellipse(screen, colour, (oldX, oldY, mx - oldX, my - oldY), 0)
                    elif (my - oldY) < 0 < (mx - oldX):  # 1st Quadrant
                        draw.ellipse(screen, colour, (oldX, my, mx - oldX, oldY - my), 0)
                    elif (mx - oldX) < 0 and (my - oldY) < 0:  # 2nd Quadrant
                        draw.ellipse(screen, colour, (mx, my, oldX - mx, oldY - my), 0)
                    elif (mx - oldX) < 0 < (my - oldY):  # 3rd Quadrant
                        draw.ellipse(screen, colour, (mx, oldY, oldX - mx, my - oldY), 0)

                elif 17 <= tool <= 23:
                    # For each stamp tool, the current stamp selected is blitted at the specified location
                    screen.blit(current_stamp, stamp_size)

                if tool not in [5, 7, 8] and canvas.collidepoint(mx, my) or tool == 9:
                    # If tool is not save, undo or redo
                    capture = screen.subsurface(canvas).copy()  # Captures the screen
                    # Deletes anything after the pointer, because if you undo and then draw something, the queue
                    # does not keep the different timeline as there is a split, and then appends the current canvas
                    # then shifts the pointer by 1, as something new has been drawn
                    undo = undo[:pointer + 1] + [screen.subsurface(canvas).copy()]
                    pointer += 1

                capture = screen.subsurface(canvas).copy()

        if evt.type == KEYDOWN:  # Keyboard input
            if tool == 11:  # User text tool
                if evt.key == K_RETURN:  # Clears the input if enter is pressed
                    user_input = ""
                elif evt.key == K_BACKSPACE:  # Removes the last letter
                    user_input = user_input[:-1]
                else:  # If it is any other key, adds the unicode of the character to the string
                    user_input += evt.unicode
            elif tool == 12:
                if evt.key == K_RETURN:  # If the filled polygon is selected and enter is pressed, resets the list
                    vertices = []

        if evt.type == SONG_END:  # SONG_END is a custom event, represents the end of a track
            mixer.music.unload()  # Unloads the song, then moves the current song to the end of the list, and plays
            songs.append(songs[0])  # The song formerly at index 1
            del songs[0]
            mixer.music.load(songs[0])
            mixer.music.play()

    draw.rect(screen, WHITE, sub_rect)  # Draws the white add and subtract size buttons
    draw.rect(screen, WHITE, add_rect)

    if sub_rect.collidepoint(mx, my) and size > 1:  # If the size is greater than 1, draws a blue box if hovered
        # or shows a red box, if the size will go out of bounds
        draw.rect(screen, L_BLUE, sub_rect)
    elif sub_rect.collidepoint(mx, my):
        draw.rect(screen, RED, sub_rect)
    elif add_rect.collidepoint(mx, my) and size < 100:
        draw.rect(screen, L_BLUE, add_rect)
    elif add_rect.collidepoint(mx, my):
        draw.rect(screen, RED, add_rect)

    screen.blit(colour_wheel, (10, 485))  # Draws the colour wheels and preview colour panel
    screen.blit(black_white, (15, 685))
    draw.rect(screen, colour, (10, 485, 30, 30))

    screen.blit(size_heading, (250, 700))  # Displays the current size
    current_size = main_font.render(str(size), True, BLACK)
    screen.blit(current_size, size_display)

    screen.blit(add_size, (339, 686, 30, 30))
    screen.blit(sub_size, (340, 725, 30, 30))

    if tool == 11:
        user_font = font.Font("Fink Heavy.ttf", size)  # Loading the Animal Crossing Font
        display_input = user_font.render(user_input, True, colour)  # Rendering the input in the colour
        input_box = Rect(mx, my, width - mx,
                         height - my)  # A boundary box between the width and height and mouse position
        screen.blit(display_input, input_box)

    if mb[0] == 1 and my >= 485:  # If the mouse is pressed over the colour selection tools
        if ((mx - 110) ** 2 + (my - 585) ** 2) ** 0.5 <= 90:  # Colour Wheel,
            # uses pythagorean distance formula for circle
            colour = screen.get_at((mx, my))  # Updates the current colour with the pixel behind the mouse
        elif 215 >= mx >= 15 and 765 >= my >= 685:  # Black and white panel
            colour = screen.get_at((mx, my))
    if mb[0] == 1:
        screen.set_clip(canvas)  # Allows only the canvas to be affected
        if tool == 0 or tool == 2:  # Pencil or eraser
            distX = mx - oldX  # Distance for the x and y planes
            distY = my - oldY
            dist = int(((my - oldY) ** 2 + (mx - oldX) ** 2) ** 0.5)  # Pythagorean distance formula
            for i in range(dist):  # Loops through the distance
                dotX = distX * i / dist + oldX  # Draws a dot
                dotY = distY * i / dist + oldY
                if tool == 0:  # If the brush tool is selected, draws a brush in any colour
                    draw.circle(screen, colour, (int(dotX), int(dotY)), size)
                else:  # If the eraser is selected, draws a brush in white
                    draw.circle(screen, WHITE, (int(dotX), int(dotY)), size)

        elif tool == 1:
            screen.blit(capture, canvas)
            draw.line(screen, colour, (mx, my), (oldX, oldY), size)  # Draws a line to the mouse, but is not saved
            # until release

        elif tool == 3:  # Spray tool
            for i in range(size // 2):  # Size increases the rate at which new dots are drawn
                rand_y = randint(my - size, my + size)  # Random value between the position +- the size
                # rand_x generates a random x value, using the pythagorean distance formula, to avoid creating
                # a square, and takes in the size and y values to not allow a dot which would be in the corner
                # x ** 2 + y ** 2 is the formula for a circle, where x is the size
                rand_x = randint(int(mx - (1 * size ** 2 - (my - rand_y) ** 2) ** 0.5),
                                 int(mx + (1 * size ** 2 - (my - rand_y) ** 2) ** 0.5))
                draw.circle(screen, colour, (rand_x, rand_y), 2)  # Draws a circle at the points

        elif tool == 4:
            draw.line(screen, colour, (mx, my), (oldX, oldY), min(5, size))  # Draws line for the pencil
            # uses the smallest of 5 or the size (1, 2, 3, 4)

        elif tool == 10 and canvas.collidepoint(mx, my):  # Dropper tool takes the current pixel as the colour
            colour = screen.get_at((mx, my))

        elif tool == 13:  # Unfilled Rect, explained above
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

        elif tool == 14:  # Unfilled Ellipse, explained above
            screen.blit(capture, canvas)
            if (mx - oldX) > 0 and (my - oldY) > 0:  # 4th Quadrant
                draw.ellipse(screen, colour, (oldX, oldY, mx - oldX, my - oldY), size)
            elif (my - oldY) < 0 < (mx - oldX):  # 1st Quadrant
                draw.ellipse(screen, colour, (oldX, my, mx - oldX, oldY - my), size)
            elif (mx - oldX) < 0 and (my - oldY) < 0:  # 2nd Quadrant
                draw.ellipse(screen, colour, (mx, my, oldX - mx, oldY - my), size)
            elif (mx - oldX) < 0 < (my - oldY):  # 3rd Quadrant
                draw.ellipse(screen, colour, (mx, oldY, oldX - mx, my - oldY), size)

        elif tool == 15:  # Filled Rect, explained above
            screen.blit(capture, canvas)
            draw_rect = Rect(oldX, oldY, mx - oldX, my - oldY)
            draw_rect.normalize()
            draw.rect(screen, colour, draw_rect, 0)

        elif tool == 16:  # Filled Ellipse, explained above
            screen.blit(capture, canvas)
            if (mx - oldX) > 0 and (my - oldY) > 0:  # 4th Quadrant
                draw.ellipse(screen, colour, (oldX, oldY, mx - oldX, my - oldY), 0)
            elif (my - oldY) < 0 < (mx - oldX):  # 1st Quadrant
                draw.ellipse(screen, colour, (oldX, my, mx - oldX, oldY - my), 0)
            elif (mx - oldX) < 0 and (my - oldY) < 0:  # 2nd Quadrant
                draw.ellipse(screen, colour, (mx, my, oldX - mx, oldY - my), 0)
            elif (mx - oldX) < 0 < (my - oldY):  # 3rd Quadrant
                draw.ellipse(screen, colour, (mx, oldY, oldX - mx, my - oldY), 0)

        elif 17 <= tool <= 23:  # Stamps are selected
            screen.blit(capture, canvas)
            current_stamp = eval("tool_" + str(tool))  # The current stamp image is obtained from the tool number
            stamp_size = Rect(oldX, oldY, mx - oldX, my - oldY)  # Stamp size is a rectangle from the current position
            stamp_size.normalize()
            current_stamp = transform.scale(current_stamp, (stamp_size[2], stamp_size[3]))  # Scales the image
            if (mx - oldX) > 0 and (my - oldY) > 0:  # 4th Quadrant
                # Flips stamps as needed
                screen.blit(current_stamp, stamp_size)
            elif (my - oldY) < 0 < (mx - oldX):  # 1st Quadrant
                current_stamp = transform.flip(current_stamp, False, True)
            elif (mx - oldX) < 0 and (my - oldY) < 0:  # 2nd Quadrant
                current_stamp = transform.flip(current_stamp, True, True)
            elif (mx - oldX) < 0 < (my - oldY):  # 3rd Quadrant
                current_stamp = transform.flip(current_stamp, True, False)
            screen.blit(current_stamp, stamp_size)

        screen.set_clip(None)

    for i in range(5):  # Draws black outline for the tool boxes
        draw.rect(screen, BLACK, (10, 50 + 85 * i, 85, 85), 2)
        draw.rect(screen, BLACK, (115, 50 + 85 * i, 85, 85), 2)
    for i in range(7):
        draw.rect(screen, BLACK, (400 + 85 * i, 685, 85, 85), 2)
    draw.rect(screen, BLACK, Tool_24, 2)

    for i in range(5):  # Draws the pink default rectangles, then the image of the tool
        draw.rect(screen, PINK, (11, 51 + 85 * i, 83, 83))
        screen.blit(eval("tool_" + str(i)), (10, 50 + 85 * i))
        draw.rect(screen, PINK, (116, 51 + 85 * i, 83, 83))
        screen.blit(eval("tool_" + str(i + 5)), (115, 50 + 85 * i))

    for i in range(7):
        draw.rect(screen, PINK, (401 + 85 * i, 686, 83, 83))
        if slide == 0:  # If the slide is set to display the shapes, then draws the shapes (indices 10 to 16)
            screen.blit(eval("tool_" + str(i + 10)), (400 + 85 * i, 685))
        elif slide == 1:  # If the slide is set to display the stamps, then draws the stamps (indices 17 to 23)
            # Transforms the stamp image to an 85 by 85 image, and displays it at the proper location
            # eval("tool_" + str(i+17)) is a way to loop through each image and display it, without 7 lines for each
            screen.blit(transform.scale(eval("tool_" + str(i + 17)), (85, 85)), (400 + 85 * i, 685))

    draw.rect(screen, PINK, (Tool_24[0] + 1, Tool_24[1] + 1, 83, 83))  # Draws the change index button
    screen.blit(tool_24, Tool_24)

    for i in range(25):  # Loops through the tools and does the light blue highlighting for hover
        if slide == 0 and i > 16:  # With the shapes selected, tools 17 to 23 are not needed
            break
        if eval("Tool_" + str(i)).collidepoint(mx, my):  # If there is collision between the mouse and each tool
            draw.rect(screen, L_BLUE, eval("Tool_" + str(i)))  # Light blue highlighting
            if i < 5:  # Draws the right tool at the right location, as the position is fixed
                screen.blit(eval("tool_" + str(i)), (10, 50 + 85 * i))
            elif i < 10:
                screen.blit(eval("tool_" + str(i)), (115, 50 + 85 * (i - 5)))
            elif i < 17 and slide == 0:  # Draws the shapes
                screen.blit(eval("tool_" + str(i)), (400 + 85 * (i - 10), 685))
            elif i < 24 and slide == 1:  # Draws the stamps, but resizes them to be 85 x 85
                screen.blit(transform.scale(eval("tool_" + str(i)), (85, 85)), eval("Tool_" + str(i)))

            if mb[0] == 1:  # If clicked
                tool = i  # The tool changes
                if tool >= 17 and slide == 0:  # Due to the fact that the stamps and shapes are in the same location
                    # The stamp tool overrides the shapes, so if the shape slide is selected, the tool is shifted 7
                    tool -= 7
                vertices = []  # Clears vertices and text
                user_input = ""

    if Tool_24.collidepoint(mx, my):  # Slide shift
        draw.rect(screen, L_BLUE, Tool_24)  # Highlighting
        screen.blit(tool_24, Tool_24)
        if mb[0] == 1:
            vertices = []
            user_input = ""

    for i in range(24):  # Green highlighting if a tool is selected
        if tool == i:
            draw.rect(screen, L_GREEN, eval("Tool_" + str(i)))  # If the tool is currently selected
            if tool < 5:  # Draws the image back on the screen depending on the tool
                screen.blit(eval("tool_" + str(i)), (10, 50 + 85 * i))
            elif i < 10:
                screen.blit(eval("tool_" + str(i)), (115, 50 + 85 * (i - 5)))
            elif i < 17 and slide == 0:
                screen.blit(eval("tool_" + str(i)), (400 + 85 * (i - 10), 685))
            elif i < 24 and slide == 1:
                screen.blit(transform.scale(eval("tool_" + str(i)), (85, 85)), (400 + 85 * (i - 17), 685))

    if canvas.collidepoint(mx, my):  # Mouse is over canvas
        # Displays the adjusted co-ordinates, where the top left corner of the canvas is (0, 0)
        coordinates = main_font.render("(%d, %d)" % (mx - canvas[0], my - canvas[1]), True, BLACK)
    else:
        # Co-ordinates are (-1, -1) to show that the mouse is off the canvas
        coordinates = main_font.render("(-1, -1)", True, BLACK)

    screen.blit(coordinates, (1100, 0))  # Displays the co-ordinates

    # Currently playing strips the .mp3 from the songs, by searching the playing song and only including the
    # characters up to the period
    currently_playing = main_font.render("Playing: " + songs[0][0: songs[0].rfind('.')], True, BLACK)
    # Draws the text and pink rectangle for the music
    screen.blit(currently_playing, (300, 0))
    draw.rect(screen, PINK, pause_play_rect)
    draw.rect(screen, PINK, skip_rect)

    # Black boxes for the pause/play and skip buttons
    draw.rect(screen, BLACK, (700, 5, 40, 40), 2)
    draw.rect(screen, BLACK, (740, 5, 40, 40), 2)

    if pause_play_rect.collidepoint(mx, my):  # Light blue highlighting for the pause/play buttons
        draw.rect(screen, L_BLUE, pause_play_rect)
        if mixer.music.get_busy():  # If the song is playing, display the pause button and vice versa
            screen.blit(pause_button, pause_play_rect)
        else:
            screen.blit(play_button, pause_play_rect)

    if skip_rect.collidepoint(mx, my):  # Display the skip image and highlighting
        draw.rect(screen, L_BLUE, skip_rect)
        screen.blit(skip_button, skip_rect)

    if mixer.music.get_busy():  # If the song is playing, display the pause button and vice versa
        screen.blit(pause_button, pause_play_rect)
    else:
        screen.blit(play_button, pause_play_rect)

    screen.blit(skip_button, skip_rect)

    if tool != 1 and tool != 6 and tool < 13:  # Brush and eraser tools use oldX and oldY differently than
        # the stamps, shapes, and line tools
        oldX, oldY = mx, my

    if tool != 1 and tool != 11 and tool < 13:
        # Captures the screen, but does not for the tools that adjust based on the current mx and my before letting go
        capture = screen.subsurface(canvas).copy()

    if (0 <= tool < 5 or 10 <= tool <= 16) and canvas.collidepoint(mx, my):  # Displays custom cursors
        try:
            mouse.set_visible(False)  # Hides the mouse
            # transforms the tool down to 16 by 16 and displays it at the mouse position
            screen.blit(transform.scale(eval("tool_" + str(tool)), (16, 16)), (mx - 8, my - 8, 16, 16))
        except NameError:
            # NameError was caused by the tool being -1, should not happen
            mouse.set_visible(True)
    else:
        mouse.set_visible(True)

    screen.blit(frame, (200, 20))  # Draws the frame over everything else
    display.flip()
    c.tick(144)
quit()
