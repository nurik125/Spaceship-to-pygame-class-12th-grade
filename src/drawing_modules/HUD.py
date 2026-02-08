import pygame

from config import (
  HUD_COLOR,
  BG_COLOR,
  
  SCORE_PADDING,
  HIGHSCORE_PADDING, 
  TIMER_PADDING, 

  HUD_RECT,
  HUD_FONT_SIZE,
  FONT_FAMILY_PATH,
  FONT_COLOR
)

class HUD:
  def __init__(self):
    self.font = pygame.font.Font(FONT_FAMILY_PATH, HUD_FONT_SIZE)
    # Properties that not change after restart
    self.highestscore = 0
    
  def draw(self, screen, score_val, timer_started):
    self.highestscore = max(self.highestscore, score_val)
    
    pygame.draw.rect(screen, BG_COLOR, HUD_RECT)
    pygame.draw.rect(screen, HUD_COLOR, HUD_RECT, 3, 5, 5, 5, 5, 5)

    #Initialize texts
    #* Updating the text surfaces
    score = self.font.render(f"SCORE:{score_val}", True, FONT_COLOR)
    score_rect = score.get_rect()
    
    score_rect.topleft = (
      HUD_RECT.left + SCORE_PADDING[0],
      HUD_RECT.top + SCORE_PADDING[1]
    )
    
    highestscore = self.font.render(f"HIGHESTSCORE:{self.highestscore}", True, FONT_COLOR)
    highestscore_rect = highestscore.get_rect()
    
    highestscore_rect.topleft = (
      HUD_RECT.left + HIGHSCORE_PADDING[0],
      HUD_RECT.top + HIGHSCORE_PADDING[1]
    )
    
    ticks_ms = pygame.time.get_ticks()-timer_started
    minutes = ticks_ms // 60000
    seconds = (ticks_ms % 60000) // 1000
    mm_ss_format = f"{minutes:02}:{seconds:02}"
    timer = self.font.render(f"Time: {mm_ss_format}", True, FONT_COLOR)
    timer_rect = timer.get_rect()
    
    timer_rect.topleft = (
      HUD_RECT.left + TIMER_PADDING[0],
      HUD_RECT.top + TIMER_PADDING[1]
    )
    
    screen.blit(score, score_rect)
    screen.blit(highestscore, highestscore_rect)
    screen.blit(timer, timer_rect)