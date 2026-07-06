# Configuration and Constants for Tetris Premium

# Screen Settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
BLOCK_SIZE = 30
GRID_WIDTH = 10
GRID_HEIGHT = 20

# UI Positions
BOARD_LEFT = (SCREEN_WIDTH - (GRID_WIDTH * BLOCK_SIZE)) // 2
BOARD_TOP = (SCREEN_HEIGHT - (GRID_HEIGHT * BLOCK_SIZE)) // 2

# Colors (Neon / Premium Palette)
BG_COLOR = (15, 15, 25)  # Very dark blue/black
GRID_COLOR = (40, 40, 60)
TEXT_COLOR = (240, 240, 255)
GHOST_COLOR = (50, 50, 70)

# Tetromino Colors (Neon)
SHAPES_COLORS = [
    (0, 255, 255),   # Cyan (I)
    (255, 255, 0),   # Yellow (O)
    (160, 32, 240),  # Purple (T)
    (0, 255, 0),     # Green (S)
    (255, 0, 0),     # Red (Z)
    (0, 0, 255),     # Blue (J)
    (255, 165, 0)    # Orange (L)
]

# Tetromino Shapes
SHAPES = [
    [['.....', '.....', '..OO.', '..OO.', '.....'],  # O
     ['.....', '.....', '..OO.', '..OO.', '.....']],
    
    [['.....', '..O..', '..O..', '..O..', '..O..'],  # I
     ['.....', 'OOOO.', '.....', '.....', '.....']],
    
    [['.....', '.....', '..O..', '.OOO.', '.....'],  # T
     ['.....', '..O..', '..OO.', '..O..', '.....'],
     ['.....', '.....', '.OOO.', '..O..', '.....'],
     ['.....', '..O..', '.OO..', '..O..', '.....']],
     
    [['.....', '.....', '..OO.', '.OO..', '.....'],  # S
     ['.....', '..O..', '..OO.', '...O.', '.....']],
     
    [['.....', '.....', '.OO..', '..OO.', '.....'],  # Z
     ['.....', '...O.', '..OO.', '..O..', '.....']],
     
    [['.....', '.....', '.O...', '.OOO.', '.....'],  # J
     ['.....', '..OO.', '..O..', '..O..', '.....'],
     ['.....', '.....', '.OOO.', '...O.', '.....'],
     ['.....', '..O..', '..O..', '.OO..', '.....']],
     
    [['.....', '.....', '...O.', '.OOO.', '.....'],  # L
     ['.....', '..O..', '..O..', '..OO.', '.....'],
     ['.....', '.....', '.OOO.', '.O...', '.....'],
     ['.....', '.OO..', '..O..', '..O..', '.....']]
]

# Note: The shapes list is a nested list. 
# Each shape has multiple rotations.
# 'O' represents a block, '.' represents empty space.
