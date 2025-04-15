import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Fullscreen with windowed border (Resizable mode)
screen = pygame.display.set_mode((1000, 1000), pygame.FULLSCREEN | pygame.RESIZABLE)
pygame.display.set_caption("Stone Paper Scissors")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (173, 216, 230)
DARK_BLUE = (25, 25, 112)

# Fonts
font = pygame.font.SysFont("Arial", 36)
big_font = pygame.font.SysFont("Arial", 48)

# Game choices
choices = ["Rock", "Paper", "Scissors"]

# Load images
def load_image(name):
    try:
        return pygame.image.load(name)
    except pygame.error as e:
        print(f"Error loading image {name}: {e}")
        sys.exit()

rock_img = load_image("Stone_Paper_Scissor/images/rock.png")
paper_img = load_image("Stone_Paper_Scissor/images/paper.png")
scissors_img = load_image("Stone_Paper_Scissor/images/scissors.png")

# Resize images for better visibility
rock_img = pygame.transform.scale(rock_img, (150, 150))
paper_img = pygame.transform.scale(paper_img, (150, 150))
scissors_img = pygame.transform.scale(scissors_img, (150, 150))

# Center alignment of images
rock_rect = rock_img.get_rect(center=(screen.get_width() // 4, screen.get_height() // 1.5))
paper_rect = paper_img.get_rect(center=(screen.get_width() // 2, screen.get_height() // 1.5))
scissors_rect = scissors_img.get_rect(center=(3 * screen.get_width() // 4, screen.get_height() // 1.5))

# Game result function
def get_winner(player, computer):
    if player == computer:
        return "It's a Draw!"
    elif (player == "Rock" and computer == "Scissors") or \
         (player == "Paper" and computer == "Rock") or \
         (player == "Scissors" and computer == "Paper"):
        return "You Win!"
    else:
        return "Computer Wins!"

def main():
    clock = pygame.time.Clock()
    result = ""
    player_choice = ""
    computer_choice = ""

    running = True
    while running:
        screen.fill(LIGHT_BLUE)  # Background color
        title = big_font.render("Stone Paper Scissors", True, DARK_BLUE)
        screen.blit(title, (screen.get_width() // 4, 50))

        # Draw images
        screen.blit(rock_img, rock_rect)
        screen.blit(paper_img, paper_rect)
        screen.blit(scissors_img, scissors_rect)

        # Show result
        if result:
            result_text = font.render(result, True, DARK_BLUE)
            screen.blit(result_text, (screen.get_width() // 4, screen.get_height() // 3))
            comp_choice_text = font.render(f"Computer chose: {computer_choice}", True, DARK_BLUE)
            screen.blit(comp_choice_text, (screen.get_width() // 4, screen.get_height() // 3 + 50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                try:
                    if rock_rect.collidepoint(pos):
                        player_choice = "Rock"
                    elif paper_rect.collidepoint(pos):
                        player_choice = "Paper"
                    elif scissors_rect.collidepoint(pos):
                        player_choice = "Scissors"
                    else:
                        raise ValueError("Clicked outside the choices!")

                    computer_choice = random.choice(choices)
                    result = get_winner(player_choice, computer_choice)

                except Exception as e:
                    print(f"Error: {e}")
                    result = "Something went wrong!"

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Unexpected Error: {e}")
        pygame.quit()
        sys.exit()
    