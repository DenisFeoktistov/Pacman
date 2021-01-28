class ScreenSize:
    WIDTH, HEIGHT = 1440, 900

    def __init__(self):
        pass

    def width(self):
        return ScreenSize.WIDTH

    def height(self):
        return ScreenSize.HEIGHT - 124  # учитывается нижняя панелька


SCREENSIZE = ScreenSize()
# сделали такой вот класс и создали его экземпляр, как константу, чтобы упростить код, когда есть
# необходимость использовать разрешение экрана
