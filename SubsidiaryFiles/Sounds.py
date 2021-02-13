import pygame.mixer as mixer


mixer.init()
mixer.music.load('data/sounds/background_music.mp3')
mixer.music.play(-1)
mixer.music.set_volume(0.2)
chomp_sound = mixer.Sound('data/sounds/pacman_chomp.wav')
chomp_sound.set_volume(0.05)
death_sound = mixer.Sound('data/sounds/pacman_death.wav')
death_sound.set_volume(0.15)
beginning_sound = mixer.Sound('data/sounds/pacman_beginning.wav')
eat_bonus_sound = mixer.Sound('data/sounds/pacman_eatfruit.wav')
eat_ghost_sound = mixer.Sound('data/sounds/pacman_eatghost.wav')
intermission_sound = mixer.Sound('data/sounds/pacman_intermission.wav')
extra_pac_sound = mixer.Sound('data/sounds/pacman_extrapac.wav')
