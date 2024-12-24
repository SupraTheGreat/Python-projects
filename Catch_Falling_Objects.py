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

# Game speed
GAME_SPEED = 20

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Catch The Apples!')

# Clock for controlling game speed
clock = pygame.time.Clock()

# Game over?
game_over = False

# X and Y
x = SCREEN_WIDTH/2
y = SCREEN_HEIGHT-75

# Bucket speed
velocity = 10

# List of drawn apples
apples = []
applex = 0 # apple x pos
appley = 0 # apple y pos

# Mouse pos
mouse_x = 0
mouse_y = 0

# Score
score = 0

# Previous spawn time
previous_seconds = 0
prev_time = 0
prev_mouse_x = x

# Font styles
font_style = pygame.font.SysFont(None, 50)
font_title = pygame.font.SysFont("comicsans", 40, bold=True) # big font for title
font_outline = pygame.font.SysFont("comicsans", 37, bold=True) # outline font for title
font_subtitle = pygame.font.SysFont("comicsans", 18, italic=True) # medium font for subtitle
font_small = pygame.font.Font(None, 24)  # Small font for the quit instructions
score_font = pygame.font.SysFont("bahnschrift", 25) # Clean font for score

def draw_bucket(screen, x, y, width=60, height=20):
    pygame.draw.rect(screen, (0, 0, 255), (x, y, width, height), 1)

def draw_bucket2(screen, x, y, width=60, height=20, blue=150):
    pygame.draw.rect(screen, (0, 0, blue), (x, y, width, height), 1)


def display_title(): # Displays the title and subtitle
    title_text = font_title.render("Catch the Apples!", True, WHITE)
    outline_text = font_title.render("Catch the Apples!", True, BLACK)
    subtitle_text = font_subtitle.render("By Supra", True, WHITE)

    # Title near the center at the top of the screen
    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 0))
    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 6))
    screen.blit(title_text, ((SCREEN_WIDTH // 2 - title_text.get_width() // 2)+3, 3))
    screen.blit(title_text, ((SCREEN_WIDTH // 2 - title_text.get_width() // 2)-3, 3))
    screen.blit(outline_text, (SCREEN_WIDTH // 2 - outline_text.get_width() // 2, 3))
    
    # Subtitle is below the title
    screen.blit(subtitle_text, (SCREEN_WIDTH // 2 - subtitle_text.get_width() // 2, 55))

def display_score(score):
    # Clear only the UI area to prevent overlapping
    pygame.draw.rect(screen, BLACK, (0, 0, SCREEN_WIDTH/4, UI_HEIGHT))
    # Draw the updated score
    value = score_font.render("Score: " + str(score), True, WHITE)
    screen.blit(value, [10, 10])

def draw_apple():
    global apples, applex, appley
    applex = random.randint(20, SCREEN_WIDTH-20)
    appley = UI_HEIGHT
    apples.append([applex, appley])
    pygame.draw.rect(screen, (255, 0, 0), (applex, appley, 15, 15), 1)

def updateApple(lst):
    global prev_time, apples
    current_time = pygame.time.get_ticks()
    if current_time - prev_time > 0.1:
        for i in range(len(lst)):
            lst[i][1] += 10  # Move each apple down
            prev_time = current_time  # Update the time
    for i in range(len(lst)):
        pygame.draw.rect(screen, (255, 0, 0), (lst[i][0], lst[i][1], 15, 15), 1)

def collision(applepos, bucketpos):

    apple_x, apple_y = applepos
    bucket_x, bucket_y= bucketpos
    bucket_x -= 30

    # pygame.draw.rect(screen, (255, 0, 0), (apple_x, apple_y, 15, 15), 1)  # apple hitbox
    # pygame.draw.rect(screen, (0, 255, 0), (bucket_x, bucket_y, 60, 20), 1)  # bucket hitbox

    # Check if the apple rectangle overlaps with the bucket rectangle
    if (apple_x + 15 > bucket_x and
        apple_x < bucket_x + 60 and
        apple_y + 15 >= bucket_y and
        apple_y <= bucket_y + 20):
        return True
    return False


while game_over != True:

    screen.fill(BLACK) # Clear the screen (refresh)
    display_title() # Display the title
    display_score(score)
    
    seconds = pygame.time.get_ticks()/1000
    
    if seconds - previous_seconds > 1.5:
        draw_apple() # Draw apple
        previous_seconds = seconds
    
    if seconds - previous_seconds > 0.01:
        prev_mouse_x = mouse_x
    draw_bucket2(screen, prev_mouse_x-30, y-40, width=60, height=20, blue=150)
    
    for i in range(len(apples)):
        if i > len(apples)-1:
            break
        if collision(apples[i], [mouse_x, y-40]):
            apples.remove(apples[i])
            score += 1

    
    updateApple(apples) # Update apples
    
    pygame.display.update() # Update the display

    mouse_x, mouse_y = pygame.mouse.get_pos() # Get mouse positions

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: # Is a key pressed?
            
            # if event.key == pygame.K_LEFT:
            #     x -= velocity
            
            # if event.key == pygame.K_RIGHT:
            #     x += velocity

            if event.key == pygame.K_q: # Quit
                pygame.quit()
                quit()

    for i in range(len(apples)):
        if apples[i][1] > SCREEN_HEIGHT-1:
            game_over = True

    if game_over == True:
        break
    draw_bucket(screen, mouse_x-30, y-40, width=60, height=20) # Draw the bucket at the correct x and y
    pygame.display.update() # Update the display
    clock.tick(GAME_SPEED)

while True:
    screen.fill(BLACK)
    end_text = font_title.render("GAME OVER", True, RED)
    screen.blit(end_text, (SCREEN_WIDTH // 2 - end_text.get_width() // 2, SCREEN_HEIGHT/2-50))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: # Is a key pressed?
            if event.key == pygame.K_q: # Quit
                pygame.quit()
                quit()
pygame.quit()
quit()