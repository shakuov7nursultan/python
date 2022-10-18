import db_tools as db
import view_result as vr
import sqlite3 as sl
import logger as log


def db_repotrs(db_name):
    marker = 1
    is_OK = True
    while is_OK:
        vr.view("Текущая база данных: ", db_name)
        marker = vr.input_data(
            " Press 1 - Общий перечень. Имена с оценками по всем предметам \n press 2 - средний балл \n press 3 - ввести свой запрос к БД \n press 4 - to previous menu\n: "
        )
        log.logger("User klick", marker)

        match marker:
            case "1":
                input_str = "SELECT name,  MATHEMATICS, RUSSIAN, HISTORY FROM PUPILS, ESTIMATE  WHERE pupil_id = PUPILS.id"
                log.logger("User print report: ", input_str)
                print("NAME | MATHEMATICS | RUSSIAN | HISTORY")
                db.print_str_db(db_name, input_str)

            case "2":
                input_str = "SELECT name,  MATHEMATICS, RUSSIAN, HISTORY FROM PUPILS, ESTIMATE  WHERE pupil_id = PUPILS.id"
                log.logger("User print report: ", input_str)
                calculation_arithmetic_mean(db_name, input_str)

            case "3":
                input_str = vr.input_data(
                    "Введите запрос, например ('SELECT * FROM pupils;'): "
                )
                log.logger("User print report: ", input_str)
                db.print_str_db(db_name, input_str)
            case "4":
                log.logger("Exit previous menu", "")
                is_OK = False
            case _:
                print("Error")
    is_OK = True


def calculation_arithmetic_mean(db_name, input_str):
    con = sl.connect(db_name)
    cur = con.cursor()
    cur.execute("{}".format(input_str))
    for i in cur:
        mean = (int(i[1]) + int(i[2]) + int(i[3])) / 3
        print("Ученик {}, средний балл: {:3.1f}".format(i[0], mean))
