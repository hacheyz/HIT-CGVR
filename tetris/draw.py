import pygame
from constants import GRID_SIZE, GRID_WIDTH, GRID_HEIGHT


class Draw:
    # 绘制网格
    @staticmethod
    def draw_grid(screen, grid):
        for y in range(GRID_HEIGHT):  # 每一行
            for x in range(GRID_WIDTH):  # 每一列
                rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)  # 网格的矩形区域
                if grid[y][x] == 0:
                    pygame.draw.rect(screen, 'black', rect, 1)  # 参数：窗口，颜色，矩形区域，线宽
                else:
                    screen.blit(grid[y][x], rect)

    # 绘制方块
    @staticmethod
    def draw_tetrimino(screen, tetrimino):
        for y, row in enumerate(tetrimino.shape):  # 形状的每一行
            for x, cell in enumerate(row):  # 形状的每一列
                if cell:  # 如果该位置有方块
                    rect = pygame.Rect((tetrimino.x + x) * GRID_SIZE, (tetrimino.y + y) * GRID_SIZE, GRID_SIZE,
                                       GRID_SIZE)  # 方块的矩形区域
                    screen.blit(tetrimino.texture, rect)  # 绘制方块纹理
