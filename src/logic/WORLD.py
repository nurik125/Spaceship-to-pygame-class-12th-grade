import pygame
import random

from src.entities.player import player
from src.entities.enemy import enemy
from src.entities.BigBoss import BigBoss
from src.entities.missile import missile
from src.entities.bossAttack import BossAttack

from src.drawing_modules.Info_text import Info

from config import (
  PLAYER_SIZE,
  ENEMY_SIZE,
  BIGBOSS_SIZE,
  TEST_ENEMY_COUNT,
  
  SCORE_PER_ENEMY,
)

class World:
  def __init__(self, test, screen, hitbox_show, agent):
    self.agent = agent
    
    # Player's score in this world
    self.timer_started = 0
    self.score = 0
    self.wave = 0
    self.last_kill = 0
    
    self.screen = screen
    self.rect = screen.get_rect()
    self.hitbox_show = hitbox_show
    
    #* Sprites container
    self.all_sprites = pygame.sprite.Group()
    self.enemies = pygame.sprite.Group()
    self.players = pygame.sprite.Group()
    self.missiles = pygame.sprite.Group()
    
    #* Player Initialization(center alignment)
    self._spawn_player(PLAYER_SIZE, self.rect.centerx, self.rect.centery)
    self.player = self.players.sprites()[0]
    
    #* Enemies Initialization
    # Spawn enemies randomly
    if test:
      for _ in range(TEST_ENEMY_COUNT):
        x_pos = random.randint(ENEMY_SIZE[0], self.rect.width - ENEMY_SIZE[0])
        y_pos = random.randint(ENEMY_SIZE[1], self.rect.height - ENEMY_SIZE[1])
        self._spawn_enemy(ENEMY_SIZE, x_pos, y_pos)
    
  def update(self, no_clip):
    if self.player:
      self.info_text.text = f"WAVE {self.wave}"
      
      self.players.update()
      self.missiles.update()
      self.enemies.update(self)
      
      self._handle_missile_collisions()
      self._handle_player_collisions(no_clip)
    else:
      self.info_text.text = "YOU DIED"
    
    # Wrapping the motion in the frame
    for sprite in self.all_sprites.sprites():
      if not self.missiles.has(sprite):
        sprite.pos[0] %= self.rect.width
        sprite.pos[1] %= self.rect.height
      else:
        self._kill_if_out_of_bounds(sprite)
        
    if len(self.enemies.sprites()) == 0:
      self.wave += 1
      enemies = self.wave * 2
      while(enemies >= 6 ):
        x_pos = self.rect.width
        y_pos = random.randint(BIGBOSS_SIZE[1], self.rect.height - BIGBOSS_SIZE[1])
        self._spawn_BigBoss(BIGBOSS_SIZE, x_pos, y_pos)
        
        enemies = enemies - 6
        
      for _ in range(enemies):
        x_pos = self.rect.width
        y_pos = random.randint(ENEMY_SIZE[1], self.rect.height - ENEMY_SIZE[1])
        self._spawn_enemy(ENEMY_SIZE, x_pos, y_pos)
    
  def _handle_missile_collisions(self):
      # Missile collision
      for missile in self.missiles.sprites():        
        for enemy in self.enemies.sprites():
          if pygame.sprite.collide_mask(missile, enemy):
            if BigBoss.__instancecheck__(enemy):
              missile.kill()
              
              #TODO Create greater score calculation
              if enemy.health > 0:
                enemy.health -= 10 / (
                  max(
                    (pygame.time.get_ticks()-self.last_kill)/1000,
                    1
                  ))
                # print(f"Enemy hit!: {enemy.health}")
              else:
                self.score += int(max(
                    5 * SCORE_PER_ENEMY / 
                    (
                        (pygame.time.get_ticks()-self.last_kill) / 3000 + 
                        2 * len(self.missiles.sprites())
                    ), 
                    1
                  ))
                # print("Killed the BigBoss!")
                enemy.kill()
            else:
                missile.kill()
                
                #TODO Create greater score calculation
                self.score += int(max(
                    SCORE_PER_ENEMY / 
                    (
                        (pygame.time.get_ticks()-self.last_kill) / 3000 + 
                        2 * len(self.missiles.sprites())
                    ), 
                    1
                  ))
                # print("Enemy Killed!")
                enemy.kill()
            self.last_kill = pygame.time.get_ticks()
            
        #! Coded for only 1 player
        if self.player:
          if pygame.sprite.collide_mask(self.player, missile):
            # print("You hit ur own missile!")
            self.player.kill()
            self.player = None
    
  def _handle_player_collisions(self, no_clip):
      # Player enemy collision
      if not no_clip:
        #! Coded for only 1 player
        if self.player:
          for enemy in self.enemies.sprites():
            if pygame.sprite.collide_mask(self.player, enemy):
              # print("Enemy attacked you!")
              self.player.kill()
              self.player = None
              break
  
  def _spawn_player(self, player_size:tuple, x_pos:int, y_pos:int):
    '''
    Spawning Player
    
    :param self: Description
    :param obj_category: Description
    :type obj_category: int
    :param player_size: Description
    :type player_size: tuple
    :param x_pos: Description
    :type x_pos: int
    :param y_pos: Description
    :type y_pos: int
    '''
    
    object_ = player(player_size, x_pos, y_pos)
    object_._toggle_hitbox(self.hitbox_show)
    
    #? Hitbox showing for objects
    self.players.add(object_)
    self.all_sprites.add(object_)
  
  def _spawn_enemy(self, enemy_size:tuple, x_pos:int, y_pos:int):
    '''
    Docstring for _spawn_enemy
    
    :param self: Description
    :param enemy_size: Description
    :type enemy_size: tuple
    :param x_pos: Description
    :type x_pos: int
    :param y_pos: Description
    :type y_pos: int
    '''
    
    object_ = enemy(enemy_size, x_pos, y_pos)
    object_._toggle_hitbox(self.hitbox_show)
    
    #? Hitbox showing for objects
    self.enemies.add(object_)
    self.all_sprites.add(object_)

  def _spawn_BigBoss(self, enemy_size:tuple, x_pos:int, y_pos:int):
    '''
    Docstring for _spawn_BigBoss
    
    :param self: Description
    :param enemy_size: Description
    :type enemy_size: tuple
    :param x_pos: Description
    :type x_pos: int
    :param y_pos: Description
    :type y_pos: int
    '''
    
    object_ = BigBoss(enemy_size, x_pos, y_pos)
    object_._toggle_hitbox(self.hitbox_show)
    
    #? Hitbox showing for objects
    self.enemies.add(object_)
    self.all_sprites.add(object_)

  def _spawn_missile(self, missile_size:tuple, x_pos:int, y_pos:int, player_angle):
    '''
    Spawning Player
    
    :param self: Description
    :param obj_category: Description
    :type obj_category: int
    :param player_size: Description
    :type player_size: tuple
    :param x_pos: Description
    :type x_pos: int
    :param y_pos: Description
    :type y_pos: int
    '''
    
    object_ = missile(missile_size, x_pos, y_pos, player_angle)
    object_._toggle_hitbox(self.hitbox_show)
    
    #? Hitbox showing for objects
    self.missiles.add(object_)
    self.all_sprites.add(object_)

  def _kill_if_out_of_bounds(self, sprite):
    if(
      sprite.pos[0] >= self.rect.right or 
      sprite.pos[0] <= self.rect.left or 
      sprite.pos[1] >= self.rect.bottom or 
      sprite.pos[1] <= self.rect.top):
      sprite.kill()
  
  @property
  def info_text(self):
    return self.agent.info_text
  
  @info_text.setter
  def info_text(self):
    self.agent.info_text = self.info_text
  