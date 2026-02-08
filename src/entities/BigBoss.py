import pygame
import numpy as np
import random

from src.entities.object import object
from src.entities.bossAttack import BossAttack

from config import (
  TIME,
  DIR,
  BOSS_MISSILE_SIZE,
)

class BigBoss(object):
  def __init__(self, BigBoss_size, x_pos, y_pos):
    #! Hardcoded PATH to BigBoss
    super().__init__(r"assets\LargeAlien.png", (0, 0, 1100, 800), BigBoss_size, x_pos, y_pos)
    
    #* temp
    self.original_image = self.image.copy()
    
    #* Properties
    #TODO IDEA: Switch to hitboxes if too hard to hit
    self.start = pygame.time.get_ticks()
    self.time = TIME
    self.dir = DIR
    self.last_attack = 0
    
    self.health = 100
    self.speed = 2
  
  def update(self, world):
    # Clearing the enemy asset from hitbox draw
    self.image = self.original_image.copy()
    
    if pygame.time.get_ticks() - self.start < self.time * 1000:
      self.move(self.dir)
    else:
      self.time = random.randint(0, 4)
      self.dir = random.randint(-1, 1)
      self.start = pygame.time.get_ticks()
      if pygame.time.get_ticks() - self.last_attack >= 1000:
        self._shoot(BOSS_MISSILE_SIZE, self.pos, world)
        self.last_attack = pygame.time.get_ticks()

    self._draw_hitbox()
  
  def move(self, dir):
    self.pos[0] += self.speed * dir
    
    self.rect.center = self.pos

  def _shoot(self, missile_size:tuple, pos, world):
    object_ = BossAttack(missile_size, pos, world.player.pos)
    # object_._toggle_hitbox(self.hitbox_show)
    
    #? Hitbox showing for objects
    world.missiles.add(object_)
    world.all_sprites.add(object_)

