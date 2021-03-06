import constants
import world_ressources
import pygame

class Sign(pygame.sprite.Sprite):
    def __init__(self,x,y,text,color=''):
        world_ressources.init_sign_ressources()
        super(Sign, self).__init__()
        #We copy the image to blot the text on it.
        name = ''

        if color == 'blue' or color == 'red' or color == 'yellow':
            name = 'sign_' + color
        else:
            name = 'sign'

        self.image = world_ressources.sign_ressources[name][0].copy()
        self.rect = world_ressources.sign_ressources[name][1].copy()
        self.rect.x=x
        self.rect.y=y-self.rect.height+3
        #Blit text
        font = pygame.font.Font("data/coders_crux/coders_crux.ttf", 26)
        t = font.render(text, 1, constants.WHITE)
        self.image.blit(t,(15,35))
