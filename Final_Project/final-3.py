import pygame                       #importing required modules
import time
import random
from pygame import mixer

pygame.init()                       #initialize the pygame

yellow=(255,255,0)                  
brown=(101,67,33)
skyblue=(205,230,242)               
golden=(155,135,12)
dred=(178,31,53)
yorange=(255,161,63)
greenc=(0,131,232)
oval=(242,240,161)
teal=(0,128,128)
light_purple=(200,190,255)          #colors to rgb
gray=(119,118,110)
black=(0,0,0)
red=(200,0,0)
green=(0,200,0) 
blue=(0,0,200)
bright_red=(255,0,0)
bright_green=(0,255,0)
bright_blue=(0,0,255)

display_width=1200              #screen dimention
display_height=750                  


#creating the display screen
screen=pygame.display.set_mode((display_width,display_height))
#Caption and Icon
pygame.display.set_caption("Survival Death Valley")
icon=pygame.image.load("car_icon.png")
pygame.display.set_icon(icon)

clock=pygame.time.Clock()

#loading the images
carimg=pygame.image.load('car.png')
backgroundpic=pygame.image.load("grass.jpg")
yellow_strip=pygame.image.load("yellow_strip.jpg")
white_strip=pygame.image.load("white_strip.jpg")
strip=pygame.image.load("strip.jpg")
intro_background=pygame.image.load("ibg2.jpg")
instruction_background=pygame.image.load("ibg1.jpg")
pause_background=pygame.image.load("ibg3.jpg")
crash_background=pygame.image.load("bg4.jpg")
credit_background=pygame.image.load("credits.jpg")

#loading car images
car_pic1=pygame.image.load("car1.png")
car_pic2=pygame.image.load("car2.png")
car_pic3=pygame.image.load("car3.png")

car_pic4=pygame.image.load("car4r.png")
car_pic5=pygame.image.load("car5r.png")
car_pic6=pygame.image.load("car6r.png")


#loading sound/music
intro_sound=pygame.mixer.Sound('kgf_intro.mpeg')
game_sound=pygame.mixer.Sound('game.mpeg')
crash_sound=pygame.mixer.Sound('crash.wav')

car_width=81
pause=False

carimg_list1=[car_pic1,car_pic2,car_pic3]           #creating the car list for storing different car images
carimg_list2=[car_pic4,car_pic5,car_pic6]

def introduction():                   #For Introduction Page

    intro=True    
    intro_sound.play(-1)

    while intro:                                
        for event in pygame.event.get():            #to check if the user has manually quit the game window
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(intro_background,(0,0))         #to draw the intro background on screen

        #to display the game name
        largetext=pygame.font.Font('madjoe.ttf',150)
        TextSurf,TextRect=text_objects("Survival",largetext,yorange)
        TextRect.center=(320,80)
        screen.blit(TextSurf,TextRect)

        TextSurf,TextRect=text_objects("Death",largetext,yorange)
        TextRect.center=(550,195)
        screen.blit(TextSurf,TextRect)

        TextSurf,TextRect=text_objects("Valley",largetext,yorange)
        TextRect.center=(700,310)
        screen.blit(TextSurf,TextRect)
        #to display the buttons on intro screen
        button("START GAME",150,500,200,50,green,bright_green,"play")
        button("INSTRUCTION",400,550,200,50,blue,bright_blue,"intro")
        button("QUIT GAME",650,600,200,50,red,bright_red,"quit")
        button("CREDITS",900,650,200,50,yellow,golden,"developers")
        pygame.display.update()
        
def button(msg,x,y,w,h,ic,ac,action=None,score=None):       #to draw the button on the screen
    
    mouse=pygame.mouse.get_pos()                            #to get the position of the mouse 
    click=pygame.mouse.get_pressed()                        # defining click
 
    if x<mouse[0]<x+w and y<mouse[1]<y+h:                   # if the mouse cursor is on the button
        pygame.draw.rect(screen,ac,(x,y,w,h))
        if click[0]==1 and action!=None:                    # if button is clicked
            if action=="play":
                intro_sound.stop()
                countdown()    
            elif action=="quit":
                crash_sound.stop()
                pygame.quit()
                quit()
            elif action=="intro":
                intro_sound.stop()
                instructions()
            elif action=="menu":
                intro_sound.stop()
                introduction()
            elif action=="pause":
                game_sound.stop()
                pause_game(score)
            elif action=="unpause":
                game_sound.play(-1)
                unpause_game()
            elif action=="developers":
                intro_sound.stop()
                credits()    
    else:
        pygame.draw.rect(screen,ic,(x,y,w,h))
    
    smalltext=pygame.font.Font("batman.ttf",20)                 
    textsurf,textrect=text_objects(msg,smalltext,light_purple)
    textrect.center=((x+(w/2)),(y+(h/2)))
    screen.blit(textsurf,textrect)

def credits():                                   #For the Credit Page which mentions the members of the project
    intro_sound.play(-1)
    credit=True
    while credit:
        for event in pygame.event.get():        #to check if the user has manually quit the game window
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        screen.blit(credit_background,(0,0))      # to draw credit page background on screen
        largetext=pygame.font.Font('valorant.ttf',80)
        smalltext=pygame.font.Font('batman.ttf',30)
        mediumtext=pygame.font.Font('batman.ttf',60)
        TextSurf,TextRect=text_objects("CREDITS",largetext,golden)
        TextRect.center=((600),(50))
        textSurf,textRect=text_objects("Done by",mediumtext,black)
        textRect.center=((600),(140))
        c1textSurf,c1textRect=text_objects("Balaji Babasaheb Sankapal                 IMT2020090",smalltext,oval)
        c1textRect.center=((590),(350))
        c2textSurf,c2textRect=text_objects("Prudhvi Nath Reddy Sagili                 IMT2020082",smalltext,oval)
        c2textRect.center=((590),(250))
        c3textSurf,c3textRect=text_objects("Jainav Sanghvi                            IMT2020098",smalltext,oval)
        c3textRect.center=((590),(550))
        c4textSurf,c4textRect=text_objects("Nandula Satya Prasanna Koushik            IMT2020096",smalltext,oval)
        c4textRect.center=((590),(450))
        screen.blit(textSurf,textRect)                  # displaying the credit page text
        screen.blit(TextSurf,TextRect)
        screen.blit(c1textSurf,c1textRect)                  
        screen.blit(c2textSurf,c2textRect)
        screen.blit(c3textSurf,c3textRect)
        screen.blit(c4textSurf,c4textRect)
        button("BACK",1100,0,100,50,green,bright_green,"menu")      # display the back button
        pygame.display.update()

def instructions():                              #For the Instruction Page
    
    intro_sound.play(-1)
    
    instruction=True
    while instruction:
        for event in pygame.event.get():    #to check if the user has manually quit the game window
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(instruction_background,(0,0))    # to draw instruction page background on screen

        largetext=pygame.font.Font('valorant.ttf',80)
        smalltext=pygame.font.Font('batman.ttf',17)
        mediumtext=pygame.font.Font('valorant.ttf',60)

        pygame.draw.rect(screen,skyblue,(50,100,800,200))
        pygame.draw.rect(screen,brown,(0,480,350,270))

        textSurf,textRect=text_objects("There is only one way to find out the driving skills of Bob. ",smalltext,black)
        textRect.center=((450),(120))
        btextSurf,btextRect=text_objects("Drive through the death vally without colliding with cars ",smalltext,black)
        btextRect.center=((450),(150))
        xtextSurf,xtextRect=text_objects("by staying on the road.",smalltext,black)
        xtextRect.center=((450),(180))
        ytextSurf,ytextRect=text_objects("Your score is based on the number of cars you passed.",smalltext,black)
        ytextRect.center=((450),(230))
        TextSurf,TextRect=text_objects("INSTRUCTION",largetext,dred)
        TextRect.center=((400),(50))
        stextSurf,stextRect=text_objects("ARROW LEFT : LEFT TURN",smalltext,oval)
        stextRect.center=((150),(550))
        hTextSurf,hTextRect=text_objects("ARROW RIGHT : RIGHT TURN" ,smalltext,oval)
        hTextRect.center=((150),(600))
        atextSurf,atextRect=text_objects("ARROW UP : ACCELERATOR",smalltext,oval)
        atextRect.center=((150),(650))
        rtextSurf,rtextRect=text_objects("ARROW DOWN : BRAKE ",smalltext,oval)
        rtextRect.center=((150),(700))
        ptextSurf,ptextRect=text_objects("P : PAUSE  ",smalltext,oval)
        ptextRect.center=((150),(500))
        sTextSurf,sTextRect=text_objects("CONTROLS",mediumtext,dred)
        sTextRect.center=((350),(425))
        
        screen.blit(TextSurf,TextRect)                  # displaying the instruction page text
        screen.blit(textSurf,textRect)
        screen.blit(sTextSurf,sTextRect)
        screen.blit(stextSurf,stextRect)
        screen.blit(hTextSurf,hTextRect)
        screen.blit(atextSurf,atextRect)
        screen.blit(rtextSurf,rtextRect)
        screen.blit(ptextSurf,ptextRect)
        screen.blit(btextSurf,btextRect)
        screen.blit(xtextSurf,xtextRect)
        screen.blit(ytextSurf,ytextRect)

        button("BACK",1100,0,100,50,green,bright_green,"menu")      # display the back button

        pygame.display.update()
        
def pause_game(score):
    global pause
    while pause:
            for event in pygame.event.get():        #to check if the user has manually quit the game window
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
            screen.blit(pause_background,(0,0))         # to draw pause page background on screen
            largetext=pygame.font.Font('valorant.ttf',115)
            TextSurf,TextRect=text_objects("PAUSED",largetext,oval)
            TextRect.center=((display_width/2-150),(display_height/2-200))
            screen.blit(TextSurf,TextRect)
            button("RESUME",350,300,200,50,green,bright_green,"unpause")        #to display the required buttons
            button("RESTART GAME",350,380,200,50,blue,bright_blue,"play")
            button("MAIN MENU",350,460,200,50,red,bright_red,"menu")

            text=pygame.font.Font("batman.ttf",40)
            game_score=text.render("Your Score: " + str(score),True,red)        #displaying score in pause menu
            screen.blit(game_score,(50,50))
            pygame.display.update()
            #clock.tick(30)

def unpause_game(): # To unpause the game
    global pause
    pause=False

def countdown_background():                         # displaying countdown to start the game
    font=pygame.font.Font('batman.ttf',20)
    x=(display_width*0.45)
    y=(display_height*0.8)

    screen.blit(backgroundpic,(0,0))                        #to display grass during the countdown
    screen.blit(backgroundpic,(0,200))
    screen.blit(backgroundpic,(0,400))      
    screen.blit(backgroundpic,(1100,0))
    screen.blit(backgroundpic,(1100,200))
    screen.blit(backgroundpic,(1100,400))

    screen.blit(yellow_strip,(600,100))             # to display divider of the road
    screen.blit(yellow_strip,(600,200))
    screen.blit(yellow_strip,(600,300))
    screen.blit(yellow_strip,(600,400))
    screen.blit(yellow_strip,(600,100))
    screen.blit(yellow_strip,(600,500))
    screen.blit(yellow_strip,(600,600))
    screen.blit(yellow_strip,(600,0))
    screen.blit(yellow_strip,(600,600))

    screen.blit(white_strip,(325,100))               # to display center of leftside of road
    screen.blit(white_strip,(325,200))
    screen.blit(white_strip,(325,300))
    screen.blit(white_strip,(325,400))
    screen.blit(white_strip,(325,500))
    screen.blit(white_strip,(325,600))

    screen.blit(white_strip,(325,0))                # to display center of Rightside of road
    screen.blit(white_strip,(325,600))
    screen.blit(white_strip,(875,100))
    screen.blit(white_strip,(875,200))
    screen.blit(white_strip,(875,300))
    screen.blit(white_strip,(875,400))
    screen.blit(white_strip,(875,500))
    screen.blit(white_strip,(875,0))
    screen.blit(white_strip,(875,600))

    screen.blit(strip,(120,200))                        # to display the boundary of road
    screen.blit(strip,(120,0))
    screen.blit(strip,(120,100))
    screen.blit(strip,(1080,100))
    screen.blit(strip,(1080,0))
    screen.blit(strip,(1080,200))

    screen.blit(carimg,(x,y))                           # to display the car
    text=font.render("PASSED: 0",True, black)           # to display score and cars passed/dodged
    score=font.render("SCORE: 0",True,red)
    screen.blit(text,(0,50))
    screen.blit(score,(0,30))
    button("PAUSE",1050,0,150,50,blue,bright_blue,"pause")   # to display pause button

def countdown():
    countdown=True

    while countdown:
            for event in pygame.event.get():        #to check if the user has manually quit the game window
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                    
            screen.fill(gray)                # filling screen with road colour
            countdown_background()
            clock.tick(1)
            largetext=pygame.font.Font('valorant.ttf',115)

            TextSurf,TextRect=text_objects("3",largetext,teal)      # to display number 3
            TextRect.center=((display_width/2),(display_height/2))
            screen.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            screen.fill(gray)
            countdown_background()

            TextSurf,TextRect=text_objects("2",largetext,teal)        # to display number 2
            TextRect.center=((display_width/2),(display_height/2))
            screen.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            screen.fill(gray)
            countdown_background()

            TextSurf,TextRect=text_objects("1",largetext,teal)         # to display number 1
            TextRect.center=((display_width/2),(display_height/2))
            screen.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            screen.fill(gray)
            countdown_background()

            TextSurf,TextRect=text_objects("GO!!!",largetext,teal)          # to display number GO!!!
            TextRect.center=((display_width/2),(display_height/2))
            screen.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            game_loop()

def score_system(passed,score):                                  # to display the score during the game
    font=pygame.font.Font("batman.ttf",20)                       # and cars dodged/passed during the game
    text=font.render("Passed :"+str(passed),True,black)
    score=font.render("Score :"+str(score),True,red)
    screen.blit(text,(0,50))
    screen.blit(score,(0,30))

def text_objects(text,font,color):
    textsurface=font.render(text,True,color)
    return textsurface,textsurface.get_rect()

def crash(score):                                                       # to display the crash page
   game_sound.stop()                                                    # stops the game sound
   crash_sound.play()                                                   # plays crash sound immediately after crash
   screen.blit(crash_background,(0,0))
   largeText = pygame.font.Font("valorant.ttf",115)
   TextSurf, TextRect = text_objects("You Crashed", largeText,teal)          # displaying you crashed
   TextRect.center = ((display_width/2),(display_height/2-200))
   screen.blit(TextSurf, TextRect)
   
   text=pygame.font.Font("batman.ttf",40)
   game_score=text.render("Your Score: " + str(score),True,red)                  # displaying the final score
   screen.blit(game_score,(50,50))

   while True:
        for event in pygame.event.get():            #to check if the user has manually quit the game window
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
             
        button("Play Again",200,400,150,75,red,bright_red,"play")   # displaying the required buttons in crash page
        button("Quit",850,400,150,75,green,bright_green,"quit")
        button("MAIN MENU",500,400,200,75,blue,bright_blue,"menu")

        pygame.display.update()
        #clock.tick(60)

def background():
    screen.blit(backgroundpic,(0,0))
    screen.blit(backgroundpic,(0,200))                  # to display grass during the game
    screen.blit(backgroundpic,(0,400))
    screen.blit(backgroundpic,(1100,0))
    screen.blit(backgroundpic,(1100,200))
    screen.blit(backgroundpic,(1100,400))

    screen.blit(yellow_strip,(600,100))                 # to display divider of the road
    screen.blit(yellow_strip,(600,200))
    screen.blit(yellow_strip,(600,300))
    screen.blit(yellow_strip,(600,400))
    screen.blit(yellow_strip,(600,100))
    screen.blit(yellow_strip,(600,500))
    screen.blit(yellow_strip,(600,600))
    screen.blit(yellow_strip,(600,0))
    screen.blit(yellow_strip,(600,600))

    screen.blit(white_strip,(325,100))
    screen.blit(white_strip,(325,200))              # to display center of leftside of road
    screen.blit(white_strip,(325,300))
    screen.blit(white_strip,(325,400))
    screen.blit(white_strip,(325,500))
    screen.blit(white_strip,(325,600))
    
    screen.blit(white_strip,(325,0))                # to display center of Rightside of road
    screen.blit(white_strip,(325,600))
    screen.blit(white_strip,(875,100))
    screen.blit(white_strip,(875,200))
    screen.blit(white_strip,(875,300))
    screen.blit(white_strip,(875,400))
    screen.blit(white_strip,(875,500))
    screen.blit(white_strip,(875,600))
    screen.blit(white_strip,(875,0))
    screen.blit(white_strip,(875,600))
    
    screen.blit(strip,(120,200))
    screen.blit(strip,(120,0))                  # to display the boundary of road
    screen.blit(strip,(120,100))
    screen.blit(strip,(1080,100))
    screen.blit(strip,(1080,0))
    screen.blit(strip,(1080,200))

def car(x,y):
    screen.blit(carimg,(x,y))           # displaying the player car and its position

def things(img, img1, img2, car1_x, car2_x, car3_x, car1_y, car2_y, car3_y):        
    if car1_x!=car2_x and car1_x!=car3_x and car1_x!=car2_x-2 and car1_x!=car3_x+2 and car1_x!=car2_x+3 and car1_x!=car3_x-1:
        screen.blit(img, (car1_x, car1_y))
    if car2_x!=car1_x and car2_x!=car3_x and car2_x!=car1_x-2 and car2_x!=car3_x-1 and car2_x!=car1_x+2 and car2_x!=car3_x+1:
        screen.blit(img1, (car2_x, car2_y))
    if car3_x!=car1_x and car3_x!=car2_x and car3_x!=car1_x-3 and car3_x!=car2_x-3 and car3_x!=car1_x+1 and car3_x!=car2_x+1:
        screen.blit(img2, (car3_x, car3_y))

def randimg1():
    image=random.choice(carimg_list1)
    return image

def randimg2():
    image=random.choice(carimg_list2)
    return image


def game_loop():
    game_sound.play(-1)             # starting the game sound
    
    global pause
    x=(display_width*0.45)
    y=(display_height*0.8)         # initial car position
    
    x_change , y_change= 0, 0               
    obstacle_speed=9
    car_speed = 7
    car_width = 80
    car_height = 160
    
    car1_x = random.randrange(120,600-80)
    car1_y = -600   
    car2_x = random.randrange(600,795)
    car2_y = -800 
    car3_x = random.randrange( 900,(display_width-200))
    car3_y = -900 

    #obs_starty=-750
    obs_width=81
    obs_height=150
    dodged=0
    level=0
    score=0
    y2=7

    bumped=False
    while not bumped:
        for event in pygame.event.get():    #to check if the user has manually quit the game window
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

            if event.type==pygame.KEYDOWN: #Controls - Left Right and Increase/Decrease while pressing Up/Down
                if event.key==pygame.K_LEFT:
                    x_change=-5
                if event.key==pygame.K_RIGHT:
                    x_change=5
                #if event.key==pygame.K_UP:
                   # obstacle_speed+=2
               #if event.key==pygame.K_DOWN:
                    #obstacle_speed-=2
            if event.type==pygame.KEYUP: #After releasing the key it should stop moving 
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_change=0
                    

        x+=x_change
        pause=True
        screen.fill(gray) 

        rel_y=y2%backgroundpic.get_rect().width #Movement of background backward as car will move forward
        screen.blit(backgroundpic,(0,rel_y-backgroundpic.get_rect().width))
        screen.blit(backgroundpic,(1100,rel_y-backgroundpic.get_rect().width))
        if rel_y<800:
            screen.blit(backgroundpic,(0,rel_y))
            screen.blit(backgroundpic,(1100,rel_y))
            screen.blit(yellow_strip,(600,rel_y))
            screen.blit(yellow_strip,(600,rel_y+100))
            screen.blit(yellow_strip,(600,rel_y+200))
            screen.blit(yellow_strip,(600,rel_y+300))
            screen.blit(yellow_strip,(600,rel_y+400))
            screen.blit(yellow_strip,(600,rel_y+500))
            screen.blit(yellow_strip,(600,rel_y+600))
            screen.blit(yellow_strip,(600,rel_y-100))
            screen.blit(white_strip,(325,rel_y))
            screen.blit(white_strip,(325,rel_y+100))
            screen.blit(white_strip,(325,rel_y+200))
            screen.blit(white_strip,(325,rel_y+300))
            screen.blit(white_strip,(325,rel_y+400))
            screen.blit(white_strip,(325,rel_y+500))
            screen.blit(white_strip,(325,rel_y+600))
            screen.blit(white_strip,(325,rel_y-100))
            screen.blit(white_strip,(875,rel_y))
            screen.blit(white_strip,(875,rel_y+100))
            screen.blit(white_strip,(875,rel_y+200))
            screen.blit(white_strip,(875,rel_y+300))
            screen.blit(white_strip,(875,rel_y+400))
            screen.blit(white_strip,(875,rel_y+500))
            screen.blit(white_strip,(875,rel_y+600))
            screen.blit(white_strip,(875,rel_y-100))
            screen.blit(strip,(120,rel_y-200))
            screen.blit(strip,(120,rel_y+20))
            screen.blit(strip,(120,rel_y+30))
            screen.blit(strip,(1080,rel_y-100))
            screen.blit(strip,(1080,rel_y+20))
            screen.blit(strip,(1080,rel_y+30))

        y2+=obstacle_speed
        #adding obstacle cars
        if car1_y<-500:
            img = randimg1() 

        if car2_y<-600:
            img1 = randimg2()

        if car3_y<-700:
            img2 = randimg2()

        things(img, img1, img2, car1_x, car2_x, car3_x, car1_y, car2_y, car3_y)#function for movements of obstacles
                                                
        car1_y += obstacle_speed
        car2_y += obstacle_speed
        car3_y += obstacle_speed
        #movements of obstacles
        if car1_y > display_height:
            car1_y = 0 - car_height
            car1_x = random.randrange(120,600-80)
            img=random.choice(carimg_list1)    
            dodged += 1
            score=dodged*10
            obstacle_speed += 0.2      

        if car2_y > display_height:
            car2_y = 0 - car_height
            car2_x = random.randrange(620,795)
            img1=random.choice(carimg_list2)    
            dodged += 1
            score=dodged*10
            obstacle_speed += 0.2  

        if car3_y > display_height:
            car3_y = 0 - car_height
            car3_x = random.randrange(900,display_width-200)
            img2=random.choice(carimg_list2)    
            dodged += 1
            score=dodged*10
            obstacle_speed += 0.2  
        
        car(x,y)
        score_system(dodged,score)

         #Crashing Part - adding restriction
        if x>display_width-(car_width+110) or x<120:
            crash(score)
        
        if y<car1_y+car_height:
            if ((x > car1_x and x < car1_x + car_width) or (x+car_width > car1_x and x+car_width < car1_x+obs_width)):
                crash(score)
        if y<car2_y+car_height:
            if ((x > car2_x and x < car2_x + car_width) or (x+car_width > car2_x and x+car_width < car2_x+obs_width)):
                crash(score)
        if y<car3_y+car_height:
            if ((x > car3_x and x < car3_x + car_width) or (x+car_width > car3_x and x+car_width < car3_x+obs_width)):
                crash(score)

        button("Pause",1050,0,150,50,blue,bright_blue,"pause",score)    # Pause Button
        pygame.display.update()
        clock.tick(60)

introduction()
game_loop()
pygame.quit()
quit()
