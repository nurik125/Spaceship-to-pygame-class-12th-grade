import pygame

from config import (
  WINDOW_SIZE,
  
  MISSILE_SIZE,
)

class InputHandler:
  def handle_events(self, agent):
    #* Event handling
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        agent.running = False
        
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          agent.running = False
        
        # Hitbox on/off
        elif event.key == pygame.K_F5:
          agent.World.hitbox_show = agent.World.hitbox_show ^ True
          for _object in agent.World.all_sprites.sprites():
            _object._toggle_hitbox(agent.World.hitbox_show)
            
        # Fullscreen on/off
        elif event.key == pygame.K_F11:
          agent.fullscreen = not agent.fullscreen
          if agent.fullscreen:
            agent.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
          else:
            agent.screen = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)
          agent.screen_rect = agent.screen.get_rect()
        
        # Player shooting
        elif event.key == pygame.K_SPACE:
          if agent.World.player:
            agent.World._spawn_missile(MISSILE_SIZE, agent.World.player.pos[0], agent.World.player.pos[1], agent.World.player.angle)
        
        elif event.key == pygame.K_r:
          agent.restart(agent.World.hitbox_show)
              
      elif event.type == pygame.MOUSEBUTTONDOWN:
        # for enemy in agent.World.enemies.sprites():
        #   if enemy.rect.collidepoint(event.pos):
        #     print(enemy.alien_type)
        if event.button == 1:
          if agent.World.player:
            agent.World._spawn_missile(MISSILE_SIZE, agent.World.player.pos[0], agent.World.player.pos[1], agent.World.player.angle)
            
      elif event.type == pygame.VIDEORESIZE:
        agent.screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)
