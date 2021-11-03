from Handler import *
from Interface import *
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


# startmenu
class StartMenuWindow(QMainWindow, Ui_StartMenu):
    def __init__(self):
        self.result = []
        super().__init__()
        self.setupUi(self)  # Загружаем дизайн
        check_len_db()
        clear_option_db()
        self.pushButton.clicked.connect(self.open_task)

        self.pushButton_2.clicked.connect(self.open_start_option_window)

        self.pushButton_4.clicked.connect(self.open_statistics_window)

        self.pushButton_3.clicked.connect(self.open_settings)

    def open_task(self):
        self.close()
        self.open_task = TaskWindow()
        self.open_task.show()

    def open_settings(self):
        self.close()
        self.open_setting = SettingWindow()
        self.open_setting.show()

    def open_start_option_window(self):
        self.close()
        self.start_option = StartOptionWindow()
        self.start_option.show()

    def open_statistics_window(self):
        self.close()
        self.open_statistics = StatisticsWindow()
        self.open_statistics.show()


# Task
class TaskWindow(QMainWindow, Ui_Task):
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
            self.open_task = AnswerWindow(str(number_task))
            self.open_task.show()

    def open_start_menu(self):
        self.close()
        self.open_start_menu = StartMenuWindow()
        self.open_start_menu.show()


# openTask
class AnswerWindow(QMainWindow, Ui_Answer):
    def __init__(self, number):
        super().__init__()
        self.setupUi(self)
        self.number = number
        self.number_task = giv_link_picture(number, "Task")
        picture_on_lable(self, self.number_task)
        self.pushButton_3.clicked.connect(self.open_task)
        self.pushButton.clicked.connect(self.check_answer)
        self.pushButton_2.clicked.connect(self.open_decision)

    def check_answer(self):
        answer_value = check(self.textEdit.toPlainText(), self.number)
        if answer_value:
            self.open_correct_window()
        else:
            self.open_incorrect_window()

    def open_correct_window(self):
        self.close()
        self.open_correct_answer = CorrectAnswerWindow()
        self.open_correct_answer.show()

    def open_incorrect_window(self):
        self.close()
        self.open_incorrect_answer = InCorrectAnswerWindow(self.number)
        self.open_incorrect_answer.show()

    def open_task(self):
        self.close()
        self.open_task = TaskWindow()
        self.open_task.show()

    def open_decision(self):
        self.close()
        self.open_decision = DecisionWindow(self.number_task)
        self.open_decision.show()


class CorrectAnswerWindow(QMainWindow, Ui_CorrectAnswer):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.open_start_window)
        self.pushButton_2.clicked.connect(self.open_task_window)
        self.pushButton_3.clicked.connect(self.open_statistics_window)

    def open_start_window(self):
        self.close()
        self.open_window = StartMenuWindow()
        self.open_window.show()

    def open_task_window(self):
        self.close()
        self.open_task = TaskWindow()
        self.open_task.show()

    def open_statistics_window(self):
        self.close()
        self.open_statistics = StatisticsWindow()
        self.open_statistics.show()


class InCorrectAnswerWindow(QMainWindow, Ui_InCorrectAnswer):
    def __init__(self, task):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.open_start_window)
        self.pushButton_2.clicked.connect(self.open_task_window)
        self.pushButton_3.clicked.connect(self.open_answer_window)
        self.pushButton_4.clicked.connect(self.open_decision_window)
        self.task = task
        self.link_task = giv_link_picture(task, "Task")

    def open_start_window(self):
        self.close()
        self.open_start_menu = StartMenuWindow()
        self.open_start_menu.show()

    def open_task_window(self):
        self.close()
        self.open_task = TaskWindow()
        self.open_task.show()

    def open_decision_window(self):
        self.close()
        self.open_decision = DecisionWindow(self.link_task)
        self.open_decision.show()

    def open_answer_window(self):
        self.close()
        self.open_answer = AnswerWindow(str(self.task))
        self.open_answer.show()


class DecisionWindow(QMainWindow, Ui_decision):
    def __init__(self, number_task):
        super().__init__()
        number_task = number_task[:9] + "Res" + number_task[13:]
        print(number_task)
        self.setupUi(self)
        picture_on_lable(self, number_task)
        self.pushButton.clicked.connect(self.open_task)
        self.pushButton_2.clicked.connect(self.open_start_menu)

    def open_start_menu(self):
        self.close()
        self.open_start_menu = StartMenuWindow()
        self.open_start_menu.show()

    def open_task(self):
        self.close()
        self.open_task = TaskWindow()
        self.open_task.show()


class SettingWindow(QMainWindow, Ui_Settings):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.open_add_task)
        self.pushButton_2.clicked.connect(self.open_start_menu)
        self.pushButton_3.clicked.connect(self.open_del_task_window)
        self.pushButton_4.clicked.connect(self.open_reset_statistics_window)

    def open_add_task(self):
        self.close()
        self.open_add_task = AddTaskWindow()
        self.open_add_task.show()

    def open_start_menu(self):
        self.close()
        self.open_start_menu = StartMenuWindow()
        self.open_start_menu.show()

    def open_del_task_window(self):
        self.close()
        self.open_del_task = DelTaskWindow()
        self.open_del_task.show()

    def open_reset_statistics_window(self):
        self.close()
        self.open_reset_statistics = ResetStatisticsWindow()
        self.open_reset_statistics.show()


class AddTaskWindow(QMainWindow, Ui_AddTask):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.open_settings_window)
        self.pushButton.clicked.connect(self.add_task)

    def open_settings_window(self):
        self.close()
        self.open_setting = SettingWindow()
        self.open_setting.show()

    def add_task(self):
        file_name = self.textEdit.toPlainText()
        user_answer = self.textEdit_2.toPlainText()
        if len(file_name) != 0 and len(user_answer) != 0:
            input_in_db(file_name, user_answer)
            self.textEdit.setPlainText('')
            self.textEdit_2.setPlainText('')


class DelTaskWindow(QMainWindow, Ui_DelTask):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.open_settings_window)
        self.pushButton.clicked.connect(self.del_task)

    def del_task(self):
        del_in_db(self.textEdit.toPlainText())
        self.textEdit.setPlainText("Удалено")

    def open_settings_window(self):
        self.close()
        self.open_setting = SettingWindow()
        self.open_setting.show()


class ResetStatisticsWindow(QMainWindow, Ui_ResetStatistics):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.open_settings_window)
        self.pushButton.clicked.connect(self.reset_statistics)

    def reset_statistics(self):
        reset_all_statistics()

    def open_settings_window(self):
        self.close()
        self.open_setting = SettingWindow()
        self.open_setting.show()


class StatisticsWindow(QMainWindow, Ui_Statistics):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.get_statistics()
        self.pushButton.clicked.connect(self.open_start_menu_window)

    def get_statistics(self):
        all_information = getting_statistics()
        number_of_tasks = all_information[1]
        correct_answer = all_information[2]
        incorrect_answer = all_information[3]
        self.textEdit.setPlainText(str(number_of_tasks))
        self.textEdit_2.setPlainText(str(correct_answer))
        self.textEdit_3.setPlainText(str(incorrect_answer))
        if incorrect_answer != 0:
            self.textEdit_4.setPlainText(str(round(correct_answer / number_of_tasks, 2)))
        else:
            self.textEdit_4.setPlainText(str(correct_answer / 1))

    def open_start_menu_window(self):
        self.close()
        self.open_start_menu = StartMenuWindow()
        self.open_start_menu.show()


class StartOptionWindow(QMainWindow, Ui_StartOption):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.open_start_menu_window)
        self.pushButton.clicked.connect(self.open_fisrt_answer_window)

    def open_start_menu_window(self):
        self.close()
        self.open_start_menu = StartMenuWindow()
        self.open_start_menu.show()

    def open_fisrt_answer_window(self):
        self.close()
        self.open_first_answer = FirstAnswerWindow()
        self.open_first_answer.show()


class FirstAnswerWindow(QMainWindow, Ui_FirstAnswerOption):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.radioButton_2.clicked.connect(self.open_second_answer_window)
        self.pushButton.clicked.connect(self.open_answer_option_window)
        self.pushButton_2.clicked.connect(self.open_answer_option_window)
        self.pushButton_3.clicked.connect(self.open_answer_option_window)
        self.pushButton_4.clicked.connect(self.open_answer_option_window)
        self.pushButton_5.clicked.connect(self.open_answer_option_window)
        self.pushButton_6.clicked.connect(self.open_answer_option_window)
        self.pushButton_7.clicked.connect(self.open_answer_option_window)
        self.pushButton_8.clicked.connect(self.open_answer_option_window)
        self.pushButton_9.clicked.connect(self.open_answer_option_window)
        self.pushButton_10.clicked.connect(self.open_answer_option_window)
        check_len_option_db()

    def open_second_answer_window(self):
        self.close()
        self.open_second_answer = SecondAnswerWindow()
        self.open_second_answer.show()

    def open_answer_option_window(self):
        name = self.sender().text()
        self.close()
        self.open_answer_option = AnswerOptionWindow(1, name.split()[1])
        self.open_answer_option.show()


class SecondAnswerWindow(QMainWindow, Ui_SecondAnswerOption):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.open_answer_option_window)
        self.pushButton_2.clicked.connect(self.open_answer_option_window)
        self.pushButton_3.clicked.connect(self.open_answer_option_window)
        self.pushButton_4.clicked.connect(self.open_answer_option_window)
        self.pushButton_5.clicked.connect(self.open_answer_option_window)
        self.pushButton_6.clicked.connect(self.open_answer_option_window)
        self.pushButton_7.clicked.connect(self.open_answer_option_window)
        self.pushButton_8.clicked.connect(self.open_answer_option_window)
        self.pushButton_9.clicked.connect(self.open_answer_option_window)

        self.radioButton.clicked.connect(self.open_fisrt_answer_window)

    def open_fisrt_answer_window(self):
        self.close()
        self.open_first_answer = FirstAnswerWindow()
        self.open_first_answer.show()

    def open_answer_option_window(self):
        name = self.sender().text()
        self.close()
        self.open_answer_option = AnswerOptionWindow(2, name.split()[1])
        self.open_answer_option.show()


class AnswerOptionWindow(QMainWindow, Ui_AnswerOption):
    def __init__(self, number_window, name_task):
        super().__init__()
        self.setupUi(self)
        self.link_task = giv_name_task(name_task)
        self.name_task = name_task
        print(self.link_task)
        if self.link_task == incorrect_answer:
            self.label.setText(incorrect_answer)
            self.textEdit.setReadOnly(True)
            self.pushButton.setEnabled(False)
        else:
            picture_on_lable(self, giv_link_picture(self.link_task, "Task"))

        if number_window == 1:
            self.pushButton_2.clicked.connect(self.open_fisrt_answer_window)
        elif number_window == 2:
            self.pushButton_2.clicked.connect(self.open_second_answer_window)
        self.pushButton.clicked.connect(self.record_user_answer)

    def record_user_answer(self):
        text = self.textEdit.toPlainText()
        print(text)
        if text.isdigit() is False:
            self.textEdit.setText(incorrect_answer_option)
        else:
            record_answer(text, self.name_task)
            self.textEdit.setText(correct_answer_option)

    def open_fisrt_answer_window(self):
        self.close()
        self.open_first_answer = FirstAnswerWindow()
        self.label.setText(correct_answer_option)
        self.open_first_answer.show()

    def open_second_answer_window(self):
        self.close()
        self.open_second_answer = SecondAnswerWindow()
        self.open_second_answer.show()
