import pygame.mixer as mixer


mixer.init()
chomp_sound = mixer.Sound('data/sounds/pacman_chomp.wav')
death_sound = mixer.Sound('data/sounds/pacman_death.wav')
beginning_sound = mixer.Sound('data/sounds/pacman_beginning.wav')
eatbonus_sound = mixer.Sound('data/sounds/pacman_eatfruit.wav')
eatghost_sound = mixer.Sound('data/sounds/pacman_eatghost.wav')
intermission_sound = mixer.Sound('data/sounds/pacman_intermission.wav')
extrapac_sound = mixer.Sound('data/sounds/pacman_extrapac.wav')
