class ScreenSize:
    def __init__(self):
        pass

    def width(self):
        return 1440

    def height(self):
        return 900 - 124  # учитывается нижняя панелька


SCREENSIZE = ScreenSize()
# сделали такой вот класс и создали его экземпляр, как константу, чтобы упростить код, когда есть
# необходимость использовать разрешение экрана
