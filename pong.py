import pygame

import random

WIDTH = 800
HEIGHT = 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255,255,255)
BLACK = (0,0,0)
PADDLE_WIDTH = 5
PADDLE_HEIGHT = 50
BALL_WIDTH = 10
BALL_HEIGHT = 10
ball_speed = 2
paddle_speed = 2
LEFT_SCORE = pygame.USEREVENT + 1
RIGHT_SCORE = pygame.USEREVENT + 2



def win_draw(left, right, ball):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, left)
    pygame.draw.rect(WIN, BLACK, right)
    pygame.draw.rect(WIN, BLACK, ball)
    pygame.display.update()

def paddle_movement(keys_pressed, left, right):
    if keys_pressed[pygame.K_w] and left.top > 0:
        left.y -= paddle_speed
    if keys_pressed[pygame.K_s] and left.bottom < HEIGHT:
        left.y += paddle_speed
    if keys_pressed[pygame.K_UP] and right.top > 0:
        right.y -= paddle_speed
    if keys_pressed[pygame.K_DOWN] and right.bottom < HEIGHT:
        right.y += paddle_speed


def scoring(ball):
    if ball.x >= WIDTH:
        pygame.event.post(pygame.event.Event(LEFT_SCORE))
        pygame.time.delay(1000)
        main()
    if ball.x <= 0:
        pygame.event.post(pygame.event.Event(RIGHT_SCORE))
        pygame.time.delay(1000)
        main()

        
def main():
    clock = pygame.time.Clock()

    left = pygame.Rect(50, (HEIGHT/2 - PADDLE_HEIGHT/2), PADDLE_WIDTH, PADDLE_HEIGHT )
    right = pygame.Rect(WIDTH - 50, (HEIGHT/2 - PADDLE_HEIGHT/2), PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = pygame.Rect((WIDTH/2 - BALL_WIDTH/2), (HEIGHT/2 - BALL_HEIGHT/2), BALL_WIDTH, BALL_HEIGHT)
    bxm = random.choice([-1,1]) * ball_speed
    bym = random.choice([-1,1]) * ball_speed
    run = True

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        #ball movement
        ball.x += bxm
        ball.y += bym
        if ball.bottom >= HEIGHT or ball.top <= 0:
            bym *= -1
        if ball.colliderect(left) or ball.colliderect(right):
            bxm *= -1

        win_draw(left, right, ball)
        keys_pressed = pygame.key.get_pressed()
        paddle_movement(keys_pressed, left, right)
        scoring(ball)
    
    pygame.quit()

if __name__ == "__main__":
    main()
