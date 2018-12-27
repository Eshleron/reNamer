# -*- coding: utf-8 -*-


import ctypes

from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QMessageBox, QFileDialog, QHBoxLayout, \
    QFormLayout, QWidget, QScrollArea, QVBoxLayout, QPushButton, QLabel, QLineEdit, QRadioButton, QButtonGroup
from PyQt5.QtGui import QIcon, QImage, QPalette, QBrush, QFont
from PyQt5.QtCore import QSize, Qt, QRect


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("Main window")
        self.setWindowIcon(QIcon('logo.png'))
        self.width = 400
        self.height = 470
        MainWindow.resize(self, self.width, self.height)

        """Menu"""
        self.mainMenu = self.menuBar()
        langMenu = self.mainMenu.addMenu('Language')
        """Menu actions"""
        self.russian_lang = QAction(QIcon('RUS.png'), 'Russian', self)
        self.russian_lang.setShortcut('Ctrl+N')
        self.english_lang = QAction(QIcon('ENG.png'), 'English', self)
        self.english_lang.setShortcut('Ctrl+N')
        # langMenu.addAction(self.russian_lang)
        # langMenu.addAction(self.english_lang)

        """CentralWidget"""
        self.ui = UserInterface(self)
        self.setCentralWidget(self.ui)

        """Vars"""
        # self.rb_var = IntVar()
        # self.random_var = IntVar()
        """Dictionary ENG-RUS"""
        self.eng_language_list = ['Start', 'Choose the folder', 'Time between changing the names',
                                  'Chosen path to the folder is: ',
                                  'Choose a few naming options', 'Random file name', 'Not random file name', 'and those',
                                  'Depends on file type', 'Depends on initial file name']

        self.eng_rus_dictionary = {'Start': 'Запуск',
                                   'Choose the folder': 'Выберете папку',
                                   'Time between changing the names': 'Время между сменой названий файлов',
                                   'Chosen path to the folder is: ': 'Путь к выбранной папке: ',
                                   'Choose a few naming options': 'Выберете необходимые настройки',
                                   'Random file name': 'Случайное имя файла',
                                   'Not random file name': 'Не случайное имя файла',
                                   'and those': 'еще настройки',
                                   'Depends on file type': 'Имя зависит от типа файла',
                                   'Depends on initial file name': 'Имя зависит от изначального имени файла'}

    def eng_language(self):
        self.launch.configure(text=self.eng_language_list[0])
        self.pick_folder.configure(text=self.eng_language_list[1])
        self.time_label.configure(text=self.eng_language_list[2])
        self.path_hint_label.configure(text=self.eng_language_list[3])
        self.pass1_label.configure(text=self.eng_language_list[4])
        self.random_name_rb.configure(text=self.eng_language_list[5])
        self.not_random_name_rb.configure(text=self.eng_language_list[6])
        self.pass2_label.configure(text=self.eng_language_list[7])
        self.file_type_rb.configure(text=self.eng_language_list[8])
        self.file_name_rb.configure(text=self.eng_language_list[9])

    def rus_language(self):
        self.launch.configure(text=self.eng_rus_dictionary[self.eng_language_list[0]])
        self.pick_folder.configure(text=self.eng_rus_dictionary[self.eng_language_list[1]])
        self.time_label.configure(text=self.eng_rus_dictionary[self.eng_language_list[2]])
        self.path_hint_label.configure(text=self.eng_rus_dictionary[self.eng_language_list[3]])
        self.pass1_label.configure(text=self.eng_rus_dictionary[self.eng_language_list[4]])
        self.random_name_rb.configure(text=self.eng_rus_dictionary[self.eng_language_list[5]])
        self.not_random_name_rb.configure(text=self.eng_rus_dictionary[self.eng_language_list[6]])
        self.pass2_label.configure(text=self.eng_rus_dictionary[self.eng_language_list[7]])
        self.file_type_rb.configure(text=self.eng_rus_dictionary[self.eng_language_list[8]])
        self.file_name_rb.configure(text=self.eng_rus_dictionary[self.eng_language_list[9]])


class UserInterface(QWidget):

    def __init__(self, parent=None):
        super(UserInterface, self).__init__(parent)
        self.__controls()
        self.__layout()

    def __controls(self):
        """
        Creating UI elements
        """

        """Buttons"""
        self.launch = PushButton('Launch', 'Click to launch')
        self.pick_folder = PushButton('Pick Folder')
        self.timeout = Label('Time between changing the names')
        self.timeout_enter = LineEdit()
        self.path_hint = Label('Chosen path to the folder is: ')
        self.show_path = Label()  # Green
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
        self.file_type.setChecked(True)
        self.file_name = RadioButton('Depends on initial file name')

        self.button_group_2 = QButtonGroup()
        self.button_group_2.addButton(self.file_type)
        self.button_group_2.addButton(self.file_name)

    def __layout(self):
        """
        Arranging UI elements
        """

        layout_v = QVBoxLayout()
        layout_v.setContentsMargins(5, 5, 5, 5)
        layout_v.addWidget(self.pick_folder, 1, Qt.AlignTop)
        layout_v.addWidget(self.timeout, 1, Qt.AlignTop)
        layout_v.addWidget(self.timeout_enter, 1, Qt.AlignTop)
        layout_v.addWidget(self.path_hint, 1, Qt.AlignCenter)
        layout_v.addWidget(self.show_path, 1, Qt.AlignCenter)
        layout_v.addWidget(self.choice_1, 1, Qt.AlignTop)
        layout_v.addWidget(self.rnd_name, 1, Qt.AlignTop)
        layout_v.addWidget(self.not_rnd_name, 1, Qt.AlignTop)
        layout_v.addWidget(self.choice_2, 1, Qt.AlignTop)
        layout_v.addWidget(self.file_type, 1, Qt.AlignTop)
        layout_v.addWidget(self.file_name, 1, Qt.AlignTop)
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
    def __init__(self, text='', tooltip=''):
        QLineEdit.__init__(self)

        self.tooltip = str(tooltip)
        self.text = str(text)

        self.setText(self.text)
        self.setToolTip(self.tooltip)


class RadioButton(QRadioButton):
    def __init__(self, text=None, tooltip=None):
        QRadioButton.__init__(self)

        self.tooltip = str(tooltip)
        self.text = str(text)

        self.setText(self.text)
        self.setToolTip(self.tooltip)

#         '''Size of the MainWindow'''
#         user32 = ctypes.windll.user32
#         screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
#         self.width = int(screensize[0] / 2)
#         self.height = int(screensize[1] - 100)
#         self.setGeometry(screensize[0] - self.width, 30, self.width, self.height)
#
#
