# Faça um programa que toque uma música com "PYGAME"

import pygame
pygame.init()
pygame.mixer.music.load(r'D:\cursos\PYTHON\Python - Curso em Video - Copia\1_fundamentos\music.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()