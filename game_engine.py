import random
from config import SHAPES, SHAPES_COLORS, GRID_WIDTH, GRID_HEIGHT

class Tetromino:
    def __init__(self, x, y, shape_idx):
        self.x = x
        self.y = y
        self.shape_idx = shape_idx
        self.color = SHAPES_COLORS[shape_idx]
        self.rotation = 0
        self.shape = SHAPES[shape_idx]

    def get_blocks(self):
        blocks = []
        format = self.shape[self.rotation % len(self.shape)]
        for i, line in enumerate(format):
            row = list(line)
            for j, column in enumerate(row):
                if column == 'O':
                    blocks.append((self.x + j - 2, self.y + i - 4))
        return blocks

class GameEngine:
    def __init__(self):
        self.grid = [[(0,0,0) for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.locked_positions = {}
        self.score = 0
        self.level = 1
        self.lines_cleared = 0
        self.current_piece = self.get_new_piece()
        self.next_piece = self.get_new_piece()
        self.game_over = False

    def get_new_piece(self):
        return Tetromino(5, 0, random.randint(0, len(SHAPES) - 1))

    def valid_space(self, piece):
        accepted_pos = [[(j, i) for j in range(GRID_WIDTH) if self.grid[i][j] == (0,0,0)] for i in range(GRID_HEIGHT)]
        accepted_pos = [j for sub in accepted_pos for j in sub]

        formatted = piece.get_blocks()

        for pos in formatted:
            if pos not in accepted_pos:
                if pos[1] > -1:
                    return False
        return True

    def check_game_over(self):
        for pos in self.locked_positions:
            x, y = pos
            if y < 0:
                return True
        return False

    def clear_rows(self):
        inc = 0
        for i in range(len(self.grid)-1, -1, -1):
            row = self.grid[i]
            if (0,0,0) not in row:
                inc += 1
                ind = i
                for j in range(len(row)):
                    try:
                        del self.locked_positions[(j, i)]
                    except:
                        continue
        
        if inc > 0:
            for key in sorted(list(self.locked_positions.keys()), key=lambda x: x[1])[::-1]:
                x, y = key
                if y < ind:
                    newKey = (x, y + inc)
                    self.locked_positions[newKey] = self.locked_positions.pop(key)
        
        # Scoring: 100 for 1, 300 for 2, 500 for 3, 800 for 4 (Tetris)
        scores = [0, 100, 300, 500, 800]
        self.score += scores[inc] * self.level
        self.lines_cleared += inc
        self.level = (self.lines_cleared // 10) + 1

    def update_grid(self):
        self.grid = [[(0,0,0) for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if (j, i) in self.locked_positions:
                    self.grid[i][j] = self.locked_positions[(j,i)]

    def drop_piece(self):
        self.current_piece.y += 1
        if not self.valid_space(self.current_piece) and self.current_piece.y > 0:
            self.current_piece.y -= 1
            for pos in self.current_piece.get_blocks():
                self.locked_positions[pos] = self.current_piece.color
            self.current_piece = self.next_piece
            self.next_piece = self.get_new_piece()
            self.clear_rows()
            if self.check_game_over():
                self.game_over = True

    def move(self, dx):
        self.current_piece.x += dx
        if not self.valid_space(self.current_piece):
            self.current_piece.x -= dx

    def rotate(self):
        self.current_piece.rotation += 1
        if not self.valid_space(self.current_piece):
            self.current_piece.rotation -= 1

    def hard_drop(self):
        while self.valid_space(self.current_piece):
            self.current_piece.y += 1
        self.current_piece.y -= 1
        for pos in self.current_piece.get_blocks():
            self.locked_positions[pos] = self.current_piece.color
        self.current_piece = self.next_piece
        self.next_piece = self.get_new_piece()
        self.clear_rows()
        if self.check_game_over():
            self.game_over = True

    def get_ghost_piece(self):
        ghost = Tetromino(self.current_piece.x, self.current_piece.y, self.current_piece.shape_idx)
        ghost.rotation = self.current_piece.rotation
        while self.valid_space(ghost):
            ghost.y += 1
        ghost.y -= 1
        return ghost
