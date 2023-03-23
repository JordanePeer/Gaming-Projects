import pygame, os, time, random

pygame.font.init()
pygame.mixer.init()

# Define the bundaries of the Game
WIDTH, HEIGHT = 1000, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Fly")
FONT = pygame.font.SysFont("comicsans", 30)
FPS = 60

# Define the music and sounds of the Game and define there volume level 
Backround_SOUND = pygame.mixer.Sound(os.path.join('Gaming_Projects', 'Space_Flying', 'Media', 'Backround.mp3'))
BG = pygame.transform.scale(pygame.image.load(
    os.path.join('Gaming_Projects', 'Space_Flying', 'Media', 'bg.jpeg')).convert_alpha(), (WIDTH, HEIGHT))

BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Gaming_Projects', 'Space_Flying', 'Media', 'Fire.mp3'))
BULLET_HIT_SOUND.set_volume(0.05)


# Define the Spaceship's and meteors' designs and characteristics 
HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

SPACESHIP_WIDTH, SPACESHIP_HEIGHT, SPACESHIP_VEL = 50, 45, 5

RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Gaming_Projects', 'Space_Flying', 'Media', 'spaceship_red.png')).convert_alpha()
RED_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 0)

RED_HIT = pygame.USEREVENT + 1


METEOR_WIDTH, METEOR_HEIGHT, METEOR_VEL = 10, 20, 3



# Define the Design and Functionality of the Game
def draw_window(player, elapsed_time, meteors, player_health):
    WIN.blit(BG, (0, 0))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))

    player_health_text = HEALTH_FONT.render(f"Health: {player_health}", 1, "white")
    WIN.blit(player_health_text, (WIDTH - player_health_text.get_width() - 10, 10))

    WIN.blit(RED_SPACESHIP, (player.x, player.y))

    for meteor in meteors:
        pygame.draw.rect(WIN, "white", meteor)

    pygame.display.update()

# Define the movement comands of the Ship
def handle_player_movement(keys_pressed, player):
    if keys_pressed[pygame.K_LEFT]: # LEFT
        player.x -= SPACESHIP_VEL
    if keys_pressed[pygame.K_RIGHT]: # RIGHT
        player.x += SPACESHIP_VEL
    if keys_pressed[pygame.K_UP]: # UP
        player.y -= SPACESHIP_VEL
    if keys_pressed[pygame.K_DOWN]: # DOWN
        player.y += SPACESHIP_VEL

# Define the logic of the Hit by Meteors Event
def handle_meteors(meteors, player):
    for meteor in meteors[:]:
        meteor.y += METEOR_VEL
        if meteor.y > HEIGHT:
            meteors.remove(meteor)
        elif meteor.y + meteor.height >= player.y and meteor.colliderect(player):
            pygame.event.post(pygame.event.Event(RED_HIT))
            meteors.remove(meteor)

# Define the logic and Functionability of the Game
def main():
    clock = pygame.time.Clock()

    Backround_SOUND.play()

    player = pygame.Rect(450, 550, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    player_health = 5

    run = True
    
    start_time = time.time()
    elapsed_time = 0

    meteor_add_increment = 2000
    meteor_count = 0

    meteors = []
    hit = False

    while run:
        meteor_count += clock.tick(FPS)
        elapsed_time = time.time() - meteor_time

        if meteor_count > meteor_add_increment:
            for _ in range(3):
                meteor_x = random.randint(0, WIDTH - METEOR_WIDTH)
                meteor = pygame.Rect(meteor_x, -METEOR_HEIGHT,
                                   METEOR_WIDTH, METEOR_HEIGHT)
                meteors.append(meteor)

            meteor_add_increment = max(200, meteor_add_increment - 50)
            meteor_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                break

            if event.type == RED_HIT:
                player_health -= 1
                BULLET_HIT_SOUND.play()

        if player_health <= 0:
            lost_text = FONT.render("You Lost!", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw_window(player, elapsed_time, meteors, player_health)
        keys_pressed = pygame.key.get_pressed()
        handle_player_movement(keys_pressed, player)
        handle_meteors(meteors, player)


    main()


if __name__ == "__main__":
    main()
