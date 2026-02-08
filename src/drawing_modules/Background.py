import pygame

from config import (
  BACKGROUND_TILE_PATH,
  BUILDINGS_TILE_PATH,
  BUILDINGS_SIZE,
  FLOOR_TILE_PATH,
)

class Background:
  def __init__(self):
    # Loading tiles
    self.surface_tile = pygame.image.load(BACKGROUND_TILE_PATH).convert_alpha()
    self.surface_tile_w, self.surface_tile_h = self.surface_tile.get_size()
    
    self.build_tile = pygame.image.load(BUILDINGS_TILE_PATH).convert_alpha()
    self.build_tile=pygame.transform.scale(self.build_tile, BUILDINGS_SIZE)
    self.build_tile_w, self.build_tile_h = self.build_tile.get_size()
    
    self.floor_tile = pygame.image.load(FLOOR_TILE_PATH).convert_alpha()
    _, self.floor_tile_h = self.floor_tile.get_size()
  
  def draw(self, screen):
    rect = screen.get_rect()
    self.BACKGROUND_TILE_Y = rect.centery
    self.SCREEN_WIDTH = rect.right
    self.SCREEN_HEIGHT = rect.bottom
    self.SCREEN_TOP = rect.top
    self.SCREEN_LEFT = rect.left
    
    for x in range(self.SCREEN_LEFT, self.SCREEN_WIDTH, self.surface_tile_w):
      for y in range(self.SCREEN_TOP, self.SCREEN_HEIGHT, self.surface_tile_h):
        screen.blit(self.surface_tile, (x, y))
      for y in range(self.BACKGROUND_TILE_Y + self.build_tile_h, self.SCREEN_HEIGHT, self.floor_tile_h):
        screen.blit(self.floor_tile, (x, y))
    for x in range(0, self.SCREEN_WIDTH, self.build_tile_w):
      for y in range(self.BACKGROUND_TILE_Y, self.BACKGROUND_TILE_Y + self.build_tile_h, self.build_tile_h):
        screen.blit(self.build_tile, (x, y))