# 🧱 Tetris Premium

This project is a **Tetris** game built with Python and the `pygame` library. The game features a clean, modular architecture, separating different functionalities to make development, maintenance, and future scalability much easier.

## 📂 Project Architecture

The game is divided into several modules, each responsible for a specific part of the system:

* **`main.py` (The Entry Point):**
  This is the core file that ties everything together. It houses the main game loop, manages the framerate (FPS), and calculates the falling speed based on the player's current level. It also handles keyboard events and routes them to the game engine.

* **`config.py` (Configuration):**
  The settings file containing all the constants for the game. This includes screen dimensions (`SCREEN_WIDTH`, `SCREEN_HEIGHT`), colors (`BG_COLOR`), and Tetromino shapes/colors. Keeping these separate makes tweaking the game's look and feel effortless.

* **`game_engine.py` (The Logic):**
  Contains the `GameEngine` and `Tetromino` classes. This is the brain of the game, responsible for:
  - Updating the grid and tracking locked pieces.
  - Handling collision detection and boundaries.
  - Rotating and moving pieces.
  - Clearing completed rows and managing the score, levels, and Game Over state.
  - Calculating the position of the Ghost piece.

* **`renderer.py` (Graphics & UI):**
  Contains the `Renderer` class, which is solely responsible for visuals. It takes the current game state from the engine and draws everything on the screen, including the grid, blocks, ghost pieces, UI panels, and subtle glow effects for a polished, premium look.

## 🎮 Controls

* **Right Arrow:** Move piece right
* **Left Arrow:** Move piece left
* **Up Arrow:** Rotate piece
* **Down Arrow:** Soft drop (faster fall)
* **Spacebar:** Hard drop (instant drop)
* **`R` Key:** Restart the game (on Game Over screen)

## 🚀 How to Run

1. Ensure you have Python installed on your system.
2. Install the `pygame` library via your terminal or command prompt:
   ```bash
   pip install pygame
