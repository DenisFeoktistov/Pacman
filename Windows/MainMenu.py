from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore

from CenteredWindow import CenteredWindow
import Fonts

WIDTH = 450
HEIGHT = 600


class MainMenu(CenteredWindow):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT)

        self.tune_window()
        self.create_interface()

    def tune_window(self):
        self.setWindowTitle("Main menu")

        self.back_pixmap = QPixmap("other/pictures/backgrounds/purple_background1.jpg")
        self.back_pixmap = self.back_pixmap.scaled(self.width() * 3, self.height(),
                                                   QtCore.Qt.IgnoreAspectRatio,
                                                   QtCore.Qt.SmoothTransformation)
        self.back_label = QLabel(self)
        self.back_label.setFixedSize(self.width(), self.height())
        self.back_label.setPixmap(self.back_pixmap)
        self.back_label.move(0, 0)

        self.pacman = QPixmap("other/pictures/pacman/pacman5.png")
        self.pacman = self.pacman.scaled(170, 170,
                                         QtCore.Qt.IgnoreAspectRatio,
                                         QtCore.Qt.SmoothTransformation)
        self.pacman_label = QLabel(self)
        self.pacman_label.setFixedSize(170, 170)
        self.pacman_label.setPixmap(self.pacman)
        self.pacman_label.move(self.width() * 0.52, self.height() * 0.64)

        self.star = QPixmap("other/pictures/star/star13.png")
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
        self.login_btn = QPushButton("Играть", self)
        self.login_btn.setFont(Fonts.pixel1)
        self.login_btn.setStyleSheet(
            "font-size: 26px; color: rgb(230, 230, 230); border-style: outset; border-width: 3px; "
            "border-radius: 5px; border-color: beige; min-width: 8em; padding: 6px;")
        self.login_btn.adjustSize()
        self.login_btn.move((self.width() - self.login_btn.width()) / 2, self.height() * 0.2)

        self.registration_btn = QPushButton("Правила", self)
        self.registration_btn.setFont(Fonts.pixel1)
        self.registration_btn.setStyleSheet(
            "font-size: 26px; color: rgb(230, 230, 230); border-style: outset; border-width: 3px; "
            "border-radius: 5px; border-color: beige; min-width: 8em; padding: 6px;")
        self.registration_btn.adjustSize()
        self.registration_btn.move((self.width() - self.registration_btn.width()) / 2,
                                   self.height() * 0.3)

        self.records_btn = QPushButton("Рекорды", self)
        self.records_btn.setFont(Fonts.pixel1)
        self.records_btn.setStyleSheet(
            "font-size: 26px; color: rgb(230, 230, 230); border-style: outset; border-width: 3px; "
            "border-radius: 5px; border-color: beige; min-width: 8em; padding: 6px;")
        self.records_btn.adjustSize()
        self.records_btn.move((self.width() - self.records_btn.width()) / 2,
                              self.height() * 0.4)

        self.settings_btn = QPushButton("Настройки", self)
        self.settings_btn.setFont(Fonts.pixel1)
        self.settings_btn.setStyleSheet(
            "font-size: 26px; color: rgb(230, 230, 230); border-style: outset; border-width: 3px; "
            "border-radius: 5px; border-color: beige; min-width: 8em; padding: 6px;")
        self.settings_btn.adjustSize()
        self.settings_btn.move((self.width() - self.settings_btn.width()) / 2,
                               self.height() * 0.5)
