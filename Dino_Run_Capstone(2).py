# Dino_Run_Capstone(2).py
# Author: Georgios Lazari (G21065613)
# Email: GLazari@uclan.ac.uk
# Description: The Dino_Run_Capstone(2).py program demonstrates the Dino Run game with additional features and original
# graphics.The user can press 'space' for the dino to jump, 'P' or 'p' to pause and unpause and 'R' or 'r' to restart
# the game. There are two kinds obstacles in the game, the cacti and a thunder. Every 100 points the cacti start
# coming at a faster pace to increase difficulty. The thunder starts coming down from the cloud after 400 points to make
# the game harder. If the dino has collision with any of the two then the game is over. A coin appears randomly and if the dino
# collects it then extra points are added to the score. Every 100 points the time of the day changes from sunrise to
# noon, then afternoon, sunset and night. At night stars appear in the sky and a planet moves across the sky. Every time
# you loose you can press 'R' or 'r' to try again.
# Bug: Sometimes the coin appears on the cacti

from tkinter import *
from random import *

# dimensions of window
WIDTH = 800
HEIGHT = 600

# create window
win = Tk()
win.title('Dino_Run_Georgios_Lazari')

# background colour starting from sunrise to noon, then afternoon, sunset, night. Found the colours from this website:
# http://cs111.wellesley.edu/archive/cs111_fall14/public_html/labs/lab12/tkintercolor.html
background_colours = ['light blue', 'khaki1', 'tomato', 'violet red', 'dark blue']
background_change = 0

canvas = Canvas(win, width=WIDTH, height=HEIGHT, background=background_colours[0])
canvas.pack()


# cactus class definition
class Cactus:
    def __init__(self, cactus_x, cactus_y, speed, img):
        self.cactus_x = cactus_x
        self.cactus_y = cactus_y
        self.img = img
        self.speed = speed
        self.window_object = canvas.create_image(cactus_x, cactus_y, image=img)

    # method to change the frame of the cactus object by using as argument a new image
    def change_image(self, new):
        canvas.itemconfig(self.window_object, image=new)

    # method to move the cactus object along the x-axis using the speed variable
    # inspired from Collisions.py in week03, step0306
    def move(self):
        self.cactus_x = self.cactus_x + self.speed

    # method to update the coordinates of the cactus object
    # inspired from Collisions.py in week03, step0306
    def draw(self):
        canvas.coords(self.window_object, self.cactus_x, self.cactus_y)


# Dino class definition
class Dino:
    def __init__(self, dino_x, dino_y, dino_image, jump_y):
        self.dino_x = dino_x
        self.dino_y = dino_y
        self.dino_image = dino_image
        self.jump_y = jump_y
        self.window_object = canvas.create_image(dino_x, dino_y, image=dino_image)

    # method to update the coordinates of the dino object
    def draw_dino(self):
        canvas.coords(self.window_object, self.dino_x, self.dino_y)

    # method to move the dino object for the jump
    def move_dino(self):
        self.dino_y = self.dino_y + self.jump_y
        canvas.coords(self.window_object, self.dino_x, self.dino_y)

    # method to change the frame of the dino object by using a new image as argument
    def change_dino_image(self, new_frame):
        canvas.itemconfig(self.window_object, image=new_frame)


# Sun class definition
class Sun:
    def __init__(self, sun_x, sun_y, sun_image):
        self.sun_x = sun_x
        self.sun_y = sun_y
        self.sun_image = sun_image
        self.window_object = canvas.create_image(sun_x, sun_y, image=sun_image)

    # method to update the coordinates of the sun
    def draw_sun(self):
        canvas.coords(self.window_object, self.sun_x, self.sun_y)

    # method to change the frame of the sun object by using a new image as argument
    def change_sun_image(self, new_image):
        canvas.itemconfig(self.window_object, image=new_image)


# ground class definition
class Ground:
    def __init__(self, ground_x, ground_y, ground_img, ground_speed):
        self.ground_x = ground_x
        self.ground_y = ground_y
        self.ground_image = ground_img
        self.ground_speed = ground_speed
        self.window_object = canvas.create_image(ground_x, ground_y, image=ground_img)

    # method to move the ground object along the x-axis using the ground_speed variable
    def ground_move(self):
        self.ground_x = self.ground_x + self.ground_speed

    # method to update the coordinates of the ground object
    def draw_ground(self):
        canvas.coords(self.window_object, self.ground_x, self.ground_y)


# coin class definition
class Coin:
    def __init__(self, coin_x, coin_y, coin_speed_x, coin_image):
        self.coin_x = coin_x
        self.coin_y = coin_y
        self.coin_speed_x = coin_speed_x
        self.coin_image = coin_image
        self.window_object = canvas.create_image(coin_x, coin_y, image=coin_image)

    # method to move and update the coordinates the coin object alone the x-axis using the coin_speed argument
    def coin_move(self, coin_speed):
        self.coin_x = self.coin_x + coin_speed
        canvas.coords(self.window_object, self.coin_x, self.coin_y)

    # method to update the coordinates of the coin object
    def draw_coin(self):
        canvas.coords(self.window_object, self.coin_x, self.coin_y)


# cloud class definition
class Cloud:
    def __init__(self, cloud_x, cloud_y, cloud_speed, cloud_img):
        self.cloud_x = cloud_x
        self.cloud_y = cloud_y
        self.cloud_img = cloud_img
        self.cloud_speed = cloud_speed
        self.window_object = canvas.create_image(cloud_x, cloud_y, image=cloud_img)

    # method to move the cloud object along the x-axis using the cloud_speed variable
    def cloud_move(self):
        self.cloud_x = self.cloud_x + self.cloud_speed

    # method to update the coordinates of the cloud object
    def draw_cloud(self):
        canvas.coords(self.window_object, self.cloud_x, self.cloud_y)


# text class definition to used for 'PAUSE' and 'GAME OVER'
class Text:
    def __init__(self, text_x, text_y, title_text, text_fill, text_font):
        self.text_x = text_x
        self.text_y = text_y
        self.title_text = title_text
        self.text_fill = text_fill
        self.text_font = text_font
        self.text_object = canvas.create_text(text_x, text_y, text=title_text, fill=text_fill, font=text_font)

    # method to change the text's context and colour
    # inspired from ShowingTextOnCanvas.py in week03, step0303
    def change_text(self, new_text, new_colour):
        canvas.itemconfig(self.text_object, fill=new_colour, text=new_text)


# planet class definition
class Planet:
    def __init__(self, planet_x, planet_y, planet_speed, planet_img):
        self.planet_x = planet_x
        self.planet_y = planet_y
        self.planet_img = planet_img
        self.planet_speed = planet_speed
        self.window_object = canvas.create_image(planet_x, planet_y, image=planet_img)

    # method to move the planet object along the x-axis using the planet_speed variable
    def move_planet(self):
        self.planet_x = self.planet_x + self.planet_speed

    # method to update the coordinates of the planet object
    def draw_planet(self):
        canvas.coords(self.window_object, self.planet_x, self.planet_y)


# thunder class definition
class Thunder:
    def __init__(self, thunder_x, thunder_y, thunder_speed_x, thunder_speed_y, thunder_img):
        self.thunder_x = thunder_x
        self.thunder_y = thunder_y
        self.thunder_speed_x = thunder_speed_x
        self.thunder_speed_y = thunder_speed_y
        self.thunder_img = thunder_img
        self.window_object = canvas.create_image(thunder_x, thunder_y, image=thunder_img)

    # method to move the thunder object along the y-axis using the thunder_speed_y variable
    def move_thunder_y(self):
        self.thunder_y = self.thunder_y + self.thunder_speed_y

    # method to move the thunder object along the x-axis using the thunder_speed_x variable
    def move_thunder_x(self):
        self.thunder_x = self.thunder_x + self.thunder_speed_x

    # method to update the coordinates of the thunder object
    def draw_thunder(self):
        canvas.coords(self.window_object, self.thunder_x, self.thunder_y)


# the below methods to load the images are used from image_viewer.py in week 6, step 0601
# ground image modified through Krita app
ground_image = PhotoImage(file='resources/ground.png')
# creating the ground
ground_object = Ground(WIDTH / 2 + 100, HEIGHT - ground_image.height() / 2 + 2, ground_image, -20)

# cloud image modified through Krita app
clouds_image = PhotoImage(file='resources/cloud.png')
#  creating two cloud objects with different x and y coordinates
# for-loop applied for the different distances and the two objects are added to the clouds list
clouds = []
diff_between_clouds = 0
for i in range(2):
    clouds_object = Cloud(WIDTH / 2 + (diff_between_clouds * 2), HEIGHT - 400 - diff_between_clouds,
                          -5, clouds_image)
    clouds.append(clouds_object)
    diff_between_clouds += 100
cloud_number = 0

# planet image created in the Krita app
planet = PhotoImage(file='resources/planet.png')
# creating the planet
planet_object = Planet(WIDTH + 240, planet.height() / 2, -10, planet)

# number of sun frames
SUN_FRAMES = 4
# sun images modified through Krita app
# the method to load the individual frames was used from interactive_flappy_wings.py in week 6, step 0604
sun_images = [PhotoImage(file='resources/sun%i.png' % i) for i in range(SUN_FRAMES)]
sun_object = Sun(sun_images[0].width() / 2, sun_images[0].height() / 2, sun_images[0])
sun_frames_index = 0

# 4 cactus images representing 1 small cactus alone, 1 big cactus alone, 2 small cactii together and  1 small and one big cactus together.
# the images were created and modified using the Krita app
two_small_cactii = PhotoImage(file='resources/two_small_cactii.png')
big_small_cactii = PhotoImage(file='resources/big-small-cactus.png')
cactus_small_img = PhotoImage(file='resources/cactus-small.png')
cactus_big_img = PhotoImage(file='resources/cactus-big.png')

# distances that the first and second cactus objects appear. The following are used from Lecture slide 34 of Week7-8_Interactive
# Animations_Adding Depth_Parallax Effect .pdf
distance1 = randrange(int(0.75 * WIDTH), int(1.25 * WIDTH), 10)
distance2 = distance1 + randrange(200, WIDTH, 10)
cactii_images_list = [cactus_small_img, cactus_big_img, two_small_cactii, big_small_cactii]
# assign a random index from the cactii_images_list for the image of each cactus object
cactus_obj_1 = Cactus(distance1, HEIGHT - 125, -20, img=choice(cactii_images_list))
cactus_obj_2 = Cactus(distance2, HEIGHT - 125, -20, img=choice(cactii_images_list))

# number of dino frames
FRAME_COUNT = 5
# dino images modified in Krita app
# flame taken from https://www.freepik.com/premium-vector/fire-flame-pixel-art-animation-sprite-frames-8bit_20821166.htm#query=burning%20flame%20pixel&position=35&from_view=search&track=ais
dino_frames = [PhotoImage(file='resources/dino%i.png' % i) for i in range(FRAME_COUNT)]
frame_index = 0
# creating the dino object
dino = Dino(300, HEIGHT - dino_frames[0].height() - 40, dino_frames[0], 0)

# coin image taken from  https://www.freepik.com/free-vector/dollar_2900482.htm#query=coin&position=0&from_view=search&track=sph
# and modified using the Krita app
coin_image = PhotoImage(file='resources/coin1.png')
# creating the coin object setting the x coordinated between the first and second cactus object
coin = Coin(randrange(distance1, distance2, 30), 450, 2, coin_image)

# thunder image created using the Krita app
thunder_image = PhotoImage(file='resources/thunder.png')
# creating the thunder object setting its x and y coordinates according to the second cloud
thunder = Thunder(clouds[1].cloud_x, clouds[1].cloud_y + 30, -5, 10, thunder_image)

# Creating a caption showing the score at the bottom-right corner of the window
# inspired from interactive_flappy_wings.py in step 0604, Week 06-Animations
score_label = Label(win, text="00000000", font=("Arial Bold", 15), bg='white')
canvas.create_window(750, HEIGHT - 20, window=score_label)
# score is set to start from zero
score = 0
# points added to the score every time the update function is called
points = 1


# Function to update the score label so that it uses 8 zeros for the score and if the score goes in hundreds or thousands
# of points the respective amount of zeros are replaced with the points
def update_score_label():
    score_str = "{:08d}".format(score)
    score_label.configure(text=score_str)
    score_label.update()


# instruction message at the bottom-left corner of the window
canvas.create_text(210, 580, text='CO1417 Dino Run | Press Space: To Jump | Q: Quit | P: Pause | R: Restart',
                   font=("Arial Bold", 9), fill='black')

# text primarily set with nothing but its contents change through the game showing the pause message or game over.
pause_game_over = Text(WIDTH / 2, HEIGHT / 2, title_text='', text_font=("Arial Bold", 40), text_fill='')

stars = []
x = 0
y = 0
# nested for-loop to create stars that primarily appear with no colour but when the background changes to night then their
# outline changes to white
for i in range(3):
    x = 0
    y += randint(50, 100)
    for l in range(7):
        x += randint(100, 400)
        star = canvas.create_polygon(
            x + 25, y + 0, x + 33, y + 12, x + 50, y + 15, x + 37, y + 25, x + 40, y + 43,
            x + 25, y + 35, x + 10, y + 43, x + 13, y + 25, x + 0, y + 15, x + 17, y + 12,
            fill='', outline='')
        stars.append(star)

# boolean variable set to determine if the game is paused or not
# used to allow the update function to run
is_pause = False
# boolean variable used to set the game_over phase
game_over = False


# event function for detecting when you press 'P' or 'p' to pause or unpause the game and 'R' or 'r' to restart the game
def on_key_press(event):
    global is_pause, score, background_change, game_over, sun_object, stars
    if event.char == 'P' or event.char == 'p':
        # boolean value changes so that the update function can run or stop
        is_pause = not is_pause
        if is_pause == True:
            # if paused display this message otherwise don't show anything
            pause_game_over.change_text('PAUSE', 'black')
        else:
            pause_game_over.change_text('', '')

    if event.char == 'R' or event.char == 'r':
        # remove any message displayed if game over or paused and set every object to their starting position
        pause_game_over.change_text('', '')
        cactus_obj_1.cactus_x = distance1
        cactus_obj_2.cactus_x = distance2
        # cacti start with their original speed
        cactus_obj_1.speed = -20
        cactus_obj_2.speed = -20
        thunder.thunder_y = clouds[1].cloud_y + 30
        thunder.thunder_x = clouds[1].cloud_x
        thunder.draw_thunder()
        sun_object.sun_x = sun_images[0].width() / 2
        sun_object.draw_sun()
        # score goes to zero again
        score -= score
        # background image changes to the morning image
        background_change = 0
        canvas.config(background=background_colours[background_change])
        # the stars' outline becomes invisible again
        for i in range(len(stars)):
            canvas.itemconfig(stars[i], outline='')
        # boolean variables for pause and game over become false so that the game can run again
        is_pause = False
        game_over = False
    # quit the game
    if event.char == 'Q' or event.char == 'q':
        quit()


# Delay for update function
DELAY = 100  # 100 ms = 0.1 sec
# change is a variable used to control the change of frames for the dino and the sun
dino_sun_frames_change = 0

# the following are copied from slide 7 of  Week7-8_Interactive Animations_Adding Depth_Parallax Effect .pdf
in_a_jump = False  # this boolean values tells us when already in a jump as to not start another one
# below are the movements of a jump over time
jump_offsets = [0, -80, -55, -20, 0, 20, 45, 70, 20]
# the jump index is used to keep track of the phase of the jump, it completes after len(jump_offsets) steps
jump_index = 0

# boolean variable to check if the animation for changing the frames of the sun and the dino should continue
animation_control = False
thunder_control = 0


# the idea of the update function is to update the animation periodically
# inspired from interactive_flappy_wings.py step 0604, Week06-Animations
# this function is used for the cactus movement, the dino jump, the coin movement, the background colour change, the clouds' movement, the sun movement,
# the planet movement, the stars' outline colour change, check for collisions and set the game over phase
def update():
    global background_change, jump_offsets, animation_control, stars, cloud_number, planet_object, in_a_jump, game_over, \
        jump_index, score, frame_index, dino_frames, jump_offsets, dino_sun_frames_change, is_pause, sun_frames_index, cactus_obj_1, \
        cactus_obj_2, cactii_images_list, two_small_cactii, points

    # check if it is paused or game_over
    if not is_pause and not game_over:
        # if the x-coordinates of the clouds is less than zero then they are moving otherwise return them to right edge of the window
        # inspired from slide 29 of Week7-8_Interactive Animations_Adding Depth_Parallax Effect .pdf
        for i in range(len(clouds)):
            clouds[i].draw_cloud()
            if clouds[i].cloud_x >= 0:
                clouds[i].cloud_move()
            else:
                clouds[i].cloud_x += WIDTH
                cloud_number += 1
        if cloud_number == 2:
            cloud_number = 0
        # every 200 points make the clouds go faster
        if score % 200 == 0:
            for i in range(len(clouds)):
                clouds[i].cloud_speed = -5
                clouds[i].cloud_move()
                clouds[i].draw_cloud()

        # update the coordinates of the thunder object and also make it move along the y-xis
        thunder.draw_thunder()
        # if the score is less than 400 points then just move the x-coordinates of the thunder, otherwise make it go downwards
        # adding an extra obstacle in the game
        if score <= 400:
            thunder.move_thunder_x()
        else:
            thunder.move_thunder_y()

        # if the x-coordinate of the thunder goes less than 0 update it with the x-coordinate of the second cloud
        if thunder.thunder_x <= 0:
            thunder.thunder_x = clouds[1].cloud_x
            thunder.draw_thunder()
        # if the thunder reaches the bottom of the window make it start from below the cloud again
        if thunder.thunder_y >= WIDTH:
            thunder.thunder_x = clouds[1].cloud_x
            thunder.thunder_y = clouds[1].cloud_y + 30
            thunder.draw_thunder()

        # make the ground move and update its coordinates, if the x coordinate of its center reaches zero then take it to the right most edge of the window again
        ground_object.ground_move()
        ground_object.draw_ground()
        # inspired from slide 29 of Week7-8_Interactive Animations_Adding Depth_Parallax Effect .pdf
        if ground_object.ground_x <= 0:
            ground_object.ground_x = WIDTH + 100  # move the background to the left by changing the X by -20

        # move and update the coordinates of the two cactus objects
        cactus_obj_1.move()  # first obstacle
        cactus_obj_2.move()  # second obstacle
        cactus_obj_1.draw()
        cactus_obj_2.draw()
        # the coin object moves according the first cactus obstacle's speed
        coin.coin_move(cactus_obj_1.speed)
        coin.draw_coin()

        # every time a cactus' x-coordinate reaches -50 then it is set at a random x-coordinate acoording based on the
        # x-coordiante of the other cactus obstacle and change its image to a random one from cactii images list
        # taken from slide 36 of Week7-8_Interactive Animations_Adding Depth_Parallax Effect .pdf
        if cactus_obj_1.cactus_x < -50:
            cactus_obj_1.change_image(choice(cactii_images_list))
            cactus_obj_1.cactus_x = cactus_obj_2.cactus_x + randrange(WIDTH, int(1.25 * WIDTH), 5)

        if cactus_obj_2.cactus_x < -50:
            cactus_obj_2.change_image(choice(cactii_images_list))
            cactus_obj_2.cactus_x = cactus_obj_1.cactus_x + randrange(int(0.3 * WIDTH), int(WIDTH), 10)

        # if a coin's x-coordinate goes below - 50 then it reset to the addition of the two starting distances of the
        # cactii plus the width of the big_small cactus image
        if coin.coin_x < - 50:
            coin.coin_x += (distance1 + distance2) + big_small_cactii.width()

        # the score is updated by adding one point every time the function is called (every 100ms)
        update_score_label()
        score += points
        # every time the score divided by 100 results is 0 then the speeds of the two cacti increase
        if score % 100 == 0:
            cactus_obj_1.speed -= 5
            cactus_obj_2.speed -= 5
        #  every time the score divided by 100 results is 0 the background changes colour going from morning, to noon, afternoon, sunset, night
        if score % 100 == 0:
            background_change += 1
            # for updating the background i used code from adding_obstacles.py step 0704, Week07-Parallax
            if background_change >= len(background_colours):
                background_change = 0
            canvas.config(background=background_colours[background_change])
            # when the fourth background colour appears(dark-blue -> night) make the star outline white so they appear,
            # otherwise make them invisible
            if background_change == 4:
                for i in range(len(stars)):
                    canvas.itemconfig(stars[i], outline='white')
            else:
                for i in range(len(stars)):
                    canvas.itemconfig(stars[i], outline='')

        # every time the score divided by 400 results is 0 the sun object goes out of the window because it is night time
        if score % 400 == 0:
            sun_object.sun_x -= 110
            sun_object.draw_sun()
        # every time the score divided by 500 results is 0, the sun object goes in the window again because it is day time
        if score % 500 == 0:
            sun_object.sun_x += 110
            sun_object.draw_sun()
        # if the sun object is out of the window then the planet moves across the night sky, else it remains outside the
        # left edge of the widnow
        if sun_object.sun_x < 0:
            planet_object.move_planet()
            planet_object.draw_planet()
        else:
            planet_object.planet_x = WIDTH + 240
            planet_object.draw_planet()

        # images of the sun and dino are updated every two times the update function is called
        if not animation_control:
            dino_sun_frames_change += 1
            if dino_sun_frames_change == 2:
                dino.change_dino_image(dino_frames[frame_index])
                sun_object.change_sun_image(sun_images[sun_frames_index])
                dino_sun_frames_change = 0
                sun_frames_index += 1
                frame_index += 1
            # copied from slide 17 Week7-8_Interactive Animations_Adding Depth_Parallax Effect .pdf
            if frame_index == FRAME_COUNT:
                frame_index = 0
            if sun_frames_index == SUN_FRAMES:
                sun_frames_index = 0

        # check collision of coin and dino if there is collision then change the x-coordinate of the coin and increase
        # the score by 20 points
        if coin.coin_x - 22 <= dino.dino_x + 22 and dino.dino_x - 22 <= coin.coin_x + 20:
            if coin.coin_y - 22 <= dino.dino_y:
                coin.coin_x += (distance1 + distance2) + big_small_cactii.width()
                score += 20
                update_score_label()
        # check collision of thunder and dino, if there is collision then the game stops, game over message appears,
        # the dino image changes to the death image
        if dino.dino_x + 22 >= thunder.thunder_x - 10 and dino.dino_x - 22 <= thunder.thunder_x + 10:
            if thunder.thunder_y >= dino.dino_y - 20:
                pause_game_over.change_text('GAME OVER', 'black')
                dino.change_dino_image(dino_frames[4])
                game_over = True
                points = 1
                update_score_label()
        # check collision of dino and first cactus object, apply the same changes as above
        if cactus_obj_1.cactus_x - 20 <= dino.dino_x + 10 and dino.dino_x - 30 <= cactus_obj_1.cactus_x + 20:
            if cactus_obj_1.cactus_y - 30 <= dino.dino_y:
                pause_game_over.change_text('GAME OVER', 'black')
                dino.change_dino_image(dino_frames[4])
                game_over = True
                points = 1
                update_score_label()
        # check collision of dino and second cactus object, apply the same changes as above
        if cactus_obj_2.cactus_x - 20 <= dino.dino_x + 10 and dino.dino_x - 30 <= cactus_obj_2.cactus_x + 20:
            if cactus_obj_2.cactus_y - 30 <= dino.dino_y:
                pause_game_over.change_text('GAME OVER', 'black')
                dino.change_dino_image(dino_frames[4])
                game_over = True
                points = 1
                update_score_label()

        dino.move_dino()
        # firstly set the dino jymping variable to zero
        dino.jump_y = 0
        # 'jump' part of dino copied from slide 9-10 of Week7-8_Interactive Animations_Adding Depth_Parallax Effect .pdf
        if in_a_jump:  # if in a jump, move the character by the number inside the jump_offsets list
            dino.jump_y = jump_offsets[jump_index]  # pick the current offset
            jump_index = jump_index + 1  # prepare for the next phase of the jump
            if jump_index > len(jump_offsets) - 1:  # when the jump ends...
                jump_index = 0  # ...reset the jump_index...
                in_a_jump = False  # ...and set in_a_jump back to False

    win.after(DELAY, update)  # repeat the loop for every DELAY value(100ms)


# copied from slide 8  Week7-8_Interactive Animations_Adding Depth_Parallax Effect .pdf
def jump(__self__):
    global in_a_jump
    if not in_a_jump:  # only process the jump event if no other jump is in progress
        in_a_jump = True


# binding the space bar press to the jump function
win.bind("<space>", jump)
# calling the update function
update()

# binding the event function
win.bind('<KeyPress>', on_key_press)

win.mainloop()
