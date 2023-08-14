import pygame
from pygame.locals import *
import sys
from dataclasses import dataclass


WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
WINDOW_DEPTH = 32

CHARACTER_BODY_SIZE = 10
MUSIC_PATH = "asset/music/maou_bgm_cyber44.mp3"


@dataclass
class Character:
    stride_length: int
    x: int
    y: int
    max_x: int
    max_y: int
    body_size: int

    def __init__(
        self,
        init_x: int,
        init_y: int,
        max_x: int,
        max_y: int,
        body_size: int,
        *,
        stride_length: int = CHARACTER_BODY_SIZE,
    ):
        self.x = init_x
        self.y = init_y
        self.max_x = max_x
        self.max_y = max_y
        self.body_size = body_size
        self.stride_length = stride_length

    def up(self):
        if (self.y - self.body_size) >= 0:
            self.y -= self.stride_length
        else:
            self.y = self.body_size

    def down(self):
        if (self.y + self.body_size) <= self.max_y:
            self.y += self.stride_length
        else:
            self.y = self.max_y - self.body_size

    def left(self):
        if (self.x - self.body_size) >= 0:
            self.x -= self.stride_length
        else:
            self.x = self.body_size

    def right(self):
        if (self.x + self.body_size) <= self.max_x:
            self.x += self.stride_length
        else:
            self.x = self.max_x - self.body_size

    def get_position(self):
        return (self.x, self.y)


def exit():
    pygame.quit()
    sys.exit()


def event_processor():
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                exit()


def keyboard_processor(character: Character):
    pressed_key = pygame.key.get_pressed()

    if pressed_key[K_LEFT]:
        character.left()

    if pressed_key[K_RIGHT]:
        character.right()

    if pressed_key[K_UP]:
        character.up()

    if pressed_key[K_DOWN]:
        character.down()


def initialize_game():
    # NOTE: ゲームの設定初期化
    pygame.init()
    pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, WINDOW_DEPTH)
    pygame.display.set_caption("GAME")

    # NOTE: 音楽
    pygame.mixer.init()
    pygame.mixer.music.load(MUSIC_PATH)
    pygame.mixer.music.play(-1, 0, 10000)


def main():
    initialize_game()

    # NOTE: 初期値
    position = Character(
        WINDOW_WIDTH / 2,
        WINDOW_HEIGHT / 2,
        WINDOW_WIDTH,
        WINDOW_HEIGHT,
        CHARACTER_BODY_SIZE * 2
    )

    # NOTE: 表示エリア取得
    screen = pygame.display.get_surface()

    while (1):
        pygame.display.update()
        pygame.time.wait(30)
        screen.fill((0, 20, 0, 0))

        pygame.draw.circle(
            screen,
            (0, 200, 0),
            position.get_position(),
            CHARACTER_BODY_SIZE
        )

        event_processor()

        keyboard_processor(position)


if __name__ == "__main__":
    main()
