import pygame
import numpy as np

from src.entities.object import object
from src.sprite_handle.spritesheet import spritesheet

class BossAttack(object):
  def __init__(self, size, boss_pos, player_pos):

    #* Properties
    v = player_pos-boss_pos
    self.angle = -np.angle(complex(v[0], v[1]), deg=True)
    self.rad = np.deg2rad(self.angle)

    #! Hardcoded PATH to Invaders
    #! Hardcoded Configuration numbers
    super().__init__(r"assets\SpaceInvaders.png", (32, 0, 16, 16), size, boss_pos[0]+np.cos(self.rad)*200, boss_pos[1]-np.sin(self.rad)*200)
    
    #* temp
    self.original_image = self.image.copy()
    
    #* Properties
    self.speed = 3
    
  def update(self):
    # Clearing the image from hitbox draw
    self.rotate()
    self.move(1)
    
    self._draw_hitbox()
    
  def move(self, dir):
    self.pos[0] += np.cos(self.rad) * self.speed * dir
    self.pos[1] -= np.sin(self.rad) * self.speed * dir
    
    self.rect.center = self.pos
    
  def rotate(self):
    self.image = pygame.transform.rotozoom(
      self.original_image,
      self.angle+90,
      1
    )
    
    self.rect = self.image.get_rect(center=self.rect.center)
  