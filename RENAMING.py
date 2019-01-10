# -*- coding: utf-8 -*-
# =======================
# reNamer
# Written in Python 3.5.4
# by Svyatoslav Pankov
# =======================


"""
TODO Total files renamed
TODO Process bar
TODO Automatically find OS encoding(language) and change software language accordingly
TODO Renaming folders
"""

import sys
import os
from pathlib import Path
import random
import time
from threading import Thread

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QMessageBox, \
    QFileDialog, QFrame, QWidget, QPushButton, QVBoxLayout, QFormLayout, QScrollArea, QHBoxLayout, QLabel, QGridLayout
from PyQt5.QtGui import QIcon, QImage, QPalette, QBrush
from PyQt5.QtCore import QSize, Qt, QRect

import gui


class MainApplication(gui.MainWindow):

    def __init__(self, parent=None):
        super(MainApplication, self).__init__(parent)

        # self.ui.launch.clicked.connect(self.printing)
        self.ui.pick_folder.clicked.connect(self.folder_pick)

        self.ui.rnd_name.toggled.connect(self.random_file_name)
        self.ui.not_rnd_name.toggled.connect(self.not_random_file_name)

        self.ui.file_type.toggled.connect(self.type_name)
        self.ui.file_set_name.toggled.connect(self.increment_name)
        """Binds"""
        # self.russian_lang.triggered.connect(self.rus_language)
        # self.english_lang.triggered.connect(self.eng_language)

        """Vars"""
        self.name = ''
        self.start_value = 0
        self.increment = 0
        self.folder = ''
        self.extensions_dict = {}
        self.file_list = []
        self.qty_files = 0

    def random_file_name(self):
        self.ui.file_type.setCheckable(False)
        self.ui.file_type.setEnabled(False)
        self.ui.file_init_name.setCheckable(False)
        self.ui.file_init_name.setEnabled(False)
        self.ui.file_set_name.setCheckable(False)
        self.ui.file_set_name.setEnabled(False)
        self.ui.launch.clicked.connect(self.random_rename)

    def not_random_file_name(self):
        self.ui.file_type.setCheckable(True)
        self.ui.file_type.setEnabled(True)
        self.ui.file_init_name.setCheckable(True)
        self.ui.file_init_name.setEnabled(True)
        self.ui.file_set_name.setCheckable(True)
        self.ui.file_set_name.setEnabled(True)

    def type_name(self):
        self.ui.launch.clicked.connect(self.type_rename)

    def increment_name(self):
        self.ui.launch.clicked.connect(self.increment_rename)

    def unique_file_name(self, extension):
        try:
            if self.extensions_dict[extension] != '':
                self.extensions_dict[extension] += 1
        except KeyError:
            self.extensions_dict[extension] = 1
        finally:
            self.name = self.extensions_dict[extension]
            return self.name

    def folder_pick(self):
        self.folder = str(QFileDialog.getExistingDirectory(self.ui, "Select Directory"))
        self.check_folder()

    def check_folder(self):
        self.file_list = []
        self.extensions_dict = {}

        if self.folder:
            for file in os.walk(self.folder):
                self.file_list.append(file)

            for address, dirs, files in self.file_list:
                for file in files:
                    self.qty_files += 1
            # print(self.file_list)
            if len(self.file_list[0]) == 0 and len(self.file_list[0]):
                self.ui.show_path.setStyleSheet('color: orange')
                self.ui.show_path.setText('Nothing in \n ', self.folder)
            else:
                self.ui.show_path.setStyleSheet('color: green')
                self.ui.show_path.setText(self.folder)

    def broad_rename(self, name='', start_value='', increment='', func=''):
        self.check_folder()

        if name != '':
            self.name = name
        if start_value != '':
            self.start_value = int(start_value)
        if increment != '':
            self.increment = int(increment)

        for address, dirs, files in self.file_list:
            for file in files:
                extension = str(Path(file).suffix)
                folder_path = address + '/'
                obj = folder_path + file

                if func == 'type':
                    self.unique_file_name(extension)
                elif func == 'rnd':
                    self.name = str(random.randint(100000, 10000000))
                elif func == 'increment':
                    self.start_value += self.increment
                elif func == 'initial':
                    pass

                try:
                    os.rename(obj, folder_path + str(self.name) + str(self.start_value) + extension)
                except FileNotFoundError:
                    QMessageBox.about(self.ui, "File not found.", "Choose folder again.")
                except FileExistsError:
                    QMessageBox.about(self.ui, "Файл уже существует.", "Выберете папку заново.")
                except:
                    QMessageBox.warning(self.ui, "Неизвестная ошибка.", "Перезапустите программу.")
                    raise

    def type_rename(self):
        self.broad_rename(func='type')

    def random_rename(self):
        self.broad_rename(func='rnd')

    def increment_rename(self):
        basis = self.ui.set_basis.text()
        start_value = self.ui.set_start_value.text()
        increment = self.ui.set_increment.text()
        self.broad_rename(name=basis, start_value=start_value, increment=increment, func='increment')


def main():
    app = QApplication(sys.argv)
    win = MainApplication()
    win.show()
    app.exec_()


if __name__ == '__main__':
    sys.exit(main())
