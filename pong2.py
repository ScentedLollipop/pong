import pygame
import random

WIDTH = 800
HEIGHT = 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255,255,255)
BLACK = (0,0,0)
PADDLE_DIMS = (5, 50)
BALL_DIMS = (10, 10)
ball_speed = 2
paddle_speed = 2

def update_game_state(keys_pressed, scores, ball, left_paddle, right_paddle):
    # Update paddles based on player input
    if keys_pressed[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= paddle_speed
    if keys_pressed[pygame.K_s] and left_paddle.bottom < HEIGHT:
        left_paddle.y += paddle_speed
    if keys_pressed[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= paddle_speed
    if keys_pressed[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
        right_paddle.y += paddle_speed

    # Update ball position and handle collisions
    ball.x += bxm
    ball.y += bym
    if ball.bottom >= HEIGHT or ball.top <= 0:
        bym *= -1
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        bxm *= -1

    # Check for scoring
    if ball.x >= WIDTH:
        scores['left'] += 1
        reset_game(scores, ball, left_paddle, right_paddle)
    if ball.x <= 0:
        scores['right'] += 1
        reset_game(scores, ball, left_paddle, right_paddle)

def draw_game(scores, ball, left_paddle, right_paddle):
    WIN.fill(WHITE)
    # Draw scores
    left_score_text = font.render(str(scores['left']), True, BLACK)
    right_score_text = font.render(str(scores['right']), True, BLACK)
    WIN.blit(left_score_text, (WIDTH // 2 - 50, 10))
    WIN.blit(right_score_text, (WIDTH // 2 + 30, 10))

    # Draw game objects
    pygame.draw.rect(WIN, BLACK, left_paddle)
    pygame.draw.rect(WIN, BLACK, right_paddle)
    pygame.draw.rect(WIN, BLACK, ball)
    pygame.display.update()

def reset_game(scores, ball, left_paddle, right_paddle):
    ball.x = WIDTH // 2 - BALL_DIMS[0] // 2
    ball.y = HEIGHT // 2 - BALL_DIMS[1] // 2
    left_paddle.y = HEIGHT // 2 - PADDLE_DIMS[1] // 2
    right_paddle.y = HEIGHT // 2 - PADDLE_DIMS[1] // 2
    global bxm, bym
    bxm = random.choice([-1,1]) * ball_speed
    bym = random.choice([-1,1]) * ball_speed
    pygame.time.delay(1000)

def main():
    scores = {'left': 0, 'right': 0}
    clock = pygame.time.Clock()

    left_paddle = pygame.Rect(50, (HEIGHT // 2 - PADDLE_DIMS[1] // 2), PADDLE_DIMS[0], PADDLE_DIMS[1])
    right_paddle = pygame.Rect(WIDTH - 50, (HEIGHT // 2 - PADDLE_DIMS[1] // 2), PADDLE_DIMS[0], PADDLE_DIMS[1])
    ball = pygame.Rect((WIDTH // 2 - BALL_DIMS[0] // 2), (HEIGHT // 2 - BALL_DIMS[1] // 2), BALL_DIMS[0], BALL_DIMS[1])
    global bxm, bym
    bxm = random.choice([-1,1]) * ball_speed
    bym = random.choice([-1,1]) * ball_speed
    run = True
    font = pygame.font.Font(None, 36)

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        update_game_state(keys_pressed, scores, ball, left_paddle, right_paddle)
        draw_game(scores, ball, left_paddle, right_paddle)
    
    pygame.quit()

if __name__ == "__main__":
    main()
