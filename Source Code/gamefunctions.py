import pygame
import sys
import os
pygame.init()


### Create Basic Colour Variables ###
black = (0, 0, 0)
white = (255, 255, 255)
red = (195, 0, 0)
blue = (58, 151, 255)
green = (0, 202, 20)
orange = (255, 162, 0)
yellow = (255, 230, 0)
purple = (173, 0, 216)
background = (230, 230, 230)
buttonnormal = (165, 165, 165)
btn_hover = (200, 200, 200)
scrollcol = (250, 236, 199)
scrollhigh = (248, 221, 157)

### Needed to load game ###
# titleimg = pygame.image.load("/Users/luke/Documents/Education/UEA/Masters /Application Programming/Assignment 2/Practise/Get_Online_v2/Images/title.png")
titleimg2 = pygame.image.load("images/titlecover.png")


display_width = 800
display_height = 600
pygame.display.set_caption("Get Online v2")
screen = pygame.display.set_mode((display_width, display_height))

vsmallText = pygame.font.Font('font/gamefont.ttf', 25)
smallText = pygame.font.Font('font/gamefont.ttf', 30)
smText = pygame.font.Font('font/gamefont.ttf', 40)
mediumText = pygame.font.Font('font/gamefont.ttf', 50)
largeText = pygame.font.Font('font/gamefont.ttf', 70)

diag1 = pygame.font.Font("font/Sansation.ttf", 20)
diag2 = pygame.font.Font("font/AUBREY.ttf", 20)
diag3 = pygame.font.Font("font/dream.ttf", 20)
diag4 = pygame.font.Font("font/fontastique.ttf", 22)


exitgame = False

sound = True

clock = pygame.time.Clock()
# Option to toggle sound effect


def button_click_sound():
    global sound
    sound = True
    pygame.mixer_music.set_volume(1)
    pygame.mixer.music.load("noise/click2.mp3")
    pygame.mixer.music.play()


def button_click_sound_off():
    global sound
    sound = False
    pygame.mixer.music.set_volume(0)

# Function to call "exit game"


def yesexit():
    pygame.quit()
    quit()


def noexit():
    global exitgame
    exitgame = False


def exit_game():
    global exitgame
    exitgame = True
    start_button = button(buttonnormal, 240, 380, 150, 50, "Yes")
    quit_button = button(buttonnormal, 420, 380, 150, 50, "No")
    while exitgame:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                exit_game()
        screen.fill(background)
        header_text("Quit")
        title_text('Are you sure you want to exit')

        draw_button(start_button, black, btn_hover,
                    buttonnormal, event_list, yesexit)
        draw_button(quit_button, black, btn_hover,
                    buttonnormal, event_list, noexit)

        pygame.display.update()
        clock.tick(60)

# Import image to title screen


def titleimage():
    screen.blit(titleimg, (150, 230))


def titleimage2():
    screen.blit(titleimg2, ((display_width/2-349), display_height/2-186))

# Render font to the display (works whereever)


def text_objects(text, font):
    global vsmallText, smallText, smText, mediumText, largeText, diag4
    textDisplay = font.render(text, True, black)
    return textDisplay, textDisplay.get_rect()

# Renders the size of the text from previous statement


def title_text(text):
    global vsmallText, smallText, smText, mediumText, largeText, diag4
    TextSurf, TextRect = text_objects(text, smallText)
    TextRect.center = ((display_width/2), (200))
    screen.blit(TextSurf, TextRect)

# Renders a different size of text from the above statements


def header_text(text):
    global vsmallText, smallText, smText, mediumText, largeText, diag4
    TextSurf, TextRect = text_objects(text, mediumText)
    TextRect.center = ((display_width/2), (150))
    screen.blit(TextSurf, TextRect)

# Allows me to create text anywhere on the screen


def createwords(text, font, x, y):
    global vsmallText, smallText, smText, mediumText, largeText, diag4
    TextSurf, TextRect = text_objects(text, font)
    TextRect.center = ((x), (y))
    screen.blit(TextSurf, TextRect)

# Button Class to determine the button behaviour; text, colour, outline colour, size, location and the font


class button():
    global font

    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, screen, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(screen, outline, (self.x-2,
                                               self.y-2, self.width+4, self.height+4), 0)
        pygame.draw.rect(screen, self.color,
                         (self.x, self.y, self.width, self.height), 0)
        if self.text != '':
            font = smallText
            text = font.render(self.text, True, black)
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2),
                               self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        # self.x + self.width > pos[0] > self.x and self.y + self.height > pos[1] > self.y:
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.x + self.width > pos[0] > self.x and self.y + self.height > pos[1] > self.y:
            return True
        else:
            return False


# Uses the above button class to create a function so buttons can be created elsewhere with ease without reusing code
def draw_button(button, outline, active, inactive, event_list, action=None):
    button.draw(screen, outline)
    for event in event_list:
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.isOver(pos):
                if sound == True:
                    button_click_sound()
                else:
                    button_click_sound_off()
                action()

        if event.type == pygame.MOUSEMOTION:
            if button.isOver(pos):
                button.color = active
            else:
                button.color = inactive


def resetgame():
    os.remove("saves/charinfo.pickle")
    os.remove("saves/charname.pickle")
    os.remove("saves/charloc.pickle")
    pygame.quit()
    quit()


def transition():
    fade = pygame.Surface((display_width, display_height))
    fade.fill(black)
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        screen.blit(fade, (0, 0))
        pygame.time.delay(5)


def information2(one, two):
    createwords(one, diag4, (display_width/2-20), 140)
    createwords(two, diag4, (display_width/2-20), 170)


def information3(one, two, three):
    createwords(one, diag4, (display_width/2-20), 120)
    createwords(two, diag4, (display_width/2-20), 150)
    createwords(three, diag4, (display_width/2-20), 180)


def information4(one, two, three, four):
    createwords(one, diag4, (display_width/2-20), 100)
    createwords(two, diag4, (display_width/2-20), 130)
    createwords(three, diag4, (display_width/2-20), 160)
    createwords(four, diag4, (display_width/2-20), 190)


def information5(one, two, three, four, five):
    createwords(one, diag4, (display_width/2-20), 80)
    createwords(two, diag4, (display_width/2-20), 110)
    createwords(three, diag4, (display_width/2-20), 140)
    createwords(four, diag4, (display_width/2-20), 170)
    createwords(five, diag4, (display_width/2-20), 200)


def change_font():
    global vsmallText, smallText, smText, mediumText, largeText, font
    vsmallText = pygame.font.Font('font/fontastique.ttf', 25)
    smallText = pygame.font.Font('font/fontastique.ttf', 30)
    smText = pygame.font.Font('font/fontastique.ttf', 40)
    mediumText = pygame.font.Font('font/fontastique.ttf', 50)
    largeText = pygame.font.Font('font/fontastique.ttf', 70)
    font = pygame.font.Font('font/fontastique.ttf', 30)
    button.font = pygame.font.Font('font/fontastique.ttf', 30)
