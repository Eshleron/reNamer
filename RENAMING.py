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

        self.ui.launch.clicked.connect(self.rename_files)
        self.ui.pick_folder.clicked.connect(self.folder_pick)

        """Binds"""
        # self.russian_lang.triggered.connect(self.rus_language)
        # self.english_lang.triggered.connect(self.eng_language)

        # self.pick_folder.bind("<Button-1>", lambda b: self.folder_pick())
        """Vars"""
        self.name = 0
        self.timer = 0
        # self.folder_path = ''
        self.folder = ''
        self.extensions_dict = {}

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
        if self.folder:
            self.ui.show_path.setText(self.folder)

    def find_extension(self, file):
        return str(Path(file).suffix)
        # import os
        # filename, extension = os.path.splitext(file)
        # return extension

    def rename_files(self):
        # self.extensions_dict = {}

        file_list = []
        for file in os.walk(self.folder):
            file_list.append(file)

        for address, dirs, files in file_list:
            for file in files:
                extension = self.find_extension(file)
                folder_path = address + '/'
                obj = folder_path + file

                self.unique_file_name(extension)
                os.rename(obj, folder_path + str(self.name) + extension)
                time.sleep(self.timer)

    # def rename(self):
    #     self.extentions_dict = {}
    #     self.name = 0
    #     try:
    #         if self.wait_timer.get() != '':
    #             self.timer = float(self.wait_timer.get())
    #
    #         file_list = []
    #         for file in os.walk(self.folder):
    #             file_list.append(file)
    #             print(file_list)
    #
    #         for address, dirs, files in file_list:
    #             for file in files:
    #                 extention = self.find_extention(file)
    #
    #                 self.path = address + '/'
    #                 obj = self.path + file
    #
    #                 selection_type = self.rb_var.get()
    #                 selection_rnd = self.random_var.get()
    #                 if selection_rnd == 1:
    #                     os.rename(obj, self.path + str(random.randint(1000, 1000000)) + extention)
    #                     time.sleep(self.timer)
    #                 else:
    #                     if selection_type == 1:
    #                         self.unique_file_name(extention)
    #                         os.rename(obj, self.path + str(self.name) + extention)
    #                         time.sleep(self.timer)
    #                     else:
    #                         os.rename(obj, self.path + str(self.name) + extention)
    #                         self.name += 1
    #                         time.sleep(self.timer)
    #
    #     except FileExistsError:
    #         print("\x1b[31mFileExistsError---Файл уже существует!\x1b[0m")


def main():
    app = QApplication(sys.argv)
    win = MainApplication()
    win.show()
    app.exec_()


if __name__ == '__main__':
    sys.exit(main())
