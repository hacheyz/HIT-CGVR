# 说明文档

## 基于 Pygame 的俄罗斯方块

这是一个基于 Pygame 的俄罗斯方块游戏的简单实现。俄罗斯方块是一款经典的益智游戏，玩家需要控制不同形状的方块（称为“四连方块”）在游戏区域内移动和旋转，以堆叠方块并消除完整的行。游戏的目标是尽可能多地消除行并获得高分。

**项目的目录结构如下：**

- `assets/texture`：包含游戏中使用的所有纹理文件。
- `constants.py`：定义了游戏中使用的常量（如窗口大小、方块形状、纹理列表等）。
- `draw.py`：定义了 `Draw` 类，它有两个静态方法，`draw_grid` 用于绘制游戏区域，`draw_tetrimino` 用于绘制当前的四连方块。
- `events.py`：实现了若干事件处理函数。
- `fonts.py`：定义了游戏中使用的字体对象。
- `main.py`：俄罗斯方块游戏的主入口点。
- `README.md`：项目的说明文档（本文件）。
- `requirements.txt`：项目的依赖项列表。
- `tetrimino.py`：定义了 `Tetrimino` 类，表示游戏中的四连方块。
- `utils.py`：实现了一系列辅助函数。

**项目中实现的一些重要的函数列举如下：**

- `Draw.draw_grid`：绘制游戏区域。
- `Draw.draw_tetrimino`：绘制当前的四连方块。
- `Tetrimino.rotate`：旋转四连方块。
- `Tetrimino.next`：生成下一个四连方块。
- `keydown_handler`：处理键盘按下事件。
- `create_grid`：创建或更新游戏网格。
- `clear_rows`：清除满行。
- `check_collision`：检查四连方块是否与游戏区域的边界或其他方块碰撞。

**原创性声明：**

本项目的所有代码均为自己独立设计和实现，纹理文件来源于 [BEIZ images](https://www.beiz.jp)。