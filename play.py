import pygame
import time

class MusicPlayer:
    def __init__(self, music_file):
        pygame.mixer.init()
        self.music_file = music_file

    def play(self):
        pygame.mixer.music.load(self.music_file)
        pygame.mixer.music.play()
        print("Müzik çalıyor...")

    def stop(self):
        pygame.mixer.music.stop()
        print("Müzik durduruldu.")

if __name__ == "__main__":
    # Müzik dosyasının yolunu buraya ekleyin
    player = MusicPlayer('ses.mp3')

    player.play()
    time.sleep(10)  # 10 saniye müzik çalsın
    player.stop()
