from Handler import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from StartMenu import Ui_MainWindow
from ui_file_2 import Ui_SecondWindow
from open_task import Ui_open_task
from Settings import Ui_Settings
from AddTask import Ui_AddTask
from PyQt5.QtGui import QPixmap
from decision import Ui_decision
from PIL import Image
import sys


# startmenu
class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.result = []
        super().__init__()
        self.setupUi(self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.task)

        self.pushButton_2.clicked.connect(self.run)

        self.pushButton_4.clicked.connect(self.run)

        self.pushButton_3.clicked.connect(self.open_settings)

    def task(self):
        self.close()
        self.openTask = TwoWindow()
        self.openTask.show()

    def open_settings(self):
        self.close()
        self.openSet = Setting()
        self.openSet.show()

    def run(self):
        pass


# Task
class TwoWindow(QMainWindow, Ui_SecondWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.open_start_menu)
        self.pushButton.clicked.connect(self.open_task)

    def open_task(self):
        number_task = check_gif_task(self.textEdit.toPlainText())
        if number_task == 0:
            self.textEdit.setPlainText('некорректный ввод')
        else:
            self.close()
            self.open_task = Task(str(number_task))
            self.open_task.show()

    def open_start_menu(self):
        self.close()
        self.open_start_menu = MyWidget()
        self.open_start_menu.show()


# openTask
class Task(QMainWindow, Ui_open_task):
    def __init__(self, number):
        super().__init__()
        self.setupUi(self)
        self.number_task = "Task-Res\Task\{}".format(number)
        self.picture_on_lable(self.number_task)
        self.pushButton_3.clicked.connect(self.open_task)
        self.pushButton.clicked.connect(self.check_answer)
        self.pushButton_2.clicked.connect(self.open_decision)

    def check_answer(self):
        answer_value = check(self.textEdit.toPlainText(), self.number_task)

    def picture_on_lable(self, link):
        link_task = link
        image = Image.open(link_task)
        size = (701, 431)
        im = image.resize(size)
        im.save(link_task)
        self.pixmap = QPixmap(link_task)
        self.image = self.label
        self.image.setPixmap(self.pixmap)

    def open_task(self):
        self.close()
        self.open_task = TwoWindow()
        self.open_task.show()

    def open_decision(self):
        self.close()
        self.open_decision = Decision(self.number_task)
        self.open_decision.show()


class Decision(QMainWindow, Ui_decision):
    def __init__(self, number_task):
        super().__init__()
        number_task = number_task[:9] + "Res" + number_task[13:]
        self.setupUi(self)
        self.picture_on_lable(number_task)
        self.pushButton.clicked.connect(self.open_task)
        self.pushButton_2.clicked.connect(self.open_start_menu)

    def picture_on_lable(self, link):
        link_task = link
        image = Image.open(link_task)
        size = (771, 451)
        im = image.resize(size)
        im.save(link_task)
        self.pixmap = QPixmap(link_task)
        self.image = self.label
        self.image.setPixmap(self.pixmap)

    def open_start_menu(self):
        self.close()
        self.open_start_menu = MyWidget()
        self.open_start_menu.show()

    def open_task(self):
        self.close()
        self.open_task = TwoWindow()
        self.open_task.show()


class Setting(QMainWindow, Ui_Settings):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.open_add_task)
        self.pushButton_2.clicked.connect(self.open_start_menu)

    def open_add_task(self):
        self.close()
        self.open_add_task = AddTask()
        self.open_add_task.show()

    def open_start_menu(self):
        self.close()
        self.open_start_menu = MyWidget()
        self.open_start_menu.show()


class AddTask(QMainWindow, Ui_AddTask):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.open_settings)
        self.pushButton.clicked.connect(self.add)

    def open_settings(self):
        self.close()
        self.open_setting = Setting()
        self.open_setting.show()

    def add(self):
        file_name = self.textEdit.toPlainText()
        user_answer = self.textEdit_2.toPlainText()
        if len(file_name) != 0 and len(user_answer) != 0:
            input_in_db(file_name, user_answer)
            self.textEdit.setPlainText('')
            self.textEdit_2.setPlainText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()  # открытие 1 окна
    sys.exit(app.exec_())
