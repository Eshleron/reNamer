# -*- coding: utf-8 -*-


import ctypes

from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QMessageBox, QFileDialog, QHBoxLayout, \
    QFormLayout, QWidget, QScrollArea, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QIcon, QImage, QPalette, QBrush, QFont
from PyQt5.QtCore import QSize, Qt, QRect


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("Main window")
        self.setWindowIcon(QIcon('logo.png'))
        self.width = 850
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
        # self.launch = QtWidgets.QPushButton(self.centralWidget)
        # self.launch.setGeometry(QtCore.QRect(90, 10, 70, 40))
        # self.launch.setToolTip("Top left corner of the rectangle.")
               
        # self.pick_folder = tk.Button(self.frame, text="Choose the folder", width=15, height=1)
        # self.pick_folder.pack()
        # # self.Folder_Button.focus_set()
        #
        # self.time_label = tk.Label(self.frame, text='Time between changing the names', width=30)
        # self.time_label.pack()
        #
        # self.wait_timer = tk.Entry(self.frame, width=3, text="")
        # self.wait_timer.pack()
        #
        # self.path_hint_label = tk.Label(self.frame, text='Chosen path to the folder is: ', width=25, height=1)
        # self.path_hint_label.pack()
        #
        # self.path_label = tk.Label(self.frame, width=50, height=3, fg="green")
        # self.path_label.pack()
        #
        # self.pass1_label = tk.Label(self.frame, text='Choose a few naming options', width=50, height=2)
        # self.pass1_label.pack()
        #
        # self.random_name_rb = tk.Radiobutton(self.frame, text='Random file name', variable=self.random_var, value=1)
        # self.random_name_rb.pack()
        #
        # self.not_random_name_rb = tk.Radiobutton(self.frame, text='Not random file name', variable=self.random_var, value=2)
        # self.not_random_name_rb.pack()
        #
        # self.pass2_label = tk.Label(self.frame, text='and those', width=15, height=2, font='sans 11')
        # self.pass2_label.pack()
        #
        # self.file_type_rb = tk.Radiobutton(self.frame, text='Depends on file type', variable=self.rb_var, value=1)
        # self.file_type_rb.pack()
        #
        # self.file_name_rb = tk.Radiobutton(self.frame, text='Depends on initial file name', variable=self.rb_var, value=2)
        # self.file_name_rb.pack()

    def __layout(self):
        """
        Arranging UI elements
        """

        layout = QHBoxLayout()
        layout.addWidget(self.launch)
        layout.addWidget(self.pick_folder)

        self.setLayout(layout)


class PushButton(QPushButton):
    def __init__(self, text, tooltip=None):
        QPushButton.__init__(self)

        self.tooltip = str(tooltip)
        self.text = text

        self.setText(text)
        self.setToolTip(self.tooltip)

# class PushButton(QPushButton):
#     def __init__(self, widget, pos_x, pos_y, width, height, text, tooltip=None):
#         QPushButton.__init__(self, widget)
#
#         self.widget = widget
#         self.pos_x = pos_x
#         self.pos_y = pos_y
#         self.width = width
#         self.height = height
#         self.tooltip = str(tooltip)
#         self.text = text
#
#         self.setText(text)
#         self.setGeometry(QRect(self.pos_x, self.pos_y, self.width, self.height))
#         self.setToolTip(self.tooltip)


class Label(QLabel):

    def __init__(self, widget, pos_x, pos_y, width, height, text, tooltip=None):
        Label.__init__(self, widget)
        self.widget = widget
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.tooltip = str(tooltip)
        self.text = text

        self.statistics_label = QLabel("Statistics", self.centralWidget)
        self.statistics_label.setGeometry(QRect(730, 10, 100, 20))
        self.statistics_label.setObjectName("statistics_label")
        self.statistics_label.setStyleSheet("color:rgb(0, 0, 0, 255)")
        self.statistics_label.setFont(QFont("Times", 12))



#         '''Size of the MainWindow'''
#         user32 = ctypes.windll.user32
#         screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
#         self.width = int(screensize[0] / 2)
#         self.height = int(screensize[1] - 100)
#         self.setGeometry(screensize[0] - self.width, 30, self.width, self.height)
#
#
