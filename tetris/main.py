import pygame
import random
from constants import TEXTURES, SHAPES, SCREEN_WIDTH, SCREEN_HEIGHT
from tetrimino import Tetrimino
from utils import check_collision, clear_rows, create_grid, create_window
from draw import Draw
from fonts import regular_font, large_font, small_font
from events import any_key_pressed, keydown_handler


# 主游戏函数
def main():
    pygame.init()  # 初始化 pygame
    screen = create_window(SCREEN_WIDTH, SCREEN_HEIGHT, "俄罗斯方块")  # 创建窗口

    clock = pygame.time.Clock()  # 创建时钟对象
    grid = create_grid()  # 创建网格，值为 0 表示该位置为空，否则为方块的纹理
    locked_positions = {}  # 锁定的方块位置
    current_tetrimino = Tetrimino(random.choice(SHAPES), random.choice(TEXTURES))  # 创建当前四连方块
    fall_time = 0  # 距离上次下落的时间
    level_time = 0  # 每隔 5s 加速一次
    score = 0  # 得分

    running = True  # 游戏是否运行
    fall_interval = 0.5  # 初始时，每隔 0.5s 下落一格
    while running:
        grid = create_grid(locked_positions)

        clock.tick()  # 时钟滴答一次
        fall_time += clock.get_rawtime()  # 更新下落时间
        level_time += clock.get_rawtime()  # 更新加速时间

        if level_time / 1000 > 5:  # level_time 已累积 5s
            level_time = 0  # 重置 level_time
            if fall_interval > 0.15:  # 控制最快下落间隔为 0.15s
                fall_interval -= 0.005  # 逐渐减小下落间隔

        if fall_time / 1000 > fall_interval:  # fall_time 已累积 fall_interval 秒
            fall_time = 0  # 重置 fall_time
            current_tetrimino.y += 1  # 方块下移
            if check_collision(grid, current_tetrimino.shape,
                               (current_tetrimino.x, current_tetrimino.y)):  # 当前四连方块与已有方块发生碰撞，或者到达底部
                current_tetrimino.y -= 1  # 方块复位
                for y, row in enumerate(current_tetrimino.shape):
                    for x, cell in enumerate(row):
                        if cell:
                            locked_positions[(current_tetrimino.x + x,
                                              current_tetrimino.y + y)] = current_tetrimino.texture  # 将方块的纹理添加到 locked_positions 中
                current_tetrimino = current_tetrimino.next()  # 生成下一个四连方块
                if check_collision(grid, current_tetrimino.shape,
                                   (current_tetrimino.x, current_tetrimino.y)):  # 下一个四连方块与已有方块发生碰撞
                    running = False  # 游戏结束

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 点击窗口关闭按钮
                running = False  # 退出游戏
            if event.type == pygame.KEYDOWN:  # 按键按下
                # if event.key == pygame.K_q:
                #     print("debug")
                running, current_tetrimino = keydown_handler(event, grid, current_tetrimino, locked_positions)  # 处理按键事件

        grid = create_grid(locked_positions)  # 更新网格
        grid, locked_positions, cleared_rows = clear_rows(grid, locked_positions)  # 清除满行并更新 locked_positions
        if cleared_rows > 0:  # 如果有满行
            score += cleared_rows * 10  # 更新得分

        screen.fill('black')  # 黑色背景
        Draw.draw_grid(screen, grid)  # 绘制网格
        Draw.draw_tetrimino(screen, current_tetrimino)  # 绘制当前四连方块
        score_text = regular_font.render(f"Score: {score}", True, 'white')  # 创建得分文本
        screen.blit(score_text, (10, 10))  # 绘制得分文本

        pygame.display.update()  # 更新屏幕

    # 图形展示最终得分
    screen.fill('black')  # 首先将屏幕全部填充为黑色
    final_score_text = large_font.render(f"Your final score: {score}", True, 'white')  # 创建最终得分文本
    screen.blit(final_score_text,
                (SCREEN_WIDTH / 2 - final_score_text.get_width() / 2, SCREEN_HEIGHT / 2))  # 将最终得分文本绘制到屏幕中央

    tip_text = small_font.render("Press any key to exit", True, 'white')  # 创建提示文本
    screen.blit(tip_text, (SCREEN_WIDTH / 2 - tip_text.get_width() / 2, SCREEN_HEIGHT / 2 + 40))  # 将提示文本绘制到屏幕中央下方

    pygame.display.update()  # 更新屏幕

    # 按任意键退出
    while not any_key_pressed():  # 等待按键按下
        pass
    pygame.quit()  # 退出 pygame


if __name__ == "__main__":
    main()
