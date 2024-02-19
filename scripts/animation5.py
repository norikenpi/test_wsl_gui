import pygame
import sys
import random

# Pygameの初期化
pygame.init()

# スクリーン設定
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bar and Ball Collision")

# 色定義
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# フレームレート
FPS = 60
clock = pygame.time.Clock()

# ボール設定
ball_pos = [random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 100)]
ball_radius = 20
ball_speed = [random.randint(-5, 5), random.randint(-5, 5)]

# 棒の設定
bar_width, bar_height = 150, 20
bar_pos = [random.randint(100, WIDTH - 100 - bar_width), random.randint(100, HEIGHT - 100 - bar_height)]
bar_speed = [random.randint(-5, 5), random.randint(-5, 5)]

# 衝突検出
def check_collision(ball_pos, ball_radius, bar_pos, bar_width, bar_height):
    if (bar_pos[0] <= ball_pos[0] <= bar_pos[0] + bar_width and
            bar_pos[1] <= ball_pos[1] <= bar_pos[1] + bar_height):
        return True
    return False

# 移動オブジェクトの更新
def update_position(pos, speed, size, screen_size):
    new_pos = [pos[0] + speed[0], pos[1] + speed[1]]
    if new_pos[0] <= 0 or new_pos[0] + size[0] >= screen_size[0]:
        speed[0] = -speed[0]
    if new_pos[1] <= 0 or new_pos[1] + size[1] >= screen_size[1]:
        speed[1] = -speed[1]
    return [pos[0] + speed[0], pos[1] + speed[1]]

# ゲームループ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ボールと棒の位置を更新
    ball_pos = update_position(ball_pos, ball_speed, [ball_radius * 2, ball_radius * 2], [WIDTH, HEIGHT])
    bar_pos = update_position(bar_pos, bar_speed, [bar_width, bar_height], [WIDTH, HEIGHT])

    # 衝突検出と応答
    if check_collision(ball_pos, ball_radius, bar_pos, bar_width, bar_height):
        ball_speed[1] = -ball_speed[1]  # 簡単な反射

    # 画面のクリア
    screen.fill(WHITE)

    # オブジェクトの描画
    pygame.draw.circle(screen, RED, (int(ball_pos[0]), int(ball_pos[1])), ball_radius)
    pygame.draw.rect(screen, BLUE, pygame.Rect(bar_pos[0], bar_pos[1], bar_width, bar_height))

    # 画面の更新
    pygame.display.flip()

    # フレームレートの制御
    clock.tick(FPS)

pygame.quit()
sys.exit()
