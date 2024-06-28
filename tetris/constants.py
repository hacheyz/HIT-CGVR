import pygame

# 定义网格大小和屏幕大小
GRID_SIZE = 30  # 每个网格长宽为 30 像素
GRID_WIDTH = 10  # 10 列
GRID_HEIGHT = 20  # 20 行
SCREEN_WIDTH = GRID_SIZE * GRID_WIDTH  # 屏幕宽度 = 网格宽度 * 网格列数
SCREEN_HEIGHT = GRID_SIZE * GRID_HEIGHT  # 屏幕高度 = 网格高度 * 网格行数

# 定义方块形状
SHAPES = [
    [[1, 1, 1, 1]],  # I 形
    [[1, 1], [1, 1]],  # O 形
    [[1, 1, 1], [0, 1, 0]],  # T 形
    [[1, 1, 0], [0, 1, 1]],  # S 形
    [[0, 1, 1], [1, 1, 0]],  # Z 形
    [[1, 0, 0], [1, 1, 1]],  # J 形
    [[0, 0, 1], [1, 1, 1]],  # L 形
]

# 加载纹理图像（水彩纹理）
TEXTURES = [
    pygame.image.load('./assets/texture/red.jpg'),  # 红色
    pygame.image.load('./assets/texture/blue.jpg'),  # 蓝色
    pygame.image.load('./assets/texture/green.jpg'),  # 绿色
    pygame.image.load('./assets/texture/yellow.jpg'),  # 黄色
    pygame.image.load('./assets/texture/pink.jpg'),  # 粉色
    pygame.image.load('./assets/texture/orange.jpg'),  # 橙色
    pygame.image.load('./assets/texture/violet.jpg'),  # 紫色
    pygame.image.load('./assets/texture/azure.jpg'),  # 天蓝色
]

# 缩放纹理到网格大小
for i in range(len(TEXTURES)):
    TEXTURES[i] = pygame.transform.scale(TEXTURES[i], (GRID_SIZE, GRID_SIZE))
