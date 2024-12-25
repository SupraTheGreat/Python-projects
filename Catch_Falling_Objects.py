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
GAME_SPEED = 25

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
difficulty = 1.5 # difficulty (1.5 is easiest, less is harder) or Apple spawn delay

# List of drawn broccoli 🤮
broccoli = []
broccolix = 0
broccoliy = 0

# Background effects?
background = []
backgroundx = 0
backgroundy = 0

# Mouse pos
mouse_x = 0
mouse_y = 0

# Score
score = 0

# Game started?
start = False

# Previous spawn time
previous_seconds = 0
previous_seconds2 = 0
previous_seconds3 = 0
prev_time = 0
prev_time2 = 0
prev_time3 = 0
prev_mouse_x = x

# Font styles
font_style = pygame.font.SysFont(None, 50)
font_title = pygame.font.SysFont("microsoftyahei", 40, bold=True) # big font for title
font_over = pygame.font.SysFont("dejavusansmono ", 80, bold=True) # game over font for title
font_countdown = pygame.font.SysFont("microsoftyahei ", 120, bold=True) # countdown to start
font_outline = pygame.font.SysFont("comicsansms ", 37, bold=True) # outline font for title
font_subtitle = pygame.font.SysFont("comicsansms ", 18, italic=True) # medium font for subtitle
font_small = pygame.font.Font(None, 24)  # Small font for the quit instructions
score_font = pygame.font.SysFont("bahnschrift", 25) # Clean font for score

def draw_bucket(screen, x, y, width=60, height=20):
    pygame.draw.rect(screen, (0, 0, 255), (x, y, width, height), 1)

def draw_bucket2(screen, x, y, width=60, height=20, blue=150):
    pygame.draw.rect(screen, (0, 0, blue), (x, y, width, height), 1)

def draw_ui_border():
    pygame.draw.line(screen, WHITE, (0, UI_HEIGHT), (SCREEN_WIDTH, UI_HEIGHT), 2)  # 2-pixel thick white line

def display_title(): # Displays the title and subtitle
    title_text = font_title.render("Catch the Apples!", True, WHITE)
    outline_text = font_title.render("Catch the Apples!", True, BLACK)
    subtitle_text = font_subtitle.render("By Supra", True, WHITE)
    instructions = font_small.render("Press Q to Quit", True, WHITE)
    instructions4 = font_small.render("Press P to Pause", True, WHITE)
    instruction2 = font_small.render("Don't touch the broccoli!", True, GREEN)
    instruction3 = font_small.render("GET THE APPLES!", True, RED)

    # Title near the center at the top of the screen
    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 0))
    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 6))
    screen.blit(title_text, ((SCREEN_WIDTH // 2 - title_text.get_width() // 2)+3, 3))
    screen.blit(title_text, ((SCREEN_WIDTH // 2 - title_text.get_width() // 2)-3, 3))
    screen.blit(title_text, ((SCREEN_WIDTH // 2 - title_text.get_width() // 2)+3, 0))
    screen.blit(title_text, ((SCREEN_WIDTH // 2 - title_text.get_width() // 2)+3, 6))
    screen.blit(title_text, ((SCREEN_WIDTH // 2 - title_text.get_width() // 2)-3, 0))
    screen.blit(title_text, ((SCREEN_WIDTH // 2 - title_text.get_width() // 2)-3, 6))
    screen.blit(outline_text, (SCREEN_WIDTH // 2 - outline_text.get_width() // 2, 3))
    
    # Subtitle is below the title
    screen.blit(subtitle_text, (SCREEN_WIDTH // 2 - subtitle_text.get_width() // 2, 55))
    screen.blit(instructions, (SCREEN_WIDTH - 70 - instructions.get_width() // 2, 10))
    screen.blit(instructions4, (SCREEN_WIDTH - 75 - instructions4.get_width() // 2, 30))
    screen.blit(instruction2, (SCREEN_WIDTH - 140 - instructions.get_width() // 2, 80))
    screen.blit(instruction3, [10, 80])

def display_score(score):
    # Clear only the UI area to prevent overlapping
    pygame.draw.rect(screen, BLACK, (0, 0, SCREEN_WIDTH/4, 20))
    # Draw the updated score
    value = score_font.render("Score: " + str(score), True, WHITE)
    screen.blit(value, [10, 10])

def draw_apple():
    global apples, applex, appley
    applex = random.randint(20, SCREEN_WIDTH-20)
    appley = UI_HEIGHT
    apples.append([applex, appley])
    pygame.draw.rect(screen, (255, 0, 0), (applex, appley, 15, 15), 1)

def draw_broccoli():
    global broccoli, broccolix, broccoliy
    broccolix = random.randint(20, SCREEN_WIDTH-20)
    broccoliy = UI_HEIGHT
    broccoli.append([broccolix, broccoliy])
    pygame.draw.rect(screen, (0, 255, 0), (broccolix, broccoliy, 15, 15), 1)

def draw_background():
    global background, backgroundx, backgroundy
    backgroundx = random.randint(20, SCREEN_WIDTH-20)
    backgroundy = UI_HEIGHT
    backspeed = random.choice([6,5,4,3])
    color = 0
    if backspeed == 6:
        color = (70,70,70)
    elif backspeed == 5:
        color = (60,60,60)
    elif backspeed == 4:
        color = (50,50,50)
    elif backspeed == 3:
        color = (30,30,30)
    background.append([backgroundx, backgroundy, backspeed, color])
    pygame.draw.rect(screen, color, (backgroundx, backgroundy, 10, 10), 1)

def updateA():
    global prev_time, apples
    current_time = pygame.time.get_ticks()
    if current_time - prev_time > 0.1:
        for i in range(len(apples)):
            apples[i][1] += 10  # Move each apple down
            prev_time = current_time  # Update the time
    for i in range(len(apples)):
        pygame.draw.rect(screen, (255,0,0), (apples[i][0], apples[i][1], 15, 15), 1)

def updateB():
    global prev_time2, broccoli
    current_time = pygame.time.get_ticks()
    if current_time - prev_time2 > 0.1:
        for i in range(len(broccoli)):
            broccoli[i][1] += 8  # Move each broccoli down
            prev_time2 = current_time  # Update the time
    for i in range(len(broccoli)):
        pygame.draw.rect(screen, (0,255,0), (broccoli[i][0], broccoli[i][1], 15, 15), 1)

def updateBack():
    global prev_time3, background
    current_time = pygame.time.get_ticks()
    if current_time - prev_time3 > 0.1:
        for i in range(len(background)):
            background[i][1] += background[i][2]  # Move each square down
            prev_time3 = current_time  # Update the time
    for i in range(len(background)):
        pygame.draw.rect(screen, background[i][3], (background[i][0], background[i][1], 10, 10), 1)

def goodcollision(applepos, bucketpos):

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

def badcollision(broccolipos, bucketpos):

    broccolix, broccoliy = broccolipos
    bucket_x, bucket_y= bucketpos
    bucket_x -= 30

    # Check if the apple rectangle overlaps with the bucket rectangle
    if (broccolix + 15 > bucket_x and
        broccolix < bucket_x + 60 and
        broccoliy + 15 >= bucket_y and
        broccoliy <= bucket_y + 20):
        return True
    return False

seconds = pygame.time.get_ticks()/1000

def pause():
    drawn = False
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:  # Quit
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_p:  # Resume
                    paused = False

        if drawn == False:
            screen.fill(BLACK)
            updateA()
            updateB()
            updateBack()
            draw_bucket(screen, mouse_x-30, y-40, width=60, height=20)
            drawn = True
            display_title()
            display_score(score)
            pygame.display.update()
            
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 120))  # slightly transparent
            screen.blit(overlay, (0, 0))

            # Draw pause text
            pause_text = font_over.render("PAUSED", True, WHITE)
            instructions_text = font_small.render("Press P to Resume or Q to Quit", True, WHITE)
            screen.blit(pause_text, (SCREEN_WIDTH // 2 - pause_text.get_width() // 2, SCREEN_HEIGHT // 2 - 70))
            screen.blit(instructions_text, (SCREEN_WIDTH // 2 - instructions_text.get_width() // 2, SCREEN_HEIGHT // 2 + 20))

            # Update the display to show the overlay and text
            pygame.display.update()

        # Control frame rate
        clock.tick(30)


while game_over != True:

    if start == False:
        for i in range(5):
            seconds = pygame.time.get_ticks()/1000
            countdown_text = font_countdown.render(str(5-i), True, WHITE)
            screen.fill(BLACK) # Clear the screen (refresh)
            display_title() # Display the title
            display_score(score)
            draw_ui_border()
            pygame.draw.rect(screen, (0, 0, 255), (x-30, y-40, 60, 20), 1)
            screen.blit(countdown_text, (SCREEN_WIDTH // 2 - countdown_text.get_width() // 2, SCREEN_HEIGHT/2-70))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN: # Is a key pressed?
                    if event.key == pygame.K_q: # Quit
                        pygame.quit()
                        quit()
            time.sleep(1)
        screen.fill(BLACK) # Clear the screen (refresh)
        display_title() # Display the title
        display_score(score)
        draw_ui_border()
        pygame.draw.rect(screen, (0, 0, 255), (x-30, y-40, 60, 20), 1)
        countdown_text = font_countdown.render("GO!", True, WHITE)
        screen.blit(countdown_text, (SCREEN_WIDTH // 2 - countdown_text.get_width() // 2, SCREEN_HEIGHT/2-70))
        pygame.display.update()
        time.sleep(1)
        prev_time = 0
        start = True

    screen.fill(BLACK) # Clear the screen (refresh)
    display_title() # Display the title
    display_score(score)
    draw_ui_border()
    
    seconds = pygame.time.get_ticks()/1000
    
    if seconds - previous_seconds > difficulty:
        draw_apple() # Draw apple
        previous_seconds = seconds
    
    if seconds - previous_seconds2 > 1.5:
        draw_broccoli()
        previous_seconds2 = seconds
    
    if seconds - previous_seconds3 > 0.04:
        draw_background()
        previous_seconds3 = seconds
    
    if seconds - previous_seconds > 0.005:
        prev_mouse_x = mouse_x
        difficulty -= 0.001
    draw_bucket2(screen, prev_mouse_x-30, y-40, width=60, height=20, blue=150)
    
    for i in range(len(apples)):
        if i > len(apples)-1:
            break
        if goodcollision(apples[i], [mouse_x, y-40]):
            apples.remove(apples[i])
            score += 1
    
    for i in range(len(broccoli)):
        if goodcollision(broccoli[i], [mouse_x, y-40]):
            broccoli.remove(broccoli[i])
            game_over = True
            break

    
    updateA() # Update apples
    updateB() # Update broccoli
    updateBack() # Update background
    
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
            if event.key == pygame.K_p: # Pause
                pause()

    for i in range(len(apples)):
        if apples[i][1] > SCREEN_HEIGHT-1:
            game_over = True
    
    for i in range(len(broccoli)):
        if i > len(broccoli)-1:
            break
        if broccoli[i][1] > SCREEN_HEIGHT-1:
            broccoli.remove(broccoli[i])
    
    for i in range(len(background)):
        if i > len(background)-1:
            break
        if background[i][1] > SCREEN_HEIGHT-1:
            background.remove(background[i])

    if game_over == True:
        break
    draw_bucket(screen, mouse_x-30, y-40, width=60, height=20) # Draw the bucket at the correct x and y
    pygame.display.update() # Update the display
    clock.tick(GAME_SPEED)

while True:
    screen.fill(BLACK)
    end_text = font_over.render("GAME OVER", True, RED)
    instructions = font_small.render("Press Q to Close", True, RED)
    screen.blit(end_text, (SCREEN_WIDTH // 2 - end_text.get_width() // 2, SCREEN_HEIGHT/2-70))
    screen.blit(instructions, (SCREEN_WIDTH // 2 - instructions.get_width() // 2, SCREEN_HEIGHT/2+20))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: # Is a key pressed?
            if event.key == pygame.K_q: # Quit
                pygame.quit()
                quit()
pygame.quit()
quit()
