# -*- coding: utf-8 -*-
"""
reNamer, Author Svyatoslav Pankov(https://github.com/Eshleron/reNamer)

Requirements:
  - json
  - os
  - pathlib
  - random
  - sys
  - time
  - PyQt5

Python:
  - 3.5.4

This file (gui.py) is part of reNamer.

"""


from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QImage, QPalette, QBrush
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, \
    QRadioButton, QButtonGroup, QProgressBar


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("reNamer by Svyatoslav Pankov")
        self.setWindowIcon(QIcon('media\icons\logo.png'))
        self.width = 400
        self.height = 470
        MainWindow.resize(self, self.width, self.height)

        bg_image = 'media\Wallpaper_scaled.jpg'
        image = QImage(bg_image)
        palette = QPalette()
        palette.setBrush(10, QBrush(image))
        self.setPalette(palette)

        """CentralWidget"""
        self.ui = UserInterface(self)
        self.setCentralWidget(self.ui)


class UserInterface(QWidget):

    def __init__(self, parent=None):
        super(UserInterface, self).__init__(parent)
        self.__controls()
        self.__layout()

    def __controls(self):
        """
        Creating UI elements.
        """

        """Buttons"""
        self.launch = PushButton('Launch', 'Click to launch')
        self.pick_folder = PushButton('Pick Folder')
        self.path_hint = Label('Chosen path to the folder is: ')
        self.show_path = Label()
        self.show_extensions = Label('')
        self.show_extensions.hide()
        self.choice_1 = Label('Choose a few naming options')

        """RadioButtons first group"""
        self.rnd_name = RadioButton('Random file name')
        self.not_rnd_name = RadioButton('Not random file name')
        self.not_rnd_name.setChecked(True)

        self.button_group_1 = QButtonGroup()
        self.button_group_1.addButton(self.rnd_name)
        self.button_group_1.addButton(self.not_rnd_name)

        self.choice_2 = Label('and those')

        """RadioButtons second group"""
        self.file_type = RadioButton('Depends on file type')
        self.file_set_name = RadioButton('Set file name')

        self.button_group_2 = QButtonGroup()
        self.button_group_2.addButton(self.file_type)
        self.button_group_2.addButton(self.file_set_name)

        self.set_basis = LineEdit(placeholder='Set basis')
        self.set_start_value = LineEdit(placeholder='Set start value')
        self.set_increment = LineEdit(placeholder='Set increment')
        self.set_basis.setEnabled(False)
        self.set_start_value.setEnabled(False)
        self.set_increment.setEnabled(False)

        self.progress_bar = ProgressBar()

    def __layout(self):
        """
        Arranging UI elements.
        """

        layout_v = QVBoxLayout()
        layout_v.setContentsMargins(5, 5, 5, 5)
        layout_v.addWidget(self.pick_folder, 1, Qt.AlignTop)
        layout_v.addWidget(self.path_hint, 1, Qt.AlignCenter)
        layout_v.addWidget(self.show_path, 1, Qt.AlignCenter)
        layout_v.addWidget(self.show_extensions, 1, Qt.AlignCenter)
        layout_v.addWidget(self.choice_1, 1, Qt.AlignTop)
        layout_v.addWidget(self.rnd_name, 1, Qt.AlignTop)
        layout_v.addWidget(self.not_rnd_name, 1, Qt.AlignTop)
        layout_v.addWidget(self.choice_2, 1, Qt.AlignTop)
        layout_v.addWidget(self.file_type, 1, Qt.AlignTop)
        layout_v.addWidget(self.file_set_name, 1, Qt.AlignTop)
        layout_v.addWidget(self.set_basis, 1, Qt.AlignTop)
        layout_v.addWidget(self.set_start_value, 1, Qt.AlignTop)
        layout_v.addWidget(self.set_increment, 1, Qt.AlignTop)
        layout_v.addWidget(self.progress_bar, 1, Qt.AlignBottom)
        layout_v.addWidget(self.launch, 2, Qt.AlignBottom)

        layout_h = QHBoxLayout()
        layout_h.setContentsMargins(5, 5, 5, 5)
        layout_h.addLayout(layout_v)

        self.setLayout(layout_h)


class PushButton(QPushButton):
    def __init__(self, text='', tooltip=''):
        QPushButton.__init__(self)

        self.tooltip = str(tooltip)
        self.text = str(text)

        self.setText(self.text)
        self.setToolTip(self.tooltip)


class Label(QLabel):
    def __init__(self, text='', tooltip=''):
        QLabel.__init__(self)

        self.tooltip = str(tooltip)
        self.text = str(text)

        self.setText(self.text)
        self.setToolTip(self.tooltip)


class LineEdit(QLineEdit):
    def __init__(self, tooltip='', placeholder=''):
        QLineEdit.__init__(self)

        self.PlaceholderText = str(placeholder)
        self.tooltip = str(tooltip)

        self.setToolTip(self.tooltip)
        self.setPlaceholderText(self.PlaceholderText)


class RadioButton(QRadioButton):
    def __init__(self, text='', tooltip=''):
        QRadioButton.__init__(self)

        self.tooltip = str(tooltip)
        self.text = str(text)

        self.setText(self.text)
        self.setToolTip(self.tooltip)


class ProgressBar(QProgressBar):
    def __init__(self):
        QProgressBar.__init__(self)
        self.setTextVisible(False)
