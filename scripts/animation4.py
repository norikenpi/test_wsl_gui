import pygame
import sys

# 初期化
pygame.init()

# 画面サイズ
WIDTH, HEIGHT = 800, 600
# 画面のサイズを設定
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# ウィンドウのタイトルを設定
pygame.display.set_caption("Simple Animation with Pygame")

# 色の定義
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 円の初期位置と速度
x, y = WIDTH // 2, HEIGHT // 2
dx, dy = 5, 5

# ゲームループ
running = True
while running:
    # イベントの処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 円の移動
    x += dx
    y += dy

    # 画面を白で塗りつぶし
    screen.fill(WHITE)

    # 円を描画
    pygame.draw.circle(screen, RED, (x, y), 30)

    # 画面を更新
    pygame.display.flip()

    # 一時停止
    pygame.time.delay(30)

    # 画面端の処理
    if x <= 0 or x >= WIDTH:
        dx *= -1
    if y <= 0 or y >= HEIGHT:
        dy *= -1

# Pygameを終了
pygame.quit()
sys.exit()
