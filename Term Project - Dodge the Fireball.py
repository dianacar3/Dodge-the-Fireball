from turtle import speed
import pygame
import sys
import random

# Initialize Pygame
pygame.init()
font = pygame.font.Font(None, 75)
lives = 3
gameover_font = pygame.font.Font(None, 150)
restart_font = pygame.font.Font(None, 50)
#background = pygame.image.load('D:\CompSci Assignments\BGimage.webp')

# Set up some constants
WIDTH, HEIGHT = 900, 800 

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Dodge the Fireball')

clock = pygame.time.Clock()

class Ball:
    x = WIDTH // 2
    y = HEIGHT // 2
    previousX = WIDTH // 2
    previousY = HEIGHT // 2
    speedX = 0
    speedY = 0

    def draw(self, radius):
        pygame.draw.circle(screen, (168, 74, 50), (self.x, self.y), radius)

    
    def moveRandom(self):
        self.speedX += random.random() * 2 - 1
        self.speedY += random.random() * 2 - 1

        max_speed = 14
        self.speedX = 1.01 * self.speedX
        self.speedY = 1.01 * self.speedY

        #make sure speed is in a threshold
        if not -max_speed <= self.speedX <= max_speed:
            self.speedX = max(min(self.speedX, max_speed), -max_speed)
        if not -max_speed <= self.speedY <= max_speed:
            self.speedY = max(min(self.speedY, max_speed), -max_speed)
            
    
        #bounce off the walls
        if self.x < 0:
            self.speedX = abs(self.speedX * 0.9)
        elif self.x > WIDTH:
            self.speedX = -abs(self.speedX * 0.9)
        if self.y < 0:
            self.speedY = abs(self.speedY * 0.9)
        elif self.y > HEIGHT:
            self.speedY = -abs(self.speedY * 0.9)

    def updatePosition(self):
        self.previousX = self.x
        self.previousY = self.y
        self.x += self.speedX
        self.y += self.speedY

class Fireball:
    balls = []

    def start(self):
        for i in range(30):
            self.balls.append(Ball())

    def draw(self):
        radius = 30
        for ball in self.balls:
            ball.draw(radius)
            radius = radius - 1

    def move(self):
        self.balls[0].moveRandom()
        self.balls[0].updatePosition()
        for i in range(0, len(self.balls) - 1):
            thisBall = self.balls[i]
            theOtherBall = self.balls[i+1]
            theOtherBall.previousX = theOtherBall.x
            theOtherBall.previousY = theOtherBall.y
            theOtherBall.x = thisBall.previousX
            theOtherBall.y = thisBall.previousY

    def reset(self):
        for ball in self.balls:
            ball.x = WIDTH // 2
            ball.y = HEIGHT // 2
            ball.previousX = ball.x
            ball.previousY = ball.y


class Iceblock:
    ICEBLOCK_WIDTH, ICEBLOCK_HEIGHT = 200, 30
    ICEBLOCK_COLOR = (30, 230, 230)
    ICEBLOCK_SPEED = 15

    def __init__(self):
        self.ICEBLOCK = pygame.Surface((self.ICEBLOCK_WIDTH, self.ICEBLOCK_HEIGHT))
        self.ICEBLOCK.fill(self.ICEBLOCK_COLOR)
        self.rect = self.ICEBLOCK.get_rect()
        self.x = WIDTH - self.ICEBLOCK_WIDTH // 2
        self.y = HEIGHT - self.ICEBLOCK_HEIGHT

    def draw(self):
        screen.blit(self.ICEBLOCK, (self.x, self.y))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.ICEBLOCK_SPEED
        if keys[pygame.K_RIGHT] and self.x < WIDTH - self.ICEBLOCK_WIDTH:
            self.x += self.ICEBLOCK_SPEED
        
    def checkCollision(self, fireball):
        if self.x <= fireball.balls[0].x <= self.x + self.ICEBLOCK_WIDTH:
            if self.y <= fireball.balls[0].y <= self.y + self.ICEBLOCK_HEIGHT:
                return True
        return False
    

fireball = Fireball()
fireball.start()
iceblock = Iceblock()
# Game loop
while True:
    pygame.display.flip()
    #screen.blit(background, (-60, -70))
    text = font.render("LIVES: " + str(lives), True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = (750, 50)
    GAMEOVER = gameover_font.render("GAME OVER", True, (186, 4, 10))
    text_gameover = GAMEOVER.get_rect()
    text_gameover.center = (450, 350)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                print("Enter key is pressed")
                
                lives = 3
                fireball.start()

    # Fill the screen with color
    screen.fill((25, 3, 38))

    fireball.draw()
    fireball.move()
    iceblock.draw()
    iceblock.move()
    if iceblock.checkCollision(fireball):
        lives -= 1
        fireball.reset()
    if lives == 0:
        screen.blit(GAMEOVER, text_gameover)
        fireball.reset()
        Restart = restart_font.render("Do you want to play again? (Press enter)", True, (255, 255, 255))
        text_restart = Restart.get_rect()
        text_restart.center = (450, 500)
        screen.blit(Restart, text_restart)
    
    screen.blit(text, text_rect)


    clock.tick(100)
