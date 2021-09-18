"""
Sept 17, 2021 - dasShaker
Watched a video on DaFluffyPotato's channel (https://www.youtube.com/c/DaFluffyPotato) that talked about how he did his
explosions.  Also watched another of his videos talking about solving problems...  So without knowing how he did it, I
tried to replicate the results.  Here is what I came up with.

I'll comment out the sound stuff.  Should work if you add your favorite boom sound effect.
"""
import pygame
from random import randint, choice

pygame.init()
# pygame.mixer.init()
# pygame.mixer.pre_init()

# Load sounds
# boom = pygame.mixer.Sound("boom.wav")
# print(str(pygame.mixer.Sound.get_length(boom)))

# Screen stuff
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Boom")

# Clock stuff
fps = 60
clock = pygame.time.Clock()

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Create color list and add colors to it.
color_list = [WHITE, RED, GREEN, BLUE]


class Boom(pygame.sprite.Sprite):
    """
    I know it's not a sprite, but I wanted to use the self.kill() action because I don't know if removing an object from
    a list will destroy it.  'del booms_list[self]' maybe?  Need to study lists more.
    I could also add in a fiery explosion sprite at the center too...
    """
    def __init__(self, x, y, color, speed=1, b_radius=5, b_thickness=50):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.speed = speed
        self.boom_radius = b_radius
        self.boom_thickness = b_thickness
        self.center = (x, y)

    def update(self):
        """
        Can draw the shockwave around an animation of an explosion.  Kill the object when the explosion is finished
        playing, but have a condition with the boom thickness only drawing the circle while the thickness isn't zero.
        The speed attribute should change the value of the thickness as a float but return an integer.  Or something.
        """
        # Draw the initial circle first using original randomized inputs.
        self.draw()
        self.boom_radius += self.speed
        self.boom_thickness -= 1
        # Kill the object when the thickness is zero.
        if self.boom_thickness < 1:
            self.kill()

    def draw(self):
        pygame.draw.circle(screen, self.color, self.center, self.boom_radius, width=self.boom_thickness)


def make_boom():
    """
    Create a boom using random values.
    x, y: Screen coordinates.
    color: Selects a random color from the color list.
    :return: The boom object to place it in the sprite group.  I know it's not a sprite.
    """
    x = randint(0, SCREEN_WIDTH)
    y = randint(0, SCREEN_HEIGHT)
    color = choice(color_list)
    radius = randint(5, 15)
    speed = randint(5, 10)
    thickness = randint(10, 30)
    return Boom(x, y, color, speed, radius, thickness)


booms_group = pygame.sprite.Group()

run = True
while run:
    for event in pygame.event.get():
        # Close window to exit.
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            # Press escape to exit.
            if event.key == pygame.K_ESCAPE:
                run = False
            # Press space to create a boom and play the sound.  Print the values that created the boom.
            if event.key == pygame.K_SPACE:
                new_boom = make_boom()
                print(f"Thickness: {new_boom.boom_thickness}, Radius: {new_boom.boom_radius}, Speed: {new_boom.speed}")
                booms_group.add(new_boom)
                # boom.play()

    screen.fill(BLACK)
    booms_group.update()
    pygame.display.update()
    clock.tick(fps)

# pygame.mixer.quit()
pygame.quit()
