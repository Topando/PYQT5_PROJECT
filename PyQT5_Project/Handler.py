import random
import os
import sqlite3
from PyQt5.QtGui import QPixmap
from PIL import Image
from Variables import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QButtonGroup
from Interface.StartMenuWindow import Ui_StartMenu
from Interface.AnswerWindow import Ui_Answer
from Interface.SettingsWindow import Ui_Settings
from Interface.AddTaskWindow import Ui_AddTask
from Interface.TaskWindow import Ui_Task
from Interface.DecisionWindow import Ui_decision
from Interface.CorrectAnswerWindow import Ui_CorrectAnswer
from Interface.InCorrectAnswerWindow import Ui_InCorrectAnswer
from Interface.DelTaskWindow import Ui_DelTask
from Interface.StatisticsWindow import Ui_Statistics
from Interface.ResetStatisticsWindow import Ui_ResetStatistics
from Interface.StartOptionWindow import Ui_StartOption
from Interface.FirstAnswerOptionWindow import Ui_FirstAnswerOption
from Interface.SecondAnswerOptionWindow import Ui_SecondAnswerOption
from Interface.AnswerOptionWindow import Ui_AnswerOption
from Interface.ResultOptionWindow import Ui_ResultOption
from DBController import *


def check_gif_task(number):
    result = []
    array_on_res = os.listdir(directory.format("Res"))
    array_on_task = os.listdir(directory.format("Task"))
    array_on_res = list(set(array_on_res) & set(array_on_task))
    array_on_task[:] = array_on_res[:]
    array = []
    for i in range(len(array_on_res)):
        if array_on_res[i].split('.')[0] != str(number):
            continue
        array.append(array_on_res[i])
    array_on_res[:] = array[:]
    if len(array_on_res) == 0:
        return 0
    array = return_link_task()
    for i in range(len(array)):
        if array[i][0].split('.')[0] == str(number):
            result.append(array[i][0])
    if len(result) == 0:
        return 0
    array_on_task = result[random.randint(0, len(result) - 1)]
    array_on_task += ".png"
    print(array_on_res, array_on_task)
    if array_on_task in array_on_res:
        creative_file(array_on_task.split('.png')[0])
        return array_on_task.split('.png')[0]


def list_link_task(*array):
    print(array)
    result_list = []
    for i in array[0]:
        result_list.append(i[0])
    return result_list


def check_len_option_db():
    check_len = len_option_db()
    if len(check_len) == 0:
        add_in_option_db()
    else:
        return


def add_in_option_db():
    for i in range(1, 20):
        name_task = check_gif_task(int(i))
        print(name_task)
        if name_task != 0 and int(i) == int(name_task.split('.')[0]):
            print(1)
            take_and_insert_answer_img(name_task)


def picture_on_lable(self, link):
    link_task = link + ".png"
    width = self.label.width()
    height = self.label.height()
    print(width, height, link_task)
    image = Image.open(link_task)
    size = (width, height - 100)
    im = image.resize(size)
    im.save(link_task)
    self.pixmap = QPixmap(link_task)
    self.image = self.label
    self.image.setPixmap(self.pixmap)


def giv_link_picture(name_task, directory):
    return name_file.format(directory, name_task)


def giv_name_task(name_task):
    name_task = name_tasks(name_task)
    if len(name_task) == 0:
        return incorrect_answer
    else:
        return name_task[0][0]


def creative_file(name_task):
    file = open(f"file\{'name_task.txt'}", 'w', encoding='utf-8')
    file.write(str(name_task))
    file.close()
    read_file()


def read_file():
    file = open(f"file\{'name_task.txt'}", 'r', encoding='utf-8')
    name_task = file.read().splitlines()
    return name_task[0]


def start_settings():
    check_len_db()
    clear_option_db()


def result_true_answer():
    array_result = all_in_option_db()
    result = 0
    for i in array_result:
        if str(i[2]) == str(i[3]):
            result += 1
    return str(result)


def get_next_window(self, name_window):
    def next_window():
        self.close()
        self.next_window = name_window()
        self.next_window.show()

    return next_window
