import pygame
from config import *

class Renderer:
    def __init__(self, screen):
        self.screen = screen
        try:
            self.font_large = pygame.font.SysFont('Orbitron', 50, bold=True)
            self.font_medium = pygame.font.SysFont('Orbitron', 30)
            self.font_small = pygame.font.SysFont('Orbitron', 20)
        except:
            self.font_large = pygame.font.SysFont('Arial', 50, bold=True)
            self.font_medium = pygame.font.SysFont('Arial', 30)
            self.font_small = pygame.font.SysFont('Arial', 20)

    def draw_block(self, x, y, color, alpha=255, is_ghost=False):
        rect = (BOARD_LEFT + x * BLOCK_SIZE, BOARD_TOP + y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
        
        if is_ghost:
            pygame.draw.rect(self.screen, GHOST_COLOR, rect, 2, border_radius=3)
        else:
            # Main block
            pygame.draw.rect(self.screen, color, rect, border_radius=3)
            # Shine effect
            pygame.draw.rect(self.screen, (255, 255, 255), (rect[0]+2, rect[1]+2, rect[2]-4, rect[3]-4), 1, border_radius=2)
            
            # Glow effect (simulated with a slightly larger semi-transparent rect)
            glow_surface = pygame.Surface((BLOCK_SIZE + 4, BLOCK_SIZE + 4), pygame.SRCALPHA)
            glow_color = (*color, 50)
            pygame.draw.rect(glow_surface, glow_color, (0, 0, BLOCK_SIZE+4, BLOCK_SIZE+4), border_radius=5)
            self.screen.blit(glow_surface, (rect[0]-2, rect[1]-2))

    def draw_grid(self):
        for i in range(GRID_HEIGHT + 1):
            pygame.draw.line(self.screen, GRID_COLOR, 
                             (BOARD_LEFT, BOARD_TOP + i * BLOCK_SIZE), 
                             (BOARD_LEFT + GRID_WIDTH * BLOCK_SIZE, BOARD_TOP + i * BLOCK_SIZE))
        for j in range(GRID_WIDTH + 1):
            pygame.draw.line(self.screen, GRID_COLOR, 
                             (BOARD_LEFT + j * BLOCK_SIZE, BOARD_TOP), 
                             (BOARD_LEFT + j * BLOCK_SIZE, BOARD_TOP + GRID_HEIGHT * BLOCK_SIZE))

    def draw_ui(self, score, level, lines, next_piece):
        # Title
        title_label = self.font_large.render('TETRIS', 1, TEXT_COLOR)
        self.screen.blit(title_label, (SCREEN_WIDTH // 2 - title_label.get_width() // 2, 20))

        # Stats Panel (Glassmorphism look)
        panel_rect = pygame.Rect(BOARD_LEFT + GRID_WIDTH * BLOCK_SIZE + 40, BOARD_TOP, 150, 400)
        pygame.draw.rect(self.screen, (30, 30, 50), panel_rect, border_radius=10)
        pygame.draw.rect(self.screen, (80, 80, 100), panel_rect, 2, border_radius=10)

        labels = [
            f"Score: {score}",
            f"Level: {level}",
            f"Lines: {lines}"
        ]

        for i, text in enumerate(labels):
            label = self.font_small.render(text, 1, TEXT_COLOR)
            self.screen.blit(label, (panel_rect.x + 15, panel_rect.y + 20 + i * 40))

        # Next Piece
        next_label = self.font_small.render('NEXT', 1, TEXT_COLOR)
        self.screen.blit(next_label, (panel_rect.x + 15, panel_rect.y + 160))
        
        format = next_piece.shape[0]
        for i, line in enumerate(format):
            row = list(line)
            for j, column in enumerate(row):
                if column == 'O':
                    pygame.draw.rect(self.screen, next_piece.color, 
                                     (panel_rect.x + 15 + j * 20, panel_rect.y + 190 + i * 20, 18, 18), border_radius=2)

    def draw_game_over(self):
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        self.screen.blit(overlay, (0, 0))

        msg = self.font_large.render('GAME OVER', 1, (255, 50, 50))
        self.screen.blit(msg, (SCREEN_WIDTH // 2 - msg.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
        
        retry = self.font_medium.render('Press R to Restart', 1, TEXT_COLOR)
        self.screen.blit(retry, (SCREEN_WIDTH // 2 - retry.get_width() // 2, SCREEN_HEIGHT // 2 + 20))

    def render(self, engine):
        self.screen.fill(BG_COLOR)
        
        # Draw background board
        pygame.draw.rect(self.screen, (20, 20, 30), (BOARD_LEFT, BOARD_TOP, GRID_WIDTH * BLOCK_SIZE, GRID_HEIGHT * BLOCK_SIZE))
        self.draw_grid()

        # Draw locked pieces
        for pos, color in engine.locked_positions.items():
            if pos[1] >= 0:
                self.draw_block(pos[0], pos[1], color)

        # Draw Ghost Piece
        ghost = engine.get_ghost_piece()
        for pos in ghost.get_blocks():
            if pos[1] >= 0:
                self.draw_block(pos[0], pos[1], ghost.color, alpha=100, is_ghost=True)

        # Draw Current Piece
        for pos in engine.current_piece.get_blocks():
            if pos[1] >= 0:
                self.draw_block(pos[0], pos[1], engine.current_piece.color)

        # Draw UI
        self.draw_ui(engine.score, engine.level, engine.lines_cleared, engine.next_piece)

        if engine.game_over:
            self.draw_game_over()

        pygame.display.update()
