import pygame

WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 1480, 800
FPS = 120

# UI configs
HUD_RECT = pygame.Rect(10, 10, 760, 80) # x, y, width, height
HUD_COLOR = (243, 254, 190) #(180, 255, 180)
BG_COLOR  = (0, 43, 64)

FONT_FAMILY_PATH = r"assets\fonts\PressStart2P\PressStart2P.ttf"
FONT_COLOR = (243, 254, 190)

# HUD Font
HUD_FONT_SIZE = 16

# Info Text
INFO_FONT_SIZE = 42 
INFO_TEXT_Y = 150

SCORE_PADDING = (10, 10)
HIGHSCORE_PADDING = (10, 30)
TIMER_PADDING = (10, 50)

# Background
BACKGROUND_TILE_PATH = r"assets\SpaceInvaders_Background.png"
BUILDINGS_TILE_PATH = r"assets\SpaceInvaders_BackgroundBuildings.png"
BUILDINGS_SIZE = (256, 256)

FLOOR_TILE_PATH = r"assets\SpaceInvaders_BackgroundFloor.png"

# GAME configs
PLAYER_SIZE      = (50, 50)
ENEMY_SIZE       = (50, 50)
BIGBOSS_SIZE     = (300, 210)
MISSILE_SIZE     = (50, 50)
BOSS_MISSILE_SIZE = (200, 200)
TEST_ENEMY_COUNT = 7

# Initial Enemy Config
TIME = 0.75
DIR = -1

# Actions
SCORE_PER_ENEMY = 1000
