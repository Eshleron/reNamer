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
"""

import sys
import os
from tkinter import filedialog
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

        self.ui.launch.clicked.connect(lambda: self.printing())

        """Binds"""
        # self.russian_lang.triggered.connect(self.rus_language)
        # self.english_lang.triggered.connect(self.eng_language)
        # self.launch.clicked.connect(lambda: self.rename())
        # self.pick_folder.bind("<Button-1>", lambda b: self.folder_pick())
        """Vars"""
        self.name = 0
        self.timer = 0
        self.path = ''
        self.folder = ''
        self.extentions_dict = {}

    def printing(self):
        print('DONE!')

    def unique_file_name(self, extention):
        try:
            if self.extentions_dict[extention] != '':
                self.extentions_dict[extention] += 1
        except KeyError:
            self.extentions_dict[extention] = 1
        finally:
            self.name = self.extentions_dict[extention]
            return self.name

    def folder_pick(self):
        self.folder = filedialog.askdirectory()
        self.path_label.configure(text=self.folder)

    def extention_find(self, file):
        length = 0
        file_length = len(file) - 1
        while length <= file_length:
            if file[length] == '.':
                letter_position = length
            length += 1
        extention = file[letter_position:]
        return extention

    def rename(self):
        self.extentions_dict = {}
        self.name = 0
        try:
            if self.wait_timer.get() != '':
                self.timer = float(self.wait_timer.get())

            file_list = []
            for file in os.walk(self.folder):
                file_list.append(file)
                print(file_list)

            for address, dirs, files in file_list:
                for file in files:
                    extention = self.extention_find(file)

                    self.path = address + '/'
                    obj = self.path + file

                    selection_type = self.rb_var.get()
                    selection_rnd = self.random_var.get()
                    if selection_rnd == 1:
                        os.rename(obj, self.path + str(random.randint(1000, 1000000)) + extention)
                        time.sleep(self.timer)
                    else:
                        if selection_type == 1:
                            self.unique_file_name(extention)
                            os.rename(obj, self.path + str(self.name) + extention)
                            time.sleep(self.timer)
                        else:
                            os.rename(obj, self.path + str(self.name) + extention)
                            self.name += 1
                            time.sleep(self.timer)

        except FileExistsError:
            print("\x1b[31mFileExistsError---Файл уже существует!\x1b[0m")


def main():
    app = QApplication(sys.argv)
    win = MainApplication()
    win.show()
    app.exec_()


if __name__ == '__main__':
    sys.exit(main())
