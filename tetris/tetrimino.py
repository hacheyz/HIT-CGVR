import random
from constants import GRID_WIDTH, SHAPES, TEXTURES


class Tetrimino:
    def __init__(self, shape, texture):
        self.shape = shape  # 形状: 二维数组
        self.texture = texture  # 纹理: pygame.Surface 对象
        self.x = GRID_WIDTH // 2 - len(shape[0]) // 2  # x 坐标
        self.y = 0  # y 坐标

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]  # 顺时针旋转90度

    def next(self):
        """
        生成下一个方块，形状和纹理随机，不与当前方块相同
        """
        next_shape = random.choice(SHAPES)  # 随机选择一个形状
        while next_shape == self.shape:  # 防止下一个方块与当前方块相同
            next_shape = random.choice(SHAPES)
        next_texture = random.choice(TEXTURES)  # 随机选择一个纹理
        while next_texture == self.texture:  # 防止下一个方块的纹理与当前方块相同
            next_texture = random.choice(TEXTURES)

        return Tetrimino(next_shape, next_texture)  # 返回下一个方块
