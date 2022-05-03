import pygame
import math
import time
from Character import Player
from Button import Button
from Slider import Slider

pygame.init()
pygame.font.init()

win = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
pygame.display.set_caption(
    "PRADA AND GUCCI DON'T GO TOGETHER, LOUIS AND DIOR I SWEAR IT GO BETTER, /n ~SMILEY"
)

song_sound = [
    pygame.mixer.Sound("audio/Songs/pinocchio_freestyle.wav"),
    pygame.mixer.Sound("audio/Songs/Cant_Take_A_Joke.wav"),
    pygame.mixer.Sound("audio/Songs/Cold Embrace.wav"),
]
font = pygame.font.SysFont("Calibri", 100)
title_font = pygame.font.SysFont("Cambria", 200)
writing = font.render("Possession Change...", False, (255, 255, 0))
title_1 = title_font.render("AA Streetball", False, (50, 120, 50))
title_2 = title_font.render("AA Streetball", False, (193, 66, 63))
title_3 = title_font.render("AA Streetball", False, (13, 20, 211))
p1_game_win_text = font.render("Player 1 Won!", False, (255, 255, 100))
p2_game_win_text = font.render("Player 2 Won!", False, (255, 255, 100))
court = pygame.image.load("images/Court.png")
pascal = pygame.image.load("images/pascal.png")
scottie = pygame.image.load("images/scottie.png")


def main():
    start_x = 0
    start_y = 0
    i = 1
    title_count = 1
    p1 = Player(774, 598, pascal, 6, 6, 50, 100, True, 1)
    p2 = Player(874, 543, scottie, 6, 6, 50, 100, False, 2)
    p1.player_movement = 1
    p2.player_movement = 2
    keys = pygame.key.get_pressed()
    run = True
    in_title = True
    in_team = False
    in_options = False
    in_music = False
    in_how_to_play = False
    in_game = False
    slider_x = 920
    slider_y = 50
    clock = pygame.time.Clock()
    win_score = 5
    title_song = True
    song_image = [
        pygame.image.load("images/Song_Image/Pinocchio Freestyle.png"),
        pygame.image.load("images/Song_Image/drake-scorpion.png"),
        pygame.image.load("images/Song_Image/Cover Art.PNG"),
    ]
    song_number = 0
    skip_timer = 0
    rewind_timer = 0
    while run:
        keys = pygame.key.get_pressed()
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        if in_title:
            if title_song:
                pygame.mixer.Sound.play(song_sound[song_number])
            title_song = False
            keys = pygame.key.get_pressed()
            win.blit(court, (0, 0))
            if start_x == 10 or start_x == -10:
                i *= -1
            title_count += 1
            start_x += i
            start_y += i
            win.blit(pascal, (160 + start_x, 100 + start_y**2))
            win.blit(scottie, (160 + start_x, 850 + start_y**2))
            if title_count <= 20:
                win.blit(title_1, (400, 400))
            elif title_count <= 40:
                win.blit(title_2, (400, 400))
            elif title_count <= 60:
                win.blit(title_3, (400, 400))
            else:
                title_count = 1
            pygame.display.update()
            pygame.display.flip()
            if keys[pygame.K_RETURN]:
                in_options = True
                in_title = False
        elif in_team == True:
            win.blit(pascal, (700, 250))
            win.blit(scottie, (700, 830))
            if keys[pygame.K_RETURN]:
                in_game = True
                in_team = False
            pygame.display.update()
            pygame.display.flip()
        elif in_options == True:

            play_game = Button(728, 385, 1185, 515, False)
            music = Button(728, 558, 1185, 695, False)
            how_to_play = Button(728, 731, 1185, 775, False)

            play_game.on_click()
            music.on_click()
            how_to_play.on_click()
            if play_game.click:
                in_team = True
                in_options = False

            if music.click:
                in_music = True
                in_options = False

            if how_to_play.click:
                in_how_to_play = True
                in_options = False
            win.blit(pygame.image.load("images/Home_Screen.png"), (0, 0))
            play_game.draw(win)
            music.draw(win)

        elif in_music:
            skip_song = Button(1020, 900, 1475, 980, False)
            rewind_song = Button(525, 900, 1035, 980, False)
            go_back = Button(27, 20, 484, 160, False)
            volume_slider = Slider(
                slider_x, slider_y, slider_x + 10, slider_y + 10, False, False
            )
            win.blit(pygame.image.load("images/Music_Screen.png"), (0, 0))
            win.blit(song_image[song_number], (718, 259))

            go_back.on_click()

            volume_slider.on_hover()
            volume_slider.on_click()

            if go_back.click:
                in_options = True
                in_music = False
                go_back.click = False
            volume_slider.draw(win)
            skip_song.on_click()
            rewind_song.on_click()
            skip_song.draw(win)
            skip_timer += 1
            rewind_timer += 1
            if skip_song.click and song_number < len(song_sound) - 1:
                pygame.mixer.Sound.stop(song_sound[song_number])
                song_number += 1
                pygame.mixer.Sound.play(song_sound[song_number])
                skip_song.click = False
            if rewind_song.click and song_number > 0:
                pygame.mixer.Sound.stop(song_sound[song_number])
                song_number -= 1
                pygame.mixer.Sound.play(song_sound[song_number])
                rewind_song.click = False
            song_sound[song_number].set_volume(volume_slider.volume)
            rewind_song.draw(win)
            go_back.draw(win)
            slider_x = volume_slider.start_x
            slider_y = volume_slider.start_y
            pygame.display.update()
            pygame.display.flip()

        elif in_game == True:
            if p1.reset_possession:
                p1.reset_possession = False
                placement_score = p1.score
                p1 = Player(774, 598, pascal, 6, 6, 50, 100, True, 1)
                p1.score = placement_score
                placement_score = p2.score
                p2 = Player(874, 543, scottie, 6, 6, 50, 100, False, 2)
                p2.score = placement_score
            if p2.reset_possession:
                p2.reset_possession = False
                placement_score = p1.score
                p1 = Player(874, 598, pascal, 6, 6, 50, 100, False, 1)
                p1.score = placement_score
                placement_score = p2.score
                p2 = Player(774, 543, scottie, 6, 6, 50, 100, True, 2)
                p2.score = placement_score
                p1.player_movement = 1
                p2.player_movement = 2
            if p1.possession_change:
                p2.reset_possession = False
                placement_score = p1.score
                p1 = Player(874, 598, pascal, 6, 6, 50, 100, False, 1)
                p1.score = placement_score
                placement_score = p2.score
                p2 = Player(774, 543, scottie, 6, 6, 50, 100, True, 2)
                p2.score = placement_score
                win.blit(writing, (200, 500))
                time.sleep(1)
            if p2.possession_change:
                p1.reset_possession = False
                placement_score = p1.score
                p1 = Player(774, 598, pascal, 6, 6, 50, 100, True, 1)
                p1.score = placement_score
                placement_score = p2.score
                p2 = Player(874, 543, scottie, 6, 6, 50, 100, False, 2)
                p2.score = placement_score
                win.blit(writing, (200, 500))
                time.sleep(1)

            if p1.score >= win_score:
                win.blit(court, (0, 0))
                win.blit(pascal, (850, 140))
                win.blit(p1_game_win_text, (850, 100))
                pygame.display.update()
                pygame.display.flip()
                time.sleep(5)
                p1.score = 0
                p2.score = 0
                in_game = False
                in_options = True
            if p2.score >= win_score:
                win.blit(court, (0, 0))
                win.blit(scottie, (850, 140))
                win.blit(p2_game_win_text, (850, 100))
                time.sleep(5)
                p1.score = 0
                p2.score = 0
                in_game = False
                in_options = True
            if p1.score == p2.score:
                if p1.score >= win_score - 1:
                    win_score += 1
                pygame.display.update()
                pygame.display.flip()
            if keys[pygame.K_ESCAPE]:
                in_options = True
            win.blit(court, (0, 0))
            p1.distance = math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p1.y) ** 2)
            p2.distance = p1.distance
            p1.move(win, p2.x, p2.y)
            p2.move(win, p1.x, p1.y)
            p1.draw(win)
            p2.draw(win)
            pygame.display.update()
            pygame.display.flip()


main()
