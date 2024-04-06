import pygame
import pygame.freetype
import random
import math
import os
# Initialize Pygame
def main_screen():
    current_dir = os.path.abspath(os.getcwd())
    current_dir = current_dir.replace('\\', '/')
    current_dir += '/gui'
    pygame.init()
    WIDTH = 1440
    HEIGHT = 900
    leaves_forground = []
    leaves_background = []
    # Set up the display
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # Load the background image
    background = pygame.image.load(current_dir+"/background2.jpg")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    # Load the firefly image
    firefly_image = pygame.image.load(current_dir + "/leaf.png")

    # Set up the font
    font = pygame.freetype.SysFont("Arial", 30)

    # Set up the heading
    heading = font.render("Renpy AI Novel Generation", (255, 255, 255))

    # Set up the description
    description = font.render("This AI novel generation called Renpy uses advanced algorithms to generate stories based on user input. Simply enter a prompt in the text box below and click the 'Generate' button to see the AI in action!", (255, 255, 255))

    # Set up the prompt box
    prompt_box = pygame.Rect(100, 500, HEIGHT, 50)

    # Set up the generate button
    generate_button = pygame.Rect(720, 500, 80, 50)

    # Load the title image
    title_image = pygame.image.load(current_dir+"/title.png")
    title_rect = title_image.get_rect(center=(WIDTH // 2, HEIGHT // 3))

    # Load the sub-heading image
    sub_heading = pygame.image.load(current_dir+'/sub_heading.png')
    sub_rect = sub_heading.get_rect(center=(WIDTH // 2, HEIGHT // 3 + 100))
    clock = pygame.time.Clock()
    FPS = 120  # Desired FPS
    frames_folder = current_dir+"/loading"  # Path to the folder containing frames
    frame_files = sorted(os.listdir(frames_folder))  # Assuming the frames are named sequentially

    # Load each frame and store them in a list
    frames = [pygame.image.load(os.path.join(frames_folder, file)).convert_alpha() for file in frame_files]

    # Index to keep track of the current frame
    frame_index = 0
    # Set up the fireflies
    fireflies = []
    for i in range(20):
        j = random.randint(1,110)
        if j<70:
            size = 2
        elif j>70 and j<90:
            size = 3
        else:
            size = 1
        firefly = {
            "position": (random.randint(0, WIDTH), random.randint(0, HEIGHT)),
            "direction": (random.randint(-5, 5), random.randint(-5, 5)),
            "size_factor": size,
            "speed": size
        }
        if(size>2):
            leaves_forground.append(firefly)
        else:
            leaves_background.append(firefly)

    # Animation variables for the title
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

            # Handle the generate button being clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and generate_button.collidepoint(event.pos):
                    print("Generate button clicked!")

            # Handle text entry
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Handle the generate button being clicked
                    print("Generate button clicked!")

                if event.key == pygame.K_BACKSPACE:
                    # Handle the backspace key being pressed
                    pass
                else:
                    # Add the key to the text
                    pass

        # Update the fireflies
        for firefly in leaves_background:
            # Update firefly position
            firefly["position"] = ((firefly["position"][0] + 1 * firefly["speed"] * 0.3),
                                (firefly["position"][1] + 1* firefly["speed"] * 0.3))

            # Check if firefly position is out of bounds and adjust
            if firefly["position"][0] < 0:
                firefly["position"] = (WIDTH, firefly["position"][1])
            elif firefly["position"][0] > WIDTH:
                firefly["position"] = (0, firefly["position"][1])
            if firefly["position"][1] < 0:
                firefly["position"] = (firefly["position"][0], HEIGHT)
            elif firefly["position"][1] > HEIGHT:
                firefly["position"] = (firefly["position"][0], 0)
            angle = -math.atan2(firefly["direction"][1], firefly["direction"][0]) * 180 / math.pi

        # Rotate the firefly image
            firefly_image_rotated = pygame.transform.rotate(firefly_image, angle)

        for firefly in leaves_forground:
            # Update firefly position
            firefly["position"] = ((firefly["position"][0] + 1 * firefly["speed"] * 0.3),
                                (firefly["position"][1] + 1* firefly["speed"] * 0.3))

            # Check if firefly position is out of bounds and adjust
            if firefly["position"][0] < 0:
                firefly["position"] = (WIDTH, firefly["position"][1])
            elif firefly["position"][0] > WIDTH:
                firefly["position"] = (0, firefly["position"][1])
            if firefly["position"][1] < 0:
                firefly["position"] = (firefly["position"][0], HEIGHT)
            elif firefly["position"][1] > HEIGHT:
                firefly["position"] = (firefly["position"][0], 0)
            angle = -math.atan2(firefly["direction"][1], firefly["direction"][0]) * 180 / math.pi

        # Rotate the firefly image
            firefly_image_rotated = pygame.transform.rotate(firefly_image, angle)

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

        # Draw the fireflies
        for firefly in leaves_background:
            firefly_image_resized = pygame.transform.scale(firefly_image, (firefly["speed"] * 5, firefly["speed"] * 5))
            screen.blit(firefly_image_resized, (firefly["position"][0], firefly["position"][1]))

        # Draw the title with scaling
        title_width = int(title_image.get_width() * title_scale)
        title_height = int(title_image.get_height() * title_scale)
        title_scaled = pygame.transform.scale(title_image, (title_width, title_height))
        title_rect_scaled = title_scaled.get_rect(center=title_rect.center)
        screen.blit(title_scaled, title_rect_scaled)

        for firefly in leaves_forground:
            firefly_image_resized = pygame.transform.scale(firefly_image, (firefly["speed"] * 5, firefly["speed"] * 5))
            screen.blit(firefly_image_resized, (firefly["position"][0], firefly["position"][1]))
        screen.blit(frames[frame_index], (0, HEIGHT-180))
        # Draw the prompt box
        # pygame.draw.rect(screen, (255, 255, 255), prompt_box)

        # Draw the generate button
        # pygame.draw.rect(screen, (0, 255, 0), generate_button)

        # Update the display
        pygame.display.flip()
        frame_index = (frame_index + 1) % len(frames)

    # Quit Pygame
    pygame.quit()
