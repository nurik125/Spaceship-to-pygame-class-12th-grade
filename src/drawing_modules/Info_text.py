import pygame

from config import (
  INFO_TEXT_Y,
  
  FONT_FAMILY_PATH,
  INFO_FONT_SIZE,
  FONT_COLOR,
)

class Info:
  def __init__(self):
    self.font = pygame.font.Font(FONT_FAMILY_PATH, INFO_FONT_SIZE)
    self.text = ""
    
  def draw(self, screen):
    info_text = self.font.render(self.text, False, FONT_COLOR)
    info_text_rect = info_text.get_rect()
    info_text_rect.topleft = (
      screen.get_rect().centerx-info_text_rect.centerx, INFO_TEXT_Y
    )
    screen.blit(info_text, info_text_rect)
    