import sys
import pygame
import json
import AnimDrawable
import Dragon
from pprint import *

print "Starting game..."

#Loads the configuration

with open('config/config.json') as config_file:
    config = json.load(config_file)

screen_size = width, height = config['screen']['width'], config['screen']['height']
fps = config['fps']

pygame.init()

# Come up with a more automated system for loading images and animations (images/dragon/fly_up001.png ... )
guy_down = pygame.image.load('images/dragon/flyup_001.png')
guy_up = pygame.image.load('images/dragon/flyup_002.png')
guy_flydown = pygame.image.load('images/dragon/flydown_001.png')
guy_fire = pygame.image.load('images/dragon/fire_001.png')
guy_rect = guy_down.get_rect()
objectAnimDrawable = AnimDrawable.AnimDrawable('glide', guy_down.get_rect(), {'glide': ({'frame': guy_down, 'time':10},
                                                                                        {'frame': guy_down, 'time':10}),
                                                                              'fly_up':({'frame': guy_up, 'time': 20},
                                                                                        {'frame': guy_down, 'time': 20}),
                                                                              'fly_down':({'frame': guy_flydown, 'time': 20},
                                                                                          {'frame': guy_flydown, 'time': 20}),
                                                                              'fire':({'frame': guy_fire, 'time': 200},
                                                                                      {'frame':guy_fire, 'time': 200})})
guy_rect = pygame.Rect(0,0,100,60)
dragon = Dragon.Dragon(objectAnimDrawable, guy_rect)
screen = pygame.display.set_mode(screen_size)

while True:
    for event in pygame.event.get():
        dragon.handleEvents(event)
        if event.type == pygame.QUIT: sys.exit()

    screen.fill((0,0,0))
    dragon.update(screen, True)
    pygame.display.flip()
    pygame.time.delay(5)


print "Finished game."
