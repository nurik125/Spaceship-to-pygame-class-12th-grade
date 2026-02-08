import pygame
import numpy as np

from src.entities.object import object
from src.sprite_handle.spritesheet import spritesheet

class missile(object):
  def __init__(self, player_size, x_pos, y_pos, player_angle):

    #* Properties
    self.angle = player_angle
    self.rad = np.deg2rad(self.angle + 90)

    #! Hardcoded PATH to Invaders
    #! Hardcoded Configuration numbers
    super().__init__(r"assets\SpaceInvaders.png", (32, 0, 16, 16), player_size, x_pos+np.cos(self.rad)*30, y_pos-np.sin(self.rad)*30)
    
    # self.shooting_images = ss.images_at(((32, 0, 16, 16), (32, 16, 16, 16), (32, 32, 16, 16), (32, 48, 16, 16), (32, 64, 16, 16)))
    
    #* temp
    self.original_image = self.image.copy()
    
    #* Properties
    self.speed = 5
    
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
      self.angle,
      1
    )
    
    self.rect = self.image.get_rect(center=self.rect.center)
  