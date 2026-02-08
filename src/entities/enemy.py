import pygame
import numpy as np
import random

from src.entities.object import object

from config import (
  TIME,
  DIR
)

class enemy(object):
  def __init__(self, enemy_size, x_pos, y_pos):
    #* Drawing Asset
    self.alien_type = random.randint(0, 9)
    #! Hardcoded PATH to Invaders
    super().__init__(r"assets\SpaceInvaders.png", (16 * (self.alien_type//5), 16 * (self.alien_type%5), 16, 16), enemy_size, x_pos, y_pos)
    
    #* temp
    self.original_image = self.image.copy()
    
    #* Properties
    #TODO IDEA: Switch to hitboxes if too hard to hit
    self.start = pygame.time.get_ticks()
    self.time = TIME
    self.dir = DIR
  
  def update(self, player):
    # Clearing the enemy asset from hitbox draw
    self.image = self.original_image.copy()
    
    if pygame.time.get_ticks() - self.start < self.time * 1000:
      self.move(self.dir)
    else:
      self.time = random.randint(0, 4)
      self.dir = random.randint(-1, 1)
      self.start = pygame.time.get_ticks()

    self._draw_hitbox()
  
  def move(self, dir):
    self.pos[0] += self.speed * dir
    
    self.rect.center = self.pos