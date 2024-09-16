import pygame

# Initialize Pygame
pygame.init()

# Set up screen (optional, just to keep pygame active)
screen = pygame.display.set_mode((400, 300))

# Dictionary to map key combinations to music files
music_map = {
    (pygame.K_LALT, pygame.K_DELETE, pygame.K_1): "./1.mp3",
    (pygame.K_LALT, pygame.K_DELETE, pygame.K_2): "./2.mp3",
    (pygame.K_LALT, pygame.K_DELETE, pygame.K_3): "./3.mp3",
    (pygame.K_LALT, pygame.K_DELETE, pygame.K_4): "./4.mp3",
    (pygame.K_LALT, pygame.K_DELETE, pygame.K_5): "./5.mp3",
    (pygame.K_LALT, pygame.K_DELETE, pygame.K_6): "./6.mp3"
}

# Function to handle key presses and play the appropriate song
def handle_key_press():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Check if keys are pressed
        keys = pygame.key.get_pressed()

        # Loop through the music map and check for key combinations
        for key_combo, song in music_map.items():
            if all(keys[key] for key in key_combo):
                print(f"Playing {song} for combination {key_combo}")
                pygame.mixer.music.load(song)
                pygame.mixer.music.play()

        pygame.display.update()

# Call the function to handle key presses
handle_key_press()

# Quit pygame when done
pygame.quit()
