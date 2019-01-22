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

This file (reName.py) is part of reNamer.

"""

import json
import os
from pathlib import Path
import random
import sys
import time


from PyQt5.QtWidgets import QApplication, QMessageBox, QFileDialog


import gui


class MainApplication(gui.MainWindow):

    def __init__(self, parent=None):
        super(MainApplication, self).__init__(parent)

        '''Connect gui elements to functions'''
        self.ui.pick_folder.clicked.connect(self.pick_folder)

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

    def reconnect(self, new_handler):
        """
        First, deletes previous connection with handlers for specified signal.
        Second, connects specified signal with new_handler.
        """
        button = self.ui.launch.clicked
        try:
            button.disconnect()
        except TypeError:
            pass
        button.connect(new_handler)

    def random_file_name(self):
        self.ui.file_type.setCheckable(False)
        self.ui.file_type.setEnabled(False)
        self.ui.file_set_name.setCheckable(False)
        self.ui.file_set_name.setEnabled(False)
        self.ui.set_basis.setEnabled(False)
        self.ui.set_start_value.setEnabled(False)
        self.ui.set_increment.setEnabled(False)
        self.reconnect(self.random_rename)

    def not_random_file_name(self):
        self.ui.file_type.setCheckable(True)
        self.ui.file_type.setEnabled(True)
        self.ui.file_set_name.setCheckable(True)
        self.ui.file_set_name.setEnabled(True)

    def type_name(self):
        self.ui.set_basis.setEnabled(False)
        self.ui.set_start_value.setEnabled(False)
        self.ui.set_increment.setEnabled(False)
        self.reconnect(self.type_rename)

    def increment_name(self):
        self.ui.set_basis.setEnabled(True)
        self.ui.set_start_value.setEnabled(True)
        self.ui.set_increment.setEnabled(True)
        self.reconnect(self.increment_rename)

    def unique_file_name(self, extension):
        """
        This function finds a unique name for the file depending on the the extension that file has.

        In form of:
        {'.docx': 2, '.css': 1, '.html': 1,}
        """

        try:
            if self.extensions_dict[extension] != '':
                self.extensions_dict[extension] += 1
        except KeyError:
            self.extensions_dict[extension] = 1

    def pick_folder(self):
        self.folder = str(QFileDialog.getExistingDirectory(self.ui, "Select Directory"))
        self.check_folder()

    def check_folder(self):
        """This function counts total files and checks if target folder is empty/not empty."""
        self.file_list = []
        self.extensions_dict = {}
        self.qty_files = 0

        if self.folder:
            for file in os.walk(self.folder):
                self.file_list.append(file)

            '''Count quantity of files'''
            if self.file_list[0][2]:
                for file in self.file_list[0][2]:
                    extension = str(Path(file).suffix)
                    self.unique_file_name(extension)
                    self.qty_files += 1
                self.ui.show_path.setStyleSheet('color: green')
                self.ui.show_path.setText(self.folder)
                self.ui.progress_bar.setRange(1, self.qty_files)
                '''Creating visual effect of refilling the bar'''
                self.ui.progress_bar.setValue(1)
                time.sleep(.01)
            else:
                '''Check if target folder is empty'''
                self.ui.show_path.setStyleSheet('color: #b22900')
                self.ui.show_path.setText('Target folder may be empty!\n' + self.folder)
                self.ui.show_extensions.hide()
                self.ui.show_extensions.setText('')

            '''Print dict values'''
            dict_values = json.dumps(self.extensions_dict)
            if dict_values != '{}':
                self.ui.show_extensions.setText(dict_values)
                self.ui.show_extensions.show()

    def generic_rename(self, name='', start_value='', increment='', func=''):
        """General function for all other types of renaming functions."""
        if self.folder:
            self.check_folder()
            address = self.file_list[0][0]
            pb_value = 0

            if func == 'increment':
                self.name = name
                self.start_value = int(start_value) - 1
                self.increment = int(increment)

            for file in self.file_list[0][2]:
                    extension = str(Path(file).suffix)
                    folder_path = address + '/'
                    obj = folder_path + file

                    if func == 'type':
                        self.start_value = ''
                        self.name = self.extensions_dict[extension]
                        self.extensions_dict[extension] -= 1
                    elif func == 'rnd':
                        self.name = random.randint(100000, 10000000)
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

    def type_rename(self):
        self.generic_rename(func='type')

    def random_rename(self):
        self.generic_rename(func='rnd')

    def increment_rename(self):
        basis = self.ui.set_basis.text()
        start_value = self.ui.set_start_value.text()
        increment = self.ui.set_increment.text()
        self.generic_rename(name=basis, start_value=start_value, increment=increment, func='increment')


def main():
    app = QApplication(sys.argv)
    win = MainApplication()
    win.show()
    app.exec_()


if __name__ == '__main__':
    sys.exit(main())
