import sqlite3
from Handler import *

connect = sqlite3.connect("Task.db")
curs = connect.cursor()


def return_link_task():
    return curs.execute(f"""SELECT LinkTask FROM TaskAnswer""").fetchall()


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


def check_len_db():
    check_len = curs.execute(f"""
                SELECT * FROM Statistics
        """).fetchall()
    if len(check_len) == 0:
        if_db_is_clear()


def take_values():
    first_id = curs.execute(f"""
                SELECT * FROM Statistics WHERE id = 1
        """).fetchall()[0]
    return first_id


def check(user_answer, file_name):
    real_answer = curs.execute(f"""
                SELECT AnswerTask FROM TaskAnswer WHERE LinkTask = {file_name}
        """).fetchall()[0][0]
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
    try:
        curs.execute(f"""DELETE FROM TaskAnswer WHERE LinkTask == {name_task}""")
    except Exception:
        pass
    connect.commit()


def getting_statistics():
    all_information = curs.execute(f"""
                SELECT * FROM Statistics WHERE id = 1
        """).fetchall()[0]
    return all_information


def reset_all_statistics():
    curs.execute(f"""DELETE FROM Statistics WHERE id == 1""")
    connect.commit()


def clear_option_db():
    curs.execute(f"""DELETE FROM Option WHERE id >= 1""")
    connect.commit()


def len_option_db():
    return curs.execute(f"""
                SELECT * FROM Option
        """).fetchall()


def name_tasks(name_task):
    return curs.execute(f"""
                    SELECT name_img FROM Option WHERE id = {name_task}
            """).fetchall()


def record_answer(text, name_task):
    curs.execute(f"""
            UPDATE Option SET user_answer = {str(text)} WHERE id = {int(name_task)}
            """)
    connect.commit()


def all_in_option_db():
    return curs.execute(f"""
                SELECT * FROM Option
        """).fetchall()


def take_and_insert_answer_img(name_task):
    answer_img = curs.execute(f"""
                    SELECT AnswerTask FROM TaskAnswer WHERE LinkTask = {str(name_task)}
            """).fetchall()[0][0]
    curs.execute(f"""
                                INSERT INTO Option(id, name_img, answer_img, user_answer) VALUES({name_task.split('.')[0]}, {name_task}, {str(answer_img)}, '')
                                """)
    connect.commit()
