import sys
import pygame as pg
import constants as const
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pg.init()
    screen = pg.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
    clock = pg.time.Clock()

    updatable = pg.sprite.Group()
    drawable = pg.sprite.Group()
    asteroids = pg.sprite.Group()
    shots = pg.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(const.SCREEN_WIDTH / 2, const.SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        for _ in updatable:
            _.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()

        screen.fill("black")

        for _ in drawable:
            _.draw(screen)

        pg.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
