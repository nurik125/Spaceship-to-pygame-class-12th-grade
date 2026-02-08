import pygame
import numpy as np
import argparse

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

pygame.init()

# Game Logic
from src.logic.WORLD import World
from src.logic.InputHandler import InputHandler

# Game Draw
from src.drawing_modules.HUD import HUD
from src.drawing_modules.Background import Background
from src.drawing_modules.Info_text import Info

from config import (
  FPS,
  WINDOW_SIZE,
)

class Agent:
  def __init__(self, test:bool=False, hitbox_show:bool=False):
    self.running = True
    self.test = test
        
    self.fullscreen = False
    if self.fullscreen:
      self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    else:
      self.screen = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)
    
    #* Configurations
    self.fps = FPS
    self.clock = pygame.time.Clock()
    
    #* Modules
    self.background = Background()
    self.input = InputHandler()
    self.hud = HUD()
    self.info_text = Info()
    
    self.restart(hitbox_show)
  
  def restart(self, hitbox_show:bool=False): 
    self.World = World(self.test, self.screen, hitbox_show, self)
    self.World.timer_started = pygame.time.get_ticks()
    self.hud.score = 0

  def run(self, no_clip:bool=False):
    '''
    Main loop of the game
    
    :param self: Description
    :param test: Spawns randomly enemies
    :type test: bool
    '''
      
    # Game Loop
    while self.running:
      self.input.handle_events(self)
      self.World.update(no_clip)
      
      self.background.draw(self.screen)
      self.World.all_sprites.draw(self.screen)
      self.hud.draw(self.screen, self.World.score, self.World.timer_started)
          
      #TODO Add dialog or monolog in the Hud before game or etc
      self.info_text.draw(self.screen)
          
      pygame.display.update()
      self.clock.tick(self.fps)
    pygame.quit()
    
if __name__ == "__main__":
  parser = argparse.ArgumentParser(
                    prog='Alive Space',
                    description='Game',
                    epilog='Text at the bottom of help')
  
  parser.add_argument('-t', '--test', action='store_true')
  parser.add_argument('-hb', '--hitbox', action='store_true')
  parser.add_argument('-nc', '--no-clip', action='store_true')
  args = parser.parse_args()
  
  game = Agent(test=args.test, hitbox_show=args.hitbox)
  game.run(no_clip=args.no_clip)