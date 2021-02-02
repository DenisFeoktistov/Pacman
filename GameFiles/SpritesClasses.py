from GameFiles.GeneralSprite import GeneralSprite


class PacmanSprite(GeneralSprite):
    def __init__(self, x, y, sprite_size_x, sprite_size_y, cycle_time):
        frames = (('data/sprites/pacman/pacman_right1.png', 'data/sprites/pacman/pacman_right2.png'),
                  ('data/sprites/pacman/pacman_up1.png', 'data/sprites/pacman/pacman_up2.png'),
                  ('data/sprites/pacman/pacman_left1.png', 'data/sprites/pacman/pacman_left2.png'),
                  ('data/sprites/pacman/pacman_down1.png', 'data/sprites/pacman/pacman_down2.png'))
        default_frame = 'data/sprites/pacman/pacman_default.png'
        super().__init__(x, y, sprite_size_x=sprite_size_x, sprite_size_y=sprite_size_y, cycle_iterations=12,
                         switches_for_cycle=4, cycle_time=cycle_time, default_frame=default_frame, frames=frames)


class RedGhostSprite(GeneralSprite):
    def __init__(self, x, y, sprite_size_x, sprite_size_y, cycle_time):
        frames = (('data/sprites/ghosts/red_right1.png', 'data/sprites/ghosts/red_right2.png'),
                  ('data/sprites/ghosts/red_up1.png', 'data/sprites/ghosts/red_up2.png'),
                  ('data/sprites/ghosts/red_left1.png', 'data/sprites/ghosts/red_left2.png'),
                  ('data/sprites/ghosts/red_down1.png', 'data/sprites/ghosts/red_down2.png'))
        default_frame = 'data/sprites/ghosts/red_up1.png'
        super().__init__(x, y, sprite_size_x=sprite_size_x, sprite_size_y=sprite_size_y, cycle_iterations=12,
                         switches_for_cycle=4, cycle_time=cycle_time, default_frame=default_frame, frames=frames)


class PinkGhostSprite(GeneralSprite):
    def __init__(self, x, y, sprite_size_x, sprite_size_y, cycle_time):
        frames = (('data/sprites/ghosts/pink_right1.png', 'data/sprites/ghosts/pink_right2.png'),
                  ('data/sprites/ghosts/pink_up1.png', 'data/sprites/ghosts/pink_up2.png'),
                  ('data/sprites/ghosts/pink_left1.png', 'data/sprites/ghosts/pink_left2.png'),
                  ('data/sprites/ghosts/pink_down1.png', 'data/sprites/ghosts/pink_down2.png'))
        default_frame = 'data/sprites/ghosts/pink_up1.png'
        super().__init__(x, y, sprite_size_x=sprite_size_x, sprite_size_y=sprite_size_y, cycle_iterations=12,
                         switches_for_cycle=4, cycle_time=cycle_time, default_frame=default_frame, frames=frames)


class BlueGhostSprite(GeneralSprite):
    def __init__(self, x, y, sprite_size_x, sprite_size_y, cycle_time):
        frames = (('data/sprites/ghosts/blue_right1.png', 'data/sprites/ghosts/blue_right2.png'),
                  ('data/sprites/ghosts/blue_up1.png', 'data/sprites/ghosts/blue_up2.png'),
                  ('data/sprites/ghosts/blue_left1.png', 'data/sprites/ghosts/blue_left2.png'),
                  ('data/sprites/ghosts/blue_down1.png', 'data/sprites/ghosts/blue_down2.png'))
        default_frame = 'data/sprites/ghosts/blue_up1.png'
        super().__init__(x, y, sprite_size_x=sprite_size_x, sprite_size_y=sprite_size_y, cycle_iterations=12,
                         switches_for_cycle=4, cycle_time=cycle_time, default_frame=default_frame, frames=frames)


class OrangeGhostSprite(GeneralSprite):
    def __init__(self, x, y, sprite_size_x, sprite_size_y, cycle_time):
        frames = (('data/sprites/ghosts/orange_right1.png', 'data/sprites/ghosts/orange_right2.png'),
                  ('data/sprites/ghosts/orange_up1.png', 'data/sprites/ghosts/orange_up2.png'),
                  ('data/sprites/ghosts/orange_left1.png', 'data/sprites/ghosts/orange_left2.png'),
                  ('data/sprites/ghosts/orange_down1.png', 'data/sprites/ghosts/orange_down2.png'))
        default_frame = 'data/sprites/ghosts/orange_up1.png'
        super().__init__(x, y, sprite_size_x=sprite_size_x, sprite_size_y=sprite_size_y, cycle_iterations=12,
                         switches_for_cycle=4, cycle_time=cycle_time, default_frame=default_frame, frames=frames)
