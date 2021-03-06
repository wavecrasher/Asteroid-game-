import pygame
from Ship import *
from Asteroid import *

pygame.init()
screen_info = pygame.display.Info()
print(screen_info)
size = (width, height) = (screen_info.current_w, screen_info.current_h) 
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (30, 0, 30)

Player = Ship()
obstacle = Asteroid()

def main():
  while True: 
    clock.tick(60)
    Player.update()
    screen.fill(color)
    screen.blit(Player.image, Player.rect)
    screen.blit(obstacle.image, obstacle.rect)
    pygame.display.flip()

if __name__ == '__main__':
  main()   






