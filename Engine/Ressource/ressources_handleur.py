
import pygame

TRYHARDER_NERD = None

def get_image_test():
    global TRYHARDER_NERD
    if TRYHARDER_NERD is None:
        TRYHARDER_NERD = pygame.image.load("./Engine/Ressource/player.png")
    return TRYHARDER_NERD
