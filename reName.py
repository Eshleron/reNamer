# -*- coding: utf-8 -*-
"""
reNamer, Author Svyatoslav Pankov(https://github.com/Eshleron/reNamer)

Requirements:
  - os
  - pathlib
  - random
  - sys
  - PyQt5

Python:
  - 3.5.4

This file (reName.py) is part of reNamer.

"""


import os
from pathlib import Path
import random
import sys


from PyQt5.QtWidgets import QApplication, QMessageBox, QFileDialog


import gui


class MainApplication(gui.MainWindow):

    def __init__(self, parent=None):
        super(MainApplication, self).__init__(parent)

        '''Connect gui elements to functions'''
        self.ui.pick_folder.clicked.connect(self.folder_pick)

        self.ui.rnd_name.toggled.connect(self.random_file_name)
        self.ui.not_rnd_name.toggled.connect(self.not_random_file_name)

        self.ui.file_type.toggled.connect(self.type_name)
        self.ui.file_set_name.toggled.connect(self.increment_name)

        '''Variables'''
        self.name = ''
        self.start_value = ''
        self.increment = ''
        self.folder = ''
        self.extensions_dict = {}
        self.file_list = []
        self.qty_files = 0

    def reconnect(self, signal, new_handler=None, old_handler=None):
        """
        First, deletes all connections with all handlers for specified signal.
        Second, connects specified signal with new_handler.
        """

        while True:
            try:
                if old_handler is not None:
                    signal.disconnect(old_handler)
                else:
                    signal.disconnect()
            except TypeError:
                break

        if new_handler is not None:
            signal.connect(new_handler)

    def random_file_name(self):
        self.ui.file_type.setCheckable(False)
        self.ui.file_type.setEnabled(False)
        self.ui.file_set_name.setCheckable(False)
        self.ui.file_set_name.setEnabled(False)
        self.ui.set_basis.setEnabled(False)
        self.ui.set_start_value.setEnabled(False)
        self.ui.set_increment.setEnabled(False)
        self.reconnect(self.ui.launch.clicked, self.random_rename)

    def not_random_file_name(self):
        self.ui.file_type.setCheckable(True)
        self.ui.file_type.setEnabled(True)
        self.ui.file_set_name.setCheckable(True)
        self.ui.file_set_name.setEnabled(True)

    def type_name(self):
        self.ui.set_basis.setEnabled(False)
        self.ui.set_start_value.setEnabled(False)
        self.ui.set_increment.setEnabled(False)
        self.reconnect(self.ui.launch.clicked, self.type_rename)

    def increment_name(self):
        self.ui.set_basis.setEnabled(True)
        self.ui.set_start_value.setEnabled(True)
        self.ui.set_increment.setEnabled(True)
        self.reconnect(self.ui.launch.clicked, self.increment_rename)

    def unique_file_name(self, extension):
        """
        This function finds a unique name for the file depending on the the extension that file has.

        In form of:
        {'.docx': 2, '.css': 1, '.html': 1,}

        returns the name of the file
        """

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
        """This function counts total files and checks state of the target folder(empty/not empty)."""

        self.file_list = []
        self.extensions_dict = {}
        self.qty_files = 0

        if self.folder:
            for file in os.walk(self.folder):
                self.file_list.append(file)

            '''Count quantity of files'''
            for _ in self.file_list[0][2]:
                self.qty_files += 1
            self.ui.progress_bar.setRange(1, self.qty_files)

            '''Check if target folder is empty'''
            if not self.file_list[0][2]:
                self.ui.show_path.setStyleSheet('color: #ff7b00')
                self.ui.show_path.setText('Target folder may be empty!\n' + self.folder)
            else:
                self.ui.show_path.setStyleSheet('color: green')
                self.ui.show_path.setText(self.folder)

    def broad_rename(self, name='', start_value='', increment='', func=''):
        """General function for all other types of renaming functions."""

        self.check_folder()
        address = self.file_list[0][0]
        pb_value = 0

        if name != '':
            self.name = name
        if start_value != '':
            self.start_value = int(start_value) - 1
        if increment != '':
            self.increment = int(increment)

        for file in self.file_list[0][2]:
                extension = str(Path(file).suffix)
                folder_path = address + '/'
                obj = folder_path + file

                if func == 'type':
                    self.start_value = ''
                    self.unique_file_name(extension)
                elif func == 'rnd':
                    self.name = str(random.randint(100000, 10000000))
                elif func == 'increment':
                    self.start_value += self.increment

                try:
                    os.rename(obj, folder_path + str(self.name) + str(self.start_value) + extension)
                    pb_value += 1
                    self.ui.progress_bar.setValue(pb_value)
                except FileNotFoundError:
                    QMessageBox.warning(self.ui, "Warning!", "File not found.")
                except FileExistsError:
                    QMessageBox.warning(self.ui, "Warning", "File already exists.")
                except:
                    QMessageBox.warning(self.ui, "Unknown error.", "Restart the program.")
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
