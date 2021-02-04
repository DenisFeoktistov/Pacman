from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore

from SubsidiaryFiles.CenteredWindow import CenteredWindow
import SubsidiaryFiles.Fonts as Fonts


class PauseMenu(CenteredWindow):
    WIDTH, HEIGHT = 450, 600

    def __init__(self, main_interface_class):
        super().__init__(PauseMenu.WIDTH, PauseMenu.HEIGHT)

        self.main_interface_class = main_interface_class
        self.tune_window()
        self.create_interface()

    def tune_window(self):
        self.setWindowTitle("MainClasses menu")

        self.back_pixmap = QPixmap("data/pictures/backgrounds/purple_background1.jpg")
        self.back_pixmap = self.back_pixmap.scaled(self.width() * 3, self.height(),
                                                   QtCore.Qt.IgnoreAspectRatio,
                                                   QtCore.Qt.SmoothTransformation)
        self.back_label = QLabel(self)
        self.back_label.setFixedSize(self.width(), self.height())
        self.back_label.setPixmap(self.back_pixmap)
        self.back_label.move(0, 0)

        self.pacman = QPixmap("data/pictures/pacman/pacman5.png")
        self.pacman = self.pacman.scaled(170, 170,
                                         QtCore.Qt.IgnoreAspectRatio,
                                         QtCore.Qt.SmoothTransformation)
        self.pacman_label = QLabel(self)
        self.pacman_label.setFixedSize(170, 170)
        self.pacman_label.setPixmap(self.pacman)
        self.pacman_label.move(self.width() * 0.52, self.height() * 0.64)

        self.star = QPixmap("data/pictures/star/star13.png")
        self.star = self.star.scaled(70, 70,
                                     QtCore.Qt.IgnoreAspectRatio,
                                     QtCore.Qt.SmoothTransformation)
        self.star_label = QLabel(self)
        self.star_label.setFixedSize(70, 70)
        self.star_label.setPixmap(self.star)
        self.star_label.move(self.width() * 0.12, self.height() * 0.64)

        self.main_label = QLabel("PACMAN", self)
        self.main_label.setFont(Fonts.pixel3)
        self.main_label.resize(self.width(), 100)
        self.main_label.setAlignment(QtCore.Qt.AlignCenter)
        self.main_label.setStyleSheet("font-size: 95px; color: rgb(255, 255, 0);")
        self.main_label.move(0, self.height() * 0.03)

    def create_interface(self):
        self.continue_btn = QPushButton("Продолжить игру", self)
        self.continue_btn.setFont(Fonts.pixel1)
        self.continue_btn.setStyleSheet(
            "font-size: 26px; color: rgb(230, 230, 230); border-style: outset; border-width: 3px; "
            "border-radius: 5px; border-color: beige; min-width: 8em; padding: 6px;")
        self.continue_btn.adjustSize()
        self.continue_btn.move((self.width() - self.continue_btn.width()) / 2, self.height() * 0.2)

        self.return_btn = QPushButton("Вернуться в главное меню", self)
        self.return_btn.setFont(Fonts.pixel1)
        self.return_btn.setStyleSheet(
            "font-size: 26px; color: rgb(230, 230, 230); border-style: outset; border-width: 3px; "
            "border-radius: 5px; border-color: beige; min-width: 8em; padding: 6px;")
        self.return_btn.adjustSize()
        self.return_btn.move((self.width() - self.return_btn.width()) / 2,
                            self.height() * 0.3)

    def set_responder(self, responder):
        self.responder = responder

        self.connect_buttons()

    def connect_buttons(self):
        self.continue_btn.clicked.connect(self.responder.continue_play)
        self.return_btn.clicked.connect(self.responder.return_to_menu)

    def show(self):
        print(8)
        super().show()

    def close(self):
        print(7)
        super().close()
        print(7)
