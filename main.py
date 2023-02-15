import pygame
import random
import sys
from pygame.locals import *
pygame.init()

#background image
main_bg=pygame.image.load("gallery\\sprites\\main_bg.png")
welcome_bg=pygame.image.load("gallery\\sprites\\welcome.png")
apple=pygame.image.load("gallery\\sprites\\apple.png")
snake_head=pygame.image.load("gallery\\sprites\\snake_head.png")

#colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
blue=(0,0,255)
yellow=(255,255,0)

#creating game window
screen_width=920
screen_height=620
gamewindow=pygame.display.set_mode((920,620))

#game title
pygame.display.set_caption("Snakes")

#my font
myFont = pygame.font.SysFont(None ,45)

#my clock
clock=pygame.time.Clock()

# plot snake
def snake_plot(gamewindow,snake_list,color,snake_size):
    for x,y in snake_list:
        gamewindow.blit(snake_head,[x,y])

#text screen
def text_screen(text, color, x, y):
    screen_text = myFont.render(text, True, color)
    gamewindow.blit(screen_text, [x,y])

with open("gallery\\highscore.txt","r") as f:
    highscore = f.read()
def welcome():
    exit_game=False
    while not exit_game:
        gamewindow.blit(welcome_bg,[0,0])
        pygame.display.update()
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                exit_game = True
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_RETURN:
                    main_game_loop()
    pygame.quit()
#game loop

def main_game_loop():
    # game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 30
    fps = 100
    score = 0
    velocity_x = 0
    velocity_y = 0
    snake_list = []
    snake_lenth = 1
    velocity_const = 5
    food_x = random.randint(snake_size, screen_width - snake_size)
    food_y = random.randint(snake_size, screen_height - 2 * snake_size)
    global highscore

    while not exit_game:
        if game_over:
            text3="GAME OVER !!! Press ENTER to play again"
            gamewindow.blit(main_bg,[0,0])
            text_screen(text3,black,150,screen_height/2-30)
            text_screen("Your Score = "+str(score),red,350,310)
            text_screen("High Score = "+highscore,blue,350,340)
            pygame.display.update()
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    exit_game = True
                    sys.exit()
                if events.type==pygame.KEYDOWN:
                    if events.key==pygame.K_RETURN:
                        main_game_loop()
        else:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    exit_game = True
                if events.type==pygame.KEYDOWN:
                    if events.key==pygame.K_RIGHT:
                        velocity_x= velocity_const
                        velocity_y=0
                    if events.key==pygame.K_DOWN:
                        velocity_y=velocity_const
                        velocity_x=0
                    if events.key==pygame.K_LEFT:
                        velocity_x= -velocity_const
                        velocity_y=0
                    if events.key==pygame.K_UP:
                        velocity_y= -velocity_const
                        velocity_x= 0

            snake_x+=velocity_x
            snake_y+=velocity_y
            snake_head=[]
            snake_head.append(snake_x)
            snake_head.append(snake_y)
            snake_list.append(snake_head)
            if len(snake_list)>snake_lenth:
                del snake_list[0]


            if (abs(snake_x-food_x)<snake_size) and (abs(snake_y-food_y)<snake_size):
                score=score+10
                food_x = random.randint(snake_size, screen_width-snake_size)
                food_y = random.randint(snake_size, screen_height-2*snake_size)
                pygame.mixer.music.load("gallery\\audio\\eatsound.ogg")
                pygame.mixer.music.play()
                snake_lenth=snake_lenth+1

                if score>int(highscore):
                    highscore=str(score)
                    with open("gallery\\highscore.txt", "w") as f:
                        f.write(highscore)

            # gamewindow.fill(blue)
            gamewindow.blit(main_bg, [0,0])


            if (snake_x>screen_width-(snake_size+15)) or (snake_x<15) or (snake_y>screen_height-(snake_size+15)) or (snake_y<15):
                game_over=True
                pygame.mixer.music.load("gallery\\audio\\diesound.ogg")
                pygame.mixer.music.play()

            snake_plot(gamewindow,snake_list, black, snake_size)
            text2 = "Score -: "+str(score)
            text_screen(text2,red,20,screen_height-35)
            gamewindow.blit(apple,[food_x,food_y])
            pygame.display.flip()
            pygame.display.update()
        clock.tick(fps)
    pygame.quit()
welcome()
quit()
