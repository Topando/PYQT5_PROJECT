from Handler import *


# startmenu
class StartMenuWindow(QMainWindow, Ui_StartMenu):
    def __init__(self):
        self.result = []
        super().__init__()
        self.setupUi(self)  # Загружаем дизайн
        start_settings()
        self.pushButton.clicked.connect(self.get_next_window(TaskWindow))

        self.pushButton_2.clicked.connect(self.get_next_window(StartOptionWindow))

        self.pushButton_4.clicked.connect(self.get_next_window(StatisticsWindow))

        self.pushButton_3.clicked.connect(self.get_next_window(SettingWindow))

    def get_next_window(self, name_window):
        def next_window():
            self.close()
            self.open_task = name_window()
            self.open_task.show()

        return next_window


# Task
class TaskWindow(QMainWindow, Ui_Task):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.get_next_window(StartMenuWindow))
        self.pushButton.clicked.connect(self.open_task)

    def open_task(self):
        number_task = check_gif_task(self.textEdit.toPlainText())
        if number_task == 0:
            self.textEdit.setPlainText('некорректный ввод')
        else:
            self.get_next_window(AnswerWindow)()

    def get_next_window(self, name_window):
        def next_window():
            self.close()
            self.next_window = name_window()
            self.next_window.show()

        return next_window


# openTask
class AnswerWindow(QMainWindow, Ui_Answer):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.number = read_file()
        self.number_task = giv_link_picture(self.number, "Task")
        picture_on_lable(self, self.number_task)
        self.pushButton_3.clicked.connect(self.get_next_window(TaskWindow))
        self.pushButton.clicked.connect(self.check_answer)
        self.pushButton_2.clicked.connect(self.get_next_window(DecisionWindow))

    def check_answer(self):
        answer_value = check(self.textEdit.toPlainText(), self.number)
        if answer_value:
            self.get_next_window(CorrectAnswerWindow)()
        else:
            self.get_next_window(InCorrectAnswerWindow)()

    def get_next_window(self, name_window):
        def next_window():
            self.close()
            self.next_window = name_window()
            self.next_window.show()

        return next_window


class CorrectAnswerWindow(QMainWindow, Ui_CorrectAnswer):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.get_next_window(StartMenuWindow))
        self.pushButton_2.clicked.connect(self.get_next_window(TaskWindow))
        self.pushButton_3.clicked.connect(self.get_next_window(StatisticsWindow))

    def get_next_window(self, name_window):
        def next_window():
            self.close()
            self.next_window = name_window()
            self.next_window.show()

        return next_window


class InCorrectAnswerWindow(QMainWindow, Ui_InCorrectAnswer):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.get_next_window(StartMenuWindow))
        self.pushButton_2.clicked.connect(self.get_next_window(TaskWindow))
        self.pushButton_3.clicked.connect(self.get_next_window(AnswerWindow))
        self.pushButton_4.clicked.connect(self.get_next_window(DecisionWindow))
        self.task = read_file()
        self.link_task = giv_link_picture(self.task, "Task")

    def get_next_window(self, name_window):
        def next_window():
            self.close()
            self.next_window = name_window()
            self.next_window.show()

        return next_window


class DecisionWindow(QMainWindow, Ui_decision):
    def __init__(self):
        self.name_task = read_file()
        super().__init__()
        link_task = name_file.format("Res", self.name_task)
        self.setupUi(self)
        picture_on_lable(self, link_task)
        self.pushButton.clicked.connect(self.get_next_window(TaskWindow))
        self.pushButton_2.clicked.connect(self.get_next_window(StartMenuWindow))

    def get_next_window(self, name_window):
        def next_window():
            self.close()
            self.next_window = name_window()
            self.next_window.show()

        return next_window


class SettingWindow(QMainWindow, Ui_Settings):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.get_next_window(AddTaskWindow))
        self.pushButton_2.clicked.connect(self.get_next_window(StartMenuWindow))
        self.pushButton_3.clicked.connect(self.get_next_window(DelTaskWindow))
        self.pushButton_4.clicked.connect(self.get_next_window(ResetStatisticsWindow))

    def get_next_window(self, name_window):
        def next_window():
            self.close()
            self.next_window = name_window()
            self.next_window.show()

        return next_window


class AddTaskWindow(QMainWindow, Ui_AddTask):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.get_next_window(SettingWindow))
        self.pushButton.clicked.connect(self.add_task)

    def get_next_window(self, name_window):
        def next_window():
            self.close()
            self.next_window = name_window()
            self.next_window.show()

        return next_window

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
        self.pushButton_2.clicked.connect(self.get_next_window(SettingWindow))
        self.pushButton.clicked.connect(self.del_task)

    def del_task(self):
        del_in_db(self.textEdit.toPlainText())
        self.textEdit.setPlainText("Удалено")

    def get_next_window(self, name_window):
        def next_window():
            self.close()
            self.next_window = name_window()
            self.next_window.show()

        return next_window


class ResetStatisticsWindow(QMainWindow, Ui_ResetStatistics):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.get_next_window(SettingWindow))
        self.pushButton.clicked.connect(self.reset_statistics)

    def reset_statistics(self):
        reset_all_statistics()

    def get_next_window(self, name_window):
        def next_window():
            self.close()
            self.next_window = name_window()
            self.next_window.show()

        return next_window


class StatisticsWindow(QMainWindow, Ui_Statistics):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.get_statistics()
        self.pushButton.clicked.connect(self.get_next_window(StartMenuWindow))

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

    def get_next_window(self, name_window):
        def next_window():
            self.close()
            self.next_window = name_window()
            self.next_window.show()

        return next_window


class StartOptionWindow(QMainWindow, Ui_StartOption):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.get_next_window(StartMenuWindow))
        self.pushButton.clicked.connect(self.get_next_window(FirstAnswerWindow))

    def get_next_window(self, name_window):
        def next_window():
            self.close()
            self.next_window = name_window()
            self.next_window.show()

        return next_window


class FirstAnswerWindow(QMainWindow, Ui_FirstAnswerOption):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.radioButton_2.clicked.connect(self.get_next_window(SecondAnswerWindow))
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

    def open_answer_option_window(self):
        name = self.sender().text()
        self.close()
        self.open_answer_option = AnswerOptionWindow(1, name.split()[1])
        self.open_answer_option.show()

    def get_next_window(self, name_window):
        def next_window():
            self.close()
            self.next_window = name_window()
            self.next_window.show()

        return next_window


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

        self.radioButton.clicked.connect(self.get_next_window(FirstAnswerWindow))
        self.pushButton_10.clicked.connect(self.get_next_window(ResultOptionWindow))

    def get_next_window(self, name_window):
        def next_window():
            self.close()
            self.next_window = name_window()
            self.next_window.show()

        return next_window

    def open_answer_option_window(self):
        name = self.sender().text()
        self.close()
        self.open_answer_option = AnswerOptionWindow(2, name.split()[1])
        self.open_answer_option.show()


class ResultOptionWindow(QMainWindow, Ui_ResultOption):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.textEdit.setText(result_true_answer())
        self.pushButton.clicked.connect(self.get_next_window(StartMenuWindow))

    def get_next_window(self, name_window):
        def next_window():
            self.close()
            self.next_window = name_window()
            self.next_window.show()

        return next_window


class AnswerOptionWindow(QMainWindow, Ui_AnswerOption):
    def __init__(self, number_window, name_task):
        super().__init__()
        self.setupUi(self)
        self.link_task = giv_name_task(name_task)
        self.name_task = name_task
        if self.link_task == incorrect_answer:
            self.label.setText(incorrect_answer)
            self.textEdit.setReadOnly(True)
            self.pushButton.setEnabled(False)
        else:
            picture_on_lable(self, giv_link_picture(self.link_task, "Task"))

        if number_window == 1:
            self.pushButton_2.clicked.connect(self.get_next_window(FirstAnswerWindow))
        elif number_window == 2:
            self.pushButton_2.clicked.connect(self.get_next_window(SecondAnswerWindow))
        self.pushButton.clicked.connect(self.record_user_answer)

    def record_user_answer(self):
        text = self.textEdit.toPlainText()
        try:
            record_answer(text, self.name_task)
            self.textEdit.setText(correct_answer_option)
        except Exception:
            self.textEdit.setText(incorrect_answer_option)

    def get_next_window(self, name_window):
        def next_window():
            self.close()
            self.next_window = name_window()
            self.next_window.show()

        return next_window
