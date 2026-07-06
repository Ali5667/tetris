import pygame
import sys
from config import SCREEN_WIDTH, SCREEN_HEIGHT, BG_COLOR
from game_engine import GameEngine
from renderer import Renderer

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Tetris Premium')
    clock = pygame.time.Clock()
    
    engine = GameEngine()
    renderer = Renderer(screen)
    
    fall_time = 0
    
    run = True
    while run:
        engine.update_grid()
        
        # Calculate fall speed based on level
        fall_speed = max(0.1, 0.5 - (engine.level - 1) * 0.05)
        fall_time += clock.get_rawtime()
        clock.tick()
        
        # Automatic piece falling
        if fall_time / 1000 >= fall_speed:
            fall_time = 0
            if not engine.game_over:
                engine.drop_piece()
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if engine.game_over:
                    if event.key == pygame.K_r:
                        engine = GameEngine()
                    continue

                if event.key == pygame.K_LEFT:
                    engine.move(-1)
                elif event.key == pygame.K_RIGHT:
                    engine.move(1)
                elif event.key == pygame.K_DOWN:
                    engine.drop_piece()
                elif event.key == pygame.K_UP:
                    engine.rotate()
                elif event.key == pygame.K_SPACE:
                    engine.hard_drop()

        renderer.render(engine)

    pygame.quit()

if __name__ == "__main__":
    main()
