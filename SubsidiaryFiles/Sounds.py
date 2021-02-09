import pygame.mixer as mixer


mixer.init()
chomp_sound = mixer.Sound('data/sounds/pacman_chomp.wav')
death_sound = mixer.Sound('data/sounds/pacman_death.wav')
beginning_sound = mixer.Sound('data/sounds/pacman_beginning.wav')
eat_bonus_sound = mixer.Sound('data/sounds/pacman_eatfruit.wav')
eat_ghost_sound = mixer.Sound('data/sounds/pacman_eatghost.wav')
intermission_sound = mixer.Sound('data/sounds/pacman_intermission.wav')
extra_pac_sound = mixer.Sound('data/sounds/pacman_extrapac.wav')
