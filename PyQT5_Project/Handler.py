import random
import os
import sqlite3
<<<<<<< HEAD

print()
connect = sqlite3.connect("Task.db")
curs = connect.cursor()


def checkAndGifTask(number):
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


def inputInDB(FileName, Answer):
    number = curs.execute(f"""
            SELECT id FROM TaskAnswer WHERE LinkTask = {FileName}
    """).fetchall()
    if len(number) == 0:
        curs.execute(f"""
                INSERT INTO TaskAnswer(LinkTask, AnswerTask) VALUES({FileName}, {Answer})
                """)
    else:
        curs.execute(f"""DELETE FROM TaskAnswer WHERE id == {number[0][0]}""")
        curs.execute(f"""
                INSERT INTO TaskAnswer(LinkTask, AnswerTask) VALUES({FileName}, {Answer})
                """)
    connect.commit()


def Check(answerUser, FileName):
    FileName = FileName[14:len(FileName) - 4]
    realAnswer = curs.execute(f"""
                SELECT AnswerTask FROM TaskAnswer WHERE LinkTask = {FileName}
        """).fetchall()[0][0]

    if str(realAnswer) == str(answerUser):
        curs.execute(f"""
                INSERT INTO Statistics(ALL, Tr, Fa) VALUES(0, 0, 0)
                """)

    connect.commit()
