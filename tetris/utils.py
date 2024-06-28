import pygame
from constants import GRID_WIDTH, GRID_HEIGHT


# 创建窗口
def create_window(width, height, caption):
    pygame.init()
    screen = pygame.display.set_mode((width, height))  # 创建窗口，并设置窗口大小
    pygame.display.set_caption(caption)  # 设置窗口标题
    return screen


# 创建网格
def create_grid(locked_positions=None):
    if locked_positions is None:
        locked_positions = {}
    grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]  # 大小为 20 行 10 列的二维数组
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if (x, y) in locked_positions:  # 如果该位置有方块
                grid[y][x] = locked_positions[(x, y)]  # 将该位置的颜色设置为方块的纹理
            else:
                grid[y][x] = 0
    return grid


# 检查碰撞
def check_collision(grid, shape, offset):
    """
    检查一个 Tetrimino 是否与 grid 中现有的方块发生碰撞
    shape: Tetrimino 的形状
    offset: Tetrimino 的坐标
    """
    off_x, off_y = offset  # offset 是一个 tuple
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            # 对于 Tetrimino 的每一个方块，检查是否越界或与 grid 中的现有方块发生碰撞
            if cell and (
                    x + off_x < 0 or x + off_x >= GRID_WIDTH or y + off_y >= GRID_HEIGHT or grid[y + off_y][x + off_x]):
                return True
    return False


# 清除满行并更新locked_positions
def clear_rows(grid, locked_positions):
    full_rows = []
    for y in range(GRID_HEIGHT):  # 遍历每一行
        if all(grid[y][x] != 0 for x in range(GRID_WIDTH)):  # 如果该行全满
            full_rows.append(y)  # 记录该行

    if not full_rows:  # 如果没有满行
        return grid, locked_positions, 0  # 返回原 grid 和 locked_positions，满行的数量为 0

    for row in full_rows:  # 遍历每一个满行
        for y in range(row, 0, -1):  # 从满行开始，向上遍历
            for x in range(GRID_WIDTH):  # 遍历每一列
                if locked_positions.get((x, y - 1), 0):  # 如果上一行有锁定方块
                    locked_positions[(x, y)] = locked_positions[(x, y - 1)]  # 将上一行的锁定方块下移
                else:
                    if (x, y) in locked_positions:
                        del locked_positions[(x, y)]  # 删除当前行的锁定方块
        for x in range(GRID_WIDTH):  # 遍历最上一行
            if (x, 0) in locked_positions:
                del locked_positions[(x, 0)]  # 删除最上一行的锁定方块

    grid = create_grid(locked_positions)  # 更新 grid
    return grid, locked_positions, len(full_rows)  # 返回更新后的 grid 和 locked_positions，以及满行的数量
