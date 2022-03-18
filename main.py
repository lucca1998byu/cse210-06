from asyncio import constants
import time
import pygame
import math
import game.constants
from game.scale import ScaleImg
from game.utils import blit_rotate_center, blit_text_center
pygame.font.init()
from game.playercar import PlayerCar
from game.computercar import ComputerCar
from game.abstractcar import AbstractCar
from game.gameinfo import GameInfo










class draw():
    def draw(win, images, player_car, computer_car, game_info):
        for img, pos in images:
            win.blit(img, pos)

        level_text = game.constants.MAIN_FONT.render(
            f"Level {game_info.level}", 1, (255, 255, 255))
        win.blit(level_text, (10, game.constants.HEIGHT - level_text.get_height() - 70))

        time_text = game.constants.MAIN_FONT.render(
            f"Time: {game_info.get_level_time()}s", 1, (255, 255, 255))
        win.blit(time_text, (10, game.constants.HEIGHT - time_text.get_height() - 40))

        vel_text = game.constants.MAIN_FONT.render(
            f"Vel: {round(player_car.vel, 1)}px/s", 1, (255, 255, 255))
        win.blit(vel_text, (10, game.constants.HEIGHT - vel_text.get_height() - 10))

        player_car.draw(win)
        computer_car.draw(win)
        pygame.display.update()


    def move_player(player_car):
        keys = pygame.key.get_pressed()
        moved = False

        if keys[pygame.K_a]:
            player_car.rotate(left=True)
        if keys[pygame.K_d]:
            player_car.rotate(right=True)
        if keys[pygame.K_w]:
            moved = True
            player_car.move_forward()
        if keys[pygame.K_s]:
            moved = True
            player_car.move_backward()

        if not moved:
            player_car.reduce_speed()


    def handle_collision(player_car, computer_car, game_info):
        if player_car.collide(game.constants.TRACK_BORDER_MASK) != None:
            player_car.bounce()

        computer_finish_poi_collide = computer_car.collide(
            game.constants.FINISH_MASK, *game.constants.FINISH_POSITION)
        if computer_finish_poi_collide != None:
            blit_text_center(game.constants.WIN, game.constants.MAIN_FONT, "You lost!")
            pygame.display.update()
            pygame.time.wait(5000)
            game_info.reset()
            player_car.reset()
            computer_car.reset()

        player_finish_poi_collide = player_car.collide(
            game.constants.FINISH_MASK, *game.constants.FINISH_POSITION)
        if player_finish_poi_collide != None:
            if player_finish_poi_collide[1] == 0:
                player_car.bounce()
            else:
                game_info.next_level()
                player_car.reset()
                computer_car.next_level(game_info.level)


    run = True
    clock = pygame.time.Clock()
    images = [(game.constants.GRASS, (0, 0)), (game.constants.TRACK, (0, 0)),
              (game.constants.FINISH, game.constants.FINISH_POSITION), (game.constants.TRACK_BORDER, (0, 0))]
    player_car = PlayerCar(4, 4)
    computer_car = ComputerCar(2, 4, game.constants.PATH)
    game_info = GameInfo()

    while run:
        clock.tick(game.constants.FPS)

        WIDTH, HEIGHT = game.constants.TRACK.get_width(), game.constants.TRACK.get_height()
        WIN = pygame.display.set_mode((WIDTH, HEIGHT))

        draw(game.constants.WIN, images, player_car, computer_car, game_info)

        while not game_info.started:
            blit_text_center(
                game.constants.WIN, game.constants.MAIN_FONT, f"Press any key to start level {game_info.level}!")
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break

                if event.type == pygame.KEYDOWN:
                    game_info.start_level()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        move_player(player_car)
        computer_car.move()

        handle_collision(player_car, computer_car, game_info)

        if game_info.game_finished():
            blit_text_center(game.constants.WIN, game.constants.MAIN_FONT, "You won the game!")
            pygame.time.wait(5000)
            game_info.reset()
            player_car.reset()
            computer_car.reset()


pygame.quit()
