import pygame
from gamefunctions import *
import time
import pickle
import os

### Initialise Pygame ###
pygame.init()

save = {}
location = {}
charname = {}

def dothesave():
    global save, location, lastlocation, charactername, charname
    gamesavepickle = open('saves/charinfo.pickle', 'wb')
    locsavepickle = open('saves/charloc.pickle', 'wb')
    characternamesave = open('saves/charname.pickle', 'wb')
    save = {gamesave1}
    charname = {charactername}
    location = {lastlocation}
    pickle.dump(save, gamesavepickle)
    pickle.dump(location, locsavepickle)
    pickle.dump(charname, characternamesave)
    gamesavepickle.close()
    locsavepickle.close()
    characternamesave.close()

def dotheload():
    global save, location, lastlocation, charactername, charname
    gamesavepickle = open('saves/charinfo.pickle', 'rb')
    locsavepickle = open('saves/charloc.pickle', 'rb')
    chararacternamesave = open('saves/charname.pickle', 'rb')

    save = pickle.load(gamesavepickle)
    location = pickle.load(locsavepickle)
    charname = pickle.load(chararacternamesave)
    gamesavepickle.close()
    locsavepickle.close()
    chararacternamesave.close()
    changetheme()



# pygame.font.Font("/Users/luke/Documents/Education/UEA/Masters /Application Programming/Assignment 2/Practise/Roboto-Light.ttf", 24")

### Initialise Clock Tick to run ###
clock = pygame.time.Clock()


def resumegame():
    global charactername
    if "Dan" in charname:
        charactername = "Dan"
    elif "Emily" in charname:
        charactername = "Emily"
    elif "Ben" in charname:
        charactername = "Ben"
    elif "Lana" in charname:
        charactername = "Lana"

    changetheme()
    if "Home" in location:
        chapterone1()
    


### Game Variables ### 
gamesave1 = ""
# gamesave2 = ""
# gamesave3 = ""
charactername = ""
characterlist = ['Dan', 'Emily', 'Ben', 'Lana']
health = 0
strength = 0
defence = 0

points = 60
spend = False


fountainluck = 0
gameattempts = 0
currentchapter = ""
inventory = []
notepad = []
weapons = []
wifi_password = "kzhhdliw"

lastlocation = ""


paused = False
viewcharacter = False
options = False
fork = False
wifi = False

def changetheme():
    global buttonnormal, btn_hover
    if charactername == "Dan":
        buttonnormal = (233,109,109)
        btn_hover = (209,139,139)
    elif charactername == "Ben":
        buttonnormal = (111,190,235)
        btn_hover = (127,182,214)
    elif charactername == "Emily":
        buttonnormal = (255, 222, 0)
        btn_hover =  (232, 201, 0)
    elif charactername == "Lana":
        buttonnormal = (225, 149, 234)
        btn_hover = (186, 131, 192)
    else:
        buttonnormal = (165, 165, 165)
        btn_hover    = (200, 200, 200)



def loadinventory():
    global fork, wifi
    if "fork" in inventory:
        fork = True
    if "wifi" in notepad:
        wifi = True
    

def unview():
    global viewcharacter
    viewcharacter = False


def viewchar():
    global viewcharacter, lastlocation
    continuegame = button(buttonnormal, 600, 515, 150, 50, "Continue")
    danimage = pygame.image.load("images/dan300.png")
    emilyimage = pygame.image.load("images/emily300.png")
    benimage = pygame.image.load("images/ben300.png")
    lanaimage = pygame.image.load("images/lana300.png")
    characterbackground = pygame.image.load("images/characterbackground.png")
    characterprint = ""

    while viewcharacter:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                exit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    unview()
        screen.fill(background)
        if charactername == "Dan":
            screen.blit(danimage, (-10, display_height/2-150))
            characterprint = "Dan"
            special = "Charm"
        elif charactername == "Emily":
            screen.blit(emilyimage, (-10, display_height/2-150))
            special = "Knowledge"
            characterprint = "Emily"
        elif charactername == "Ben":
            screen.blit(benimage, (-10, display_height/2-150))
            characterprint = "Ben"
            special = "Strength"
        elif charactername == "Lana":
            screen.blit(lanaimage, (-10, display_height/2-150))
            characterprint = "Lana"
            special = "Telepathy"

        createwords(characterprint, mediumText, (display_width/2-20), 50)
        createwords("Current Location: " + lastlocation, diag4, (display_width/2-20), 100)
        screen.blit(characterbackground, (250, 125))

        draw_button(continuegame, black, btn_hover, buttonnormal, event_list, unview)
        createwords("Current Health: {}".format(health), diag4, 200, 515)
        createwords("Strength: {}".format(strength), diag4, 400, 515)
        createwords("Defence: {}".format(defence), diag4, 200, 560)
        createwords("Special: {}".format(special), diag4, 400, 560)
        if "fork" in inventory:
            createwords("A fork", diag4, 380, 180)
        if "wifi" in notepad:
            createwords("WiFi = " + wifi_password, diag4, 450, 350)
        

        pygame.display.update()
        clock.tick(60)

def unpause():
    global paused
    paused = False


def pausemenu():
    global paused
    continuegame = button(buttonnormal, 240, 410, 320, 50, "Continue")
    quit_button = button(buttonnormal, 240, 320, 320, 50, "Exit")
    mainmenubutton = button(buttonnormal, 240, 250, 320, 50, "Main Menu")
    while paused:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                exit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    unpause()
        screen.fill(background)
        header_text('Game Paused')
        title_text("Press continue to resume")

        draw_button(continuegame, black, btn_hover, buttonnormal, event_list, unpause)
        draw_button(quit_button, black, btn_hover, buttonnormal, event_list, exit_game)
        draw_button(mainmenubutton, black, btn_hover, buttonnormal, event_list, mainmenu)

        pygame.display.update()
        clock.tick(60)





   
# Calls the titlescreen when application first run 
def titlescreen():
    global paused, smallText
    active = True
    start_button = button(buttonnormal, 240, 500, 150, 50, "START")
    quit_button = button(buttonnormal, 420, 500, 150, 50, "quit")
    while active:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = True
                    pausemenu()
        screen.fill(background)
        createwords('Welcome To', smallText, display_width/2, 100)
        titleimage2()

        draw_button(start_button, black, btn_hover, buttonnormal, event_list, mainmenu)
        draw_button(quit_button, black, btn_hover, buttonnormal, event_list, exit_game)

        pygame.display.update()
        clock.tick(60)

# Main menu screen when start is pressed. 
def mainmenu():
    global paused
    active = True
    newgame_button = button(buttonnormal, 240,250, 150, 50, "New game")
    loadgame_button = button(buttonnormal, 410,250, 150, 50, "Resume")
    returnto_button = button(buttonnormal, 240, 430, 320, 50, "return to title screen")
    options_button = button(buttonnormal, 240,320, 320, 50, "options")
    while active:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                exit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = True
                    pausemenu()
        screen.fill(background)
        header_text('Main Menu')

        draw_button(newgame_button, black, btn_hover, buttonnormal, event_list, create_character)
        draw_button(loadgame_button, black, btn_hover, buttonnormal, event_list, resumegame)
        draw_button(returnto_button, black, btn_hover, buttonnormal, event_list, titlescreen)
        draw_button(options_button, black, btn_hover, buttonnormal, event_list, option_menu)

        pygame.display.update()
        clock.tick(60)

# Options Menu
def option_menu():
    global paused
    active = True
    returnto_button = button(buttonnormal, 240, 470, 320, 50, "back")
    soundon_button = button(buttonnormal, 240, 230, 150, 50, "sound on")
    changegamefont = button(buttonnormal, 240, 300, 320, 50, "Change font")
    mutesound_button = button(buttonnormal, 410, 230, 150, 50, "Sound Off")
    resetgame1 = button(buttonnormal, 240, 370, 320, 50, "Delete all save data")
    while active:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                exit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = True
                    pausemenu()
        screen.fill(background)
        header_text("Options")
        paused = True

        draw_button(returnto_button, black, btn_hover, buttonnormal, event_list, mainmenu)
        draw_button(soundon_button, black, btn_hover, buttonnormal, event_list, button_click_sound)
        draw_button(mutesound_button, black, btn_hover, buttonnormal, event_list, button_click_sound_off)
        draw_button(resetgame1, black, btn_hover, buttonnormal, event_list, deletealldata)
        draw_button(changegamefont, black, btn_hover, buttonnormal, event_list, change_font)

        pygame.display.update()
        clock.tick(60)

# First Instance of New Game
def new_game():
    global paused
    active = True
    new_game1 = button(buttonnormal, 240, 230, 320, 50, str("".join(save)))
    # new_game2 = button(buttonnormal, 240, 300, 320, 50, gamesave2)
    # new_game3 = button(buttonnormal, 240, 370, 320, 50, gamesave3)
    returnto_button = button(buttonnormal, 240, 470, 320, 50, "back")
    while active:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                exit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = True
                    pausemenu()
        screen.fill(background)
        header_text("New Game")

        draw_button(new_game1, black, btn_hover, buttonnormal, event_list, create_character)
        # draw_button(new_game2, black, btn_hover, buttonnormal, event_list, create_character)
        # draw_button(new_game3, black, btn_hover, buttonnormal, event_list, create_character)
        draw_button(returnto_button, black, btn_hover, buttonnormal, event_list, mainmenu)

        pygame.display.update()
        clock.tick(60)

            

def create_character():
    global gamesave1, save, paused
    active = True
    player_name = pygame.Rect(240, 250, 320, 50)
    next_step = button(buttonnormal, 240, 320, 320, 50, "next")
    returnto_button = button(buttonnormal, 240, 430, 320, 50, "Main Menu")
    base_font = smText
    color_active = False
    color = buttonnormal
    while active:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                exit_game()
            if gamesave1 == "Slot 1":
                gamesave1 = ""
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_name.collidepoint(event.pos):
                    color_active = True
                else:
                    color_active = False
            if event.type == pygame.KEYDOWN:
                if color_active == True:
                    if event.key == pygame.K_BACKSPACE:
                        gamesave1 = gamesave1[0:-1]
                    elif event.key == pygame.K_RETURN:
                        selectdan()
                    else:
                        gamesave1 += event.unicode
        if color_active:
            color = black
        else:
            color = buttonnormal

        screen.fill(background)
        header_text("Create a Character")
        title_text("What should we call you?")

        text_surface = base_font.render(gamesave1, True, black)
        pygame.draw.rect(screen, color, player_name,2)
        screen.blit(text_surface, (player_name.x + 5, player_name.y +10))
        player_name.w = max(320, text_surface.get_width() + 5)

        draw_button(returnto_button, black, btn_hover, buttonnormal, event_list, mainmenu)
        draw_button(next_step, black, btn_hover, buttonnormal, event_list, selectdan)

        pygame.display.update()
        clock.tick(60)

def selectdan():
    global paused
    dothesave()
    active = True
    returnto_button = button(buttonnormal, 240, 520, 320, 50, "select character")
    left = button(buttonnormal, 20, (display_height/2-20), 40, 40, "<")
    right = button(buttonnormal, 730, (display_height/2-20), 40, 40, ">")
    image = pygame.image.load("images/dan.png")
    while active:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                exit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = True
                    pausemenu()
        screen.fill(background)

        createwords("Select a character", mediumText, (display_width/2), 50)
        draw_button(returnto_button, black, btn_hover, buttonnormal, event_list, danbridge)
        draw_button(left, black, btn_hover, buttonnormal, event_list, selectlana)
        draw_button(right, black, btn_hover, buttonnormal, event_list, selectemily)
        createwords("---- Dan ----", smallText, (display_width/2), 110)
        screen.blit(image, (display_width/2 - 100, 140))

        createwords("A prolific writer from the depths of Kent.", smallText, 400, 380)
        createwords("With his superior knowledge of the English language,", smallText, 400, 410)
        createwords("charming his way out of sticky situations with the art of", smallText, 400, 440)
        createwords("conversation is where Dan and his blue eyes, really shine.", smallText, 400, 470)

        pygame.display.update()
        clock.tick(60)

def selectemily():
    global paused
    active = True
    returnto_button = button(buttonnormal, 240, 520, 320, 50, "select character")
    left = button(buttonnormal, 20, (display_height/2-20), 40, 40, "<")
    right = button(buttonnormal, 730, (display_height/2-20), 40, 40, ">")
    image = pygame.image.load("images/emily.png")
    while active:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                exit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = True
                    pausemenu()
        screen.fill(background)
        
        createwords("Select a character", mediumText, (display_width/2), 50)
        draw_button(returnto_button, black, btn_hover, buttonnormal, event_list, emilybridge)
        draw_button(left, black, btn_hover, buttonnormal, event_list, selectdan)
        draw_button(right, black, btn_hover, buttonnormal, event_list, selectben)
        createwords("---- Emily ----", smallText, (display_width/2), 110)
        screen.blit(image, (display_width/2 - 100, 140))

        createwords("A firey mathmatician, with a burning desire for", smallText, 400, 380)
        createwords("Ben. Reigning pub quiz champion, she knows everything", smallText, 400, 410)
        createwords("about anything. Her brain may be perfect, but her eyes", smallText, 400, 440)
        createwords("certainly aren't. She has the eyesight of an elderly mole.", smallText, 400, 470)

        pygame.display.update()
        clock.tick(60)


def selectben():
    global paused
    active = True
    returnto_button = button(buttonnormal, 240, 520, 320, 50, "select character")
    left = button(buttonnormal, 20, (display_height/2-20), 40, 40, "<")
    right = button(buttonnormal, 730, (display_height/2-20), 40, 40, ">")
    image = pygame.image.load("images/ben.png")
    while active:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                exit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = True
                    pausemenu()
        screen.fill(background)
        
        createwords("Select a character", mediumText, (display_width/2), 50)
        draw_button(returnto_button, black, btn_hover, buttonnormal, event_list, benbridge)
        draw_button(left, black, btn_hover, buttonnormal, event_list, selectemily)
        draw_button(right, black, btn_hover, buttonnormal, event_list, selectlana)
        createwords("---- Ben ----", smallText, (display_width/2), 110)
        screen.blit(image, (display_width/2 - 100, 140))

        createwords("AKA Big Ben. Not to be confused with the London landmark", smallText, 400, 380)
        createwords("Big Ben is 6ft 5 and 15 stone of pure British beef. An", smallText, 400, 410)
        createwords("amateur body builder, he is sure never to lose a battle.", smallText, 400, 440)

        pygame.display.update()
        clock.tick(60)


def selectlana():
    global paused
    active = True
    returnto_button = button(buttonnormal, 240, 520, 320, 50, "select character")
    left = button(buttonnormal, 20, (display_height/2-20), 40, 40, "<")
    right = button(buttonnormal, 730, (display_height/2-20), 40, 40, ">")
    image = pygame.image.load("images/lana.png")
    while active:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                exit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = True
                    pausemenu()
        screen.fill(background)
        
        createwords("Select a character", mediumText, (display_width/2), 50)
        draw_button(returnto_button, black, btn_hover, buttonnormal, event_list, lanabridge)
        draw_button(left, black, btn_hover, buttonnormal, event_list, selectben)
        draw_button(right, black, btn_hover, buttonnormal, event_list, selectdan)
        createwords("---- Lana ----", smallText, (display_width/2), 110)
        screen.blit(image, (display_width/2 - 100, 140))

        createwords("Vegan, pisces, 21. An activist for animal rights.", smallText, 400, 380)
        createwords("Her life long devotion to the lives of our furry", smallText, 400, 410)
        createwords("friends, has lead her to develop animal telepathy.", smallText, 400, 440)
        createwords("A strange but somewhat useful skill.", smallText, 400, 470)

        pygame.display.update()
        clock.tick(60)


def danbridge():
    global charactername
    charactername = "Dan"
    changetheme()
    customisecharacter()
    print(charactername)

def emilybridge():
    global charactername
    charactername = "Emily"
    changetheme()
    customisecharacter()
    print(charactername)

def benbridge():
    global charactername
    charactername = "Ben"
    changetheme()
    customisecharacter()
    print(charactername)

def lanabridge():
    global charactername
    charactername = "Lana"
    changetheme()
    customisecharacter()
    print(charactername)


def customisecharacter():
    global charactername, health, strength, defence, paused, spend
    active = True
    danimage = pygame.image.load("images/dan300.png")
    emilyimage = pygame.image.load("images/emily300.png")
    benimage = pygame.image.load("images/ben300.png")
    lanaimage = pygame.image.load("images/lana300.png")

    back = button(buttonnormal, (display_width/2-75), 500, 150, 50, 'back')
    default = button(buttonnormal, (display_width/2 - 245), 500, 150, 50, 'Default')
    continuegame = button(buttonnormal, (display_width/2 + 95), 500, 150, 50, 'Start >')
    healthup = button(buttonnormal, (display_width/2 + 180), 185, 50, 50, '+')
    strengthup = button(buttonnormal, (display_width/2 + 180), 245, 50, 50, '+')
    defenceup = button(buttonnormal, (display_width/2 + 180), 305, 50, 50, '+')
    healthdown = button(buttonnormal, (display_width/2 + 250), 185, 50, 50, '-')
    strengthdown = button(buttonnormal, (display_width/2 + 250), 245, 50, 50, '-')
    defencedown = button(buttonnormal, (display_width/2 + 250), 305, 50, 50, '-')
    while active:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                exit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = True
                    pausemenu()
    
        
        screen.fill(background)
        
        if charactername == "Dan":
            screen.blit(danimage, (50, display_height/2-150))
            createwords("---- Dan ----", smallText, (display_width/2), 110)
            createwords("Health: {}".format(health), smText, 420, 210)
            createwords("Strength: {}".format(strength), smText, 435, 270)
            createwords("Defence: {}".format(defence), smText, 420, 330)
            createwords("Special: Charm", smText, 440, 390)
            createwords("Points Left: {}".format(points), vsmallText, 620, 450)
        
        elif charactername == "Emily":
            screen.blit(emilyimage, (50, display_height/2-150))
            createwords("---- Emily ----", smallText, (display_width/2), 110)
            createwords("Health: {}".format(health), smText, 420, 210)
            createwords("Strength: {}".format(strength), smText, 435, 270)
            createwords("Defence: {}".format(defence), smText, 420, 330)
            createwords("Special: Knowledge", smText, 480, 390)
            createwords("Points Left: {}".format(points), vsmallText, 620, 450)

        
        elif charactername == "Ben":
            screen.blit(benimage, (50, display_height/2-150))
            createwords("---- Ben ----", smallText, (display_width/2), 110)
            createwords("Health: {}".format(health), smText, 420, 210)
            createwords("Strength: {}".format(strength), smText, 435, 270)
            createwords("Defence: {}".format(defence), smText, 420, 330)
            createwords("Special: Strength", smText, 475, 390)
            createwords("Points Left: {}".format(points), vsmallText, 620, 450)

        
        elif charactername == "Lana":
            screen.blit(lanaimage, (50, display_height/2-150))
            createwords("---- Lana ----", smallText, (display_width/2), 110)
            createwords("Health: {}".format(health), smText, 420, 210)
            createwords("Strength: {}".format(strength), smText, 435, 270)
            createwords("Defence: {}".format(defence), smText, 420, 330)
            createwords("Special: Telepathy", smText, 480, 390)
            createwords("Points Left: {}".format(points), vsmallText, 620, 450)

        
        draw_button(back, black, btn_hover, buttonnormal, event_list, selectdan)
        draw_button(default, black, btn_hover, buttonnormal, event_list, resetstats)
        draw_button(healthup, background, btn_hover, background, event_list, favourhealth)
        draw_button(strengthup, background, btn_hover, background, event_list, favourstrength)
        draw_button(defenceup, background, btn_hover, background, event_list, favourdefence)
        draw_button(healthdown, background, btn_hover, background, event_list, removehealth)
        draw_button(strengthdown, background, btn_hover, background, event_list, removestrength)
        draw_button(defencedown, background, btn_hover, background, event_list, removedefence)
        createwords("Customise character", mediumText, (display_width/2), 50)

        if points == 0:
            draw_button(continuegame, black, btn_hover, buttonnormal, event_list, prologue1)
        else:
            spend = True
            draw_button(continuegame, black, btn_hover, buttonnormal, event_list, spendtherest)
    
        pygame.display.update()
        clock.tick(60)

def spendtherest():
    global spend
    quit_button = button(buttonnormal, 240, 450, 320, 50, "Spend the Rest")
    while spend:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                exit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    unpause()
        screen.fill(background)
        createwords("Wait!", largeText, (display_width/2), 150)
        createwords("You still have", smallText, (display_width/2), 240)
        createwords("{}".format(points), smText, (display_width/2), 300)
        createwords("Points to spend!", smallText, (display_width/2), 360)

        draw_button(quit_button, black, btn_hover, buttonnormal, event_list, resumespending)


        pygame.display.update()
        clock.tick(60)

def resumespending():
    global spend
    spend = False

def resetstats():
    global health, strength, defence, points
    health = 20
    strength = 20
    defence = 20
    points = 0

def favourhealth():
    global health, strength, defence, points
    if points >0:
        health +=1
        points -=1
   

def favourstrength():
    global health, strength, defence, points
    if points >0:
        strength +=1
        points -=1
    

def favourdefence():
    global health, strength, defence, points
    if points >0:
        defence +=1
        points -=1


def removehealth():
    global health, strength, defence, points
    if points <60 >=0 and health >0:
        health -=1
        points +=1


def removestrength():
    global health, strength, defence, points
    if points <60 >=0 and strength >0:
        strength -=1
        points +=1


def removedefence():
    global health, strength, defence, points
    if points <60 >=0 and defence >0:
        defence -=1
        points +=1





def deletealldata():
    global paused
    active = True
    deleteallyes = button(buttonnormal, 240, 280, 320, 50, "yes")
    deleteallno = button(buttonnormal, 240, 350, 320, 50, "no")
    while active:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                exit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = True
                    pausemenu()
        screen.fill(background)
        header_text("delete all save data")
        title_text("This will quit the game")
        draw_button(deleteallyes, black, btn_hover, buttonnormal, event_list, resetgame)
        draw_button(deleteallno, black, btn_hover, buttonnormal, event_list, mainmenu)
        pygame.display.update()
        clock.tick(60)

def preload():
    try:
        if not os.path.exists("saves/charloc.pickle"):
            open("saves/charloc.pickle", "wb").close()
        if not os.path.exists("saves/charinfo.pickle"):
            open("saves/charinfo.pickle", "wb").close()
        if not os.path.exists("saves/charname.pickle"):
            open("saves/charname.pickle", "wb").close()
            titlescreen()
        else:
            dotheload()
            titlescreen()
    except EOFError:
        ## This error happens when trying to load a save file that 'exists' but has no content.
        ## In this case, the program prints the error, deletes the save, and then reloads the game.
        print("Error Loading Game. Restarting...")
        os.remove("saves/charinfo.pickle")
        os.remove("saves/charloc.pickle")
        os.remove("saves/charname.pickle")
        preload()
        
# def transition():
#     fade = pygame.Surface((display_width, display_height))
#     fade.fill(background)
#     for alpha in range (0,300):
#         fade.set_alpha(alpha)
#         screen.blit(fade, (0,0))
#         pygame.display.update()
#         pygame.time.delay(2)

































































### MAIN GAME ###
def prologue1():
    global paused
    active = True
    continue_button = button(buttonnormal, 460, 500, 150, 50, "continue >")
    scroll = pygame.image.load("images/textbackground.png")
    while active:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                exit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = True
                    pausemenu()
        screen.fill(black)
        screen.blit(scroll, (display_width/2-375, 340))
        draw_button(continue_button, scrollcol, scrollhigh, scrollcol, event_list, prologue2)
        createwords("You wake up in your gloomy one bedroom flat in Milton", diag4, (display_width/2-20), 420)
        createwords("Keynes. Clothes are thrown all over the floor and you", diag4, (display_width/2-20), 450)
        createwords("can't help but notice the strong odour of rotten food.", diag4, (display_width/2-20), 480)

        pygame.display.update()
        clock.tick(60)

def prologue2():
    global paused
    active = True
    continue_button = button(buttonnormal, 460, 500, 150, 50, "continue >")
    scroll = pygame.image.load("images/textbackground.png")
    while active:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                exit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = True
                    pausemenu()
        screen.fill(black)
        screen.blit(scroll, (display_width/2-375, 340))
        draw_button(continue_button, scrollcol, scrollhigh, scrollcol, event_list, prologue3)
        createwords("You scan the room with your blurry vision. To your", diag4, (display_width/2-20), 420)
        createwords("East, you have the assortment of old pot noodles,", diag4, (display_width/2-20), 450)
        createwords("the source of the smell.", diag4, (display_width/2-20), 480)

        pygame.display.update()
        clock.tick(60)
def prologue3():
    global paused
    active = True
    continue_button = button(buttonnormal, 460, 500, 150, 50, "continue >")
    scroll = pygame.image.load("images/textbackground.png")
    while active:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                exit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = True
                    pausemenu()
        screen.fill(black)
        screen.blit(scroll, (display_width/2-375, 340))
        draw_button(continue_button, scrollcol, scrollhigh, scrollcol, event_list, chapterone)
        createwords("Your phone is to your left, its screen cracked.", diag4, (display_width/2-20), 420)
        createwords("In front of you, there is a door.", diag4, (display_width/2-20), 450)
        createwords("It looks to be unlocked.", diag4, (display_width/2-20), 480)

        pygame.display.update()
        clock.tick(60)

def chapterone():
    global paused, lastlocation, viewcharacter
    lastlocation = "Home"
    dothesave()
    active = True
    look_button = button(buttonnormal, 50, 490, 150, 50, "Look")
    scroll = pygame.image.load("images/textbackground.png")
    while active:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                exit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = True
                    pausemenu()
                elif event.key == pygame.K_SPACE:
                    viewcharacter = True
                    viewchar()
        screen.fill(background)
        screen.blit(scroll, (display_width/2-375, 10))
        draw_button(look_button, black, btn_hover, buttonnormal, event_list, chapterone1)
        createwords("At any time, press 'p' to pause. ", diag4, (display_width/2-20), 100)
        createwords("Press 'look' to look around. ", diag4, (display_width/2-20), 130)
        createwords("Press 'space' to view current stats about the player. ", diag4, (display_width/2-20), 160)
        
        pygame.display.update()
        clock.tick(60)


def chapterone1():
    global paused, lastlocation, viewcharacter
    lastlocation = "Home"
    active = True
    dothesave()
    look_button = button(buttonnormal, 50, 490, 150, 50, "Look")
    travelnorth = button(buttonnormal, (display_width/2-25), 450, 50, 50, "N")
    travelsouth = button(buttonnormal, (display_width/2-25), 525, 50, 50, "S")
    traveleast = button(buttonnormal, (display_width/2+50), 490, 50, 50, "E")
    travelwest = button(buttonnormal, (display_width/2-100), 490, 50, 50, "W")
    # yes_button = button(buttonnormal, 600, 490, 50, 50, "Y")
    # no_button = button(buttonnormal, 675, 490, 50, 50, "N")

    scroll = pygame.image.load("images/textbackground.png")


    while active:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                exit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = True
                    pausemenu()
                elif event.key == pygame.K_SPACE:
                    viewcharacter = True
                    viewchar()
        screen.fill(background)
        screen.blit(scroll, (display_width/2-375, 10))
        draw_button(look_button, black, btn_hover, buttonnormal, event_list, chapterone1)
        draw_button(travelnorth, black, btn_hover, buttonnormal, event_list, chapteronenorth)
        draw_button(travelsouth, black, btn_hover, buttonnormal, event_list, chapteronesouth)
        draw_button(traveleast, black, btn_hover, buttonnormal, event_list, chapteroneeast)
        draw_button(travelwest, black, btn_hover, buttonnormal, event_list, chapteronewest)
        # draw_button(yes_button, black, btn_hover, buttonnormal, event_list, chapterone1)
        # draw_button(no_button, black, btn_hover, buttonnormal, event_list, chapterone1)

        # createwords("You look around.", diag4, (display_width/2-20), 80)
        # createwords("To your North there is a door.", diag4, (display_width/2-20), 110)
        # createwords("To your East there is the source of the smell.", diag4, (display_width/2-20), 140)
        # createwords("To your South there is your bed.", diag4, (display_width/2-20), 170)
        # createwords("To your West there is your phone.", diag4, (display_width/2-20), 220)
        information5("You look around.", "To the North there is a door.", "To the East there is the source of the smell, old pot noodles.", "To the South is your bed.", "To the West is your phone.")



        pygame.display.update()
        clock.tick(60)


def chapteronenorth():
    global paused, lastlocation, viewcharacter
    lastlocation = "Home"
    active = True
    look_button = button(buttonnormal, 50, 490, 150, 50, "Look")
    travelnorth = button(buttonnormal, (display_width/2-25), 450, 50, 50, "N")
    travelsouth = button(buttonnormal, (display_width/2-25), 525, 50, 50, "S")
    traveleast = button(buttonnormal, (display_width/2+50), 490, 50, 50, "E")
    travelwest = button(buttonnormal, (display_width/2-100), 490, 50, 50, "W")
    yes_button = button(buttonnormal, 600, 490, 50, 50, "Y")
    no_button = button(buttonnormal, 675, 490, 50, 50, "N")
    scroll = pygame.image.load("images/textbackground.png")
    while active:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                exit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = True
                    pausemenu()
                elif event.key == pygame.K_SPACE:
                    viewcharacter = True
                    viewchar()
        screen.fill(background)
        screen.blit(scroll, (display_width/2-375, 10))
        draw_button(look_button, black, btn_hover, buttonnormal, event_list, chapterone1)
        draw_button(travelnorth, black, btn_hover, buttonnormal, event_list, chapteronenorth)
        draw_button(travelsouth, black, btn_hover, buttonnormal, event_list, chapteronesouth)
        draw_button(traveleast, black, btn_hover, buttonnormal, event_list, chapteroneeast)
        draw_button(travelwest, black, btn_hover, buttonnormal, event_list, chapteronewest)
        draw_button(yes_button, black, btn_hover, buttonnormal, event_list, chapterone1)
        draw_button(no_button, black, btn_hover, buttonnormal, event_list, chapterone1)
        if not inventory:
            information4("You walk towards the door.", "It looks to be unlocked.", "There might still be useful items in this room.", "Best not to leave just yet.")
        elif "fork" in inventory: 
            information3("You walk towards the door.", "It looks to be unlocked.", "Do you leave?")
        

        pygame.display.update()
        clock.tick(60)

def chapteroneeast():
    global paused, lastlocation, viewcharacter
    lastlocation = "Home"
    active = True
    look_button = button(buttonnormal, 50, 490, 150, 50, "Look")
    travelnorth = button(buttonnormal, (display_width/2-25), 450, 50, 50, "N")
    travelsouth = button(buttonnormal, (display_width/2-25), 525, 50, 50, "S")
    traveleast = button(buttonnormal, (display_width/2+50), 490, 50, 50, "E")
    travelwest = button(buttonnormal, (display_width/2-100), 490, 50, 50, "W")
    yes_button = button(buttonnormal, 600, 490, 50, 50, "Y")
    no_button = button(buttonnormal, 675, 490, 50, 50, "N")
    scroll = pygame.image.load("images/textbackground.png")
    while active:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                exit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = True
                    pausemenu()
                elif event.key == pygame.K_SPACE:
                    viewcharacter = True
                    viewchar()
        screen.fill(background)
        screen.blit(scroll, (display_width/2-375, 10))
        draw_button(look_button, black, btn_hover, buttonnormal, event_list, chapterone1)
        draw_button(travelnorth, black, btn_hover, buttonnormal, event_list, chapteronenorth)
        draw_button(travelsouth, black, btn_hover, buttonnormal, event_list, chapteronesouth)
        draw_button(traveleast, black, btn_hover, buttonnormal, event_list, chapteroneeast)
        draw_button(travelwest, black, btn_hover, buttonnormal, event_list, chapteronewest)
        draw_button(yes_button, black, btn_hover, buttonnormal, event_list, chapteroneeastyes)
        draw_button(no_button, black, btn_hover, buttonnormal, event_list, chapterone1)
        
        if not inventory:
            information5("You are utterly disgusting. The stench", "is awful and there looks to be fur growing", "in some of the pots. Tucked behind", "one of the pots is a surprisingly clean fork.", "Do you take it?")
        else:
            information3("The noodles are still there. Growing.", "You should sort your life out.", "You have already taken the fork. One should suffice.")

        pygame.display.update()
        clock.tick(60)

def chapteroneeastyes():
    global paused, lastlocation, viewcharacter
    lastlocation = "Home"
    active = True
    look_button = button(buttonnormal, 50, 490, 150, 50, "Look")
    travelnorth = button(buttonnormal, (display_width/2-25), 450, 50, 50, "N")
    travelsouth = button(buttonnormal, (display_width/2-25), 525, 50, 50, "S")
    traveleast = button(buttonnormal, (display_width/2+50), 490, 50, 50, "E")
    travelwest = button(buttonnormal, (display_width/2-100), 490, 50, 50, "W")
    yes_button = button(buttonnormal, 600, 490, 50, 50, "Y")
    no_button = button(buttonnormal, 675, 490, 50, 50, "N")
    scroll = pygame.image.load("images/textbackground.png")
    while active:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                exit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = True
                    pausemenu()
                elif event.key == pygame.K_SPACE:
                    viewcharacter = True
                    viewchar()
        screen.fill(background)
        screen.blit(scroll, (display_width/2-375, 10))
        draw_button(look_button, black, btn_hover, buttonnormal, event_list, chapterone1)
        draw_button(travelnorth, black, btn_hover, buttonnormal, event_list, chapteronenorth)
        draw_button(travelsouth, black, btn_hover, buttonnormal, event_list, chapteronesouth)
        draw_button(traveleast, black, btn_hover, buttonnormal, event_list, chapteroneeast)
        draw_button(travelwest, black, btn_hover, buttonnormal, event_list, chapteronewest)
        draw_button(yes_button, black, btn_hover, buttonnormal, event_list, chapterone1)
        draw_button(no_button, black, btn_hover, buttonnormal, event_list, chapterone1)
        
        information2("A small fork has been added to your", "inventory. Press space to view.")
        inventory.append("fork")
        loadinventory()
        
        

        pygame.display.update()
        clock.tick(60)


def chapteronesouth():
    global paused, lastlocation, viewcharacter
    lastlocation = "Home"
    active = True
    look_button = button(buttonnormal, 50, 490, 150, 50, "Look")
    travelnorth = button(buttonnormal, (display_width/2-25), 450, 50, 50, "N")
    travelsouth = button(buttonnormal, (display_width/2-25), 525, 50, 50, "S")
    traveleast = button(buttonnormal, (display_width/2+50), 490, 50, 50, "E")
    travelwest = button(buttonnormal, (display_width/2-100), 490, 50, 50, "W")
    scroll = pygame.image.load("images/textbackground.png")
    while active:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                exit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = True
                    pausemenu()
                elif event.key == pygame.K_SPACE:
                    viewcharacter = True
                    viewchar()
        screen.fill(background)
        screen.blit(scroll, (display_width/2-375, 10))
        draw_button(look_button, black, btn_hover, buttonnormal, event_list, chapterone1)
        draw_button(travelnorth, black, btn_hover, buttonnormal, event_list, chapteronenorth)
        draw_button(travelsouth, black, btn_hover, buttonnormal, event_list, chapteronesouth)
        draw_button(traveleast, black, btn_hover, buttonnormal, event_list, chapteroneeast)
        draw_button(travelwest, black, btn_hover, buttonnormal, event_list, chapteronewest)
        
        information2("You look back at your bed.", "It looks slept in. Nothing more to see there.")
        

        pygame.display.update()
        clock.tick(60)

def chapteronewest():
    global paused, lastlocation, viewcharacter
    lastlocation = "Home"
    active = True
    look_button = button(buttonnormal, 50, 490, 150, 50, "Look")
    travelnorth = button(buttonnormal, (display_width/2-25), 450, 50, 50, "N")
    travelsouth = button(buttonnormal, (display_width/2-25), 525, 50, 50, "S")
    traveleast = button(buttonnormal, (display_width/2+50), 490, 50, 50, "E")
    travelwest = button(buttonnormal, (display_width/2-100), 490, 50, 50, "W")
    continue_button = button(buttonnormal, 460, 175, 150, 50, "continue >")

    scroll = pygame.image.load("images/textbackground.png")
    while active:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                exit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = True
                    pausemenu()
                elif event.key == pygame.K_SPACE:
                    viewcharacter = True
                    viewchar()
        screen.fill(background)
        screen.blit(scroll, (display_width/2-375, 10))
        draw_button(look_button, black, btn_hover, buttonnormal, event_list, chapterone1)
        draw_button(travelnorth, black, btn_hover, buttonnormal, event_list, chapteronenorth)
        draw_button(travelsouth, black, btn_hover, buttonnormal, event_list, chapteronesouth)
        draw_button(traveleast, black, btn_hover, buttonnormal, event_list, chapteroneeast)
        draw_button(travelwest, black, btn_hover, buttonnormal, event_list, chapteronewest)
        
        draw_button(continue_button, scrollcol, scrollhigh, scrollcol, event_list, chapteronewest2)


        information4("You glance over at your phone. The cracked screen", "wasn't there before. How did that happen, you wonder.", "No wifi connection either, strange.", "")
        

        pygame.display.update()
        clock.tick(60)

def chapteronewest2():
    global paused, lastlocation, viewcharacter
    lastlocation = "Home"
    active = True
    look_button = button(buttonnormal, 50, 490, 150, 50, "Look")
    travelnorth = button(buttonnormal, (display_width/2-25), 450, 50, 50, "N")
    travelsouth = button(buttonnormal, (display_width/2-25), 525, 50, 50, "S")
    traveleast = button(buttonnormal, (display_width/2+50), 490, 50, 50, "E")
    travelwest = button(buttonnormal, (display_width/2-100), 490, 50, 50, "W")
    continue_button = button(buttonnormal, 460, 175, 150, 50, "continue >")

    scroll = pygame.image.load("images/textbackground.png")
    while active:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                exit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = True
                    pausemenu()
                elif event.key == pygame.K_SPACE:
                    viewcharacter = True
                    viewchar()
        screen.fill(background)
        screen.blit(scroll, (display_width/2-375, 10))
        draw_button(look_button, black, btn_hover, buttonnormal, event_list, chapterone1)
        draw_button(travelnorth, black, btn_hover, buttonnormal, event_list, chapteronenorth)
        draw_button(travelsouth, black, btn_hover, buttonnormal, event_list, chapteronesouth)
        draw_button(traveleast, black, btn_hover, buttonnormal, event_list, chapteroneeast)
        draw_button(travelwest, black, btn_hover, buttonnormal, event_list, chapteronewest)
        
        draw_button(continue_button, scrollcol, scrollhigh, scrollcol, event_list, chapteronewest3)


        information4("There's a text from Uncle Darren, your landlord.", "Why does he call himself that? He isn't even your uncle.", "Regardless, the text reads:", "")
        

        pygame.display.update()
        clock.tick(60)

def chapteronewest3():
    global paused, lastlocation, viewcharacter
    lastlocation = "Home"
    active = True
    look_button = button(buttonnormal, 50, 490, 150, 50, "Look")
    travelnorth = button(buttonnormal, (display_width/2-25), 450, 50, 50, "N")
    travelsouth = button(buttonnormal, (display_width/2-25), 525, 50, 50, "S")
    traveleast = button(buttonnormal, (display_width/2+50), 490, 50, 50, "E")
    travelwest = button(buttonnormal, (display_width/2-100), 490, 50, 50, "W")
    continue_button = button(buttonnormal, 460, 175, 150, 50, "continue >")

    scroll = pygame.image.load("images/textbackground.png")
    while active:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                exit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = True
                    pausemenu()
                elif event.key == pygame.K_SPACE:
                    viewcharacter = True
                    viewchar()
        screen.fill(background)
        screen.blit(scroll, (display_width/2-375, 10))
        draw_button(look_button, black, btn_hover, buttonnormal, event_list, chapterone1)
        draw_button(travelnorth, black, btn_hover, buttonnormal, event_list, chapteronenorth)
        draw_button(travelsouth, black, btn_hover, buttonnormal, event_list, chapteronesouth)
        draw_button(traveleast, black, btn_hover, buttonnormal, event_list, chapteroneeast)
        draw_button(travelwest, black, btn_hover, buttonnormal, event_list, chapteronewest)
        
        draw_button(continue_button, scrollcol, scrollhigh, scrollcol, event_list, chapteronewest4)


        information4("Uncle D:", "If you want to get back on the internet, you have two", "options. Decipher the code, or...", "")

        

        pygame.display.update()
        clock.tick(60)

def chapteronewest4():
    global paused, lastlocation, viewcharacter
    lastlocation = "Home"
    active = True
    look_button = button(buttonnormal, 50, 490, 150, 50, "Look")
    travelnorth = button(buttonnormal, (display_width/2-25), 450, 50, 50, "N")
    travelsouth = button(buttonnormal, (display_width/2-25), 525, 50, 50, "S")
    traveleast = button(buttonnormal, (display_width/2+50), 490, 50, 50, "E")
    travelwest = button(buttonnormal, (display_width/2-100), 490, 50, 50, "W")
    yes_button = button(buttonnormal, 600, 490, 50, 50, "Y")
    no_button = button(buttonnormal, 675, 490, 50, 50, "N")

    scroll = pygame.image.load("images/textbackground.png")
    while active:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                exit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = True
                    pausemenu()
                elif event.key == pygame.K_SPACE:
                    viewcharacter = True
                    viewchar()
        screen.fill(background)
        screen.blit(scroll, (display_width/2-375, 10))
        draw_button(look_button, black, btn_hover, buttonnormal, event_list, chapterone1)
        draw_button(travelnorth, black, btn_hover, buttonnormal, event_list, chapteronenorth)
        draw_button(travelsouth, black, btn_hover, buttonnormal, event_list, chapteronesouth)
        draw_button(traveleast, black, btn_hover, buttonnormal, event_list, chapteroneeast)
        draw_button(travelwest, black, btn_hover, buttonnormal, event_list, chapteronewest)
        draw_button(yes_button, black, btn_hover, buttonnormal, event_list, chapteronewest4yes)
        draw_button(no_button, black, btn_hover, buttonnormal, event_list, chapterone1)
        

        if "wifi" in notepad:
            information4("You have already added this to your notepad.", "Probably best to continue with the mission at hand.", "Find the marsbar or decipher the code.", "Good Luck!")
        else:
            information4("... go to the shop and bring me back a marsbar.", "IM HUNGRY. The code for the wifi is: ", wifi_password + ". ","Do you want to add this to your notepad?")
        

        pygame.display.update()
        clock.tick(60)
def chapteronewest4yes():
    global paused, lastlocation, viewcharacter
    lastlocation = "Home"
    active = True
    look_button = button(buttonnormal, 50, 490, 150, 50, "Look")
    travelnorth = button(buttonnormal, (display_width/2-25), 450, 50, 50, "N")
    travelsouth = button(buttonnormal, (display_width/2-25), 525, 50, 50, "S")
    traveleast = button(buttonnormal, (display_width/2+50), 490, 50, 50, "E")
    travelwest = button(buttonnormal, (display_width/2-100), 490, 50, 50, "W")
    continue_button = button(buttonnormal, 460, 175, 150, 50, "continue >")
    yes_button = button(buttonnormal, 600, 490, 50, 50, "Y")
    no_button = button(buttonnormal, 675, 490, 50, 50, "N")

    scroll = pygame.image.load("images/textbackground.png")
    while active:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                exit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = True
                    pausemenu()
                elif event.key == pygame.K_SPACE:
                    viewcharacter = True
                    viewchar()
        screen.fill(background)
        screen.blit(scroll, (display_width/2-375, 10))
        draw_button(look_button, black, btn_hover, buttonnormal, event_list, chapterone1)
        draw_button(travelnorth, black, btn_hover, buttonnormal, event_list, chapteronenorth)
        draw_button(travelsouth, black, btn_hover, buttonnormal, event_list, chapteronesouth)
        draw_button(traveleast, black, btn_hover, buttonnormal, event_list, chapteroneeast)
        draw_button(travelwest, black, btn_hover, buttonnormal, event_list, chapteronewest)
        draw_button(yes_button, black, btn_hover, buttonnormal, event_list, chapterone1)
        draw_button(no_button, black, btn_hover, buttonnormal, event_list, chapterone1)
        
        draw_button(continue_button, scrollcol, scrollhigh, scrollcol, event_list, chapterone1)

       
        information4("'WiFi = " + wifi_password + "'", "has been added to your notepad.","To view, press 'space'.", "")
        notepad.append("wifi")
        loadinventory()
        

        pygame.display.update()
        clock.tick(60)




















preload()

pygame.quit()
quit()



