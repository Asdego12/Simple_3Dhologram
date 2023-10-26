import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D Rectangle Faux Hologram")
clock = pygame.time.Clock()

# Function to project 3D coordinates to 2D screen
def project_3d_to_2d(x, y, z):
    fov = 256  # Field of view
    scale = fov / (fov + z)
    screen_x = int(WIDTH / 2 + x * scale)
    screen_y = int(HEIGHT / 2 + y * scale)
    return screen_x, screen_y

# Function to draw a line between two 3D points
def draw_3d_line(start, end):
    start_2d = project_3d_to_2d(*start)
    end_2d = project_3d_to_2d(*end)
    pygame.draw.line(screen, WHITE, start_2d, end_2d)

# Function to draw the 3D faux hologram rectangle
def draw_3d_rectangle():
    vertices = [
        (-50, -50, -50), (-50, 50, -50),
        (50, 50, -50), (50, -50, -50),
        (-50, -50, 50), (-50, 50, 50),
        (50, 50, 50), (50, -50, 50),
    ]

    # Connect the vertices to form a cube
    draw_3d_line(vertices[0], vertices[1])
    draw_3d_line(vertices[1], vertices[2])
    draw_3d_line(vertices[2], vertices[3])
    draw_3d_line(vertices[3], vertices[0])

    draw_3d_line(vertices[4], vertices[5])
    draw_3d_line(vertices[5], vertices[6])
    draw_3d_line(vertices[6], vertices[7])
    draw_3d_line(vertices[7], vertices[4])

    draw_3d_line(vertices[0], vertices[4])
    draw_3d_line(vertices[1], vertices[5])
    draw_3d_line(vertices[2], vertices[6])
    draw_3d_line(vertices[3], vertices[7])

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(BLACK)

    # Draw the 3D faux hologram rectangle
    draw_3d_rectangle()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)