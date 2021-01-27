from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore

from SubsidiaryFiles.CenteredWindow import CenteredWindow
import SubsidiaryFiles.Fonts as Fonts

WIDTH = 450
HEIGHT = 600


class MainMenu(CenteredWindow):
    def __init__(self, main_interface_class):
        super().__init__(WIDTH, HEIGHT)

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
        self.play_btn = QPushButton("Играть", self)
        self.play_btn.setFont(Fonts.pixel1)
        self.play_btn.setStyleSheet(
            "font-size: 26px; color: rgb(230, 230, 230); border-style: outset; border-width: 3px; "
            "border-radius: 5px; border-color: beige; min-width: 8em; padding: 6px;")
        self.play_btn.adjustSize()
        self.play_btn.move((self.width() - self.play_btn.width()) / 2, self.height() * 0.2)

        self.rules_btn = QPushButton("Правила", self)
        self.rules_btn.setFont(Fonts.pixel1)
        self.rules_btn.setStyleSheet(
            "font-size: 26px; color: rgb(230, 230, 230); border-style: outset; border-width: 3px; "
            "border-radius: 5px; border-color: beige; min-width: 8em; padding: 6px;")
        self.rules_btn.adjustSize()
        self.rules_btn.move((self.width() - self.rules_btn.width()) / 2,
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

    def set_responder(self, responder):
        self.responder = responder

        self.connect_buttons()

    def connect_buttons(self):
        self.play_btn.clicked.connect(self.responder.play)
