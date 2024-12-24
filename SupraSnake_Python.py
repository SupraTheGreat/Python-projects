import pygame
import time
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
UI_HEIGHT = 100

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Snake and speed
SNAKE_BLOCK = 20
SNAKE_SPEED = 10

# Snake positions
snake_x = []
snake_y = []

# Apple positions
applex = 0.0
appley = 0.0

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')

# Clock for controlling game speed
clock = pygame.time.Clock()

# Font styles
font_style = pygame.font.SysFont(None, 50)
font_title = pygame.font.SysFont("comicsans", 40, bold=True) # big font for title
font_subtitle = pygame.font.SysFont("comicsans", 18, italic=True) # medium font for subtitle
font_small = pygame.font.Font(None, 24)  # Small font for the quit instructions
score_font = pygame.font.SysFont("bahnschrift", 25) # Clean font for score

# Game over?
game_over = False

startx = SCREEN_WIDTH/2 # Center x of the screen
starty = SCREEN_HEIGHT/2 # Center y of the screen
pygame.draw.rect(screen, (0, 255, 0), (startx, starty, SNAKE_BLOCK, SNAKE_BLOCK)) # Spawn the snake in the center

# Add this function to draw the border between the UI and the actual field where the snake is
def draw_ui_border():
    pygame.draw.line(screen, WHITE, (0, UI_HEIGHT), (SCREEN_WIDTH, UI_HEIGHT), 2)  # 2-pixel thick white line

def display_score(score):
    # Clear only the UI area to prevent overlapping
    pygame.draw.rect(screen, BLACK, (0, 0, SCREEN_WIDTH/4, UI_HEIGHT))
    # Draw the updated score
    value = score_font.render("Score: " + str(score), True, WHITE)
    screen.blit(value, [10, 10])

def getRandomPos():
    randomx = float(random.randint(0, (SCREEN_WIDTH-20)/SNAKE_BLOCK)*SNAKE_BLOCK) # Getting random x for apple
    randomy = float(random.randint((UI_HEIGHT/SNAKE_BLOCK), (SCREEN_HEIGHT-20)/SNAKE_BLOCK)*SNAKE_BLOCK) # Getting random y for apple
    return randomx, randomy

def placeApple():
    # First 3 numbers are (r, g, b)
    # Second 4 numbers are (x, y, base, height)
    # origin is at the top right corner
    applex, appley = getRandomPos()
    if applex not in snake_x and appley not in snake_y:
        pygame.draw.rect(screen, (255, 0, 0), (applex, appley, SNAKE_BLOCK, SNAKE_BLOCK)) # Drawing apple at that random pos
    else:
        applex, appley = placeApple()
        return applex, appley
    return applex, appley # Returning the apple's x and y positions

def drawSnake(drawx, drawy):
    pygame.draw.rect(screen, (0, 255, 0), (drawx, drawy, SNAKE_BLOCK, SNAKE_BLOCK)) # Drawing the snake at drawx, drawy
    snake_x.append(drawx) # Adding x position to list of snake x positions
    snake_y.append(drawy) # Adding y position to list of snake y positions

def check():
    global x, y, applex, appley, score, snake_length # Making these variables global

    if x == applex and y == appley: # Checking if the snake is on the apple, meaning it eats the apple
        score += 1 # increase the score by one
        snake_length += 1
        applex, appley = placeApple() # We generate a new apple
        print("APPLE APPLE APPLE APPLE APPLE APPLE APPLE")
        return
    
    if (applex in snake_x) and (appley in snake_y):
        if snake_x.index(applex) == snake_y.index(appley):
            score += 1
            snake_length += 1
            applex, appley = placeApple()
            print("APPLE APPLE APPLE APPLE APPLE APPLE APPLE")
            return

def display_title(): # Displays the title and subtitle
    title_text = font_title.render("Snake Game", True, WHITE)
    subtitle_text = font_subtitle.render("By Supra", True, WHITE)

    # Title near the center at the top of the screen
    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 0))

    # Subtitle is below the title
    screen.blit(subtitle_text, (SCREEN_WIDTH // 2 - subtitle_text.get_width() // 2, 55))

def display_quit_message():
    quit_text = font_small.render("Press Q to quit", True, WHITE)
    screen.blit(quit_text, (SCREEN_WIDTH - quit_text.get_width() - 10, 10))  # Position it near the top-right

applex, appley = getRandomPos() # Getting first apple position
pygame.draw.rect(screen, (255, 0, 0), (applex, appley, SNAKE_BLOCK, SNAKE_BLOCK)) # Drawing apple at that random position

display_quit_message()  # Show the quit instructions
display_title() # Display the title and subtitle

x = startx # Setting the current snake x to the starting x when the game begins
y = starty # Setting the current snake y to the starting y when the game begins

dir = "none" # The snake is not moving in any direction, so set dir to 'none'
snake_length = 2 # Setting the snake's initial length
score = 0 # The number of apples the snake has eaten

def game_loop(): # Overall game loop

    # Making all variables global
    global x, y, applex, appley, dir, SCREEN_WIDTH, SCREEN_HEIGHT, UI_HEIGHT, game_over, clock, screen, SNAKE_BLOCK, SNAKE_SPEED, snake_x, snake_y, score

    while game_over != True: # While the game is not over:

        draw_ui_border() # Draw the UI border

        pygame.draw.rect(screen, (255, 0, 0), (applex, appley, SNAKE_BLOCK, SNAKE_BLOCK)) # Continally redrawing the apple

        print("X is " + str(x) + " and applex is " + str(applex)) # Printing x positions of snake and apple
        print("Y is " + str(y) + " and appley is " + str(appley)) # Printing y positions of snake and apple
        print("Snake length is " + str(len(snake_x))) # Printing the length of the snake

        check() # Scroll up to check function for details

        while len(snake_x) > (snake_length): # While the snake is longer than what it's supposed to be, terminate the longer blocks
            pygame.draw.rect(screen, (0, 0, 0), (snake_x[0], snake_y[0], SNAKE_BLOCK, SNAKE_BLOCK)) # Remove the oldest block
            snake_x.remove(snake_x[0]) # Terminate it from list of x positions
            snake_y.remove(snake_y[0]) # Terminate it from list of y positions

        pygame.display.update() # Update the display

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN: # Is a key pressed?

                if event.key == pygame.K_LEFT: # If the left arrow is pressed:

                    drawSnake(x, y) # Draw the snake at its current position
                    check() # Scroll up to check function for details
                    x -= SNAKE_BLOCK # Make the x decrease
                    dir = "left"

                if event.key == pygame.K_RIGHT: # If the right arrow is pressed:

                    drawSnake(x, y) # Draw the snake at its current position
                    check() # Scroll up to check function for details
                    x += SNAKE_BLOCK # Make the x increase
                    dir = "right"

                if event.key == pygame.K_UP: # If the up arrow is pressed

                    drawSnake(x, y) # Draw the snake at its current position
                    check() # Scroll up to check function for details
                    y -= SNAKE_BLOCK # Make the y go down (which moves the snake up since the origin is at the top-left)
                    dir = "up"

                if event.key == pygame.K_DOWN: # if the down arrow is pressed

                    drawSnake(x, y) # Draw the snake at its current position
                    check() # Scroll up to check function for details
                    y += SNAKE_BLOCK # Move the y go up (which moves the snake down since the origin is at the top-left)
                    dir = "down"

                if event.key == pygame.K_q: # If the 'Q' key is pressed:

                    pygame.quit() # Quit pygame
                    quit() # End the runtime
            
        if x > SCREEN_WIDTH-20 or x < 0 or y > SCREEN_HEIGHT-20 or y < UI_HEIGHT: # Does the snake hit a wall?
            pygame.quit() # Quit pygame
            quit() # End runtime
    
        drawSnake(x, y) # Draw the snake

        if dir == "left": # if the direction is left:
            x -= SNAKE_BLOCK # Keep the x changing in that direction
        if dir == "right": # if the direction is right:
            x += SNAKE_BLOCK # Keep the x changing in that direction
        if dir == "up": # if the direction is up:
            y -= SNAKE_BLOCK # Keep the y changing in that direction
        if dir == "down": # if the direction is down:
            y += SNAKE_BLOCK # Keep the y changing in that direction
    
        display_score(score) # Display and update the score
        pygame.display.update() # Update the display once more
        clock.tick(SNAKE_SPEED) # Controls the speed of the snake


game_loop()