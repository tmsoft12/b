import pygame
import time

class MusicPlayer:
    def __init__(self, music_file):
        pygame.mixer.init()
        self.music_file = music_file

    def play(self):
        pygame.mixer.music.load(self.music_file)
        pygame.mixer.music.play()
        print("Baslydy...")

    def stop(self):
        pygame.mixer.music.stop()
        print("Durdy.")

if __name__ == "__main__":
    player = MusicPlayer('ses.mp3')

    player.play()
    time.sleep(10) 
    player.stop()
