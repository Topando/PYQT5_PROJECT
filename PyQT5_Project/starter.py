import sys
from Handler import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from StartMenu import Ui_MainWindow
from ui_file_2 import Ui_SecondWindow
from open_task import Ui_open_task
from Settings import Ui_Settings
from AddTask import Ui_AddTask
from PyQt5.QtGui import QPixmap
from PIL import Image
import sys
import os


# startmenu
class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.result = []
        super().__init__()
        self.setupUi(self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.task)

        self.pushButton_2.clicked.connect(self.run)

        self.pushButton_4.clicked.connect(self.run)

        self.pushButton_3.clicked.connect(self.openSettings)

    def task(self):
        self.close()
        self.openTask = TwoWindow()
        self.openTask.show()

    def openSettings(self):
        self.close()
        self.openSet = Sets()
        self.openSet.show()

    def run(self):
        pass


# Task
class TwoWindow(QMainWindow, Ui_SecondWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.startMenu)
        self.pushButton.clicked.connect(self.open_task)

    def open_task(self):
        NumberTask = checkAndGifTask(self.textEdit.toPlainText())
        print(NumberTask)
        if NumberTask == 0:
            self.textEdit.setPlainText('некорректный ввод')
        else:
            print(NumberTask)
            self.close()
            self.openTask = openTask(str(NumberTask))
            self.openTask.show()

    def startMenu(self):
        self.close()
        self.openStartMenu = MyWidget()
        self.openStartMenu.show()


# openTask
class openTask(QMainWindow, Ui_open_task):
    def __init__(self, number):
        super().__init__()
        self.setupUi(self)
        print(number)
        self.NumberTask = "Task-Res\Task\{}".format(number)
        print(self.NumberTask)
        self.pictureOnLable(self.NumberTask)
        self.pushButton_3.clicked.connect(self.open_task)
        self.pushButton.clicked.connect(self.checkAnswer)

    def checkAnswer(self):
        Check(self.textEdit.toPlainText(), self.NumberTask)

    def pictureOnLable(self, link):
        linkT = link

        image = Image.open(linkT)
        size = (701, 431)
        im = image.resize(size)
        im.save(linkT)
        self.pixmap = QPixmap(linkT)
        self.image = self.label
        self.image.setPixmap(self.pixmap)

    def open_task(self):
        self.close()
        self.openTask = TwoWindow()
        self.openTask.show()


class Sets(QMainWindow, Ui_Settings):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.open_AddTask)
        self.pushButton_2.clicked.connect(self.startMenu)

    def open_AddTask(self):
        self.close()
        self.openAddTask = AddTask()
        self.openAddTask.show()

    def startMenu(self):
        self.close()
        self.openStartMenu = MyWidget()
        self.openStartMenu.show()


class AddTask(QMainWindow, Ui_AddTask):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.openSets)
        self.pushButton.clicked.connect(self.Add)

    def openSets(self):
        self.close()
        self.openSetting = Sets()
        self.openSetting.show()

    def Add(self):
        FileName = self.textEdit.toPlainText()
        Answer = self.textEdit_2.toPlainText()
        if len(FileName) != 0 and len(Answer) != 0:
            inputInDB(FileName, Answer)
            self.textEdit.setPlainText('')
            self.textEdit_2.setPlainText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()  # открытие 1 окна
    sys.exit(app.exec_())
