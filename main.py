import sys
import numpy as np
import re
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QWidget, QStackedWidget
from PyQt6.QtCore import *
from faker import Faker
import csv
from class_files.break_three import Ui_BreakThreeForm
from class_files.firstWindow import Ui_Form
import math
from class_files.secondWindow import Second_Form
from class_files.test_fifth import Ui_TestFifthForm
from class_files.test_fifth2 import Ui_TestFifth2Form
from class_files.test_fourth import Ui_TestFourthForm
from class_files.thirdWindow import Ui_Third_Form
from class_files.exerciseFirst import Exercise_First_Form
from class_files.question import Question_Form
from class_files.exerciseSecondForm import ExerciseSecondForm
from class_files.breakWindow import BreakForm
from class_files.test_info_first import TestInfoFirstForm
from class_files.test_first import TestFirstForm
from class_files.test_second import Ui_TestSecondForm
from class_files.test_third import Third_Form
from class_files.break_two import Ui_BreakTwoForm
from class_files.test_fourth import Ui_TestFourthForm
from class_files.test_fourth2 import Ui_TestFourth2Form
from class_files.break_three import Ui_BreakThreeForm
from class_files.test_fifth import Ui_TestFifthForm
from class_files.test_fifth2 import Ui_TestFifth2Form
from class_files.test_fifth_break import Ui_TestFifthBreakForm
from class_files.test_answer_fifth import Ui_TestFifthAnswerForm
from class_files.break_fourth import Ui_BreakFourthForm
from class_files.test_sixth import Ui_TestSixthForm
from class_files.test_sixth_break import Ui_TestSixthBreakForm
from class_files.test_answer_sixth import Ui_TestSixthAnswerForm
from class_files.final import Ui_FinallForm


people_data = {}
words = []
def add_person_data(fio, age, sex):
    global people_data
    people_data = {
        'FIO': fio,
        'Age': age,
        'Gender': sex,
        'Tasks': {'Task1': {},
                  'Task2': {},
                  'Task3': {},
                  'Task4': {},
                  'Task5': {},
                  'Task6': {}}  # Здесь будут храниться данные о задачах для данного человека
    }
    #print(people_data)


def levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]


class firstWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.open_second_window)

    def open_second_window(self):
        widget.addWidget(secondWindow())
        widget.setCurrentIndex(widget.currentIndex() + 1)



class secondWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Second_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.registry)

    def registry(self):

        # подключиться к базе данных и вытащить айдишники из таблицы  # Генерация уникального идентификатора БАЗА ДАННЫХ

        # проверка типа введенных данных

        fio = self.ui.FIOlineEdit.text()
        fio_parts = fio.split()
        if not isinstance(fio, str) or (len(fio_parts) != 3 and len(fio_parts) != 2) or not all(
                part.isalpha() for part in fio_parts):
            self.show_error_dialog("ui/FIOError.ui")
            self.ui.FIOlineEdit.clear()
            return

        try:
            age = int(self.ui.AgelineEdit.text())
        except ValueError:
            self.show_error_dialog("ui/AgeError.ui")
            self.ui.AgelineEdit.clear()
            return
        if age >= 100 or age <= 8:
            self.show_error_dialog("ui/AgeError.ui")
            self.ui.AgelineEdit.clear()
            return

        sex = self.ui.Gender.currentText()
        if not sex:
            self.show_error_dialog("ui/SexError.ui")
            self.ui.Gender.setCurrentIndex(0)
            return

        add_person_data(fio, age, sex)
        self.open_third_window()
    def show_error_dialog(self, ui_file):
        dialog = QDialog()
        uic.loadUi(ui_file, dialog)
        dialog.exec()

    def open_third_window(self):
        widget.addWidget(thirdWindow())
        widget.setCurrentIndex(widget.currentIndex() + 1)

class thirdWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Third_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.open_exercise_first)

    def open_exercise_first(self):
        widget.addWidget(exerciseFirstWindow())
        widget.setCurrentIndex(widget.currentIndex() + 1)



class exerciseFirstWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Exercise_First_Form()
        self.ui.setupUi(self)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.time_remaining = QTime(0, 100)
        self.timer.start(1000)
        self.update_timer()
        self.ui.pushButton.clicked.connect(self.first_task)

    def update_timer(self):
        self.time_remaining = self.time_remaining.addSecs(-1)
        if self.time_remaining == QTime(0,0):
            self.timer.stop()
    def first_task(self):
        time_out = (self.timer.remainingTime()) / 100
        if time_out < 0:
            time_out = 0.0 #исрпваить ведь прошедшее время 5 минут
        answer_first = -1000000
        answer_second = -1000000
        answer_third = -1000000
        counter = 0
        ui_name = "ui/Task1Error.ui"
        # проверка типа введенных данных
        try:
            answer_first = int(self.ui.AnswerFirstlineEdit.text())
        except ValueError:
            self.show_error_dialog(ui_name)
            self.ui.AnswerFirstlineEdit.clear()
            return

        try:
            answer_second = int(self.ui.AnswerSecondlineEdit.text())
        except ValueError:
            self.show_error_dialog(ui_name)
            self.ui.AnswerSecondlineEdit.clear()
            return

        try:
            answer_third = int(self.ui.AnswerThirdlineEdit.text())
        except ValueError:
            self.show_error_dialog(ui_name)
            self.ui.AnswerThirdlineEdit.clear()
            return
        if answer_first != 9:
            counter += 1
        if answer_second != 3:
            counter += 1
        if answer_third != 54:
            counter += 1
        #print(people_data)
        self.open_question_window()

    def show_error_dialog(self, ui_file):
        dialog = QDialog()
        uic.loadUi(ui_file, dialog)
        dialog.exec()

    def open_question_window(self):
        widget.addWidget(questionWindow("exercise_Second"))
        widget.setCurrentIndex(widget.currentIndex() + 1)


class questionWindow(QWidget):
    def __init__(self, next_window):
        super().__init__()
        self.ui = Question_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.answer)
        self.next_window = next_window

    def answer(self):
        if self.ui.comboBox.currentText() == 'Нет':
            flag = 0
        else:
            flag = 1
        # if self.next_window == "exercise_Second":
        #     people_data['Tasks']['Task1']["Question"] = flag
        # elif self.next_window == "break_Window":
        #     people_data['Tasks']['Task2']['Question'] = flag
        if self.next_window == "TestSecond":
            people_data['Tasks']['Task1']['Question'] = flag
        elif self.next_window == "TestThird":
            people_data['Tasks']['Task2']['Question'] = flag
        elif self.next_window == "BreakTwo":
            people_data['Tasks']['Task3']['Question'] = flag
        elif self.next_window == "BreakThree":
            people_data['Tasks']['Task4']['Question'] = flag
        elif self.next_window == 'BreakFourth':
            people_data['Tasks']['Task5']['Question'] = flag
        elif self.next_window == 'Finall':
            people_data['Tasks']['Task6']['Question'] = flag
        #print(people_data)
        self.open_next_window()
    def open_next_window(self):
        if self.next_window == "exercise_Second":
            widget.addWidget(exerciseSecondWindow())
            # self.exercise_second.show()
        elif self.next_window == "break_Window":
            widget.addWidget(break_window())
        elif self.next_window == "TestSecond":
            widget.addWidget(TestSecond())
        elif self.next_window == "TestThird":
            widget.addWidget(TestThird())
            widget.setFixedWidth(990)
            widget.setFixedHeight(700)
        elif self.next_window == "BreakTwo":
            widget.addWidget(BreakTwo())
        elif self.next_window == "BreakThree":
            widget.addWidget(BreakThree())
        elif self.next_window == 'BreakFourth':
            widget.addWidget(BreakFourth())
        elif self.next_window == 'Finall':
            widget.addWidget(Finall())
            widget.setFixedWidth(800)
            widget.setFixedHeight(600)
        # self.hide()
        widget.setCurrentIndex(widget.currentIndex()+1)


class exerciseSecondWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = ExerciseSecondForm()
        self.ui.setupUi(self)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.time_remaining = QTime(0, 100)
        self.timer.start(1000)
        self.update_timer()
        self.ui.pushButton.clicked.connect(self.secondTask)

    def update_timer(self):
        self.time_remaining = self.time_remaining.addSecs(-1)
        if self.time_remaining == QTime(0,0):
            self.timer.stop()
            self.ui.ExerciseSecondtextEdit.setDisabled(True)

    def secondTask(self):
        time_out = (self.timer.remainingTime()) / 100
        if time_out < 0:
            time_out = 0.0
        dictionary = self.ui.ExerciseSecondtextEdit.toPlainText()
        tmp = ("Вечер зашел своим серебрянным мантием"
               ", и воздух наполнился запахом свежеиспеченного хлеба"
               ", витающего в воздухе, как нежное прикосновение."
               " Люди торопились по улицам, суетливо встречаясь и прощаясь, "
               "словно вечернее представление на большой сцене, где каждый "
               "игрок исполнял свою роль беззаботно, не подозревая, что за "
               "кулисами их ждет неизвестность.")
        if dictionary.strip() == "":
            self.show_error_dialog()
            self.ui.ExerciseSecondtextEdit.setPlainText(
                "Вечер зашел своим серебрянным мантием,"
                " и воздух наполнился запахом свежеиспеченого хлеба, "
                "витающего в воздухе, как нежное прикосновение; люди торопились"
                " по улицам, суетливо встречаясь и прощаясь, словно вечернее "
                "представление на большой сцене, где каждый игрок исполнял свою "
                "роль беззаботно, не подозревая, что за кулисами их ждет неизвестность.")
            return
        if dictionary.strip() != tmp.strip():
            errors = levenshtein_distance(dictionary, tmp)
        else:
            errors = 0

        #print(people_data)
        self.open_question_window()

    def show_error_dialog(self):
        dialog = QDialog()
        uic.loadUi("Task2Error.ui", dialog)
        dialog.exec()



    def open_question_window(self):
        widget.addWidget(questionWindow("break_Window"))
        widget.setCurrentIndex(widget.currentIndex() + 1)

class break_window(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = BreakForm()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.open_test_info_first)

    def open_test_info_first(self):
        widget.addWidget(test_info_first())
        widget.setCurrentIndex(widget.currentIndex() + 1)

class test_info_first(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = TestInfoFirstForm()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.open_test_first)

    def open_test_first(self):
        widget.addWidget(test_first())
        widget.setCurrentIndex(widget.currentIndex() + 1)

class test_first(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = TestFirstForm()
        self.ui.setupUi(self)
        self.generate_questions()
        self.timer = QTimer()
        self.elapse = []
        self.elapsed_timer = QElapsedTimer()
        self.timer.timeout.connect(self.update_timer)
        self.time_remaining = QTime(0,1)
        self.elapsed_timer.start()
        self.timer.start(1000)
        self.update_timer()
        self.ui.pushButton.clicked.connect(self.open_question_window)

    def update_timer(self):
        self.time_remaining = self.time_remaining.addSecs(-1)
        self.ui.label.setText(self.time_remaining.toString(Qt.DateFormat.ISODate))
        if self.time_remaining == QTime(0,0):
            self.timer.stop()
            self.validate_answers()
            self.ui.AnswerFirstlineEdit.setDisabled(True)
            self.ui.AnswerSecondlineEdit.setDisabled(True)
            self.ui.AnswerThirdlineEdit.setDisabled(True)

    def generate_questions(self):
        # Генерируем три случайных арифметических выражения
        self.expression1 = f"{np.random.randint(1, 10)} + {np.random.randint(1, 10)}"
        self.expression2 = f"{np.random.randint(1, 10)} - {np.random.randint(1, 10)}"
        self.expression3 = f"{np.random.randint(1, 10)} * {np.random.randint(1, 10)}"

        # Вычисляем результаты выражений
        self.result1 = eval(self.expression1)
        self.result2 = eval(self.expression2)
        self.result3 = eval(self.expression3)

        # Записываем выражения в метки (labels)
        self.ui.label_2.setText(self.expression1 + " = ")
        self.ui.label_3.setText(self.expression2 + " = ")
        self.ui.label_4.setText(self.expression3 + " = ")

    def is_integer(self,s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def validate_answers(self):
        error = 0
        time_out = self.elapsed_timer.elapsed() / 1000
        self.elapse.append(time_out)
        self.timer.stop()
        # if time_out < 0:
        #     time_out = 60.0
        answer_first = self.ui.AnswerFirstlineEdit.text()
        answer_second = self.ui.AnswerSecondlineEdit.text()
        answer_third = self.ui.AnswerThirdlineEdit.text()

        # Сравниваем ответы пользователя с эталонными
        if not self.is_integer(answer_first.strip()) or int(answer_first) != self.result1:
            error += 1
        if not self.is_integer(answer_second.strip()) or int(answer_second) != self.result2:
            error += 1
        if not self.is_integer(answer_third.strip()) or int(answer_third) != self.result3:
            error += 1

        if error >= 0:
            people_data['Tasks']['Task1']['Error'] = error
        people_data['Tasks']['Task1']['Error'] = error
        people_data['Tasks']['Task1']['Time'] = self.elapse[0]

        #print(people_data)


    def open_question_window(self):
        self.validate_answers()
        widget.addWidget(questionWindow("TestSecond"))
        widget.setCurrentIndex(widget.currentIndex() + 1)

class TestSecond(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TestSecondForm()
        self.ui.setupUi(self)
        self.elapse = []
        self.elapsed_timer = QElapsedTimer()
        self.equations = []
        self.generate_random_equations()  # генерим рандомные уравнения
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.time_remaining = QTime(0, 5)
        self.timer.start(1000)
        self.elapsed_timer.start()
        self.update_timer()
        self.extract_coefficients()  # разделяем на коэфы
        self.solve_equation()  # ищем решение
        self.ui.pushButton.clicked.connect(self.open_question_window)

    def update_timer(self):
        self.time_remaining = self.time_remaining.addSecs(-1)
        self.ui.label.setText(self.time_remaining.toString(Qt.DateFormat.ISODate))
        if self.time_remaining == QTime(0, 0):
            self.timer.stop()
            self.validate_answers()
            self.ui.AnswerTestSecondlineEdit.setDisabled(True)

    def generate_random_equations(self):
        while True:
            coefficients = np.random.randint(-10, 11, size=(2, 2))
            #print(coefficients)
            results = np.random.randint(-10, 10, size=2)
            if np.linalg.matrix_rank(coefficients) == 2:
                break
        for i in range(2):
            x_part = f"{coefficients[i, 0]}x"
            y_part = f"{'+' if coefficients[i, 1] >= 0 else ''}{coefficients[i, 1]}y"
            equation = f"{x_part} {y_part} = {results[i]}"
            self.equations.append(equation)
        # Displaying equations in UI labels
        self.ui.label_6.setText(self.equations[0])
        self.ui.label_7.setText(self.equations[1])

    def extract_coefficients(self):
        self.coefficient_matrix = []
        self.result_matrix = []
        for equation in self.equations:
            equation = equation.replace(' ', '')
            coefficients = list(map(int, re.findall(r'[-+]?\d+', equation.split('=')[0])))
            result = int(equation.split('=')[1].strip())
            self.coefficient_matrix.append(coefficients)
            self.result_matrix.append(result)

    def solve_equation(self):
        self.coefficient_matrix = np.array(self.coefficient_matrix)
        self.result_matrix = np.array(self.result_matrix)
        self.solutions = np.linalg.solve(self.coefficient_matrix, self.result_matrix)

    def validate_answers(self):
        error = 0
        self.timer.stop()
        time_out = (self.elapsed_timer.elapsed()) / 1000
        self.elapse.append(time_out)
        # Получаем ответы пользователя
        user_answers = []
        for item in self.ui.AnswerTestSecondlineEdit.text().split(', '):
            try:
                x = float(item)
                user_answers.append(x)
            except ValueError:
                user_answers.append(-10000000)

        # Проверяем, совпадают ли ответы пользователя с решениями уравнений
        #print(user_answers)
        for i, solution in enumerate(self.solutions):
            if len(user_answers) < (i+1):
                error += abs(i - len(self.solutions))
                break
            if round(solution, 1) != user_answers[i]:
                    error += 1
                    #print(solution)
        people_data['Tasks']['Task2']['Error'] = error
        people_data['Tasks']['Task2']['Time'] = self.elapse[0]

    def open_question_window(self):
        self.validate_answers()
        widget.addWidget(questionWindow("TestThird"))
        widget.setCurrentIndex(widget.currentIndex() + 1)

#след задача
class TestThird(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Third_Form()
        self.ui.setupUi(self)
        self.elapse = []
        self.elapsed_timer = QElapsedTimer()
        self.equations = []
        self.generate_random_equations()  # генерим рандомные уравнения
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.time_remaining = QTime(0, 7)
        self.timer.start(1000)
        self.elapsed_timer.start()
        self.update_timer()
        self.extract_coefficients()  # разделяем на коэфы
        self.solve_equation()  # ищем решение
        self.ui.pushButton.clicked.connect(self.open_question_window)

    def update_timer(self):
        self.time_remaining = self.time_remaining.addSecs(-1)
        self.ui.label.setText(self.time_remaining.toString(Qt.DateFormat.ISODate))
        if self.time_remaining == QTime(0, 0):
            self.timer.stop()
            self.validate_answers()
            self.ui.AnswerTestThirdlineEdit.setDisabled(True)
            self.ui.ExerciseThirdtextEdit.setDisabled(True)

    def generate_random_equations(self):
        while True:
            coefficients = np.random.randint(-10, 11, size=(2, 2))
            #print(coefficients)
            results = np.random.randint(-10, 10, size=2)
            if np.linalg.matrix_rank(coefficients) == 2:
                break
        for i in range(2):
            x_part = f"{coefficients[i, 0]}x"
            y_part = f"{'+' if coefficients[i, 1] >= 0 else ''}{coefficients[i, 1]}y"
            equation = f"{x_part} {y_part} = {results[i]}"
            self.equations.append(equation)
        # Displaying equations in UI labels
        self.ui.label_7.setText(self.equations[0])
        self.ui.label_8.setText(self.equations[1])

    def extract_coefficients(self):
        self.coefficient_matrix = []
        self.result_matrix = []
        for equation in self.equations:
            equation = equation.replace(' ', '')
            coefficients = list(map(int, re.findall(r'[-+]?\d+', equation.split('=')[0])))
            result = int(equation.split('=')[1].strip())
            self.coefficient_matrix.append(coefficients)
            self.result_matrix.append(result)

    def solve_equation(self):
        self.coefficient_matrix = np.array(self.coefficient_matrix)
        self.result_matrix = np.array(self.result_matrix)
        self.solutions = np.linalg.solve(self.coefficient_matrix, self.result_matrix)

    def validate_answers(self):
        error = 0
        self.timer.stop()
        time_out = (self.elapsed_timer.elapsed()) / 1000
        self.elapse.append(time_out)
        # Получаем ответы пользователя
        user_answers = []
        for item in self.ui.AnswerTestThirdlineEdit.text().split(', '):
            try:
                x = float(item)
                user_answers.append(x)
            except ValueError:
                user_answers.append(-10000000)

        # Проверяем, совпадают ли ответы пользователя с решениями уравнений
        for i, solution in enumerate(self.solutions):
            if len(user_answers) < (i+1):
                error += abs(i - len(self.solutions))
                break
            if round(solution, 1) != user_answers[i]:
                    error += 1

        #print(error)
        dictionary = self.ui.ExerciseThirdtextEdit.toPlainText()
        tmp = ("Психология - это увлекательное путешествие в глубины человеческой души. "
               "Она исследует тайны ума, разгадывает загадки поведения и помогает нам "
               "понять себя и окружающих. В мире психологии мы изучаем, как мы мыслим, "
               "чувствуем и взаимодействуем друг с другом. Это наука, которая помогает "
               "нам стать лучше, обрести гармонию с собой и окружающим миром. Погружаясь "
               "в психологию, мы расширяем горизонты своего понимания и открываем новые "
               "возможности для личностного роста и развития. Она даёт ключи к разгадке "
               "наших собственных мыслей, чувств и поведения, помогая нам стать более"
               " осознанными и счастливыми людьми.")
        if dictionary.strip() != tmp.strip():
            error += levenshtein_distance(dictionary, tmp)
            #print(error)

        people_data['Tasks']['Task3']['Error'] = error
        people_data['Tasks']['Task3']['Time'] = self.elapse[0]
    def open_question_window(self):
        self.validate_answers()
        widget.addWidget(questionWindow("BreakTwo"))
        widget.setFixedWidth(650)
        widget.setFixedHeight(500)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class BreakTwo(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_BreakTwoForm() # не запутався лублу кисинечека
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.open_test_fourth)

    def open_test_fourth(self):
        widget.addWidget(test_fourth())
        widget.setCurrentIndex(widget.currentIndex() + 1)

class test_fourth(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TestFourthForm()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.open_test_fourth)
    def open_test_fourth(self):
        widget.addWidget(TestFourth2())
        widget.setFixedWidth(800)
        widget.setFixedHeight(600)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class TestFourth2(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TestFourth2Form()
        self.ui.setupUi(self)
        self.timer = QTimer()
        self.elapse = []
        self.elapsed_timer = QElapsedTimer()
        self.timer.timeout.connect(self.update_timer)
        self.time_remaining = QTime(0, 100)
        self.timer.start(1000)
        self.elapsed_timer.start()
        self.update_timer()
        self.ui.pushButton.clicked.connect(self.open_question_window)

    def update_timer(self):
        self.time_remaining = self.time_remaining.addSecs(-1)
        if self.time_remaining == QTime(0, 0):
            self.timer.stop()
            self.ui.AnswerTestFourthlineEdit.setDisabled(True)

    def validate_answers(self):
        # Получаем текст из поля ввода
        # self.timer.stop()
        error = 0
        # time_out = self.elapsed_timer.elapsed() / 1000
        # self.elapse.append(time_out)
        self.user_input = self.ui.AnswerTestFourthlineEdit.text()
        if len(self.user_input) == 0:
            people_data['Tasks']['Task4']['Error'] = 9
            return
        self.user_input_int_array = []
        for item in self.user_input.split(', '):
            try:
                x = int(item)
                self.user_input_int_array.append(x)
            except ValueError:
                self.user_input_int_array.append(-1)
        #print(self.user_input_int_array)


        # Заданная идеальная последовательность
        tmp = [3, 4, 5, 1, 2, 6, 8, 9, 7]
        for i in range(len(tmp)):
            if len(self.user_input_int_array) < (i+1):
                error += abs(len(tmp) - len(self.user_input_int_array))
                break
            if self.user_input_int_array[i] != tmp[i]:
                error += 1

        people_data['Tasks']['Task4']['Error'] = error

    def open_question_window(self):
        self.timer.stop()
        time_out = self.elapsed_timer.elapsed() / 1000
        self.elapse.append(time_out)
        people_data['Tasks']['Task4']['Time'] = self.elapse[0]
        self.validate_answers()
        widget.addWidget(questionWindow("BreakThree"))
        widget.setFixedWidth(650)
        widget.setFixedHeight(500)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class BreakThree(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_BreakThreeForm()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.open_test_fifth)

    def open_test_fifth(self):
        widget.addWidget(test_fifth())
        widget.setCurrentIndex(widget.currentIndex() + 1)

class test_fifth(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TestFifthForm()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.open_test_fifth)
    def open_test_fifth(self):
        widget.addWidget(TestFifth())
        widget.setCurrentIndex(widget.currentIndex() + 1)

class TestFifth(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TestFifth2Form()
        self.ui.setupUi(self)
        self.original_words = []
        self.generate_words()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.time_remaining = QTime(0, 1)
        self.timer.start(1000)
        self.update_timer()

    def update_timer(self):
        self.time_remaining = self.time_remaining.addSecs(-1)
        self.ui.label_9.setText(self.time_remaining.toString(Qt.DateFormat.ISODate))
        if self.time_remaining == QTime(0, 0):
            self.timer.stop()
            self.ui.label.setDisabled(True)
            self.ui.label_2.setDisabled(True)
            self.ui.label_3.setDisabled(True)
            self.ui.label_4.setDisabled(True)
            self.ui.label_5.setDisabled(True)
            self.ui.label_6.setDisabled(True)
            self.ui.label_7.setDisabled(True)
            widget.addWidget(test_fifth_break(self.original_words))
            widget.setCurrentIndex(widget.currentIndex() + 1)

    def generate_words(self):
        fake = Faker()
        random_words = [fake.word() for _ in range(7)]
        self.original_words = random_words
        #print(self.original_words)
        # Выводим слова в соответствующие QLabel
        labels = [
            self.ui.label, self.ui.label_2, self.ui.label_3,
            self.ui.label_4, self.ui.label_5, self.ui.label_6,
            self.ui.label_7
        ]
        for label, word in zip(labels, random_words):
            label.setText(word)


class test_fifth_break(QWidget):
    def __init__(self, original_words):
        super().__init__()
        self.ui = Ui_TestFifthBreakForm()
        self.ui.setupUi(self)
        self.original_words = original_words
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.time_remaining = QTime(0, 3)
        self.timer.start(1000)
        self.update_timer()

    def update_timer(self):
        self.time_remaining = self.time_remaining.addSecs(-1)
        self.ui.label_2.setText(self.time_remaining.toString(Qt.DateFormat.ISODate))
        if self.time_remaining == QTime(0, 0):
            self.timer.stop()
            #print(self.original_words)
            widget.addWidget(test_answer_fifth(self.original_words))
            widget.setCurrentIndex(widget.currentIndex() + 1)

class test_answer_fifth(QWidget):
    def __init__(self, original_words):
        super().__init__()
        self.ui = Ui_TestFifthAnswerForm()
        self.ui.setupUi(self)
        self.elapse = []
        self.elapsed_timer = QElapsedTimer()
        self.words_count = 0
        self.original_words = original_words  # Сохраняем оригинальные слова
        self.generated_words = self.generate_words()
        self.list_of_words = []
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.time_remaining = QTime(0, 100)
        self.timer.start(1000)
        self.elapsed_timer.start()
        self.update_timer()
        #self.ui.pushButton.clicked.connect(self.open_question_window)
        # Создаем кнопки и присваиваем им текст
        self.buttons = []
        #print(self.original_words)
        for i in range(1, 18):
            button = getattr(self.ui, f"pushButton_{i}")
            button.setText(self.generated_words[i - 1])
            button_text = button.text()
            #print(button_text)
            button.clicked.connect(lambda _, text=button_text: self.add_word_to_dict(text))

    def update_timer(self):
        self.time_remaining = self.time_remaining.addSecs(-1)
        if self.time_remaining == QTime(0, 0):
            self.timer.stop()
            self.compare_lists()

    def add_word_to_dict(self, word):
        self.list_of_words.append(word)
        self.words_count += 1
        if self.words_count == 7:
            self.open_question_window()
            #print('mat')
        #print(self.list_of_words)
        #print(word)


    def open_question_window(self):
        error = self.compare_lists()
        self.timer.stop()
        time_out = (self.elapsed_timer.elapsed()) / 1000
        self.elapse.append(time_out)
        people_data['Tasks']['Task5']['Time'] = self.elapse[0]
        people_data['Tasks']['Task5']['Error'] = error

        # self.question_window = questionWindow("BreakFourth")
        # self.question_window.show()
        # self.hide()
        widget.addWidget(questionWindow("BreakFourth"))
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def generate_words(self):
        all_words = self.original_words.copy()
        fake = Faker()
        random_words = [fake.word() for _ in range(10)]
        all_words += random_words

        np.random.shuffle(all_words)  # Перемешиваем список
        return all_words


    def compare_lists(self):

        set_original_words = set(self.original_words)
        set_list_of_words = set(self.list_of_words)
        differences = 7 - len(set_original_words.intersection(set_list_of_words))

        #print(people_data)
        return differences

class BreakFourth(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_BreakFourthForm()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.open_test_sixth)

    def open_test_sixth(self):
        widget.addWidget(TestSixth())
        widget.setCurrentIndex(widget.currentIndex() + 1)

class TestSixth(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TestSixthForm()
        self.ui.setupUi(self)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.time_remaining = QTime(0, 1)
        self.timer.start(1000)
        self.update_timer()

    def update_timer(self):
        self.time_remaining = self.time_remaining.addSecs(-1)
        self.ui.label_9.setText(self.time_remaining.toString(Qt.DateFormat.ISODate))
        if self.time_remaining == QTime(0, 0):
            self.timer.stop()
            widget.addWidget(test_sixth_break())
            widget.setFixedWidth(650)
            widget.setFixedHeight(500)
            widget.setCurrentIndex(widget.currentIndex() + 1)

class test_sixth_break(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TestSixthBreakForm()
        self.ui.setupUi(self)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.time_remaining = QTime(0, 3)
        self.timer.start(1000)
        self.update_timer()

    def update_timer(self):
        self.time_remaining = self.time_remaining.addSecs(-1)
        self.ui.label_2.setText(self.time_remaining.toString(Qt.DateFormat.ISODate))
        if self.time_remaining == QTime(0, 0):
            self.timer.stop()
            widget.addWidget(test_answer_sixth())
            widget.setFixedWidth(800)
            widget.setFixedHeight(600)
            widget.setCurrentIndex(widget.currentIndex() + 1)
            self.hide()

class test_answer_sixth(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TestSixthAnswerForm()
        self.ui.setupUi(self)
        self.timer = QTimer()
        self.elapse = []
        self.elapsed_timer = QElapsedTimer()
        self.timer.timeout.connect(self.update_timer)
        self.time_remaining = QTime(0, 100)
        self.timer.start(1000)
        self.elapsed_timer.start()
        self.update_timer()
        self.ui.pushButton.clicked.connect(self.open_question_window)

    def update_timer(self):
        self.time_remaining = self.time_remaining.addSecs(-1)
        if self.time_remaining == QTime(0, 0):
            self.timer.stop()
            self.chek_answer()
            self.ui.AnswerlineEdit.setDisabled(True)

    def chek_answer(self):
        error = 0

        self.user_input = self.ui.AnswerlineEdit.text()
        if len(self.user_input) == 0:
            people_data['Tasks']['Task6']['Error'] = 18
            return
        self.user_input_int_array = []
        for item in self.user_input.split(', '):
            try:
                x = int(item)
                self.user_input_int_array.append(x)
            except ValueError:
                self.user_input_int_array.append(-1)
        #print(self.user_input_int_array)

        # Заданная идеальная последовательность
        ideal = [8, 14, 18, 4, 1, 10, 13]
        for i in range(len(ideal)):
            if len(self.user_input_int_array) < (i + 1):
                error += abs(len(ideal) - len(self.user_input_int_array))
                break
            if self.user_input_int_array[i] != ideal[i]:
                error += 1
        people_data['Tasks']['Task6']['Error'] = error


    def open_question_window(self):
        self.timer.stop()
        time_out = (self.elapsed_timer.elapsed()) / 1000
        self.elapse.append(time_out)
        people_data['Tasks']['Task6']['Time'] = self.elapse[0]
        self.chek_answer()
        print(people_data)
        widget.addWidget(questionWindow("Finall"))
        widget.setFixedWidth(650)
        widget.setFixedHeight(500)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Finall(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_FinallForm()
        self.ui.setupUi(self)
        self.calculate_res_formula(people_data['Tasks'])
        self.result_ball(people_data)
        self.create_csv()

    def result_ball(self, people_data):
        max_score = 100
        final_scores = {}
        total_score = 0
        # Параметры для каждой задачи
        task_params = {
            'Task1': {'max_errors': 3, 'error_threshold': 0, 'time_threshold': 30},
            'Task2': {'max_errors': 2, 'error_threshold': 1, 'time_threshold': 150},
            'Task3': {'max_errors': 10, 'error_threshold': 3, 'time_threshold': 210},
            'Task4': {'max_errors': 9, 'error_threshold': 4, 'time_threshold': 60},
            'Task5': {'max_errors': 7, 'error_threshold': 2, 'time_threshold': 60},
            'Task6': {'max_errors': 18, 'error_threshold': 4, 'time_threshold': 90}
        }

        for task, details in people_data['Tasks'].items():
            score = max_score
            errors = details['Error']
            time = details['Time']
            wants_distraction = details['Question']

            # Получаем параметры для задачи
            params = task_params[task]

            # Штраф за ошибки
            if errors > params['error_threshold']:
                score -= ((errors - params['error_threshold']) / params['max_errors']) * max_score

            # Штраф за время
            if time > params['time_threshold']:
                score -= ((time - params['time_threshold']) / params['time_threshold']) * max_score * 0.1

            # Штраф за пропущенные вопросы
            if wants_distraction > 0:
                score -= wants_distraction * 10  # Штраф 10 баллов за желание отвлечься

            # Убедимся, что балл не упадет ниже 0
            score = max(0, score)
            final_scores[task] = score
            total_score += score

            # Нормализуем итоговый балл до 100
        normalized_total_score = (total_score / (6 * max_score)) * 100
        self.ui.label_5.setText(f"В баллах: {normalized_total_score:.2f}")

    def calculate_res_formula(self, task_details):
        # Пример нормативного времени, необходимо установить реальное значение

        task_params_minimum = [
            {'max_errors': 3, 'error_threshold': 0, 'time_threshold': 30},  # Задача 1
            {'max_errors': 2, 'error_threshold': 1, 'time_threshold': 150},  # Задача 2
            {'max_errors': 10, 'error_threshold': 3, 'time_threshold': 210},  # Задача 3
            {'max_errors': 9, 'error_threshold': 4, 'time_threshold': 60},  # Задача 4
            {'max_errors': 7, 'error_threshold': 2, 'time_threshold': 60},  # Задача 5
            {'max_errors': 18, 'error_threshold': 4, 'time_threshold': 90}  # Задача 6
        ]
        i = 0
        result = 0
        max_result_for_formula = [0.07, 0.12, 0.014, 0.09]
        mn_for_tasks_3 = [1, 5, 7, 2, 2, 3]
        id_for_tasks = [[0.5, 3], [0.5, 10], [3, 0.5], [3, 3]]
        for details in task_details:
            T_i = task_details[details]['Time']
            E_i = task_details[details]['Error']
            distraction = task_details[details]['Question']
            formula = 0
            if T_i <= task_params_minimum[i]['time_threshold'] and E_i <= task_params_minimum[i]['error_threshold']:
                formula = (1 / (id_for_tasks[0][0] * (T_i) / mn_for_tasks_3[i] + id_for_tasks[0][1] * E_i + 1))
                #print(formula)
                if formula > max_result_for_formula[0]:
                    x = 1
                else:
                    x = formula / max_result_for_formula[0]
                if distraction == 1:
                    result += x * 0.75
                else:
                    result += x
            elif T_i <= task_params_minimum[i]['time_threshold'] and E_i > task_params_minimum[i]['error_threshold']:
                formula = (1 / (id_for_tasks[1][0] * (T_i / mn_for_tasks_3[i]) + id_for_tasks[1][1] * E_i))
                x = formula / max_result_for_formula[1]
                if distraction == 1:
                    result += x * 0.75
                else:
                    result += x
            elif T_i > task_params_minimum[i]['time_threshold'] and E_i <= task_params_minimum[i]['error_threshold']:
                formula = (1 / (id_for_tasks[2][0] * T_i / mn_for_tasks_3[i] + id_for_tasks[2][1] * E_i))
                x = formula / max_result_for_formula[2]
                if distraction == 1:
                    result += x * 0.75
                else:
                    result += x
            elif T_i > task_params_minimum[i]['time_threshold'] and E_i > task_params_minimum[i]['error_threshold']:
                formula = (1 / (id_for_tasks[3][0] * T_i / mn_for_tasks_3[i] + id_for_tasks[3][1] * E_i))
                x = formula / max_result_for_formula[3]
                if distraction == 1:
                    result += x * 0.75
                else:
                    result += x
            i += 1
        final_result = (result / 6) * 100
        if 35 >= final_result >= 0:
            self.ui.label_4.setText("Низкая устойчивость к прокрастинации.")
        elif 65 >= final_result > 35:
            self.ui.label_4.setText("Средняя устойчивость к прокрастинации.")
        elif 100 >= final_result > 65:
            self.ui.label_4.setText("Высокая устойчивость к прокрастинации.")
        self.ui.label_3.setText(f"В процентном соотношении: {final_result:.2f}%")


    def transliterate(self, rus_to_eng, fio):
        return ''.join(rus_to_eng.get(char, char) for char in fio)
    def create_csv(self):
        rus_to_eng = {
            'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E', 'Ж': 'Zh', 'З': 'Z',
            'И': 'I', 'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R',
            'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'Kh', 'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch',
            'Ы': 'Y', 'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya',
            'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh', 'з': 'z',
            'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
            'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
            'ы': 'y', 'э': 'e', 'ю': 'yu', 'я': 'ya'
        }
        fields = ['FIO', 'Age', 'Gender']
        task_fields = ['Task', 'Error', 'Time', 'Question']
        rows = []
        rus_to_eng = {
            'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E', 'Ж': 'Zh', 'З': 'Z',
            'И': 'I', 'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R',
            'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'Kh', 'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch',
            'Ы': 'Y', 'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya', 'Ь': '', 'Ъ': '',
            'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh', 'з': 'z',
            'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
            'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
            'ы': 'y', 'э': 'e', 'ю': 'yu', 'я': 'ya', 'ь': '', 'ъ': ''
        }

        people_data['FIO'] = self.transliterate(rus_to_eng, people_data['FIO'])
        # Добавление данных о задачах
        for task, details in people_data['Tasks'].items():
            row = [people_data['FIO'], people_data['Age'], people_data['Gender'], task, details['Error'],
                   details['Time'], details['Question']]
            rows.append(row)

        # Имена заголовков для CSV файла
        header = fields + task_fields
        words = people_data['FIO'].split(' ')
        name = ''
        for i,  word in enumerate(words):
            if i != len(words) - 1:
                name += word + '_'
            else:
                name += word

        # Запись в файл
        with open(f'people_data_{name}.csv', 'w', newline='', encoding='utf-8-sig') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(rows)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = firstWindow()
    widget = QStackedWidget()
    widget.setFixedHeight(500)
    widget.setFixedWidth(650)
    widget.addWidget(form)
    widget.show()
    sys.exit(app.exec())
