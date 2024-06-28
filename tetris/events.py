import pygame
from utils import check_collision


# 检查是否有按键按下
def any_key_pressed():
    for event in pygame.event.get():  # 获取所有事件
        if event.type == pygame.KEYDOWN:  # 如果有按键按下
            return True  # 返回 True
    return False  # 否则返回 False


# 游戏中事件处理函数
def keydown_handler(event, grid, current_tetrimino, locked_positions):
    if event.key == pygame.K_LEFT:  # 按下左键
        current_tetrimino.x -= 1  # 方块左移
        if check_collision(grid, current_tetrimino.shape, (current_tetrimino.x, current_tetrimino.y)):  # 如果发生碰撞
            current_tetrimino.x += 1  # 方块复位
    if event.key == pygame.K_RIGHT:  # 按下右键
        current_tetrimino.x += 1  # 方块右移
        if check_collision(grid, current_tetrimino.shape, (current_tetrimino.x, current_tetrimino.y)):  # 如果发生碰撞
            current_tetrimino.x -= 1  # 方块复位
    if event.key == pygame.K_DOWN:  # 按下下键
        current_tetrimino.y += 1  # 方块下移
        if check_collision(grid, current_tetrimino.shape, (current_tetrimino.x, current_tetrimino.y)):  # 如果发生碰撞
            current_tetrimino.y -= 1  # 方块复位
    if event.key == pygame.K_UP:  # 按下上键
        current_tetrimino.rotate()  # 旋转方块
        if check_collision(grid, current_tetrimino.shape, (current_tetrimino.x, current_tetrimino.y)):  # 如果发生碰撞
            for _ in range(3):
                current_tetrimino.rotate()  # 再旋转方块
    if event.key == pygame.K_SPACE:  # 按下空格键
        while not check_collision(grid, current_tetrimino.shape, (current_tetrimino.x, current_tetrimino.y)):  # 如果没有碰撞
            current_tetrimino.y += 1  # 将方块持续下移
        current_tetrimino.y -= 1  # 方块上移
        for y, row in enumerate(current_tetrimino.shape):  # 遍历方块的每一行
            for x, cell in enumerate(row):
                if cell:
                    locked_positions[(current_tetrimino.x + x,
                                      current_tetrimino.y + y)] = current_tetrimino.texture  # 将方块的纹理添加到 locked_positions 中
        current_tetrimino = current_tetrimino.next()  # 生成下一个方块
        if check_collision(grid, current_tetrimino.shape,
                           (current_tetrimino.x, current_tetrimino.y)):  # 如果下一个方块与已有方块发生碰撞
            return False, None  # 返回 False，游戏结束
    return True, current_tetrimino  # 返回 True，游戏继续
