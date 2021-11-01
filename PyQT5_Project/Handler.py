import random
import os
import sqlite3

connect = sqlite3.connect("Task.db")
curs = connect.cursor()


def check_gif_task(number):
    result = []
    array_on_res = os.listdir("Task-Res\Res")
    array_on_task = os.listdir("Task-Res\Task")
    array_on_res = list(set(array_on_res) & set(array_on_task))
    array_on_task[:] = array_on_res[:]
    array = []
    for i in range(len(array_on_res)):
        if array_on_res[i].split('.')[0] != number:
            continue
        array.append(array_on_res[i])
    array_on_res[:] = array[:]
    if len(array_on_res) == 0:
        return 0
    array = curs.execute(f"""SELECT LinkTask FROM TaskAnswer""").fetchall()
    for i in range(len(array)):
        if array[i][0].split('.')[0] == number:
            result.append(array[i][0])
    array_on_task = result[random.randint(0, len(result) - 1)]

    array_on_task += ".png"
    if array_on_task in array_on_res:
        return array_on_task


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


def del_in_db(name_task):
    print(1)
    all_task = curs.execute(f"""
                SELECT LinkTask FROM TaskAnswer WHERE id >= 1
        """).fetchall()
    all_task = list_link_task(all_task)
    if name_task in all_task:
        curs.execute(f"""DELETE FROM TaskAnswer WHERE LinkTask == {name_task}""")
    connect.commit()


def list_link_task(array):
    result_list = []
    for i in array:
        result_list.append(i[0])
    return result_list
