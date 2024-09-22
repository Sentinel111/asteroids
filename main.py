import pygame as pg
import constants as const


def main():
    pg.init()
    print("Starting asteroids!")
    print(f"Screen width: {const.SCREEN_WIDTH}")
    print(f"Screen height: {const.SCREEN_HEIGHT}")
    screen = pg.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))

    while True:
        screen.fill(const.BLACK)
        pg.display.flip()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return


if __name__ == "__main__":
    main()
