import pygame
import pygame.freetype
import random
import sys
from Prompt import open_tkinter
from loading import main_screen

# Initialize Pygame
pygame.init()
WIDTH = 1440
HEIGHT = 900

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
color = pygame.Color('chartreuse4')


background = pygame.image.load("bg.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Load the firefly image
firefly_image = pygame.image.load("firefly.png")


# Load the title image
title_image = pygame.image.load("title.png")
title_rect = title_image.get_rect(center=(WIDTH // 2, HEIGHT // 3))

# Load the sub-heading image
sub_heading = pygame.image.load('sub_heading.png')

sub_rect = sub_heading.get_rect(center=(WIDTH // 2, HEIGHT // 3 + 100))

clock = pygame.time.Clock()
FPS = 120  # Desired FPS


fireflies = []
for i in range(20):
    size = random.randint(1, 3)
    firefly = {
        "position": (random.randint(0, WIDTH), random.randint(0, HEIGHT)),
        "direction": (random.randint(-5, 5), random.randint(-5, 5)),
        "size_factor": size,
        "speed": size
    }
    fireflies.append(firefly)

original_image = pygame.image.load("Generate_normal.png").convert_alpha()
hover_image = pygame.image.load("Generate_hover.png").convert_alpha()
original_width, original_height = original_image.get_size()

scaled_width = 200
scaled_height = int(original_height * (scaled_width / original_width))
original_image = pygame.transform.scale(original_image, (scaled_width, scaled_height))
hover_image = pygame.transform.scale(hover_image, (scaled_width, scaled_height))



current_image = original_image





title_scale = 1.0
title_scale_increment = 0.000298
title_scaling_up = True

# Main game loop
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle text entry
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Handle the generate button being clicked
                print("Generate button clicked!")

            elif event.key == pygame.K_BACKSPACE:
                # Handle the backspace key being pressed
                prompt = prompt[:-1]
            else:
                prompt += event.unicode

    # Update the fireflies
    for firefly in fireflies:
        # Update firefly position
        firefly["position"] = ((firefly["position"][0] + firefly["direction"][0] * firefly["speed"] * 0.3),
                               (firefly["position"][1] + firefly["direction"][1] * firefly["speed"] * 0.3))

        # Check if firefly position is out of bounds and adjust
        if firefly["position"][0] < 0:
            firefly["position"] = (WIDTH, firefly["position"][1])
        elif firefly["position"][0] > WIDTH:
            firefly["position"] = (0, firefly["position"][1])
        if firefly["position"][1] < 0:
            firefly["position"] = (firefly["position"][0], HEIGHT)
        elif firefly["position"][1] > HEIGHT:
            firefly["position"] = (firefly["position"][0], 0)

    # Update the title scale gradually
    if title_scaling_up:
        title_scale += title_scale_increment
        if title_scale > 1.1:
            title_scaling_up = False
    else:
        title_scale -= title_scale_increment
        if title_scale < 1.0:
            title_scaling_up = True

    # Draw the background
    screen.blit(background, (0, 0))

    # Draw the sub-heading
    screen.blit(sub_heading, sub_rect)

    # Draw the fireflies
    for firefly in fireflies:
        firefly_image_resized = pygame.transform.scale(firefly_image, (firefly["speed"] * 5, firefly["speed"] * 5))
        screen.blit(firefly_image_resized, (firefly["position"][0], firefly["position"][1]))

    mouse_x, mouse_y = pygame.mouse.get_pos()
    image_rect = current_image.get_rect(center=(WIDTH // 2,(HEIGHT*3) // 4))
    if image_rect.collidepoint(mouse_x, mouse_y):
        current_image = hover_image
    else:
        current_image = original_image

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if image_rect.collidepoint(event.pos):
                open_tkinter()

    # Check if mouse is over the image
    if image_rect.collidepoint(mouse_x, mouse_y):
        current_image = hover_image
    else:
        current_image = original_image

    # Draw the title with scaling
    title_width = int(title_image.get_width() * title_scale)
    title_height = int(title_image.get_height() * title_scale)
    title_scaled = pygame.transform.scale(title_image, (title_width, title_height))
    title_rect_scaled = title_scaled.get_rect(center=title_rect.center)
    screen.blit(title_scaled, title_rect_scaled)
    screen.blit(current_image, (WIDTH // 2 - scaled_width // 2, (HEIGHT * 3)// 4 - scaled_height // 2))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
