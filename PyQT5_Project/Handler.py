import random
import os
import sqlite3

connect = sqlite3.connect("Task.db")
curs = connect.cursor()


def check_gif_task(number):
    result = []
    Res = os.listdir("Task-Res\Res")
    Task = os.listdir("Task-Res\Task")
    Res = list(set(Res) & set(Task))
    Task[:] = Res[:]
    array = []
    for i in range(len(Res)):
        if Res[i].split('.')[0] != number:
            continue
        array.append(Res[i])
    Res[:] = array[:]
    if len(Res) == 0:
        return 0
    array = curs.execute(f"""SELECT LinkTask FROM TaskAnswer""").fetchall()
    for i in range(len(array)):
        if array[i][0].split('.')[0] == number:
            result.append(array[i][0])
    Task = result[random.randint(0, len(result) - 1)]

    Task += ".png"
    if Task in Res:
        return Task


def input_in_db(file_name, user_answer):
    number = curs.execute(f"""
            SELECT id FROM TaskAnswer WHERE LinkTask = {file_name}
    """).fetchall()
    if len(number) == 0:
        curs.execute(f"""
                INSERT INTO TaskAnswer(LinkTask, AnswerTask) VALUES({file_name}, {user_answer})
                """)
    else:
        curs.execute(f"""DELETE FROM TaskAnswer WHERE id == {number[0][0]}""")
        curs.execute(f"""
                INSERT INTO TaskAnswer(LinkTask, AnswerTask) VALUES({file_name}, {user_answer})
                """)
    connect.commit()


def if_db_is_clear():
    curs.execute(f"""
                    INSERT INTO Statistics(number_of_tasks, correct_answer, incorrect_answer) VALUES(0, 0, 0)
                    """)
    connect.commit()


def take_values():
    first_id = curs.execute(f"""
                SELECT * FROM Statistics WHERE id = 1
        """).fetchall()[0]
    return first_id


def check(user_answer, file_name):
    file_name = file_name[14:len(file_name) - 4]
    real_answer = curs.execute(f"""
                SELECT AnswerTask FROM TaskAnswer WHERE LinkTask = {file_name}
        """).fetchall()[0][0]
    check_len_db = curs.execute(f"""
                SELECT * FROM Statistics
        """).fetchall()
    if len(check_len_db) == 0:
        if_db_is_clear()
    curs.execute(f"""
            UPDATE Statistics SET number_of_tasks = {take_values()[1] + 1} WHERE id = 1
            """)
    if str(real_answer) == str(user_answer):
        curs.execute(f"""
                UPDATE Statistics SET correct_answer = {take_values()[2] + 1} WHERE id = 1
                """)
        answer_value = True

    else:
        curs.execute(f"""
                UPDATE Statistics SET incorrect_answer = {take_values()[3] + 1} WHERE id = 1
                """)
        answer_value = False
    connect.commit()
    return answer_value
