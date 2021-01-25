from PyQt5.QtWidgets import QMainWindow

from ScreenSize import SCREENSIZE


# Этот класс создает окно, которое находится ровно посередине экрана (с разрешением 1440x900).
# В документации QT к QMainWindow написано, что "If the position is left uninitialized, then the platform
# window will allow the windowing system to position the window." Поэтому было решено сделать такой класс,
# чтобы уж точно размещать окно ровно. На всякий случай была добавлена переменная centered, изменение
# которой фактически отключает такое центрирование вручную. Она была созданна именно в классе, а не,
# например, в параметрах, чтобы такое действие делалось легко, без поисков по всему коду программы.

# По умолчанию переменная  centered равна false, так как конкретно этот проект не будет использовать только 1 человек
# (как минимум потому, что он командный), а значит лучше понадеяться на windowing system, чем сделать иначе, из-за чего
# кто-то испытает с этим неудобства. Тем не менее, если windowing system не может коректно разместить окно, что мешает
# Вашей игре, достаточно в ScreenSize ввести Ваше разрешение, а значение переменно сделать true.

class CenteredWindow(QMainWindow):
    centered = False

    def __init__(self, width, height):
        super().__init__()
        self.setFixedSize(width, height)
        if CenteredWindow.centered:
            self.move((SCREENSIZE.width() - self.width()) / 2,
                      (SCREENSIZE.height() - self.height()) / 2)
