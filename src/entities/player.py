import pygame
import numpy as np

from src.entities.object import object
# from src.sprite_handle.spritesheetAnim import SpriteStripAnim
# from config import FPS

class player(object):
  def __init__(self, player_size, x_pos, y_pos):
    #! Hardcoded PATH to Invaders
    super().__init__(r"assets\SpaceInvaders.png", (64, 0, 16, 16), player_size, x_pos, y_pos)
    
    #* temp
    self.original_image = self.image.copy()
    
    #* Properties
    self._hitbox = False
    self.angle = 0
    self.speed = 4

    # self.frames = FPS / 1
    # self.strips = [
    #   SpriteStripAnim(r"assets\SpaceInvaders.png", (32, 0, 16, 16), 1, loop=True, frames=self.frames)
    # ]
    
    # self.n = 0
    # self.strips[self.n].iter()
    # self.rocket_image = self.strips[self.n].next()
  
  def update(self):
    # Clearing the image from hitbox draw
    self.rotate(0)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[pygame.K_UP]:
      self.move(0.5)

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
      self.rotate(2)
      self.move(.1)
      
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
      self.move(-0.5)
      
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
      self.rotate(-2)
      self.move(.1)
      
    self._draw_hitbox()
      
  def rotate(self, delta):
    self.angle += delta
    # Keep angle within 0-360 degrees
    self.angle %= 360
    
    self.image = pygame.transform.rotozoom(
      self.original_image,
      self.angle,
      1
    )
    
    self.rect = self.image.get_rect(center=self.rect.center)
    
  def move(self, dir):
    #TODO Animation of rocket launch
    # self.image.blit(self.rocket_image,)
    
    rad = np.deg2rad(self.angle + 90)
    self.pos[0] += np.cos(rad) * self.speed * dir
    self.pos[1] -= np.sin(rad) * self.speed * dir
    
    self.rect.center = self.pos