import pygame
import time
import random

#defining colours
black = 0, 0, 0
green = 0, 255 , 0
red = 255, 0, 0

#Window size
width = 720
height = 480
pygame.display.set_caption('ICU4U Snake Game')
screen = pygame.display.set_mode((width,height))

#Initialize pygame
pygame.init()

#Snake
#Initial position
snake_position = [100, 50]

#Starting snake
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]]

#setting direction and speed
snake_speed = 15
direction = 'RIGHT'

#score
score = 0

#Let's add some fruit
fruit_position = [random.randrange(0, ((width-10)//10))*10,
                  random.randrange(0, ((height-10)//10))*10]
#fruit_spawn = True

#FPS Controller
fps = pygame.time.Clock()

def die():
    #create a font object
    my_font = pygame.font.SysFont('comicsansms', 50)

    #create a text surface
    game_over_surface = my_font.render('GAME OVER ' + 'Score = '+ str(score), True, red)

    #create a rectangle object for the surface
    game_over_rect = game_over_surface.get_rect()

    #set the position of the rectangle
    game_over_rect.center = [(width/2), (height/2)]

    #blit command: draw the text into the rectangle
    screen.blit(game_over_surface, game_over_rect)

    #Update the screen
    pygame.display.flip()

    time.sleep(2)

    #deactive the pygame library and quit
    pygame.quit()
    quit()

#Display the score
def scoring(score):
    #create a font object
    score_font = pygame.font.SysFont('comicsansms', 20)

    #create a text surface
    score_surface = score_font.render('Score:'+ str(score), True, red)

    #create a rectangle object for the surface
    score_rect = score_surface.get_rect()

    #blit command: draw the text into the rectangle
    screen.blit(score_surface, score_rect)

    #Update the screen
    pygame.display.flip()


#The loop that runs the game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction!= 'DOWN':
                direction = 'UP'
            if event.key == pygame.K_DOWN and direction!= 'UP':
                direction = 'DOWN'
            if event.key == pygame.K_LEFT and direction!= 'RIGHT':
                direction = 'LEFT'
            if event.key == pygame.K_RIGHT and direction!= 'LEFT':
                direction = 'RIGHT'

    #Filling the background
    screen.fill(black)

    #Drawing the snake
    for pos in snake_body:
        pygame.draw.rect(screen, green,pygame.Rect(pos[0], pos[1], 10, 10))
    
    #Draw the fruit
    #pygame.draw.rect(screen, red, pygame.Rect(fruit_position[0],fruit_position[1],10,10))
    pygame.draw.circle(screen, red,(fruit_position[0]+5, fruit_position[1]+5),5)

    #Moving the snake
    if direction == 'RIGHT':
        snake_position[0] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    
    #Move the snake
    snake_body.insert(0, list(snake_position))

    #Fruit eating part
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        fruit_position = [random.randrange(0, ((width-10)//10))*10,
                          random.randrange(0, ((height-10)//10))*10]
        score += 10
    else:
        snake_body.pop()

    #Display the score
    scoring(score)

    #Update the screen
    pygame.display.flip()

    #Increment time
    fps.tick(snake_speed)

    #Game Over Conditions
    if snake_position[0] < 0 or snake_position[0] > width:
        die()
    if snake_position[1] < 0 or snake_position[1] > height:
        die()
    
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            die()
    

pygame.quit()