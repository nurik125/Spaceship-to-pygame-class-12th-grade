import pygame
import numpy as np

from src.sprite_handle.spritesheet import spritesheet

class object(pygame.sprite.Sprite):
  def __init__(self, SPRITESHEET_PATH, SPRITE_RECT, object_size, x_pos, y_pos):
    super().__init__()
    #* Hitbox
    ss = spritesheet(SPRITESHEET_PATH)
    self.image = ss.image_at(SPRITE_RECT)
    self.image = pygame.transform.scale(self.image, object_size)
    self.rect = self.image.get_rect()
    
    # print(x_pos - object_size[0]//2)
    self.rect.x = x_pos - object_size[0]//2
    self.rect.y = y_pos - object_size[1]//2
    
    #* Object properties
    self._hitbox = False
    self.pos = np.array([x_pos, y_pos], dtype=float)
    self.speed  = 2
    
  def _toggle_hitbox(self, val):
    self._hitbox = val
    
  def _draw_hitbox(self):
    if self._hitbox:
      # recreate mask
      self.mask = pygame.mask.from_surface(self.image)

      if self._hitbox:
        outline = self.mask.outline()
        if len(outline) > 1:
            pygame.draw.polygon(self.image, (255, 0, 0), outline, 1)