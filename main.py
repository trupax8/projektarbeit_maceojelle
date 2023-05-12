#import pygame package
import pygame 
#import the time package to restart the game
import time   
#import for the random library to randomize the car coming from the opposite side.
import random   

#test

#initiate package
pygame.init() 
#color code in RGB form
gray=(60,60,60)
#color code in RGB form
black=(255,0,0) 
#set width & height of the display
display=pygame.display.set_mode((830,600))
#set name of the game window
pygame.display.set_caption("Racing game built with python")    

#load car image
carimg=pygame.image.load("car1.png")
#load background image for the left side
backgroundleft=pygame.image.load("left.png")
#load background image for the right side
backgroundright=pygame.image.load("right.png")
#Defined car width
car_width=23

#define car functions that are coming from the opposite side.#(we are naming car that are coming from the opposite side policecar)
def policecar(police_startx,police_starty,police):
    if police==0:
        #for police car no 2
        police_come=pygame.image.load("car2.png") 
    if police==1: 
        #for police car no 3
        police_come=pygame.image.load("car3.png")
    if police==2:
        #for police car no 1
        police_come=pygame.image.load("car1.png") 
    #display the police car
    display.blit(police_come,(police_startx,police_starty))

def background():
    #defining the position of background image for left side in x axis & y axis
    display.blit(backgroundleft,(0,0))
    #defining the position of background image for right side in x axis & y axis
    display.blit(backgroundright,(700,0)) 

    #creating the function that will display the game over message
def crash():       
    message_display("Game Over")

#create function for customizing the game over message
def message_display(text):     
    #set font style and size of the message
    large_text=pygame.font.Font("freesansbold.ttf",80) 
    #set function to edit the message
    textsurf,textrect=text_object(text,large_text) 
    #set the position of the message on the screen
    textrect.center=((400),(300)) 
    #display the message
    display.blit(textsurf,textrect)
    pygame.display.update()
    #After the car has crashed, wait 3 seconds.
    time.sleep(3)     
    #call the loop function to restart the game
    loop()     

#This function will display the message after the car has crashed.
def text_object(text,font):    
    #set color of the message
    text_surface=font.render(text,True,black) 
    #after that restart the game & ready to give some input 
    return text_surface,text_surface.get_rect()  

#create car function
def car(x,y): 
    #set position of the car
    display.blit(carimg,(x,y))

#all the function are called using this function
def loop():
    #set car position for x and y axis  
    x=400 
    y=540 
    #set changing position of the car
    x_change=0 
    y_change=0
    #set police car speed
    policecar_speed=9
    #set starting stage for the police car 
    police=0   
    #with this police car will come randomly
    police_startx=random.randrange(130,(700-car_width))
    #police car will comes in y axis in negative value because car is coming from opposite side 
    police_starty=-600
    # set police car height and width
    police_width=23
    police_height=47

    #if the game doesn't have any problem to start
    bumped=False
    #start the game 
    while not bumped: 
        #defining the input of the game
        for event in pygame.event.get():   
            #if quit input is given
            if event.type==pygame.QUIT:   
            #   bumped=True     #game will stop
                pygame.quit()
                quit()

            #defining the arrow keys
            if event.type==pygame.KEYDOWN: 
                #if user is pressing the left arrow
                if event.key==pygame.K_LEFT:
                    #car will move left side -1 
                    x_change=-1   
                #if user is pressing the right arrow
                if event.key==pygame.K_RIGHT: 
                    #car will move left side 1
                    x_change=1     
            #if any key is not being pressed then stop the car
            if event.type==pygame.KEYUP:   
                x_change=0
        x+=x_change

                #setting the color of the road
        display.fill(gray) 
        #car speed that are coming from opposite side(y axis)
        background()
        police_starty-=(policecar_speed/1.2)   
        policecar(police_startx,police_starty,police) 
        #police car speed will increase slowly
        police_starty+=policecar_speed         
        car(x,y)   
        #if the car goes out of range(side wall of the road)
        if x<130 or x>700-car_width:       
        #bumped=True    #game is over
            #call crash function
            crash()

                    #seting how far the police car will go
        if police_starty>600:     
            #only one car will cross the road in one time
            police_starty=0-police_height 
            #then other car will come
            police_startx=random.randrange(130,(1000-300)) 
            #set how many car will come
            police=random.randrange(0,2)   

        #if the police car does not cross the road then crash the car
        if y<police_starty+police_height:
            if x > police_startx and x < police_startx + police_width or x + car_width > police_startx and x + car_width < police_startx + police_width :
                crash()   

                        #restart the game
        pygame.display.update() 
loop() # exiting from game
pygame.quit() 
quit()