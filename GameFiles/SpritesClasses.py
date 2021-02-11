from GameFiles.GeneralSprite import GeneralSprite


class PacmanSprite(GeneralSprite):
    SWITCHES_FOR_CYCLE = 3
    CYCLE_ITERATIONS = 12

    def __init__(self, x, y, sprite_size_x, sprite_size_y, cycle_time):
        frames = (('data/sprites/pacman/move/right/1.png', 'data/sprites/pacman/move/right/2.png'),
                  ('data/sprites/pacman/move/up/1.png', 'data/sprites/pacman/move/up/2.png'),
                  ('data/sprites/pacman/move/left/1.png', 'data/sprites/pacman/move/left/2.png'),
                  ('data/sprites/pacman/move/down/1.png', 'data/sprites/pacman/move/down/2.png'))
        default_frame = 'data/sprites/pacman/move/default/1.png'
        super().__init__(x, y, sprite_size_x=sprite_size_x, sprite_size_y=sprite_size_y,
                         cycle_iterations=PacmanSprite.CYCLE_ITERATIONS,
                         switches_for_cycle=PacmanSprite.SWITCHES_FOR_CYCLE, cycle_time=cycle_time,
                         default_frame=default_frame, frames=frames)


class GhostSprite(GeneralSprite):
    SWITCHES_FOR_CYCLE = 4
    CYCLE_ITERATIONS = 12

    def __init__(self, x, y, sprite_size_x, sprite_size_y, cycle_time, color="red"):
        if color not in ["red", "pink", "blue", "orange"]:
            color = "red"
        frames = ((f'data/sprites/ghosts/{color}/right/{color}_right1.png',
                   f'data/sprites/ghosts/{color}/right/{color}_right2.png'),
                  (f'data/sprites/ghosts/{color}/up/{color}_up1.png',
                   f'data/sprites/ghosts/{color}/up/{color}_up2.png'),
                  (f'data/sprites/ghosts/{color}/left/{color}_left1.png',
                   f'data/sprites/ghosts/{color}/left/{color}_left2.png'),
                  (f'data/sprites/ghosts/{color}/down/{color}_down1.png',
                   f'data/sprites/ghosts/{color}/down/{color}_down2.png'))
        super().__init__(x, y, sprite_size_x=sprite_size_x, sprite_size_y=sprite_size_y,
                         cycle_iterations=GhostSprite.CYCLE_ITERATIONS,
                         switches_for_cycle=GhostSprite.SWITCHES_FOR_CYCLE, cycle_time=cycle_time,
                         default_frame=None, frames=frames)
