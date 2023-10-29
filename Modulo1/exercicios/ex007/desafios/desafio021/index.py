#Redproduz audio em mp3

import pygame

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('exercicios/ex007/desafios/desafio021/musica.mp3')
pygame.mixer.music.play()

pygame.event.wait()
