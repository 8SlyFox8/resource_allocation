from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from main_window import Ui_MainWindow
from multiprocessing import Process
import random
import time
from itertools import *

from graph_construction import plot

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt


def distribution_of_tasks(task_mas):
    if task_mas is not None:
        for number in range(len(task_mas)):
            if task_mas[number] == 0:
                continue
            elif task_mas[number] == 1:
                factorial(1)
            elif task_mas[number] == 2:
                factorial(2)
            elif task_mas[number] == 3:
                factorial(3)
            else:
                factorial(4)


def start_wave(current_wave):
    wave = current_wave
    task_mas1 = []
    task_mas2 = []
    task_mas3 = []
    task_mas4 = []
    random.shuffle(wave)
    for number in range(len(wave)):
        dice = random.randint(1, 4)
        if dice == 1:
            task_mas1.append(wave[number])
        elif dice == 2:
            task_mas2.append(wave[number])
        elif dice == 3:
            task_mas3.append(wave[number])
        else:
            task_mas4.append(wave[number])

    if task_mas1 is not None:
        for number in range(len(task_mas1)):
            if task_mas1[number] == 1:
                ui.gridLayout_1.addWidget(ui.pushButton_1_1, 0, 0)
            elif task_mas1[number] == 2:
                ui.gridLayout_1.addWidget(ui.pushButton_2_1, 0, 1)
            elif task_mas1[number] == 3:
                ui.gridLayout_1.addWidget(ui.pushButton_2_2, 1, 1)
            elif task_mas1[number] == 4:
                ui.gridLayout_1.addWidget(ui.pushButton_3_1, 0, 2)

    if task_mas2 is not None:
        for number in range(len(task_mas2)):
            if task_mas2[number] == 1:
                ui.gridLayout_2.addWidget(ui.pushButton_1_1, 0, 0)
            elif task_mas2[number] == 2:
                ui.gridLayout_2.addWidget(ui.pushButton_2_1, 0, 1)
            elif task_mas2[number] == 3:
                ui.gridLayout_2.addWidget(ui.pushButton_2_2, 1, 1)
            elif task_mas2[number] == 4:
                ui.gridLayout_2.addWidget(ui.pushButton_3_1, 0, 2)

    if task_mas3 is not None:
        for number in range(len(task_mas3)):
            if task_mas3[number] == 1:
                ui.gridLayout_3.addWidget(ui.pushButton_1_1, 0, 0)
            elif task_mas3[number] == 2:
                ui.gridLayout_3.addWidget(ui.pushButton_2_1, 0, 1)
            elif task_mas3[number] == 3:
                ui.gridLayout_3.addWidget(ui.pushButton_2_2, 1, 1)
            elif task_mas3[number] == 4:
                ui.gridLayout_3.addWidget(ui.pushButton_3_1, 0, 2)

    if task_mas4 is not None:
        for number in range(len(task_mas4)):
            if task_mas4[number] == 1:
                ui.gridLayout_4.addWidget(ui.pushButton_1_1, 0, 0)
            elif task_mas4[number] == 2:
                ui.gridLayout_4.addWidget(ui.pushButton_2_1, 0, 1)
            elif task_mas4[number] == 3:
                ui.gridLayout_4.addWidget(ui.pushButton_2_2, 1, 1)
            elif task_mas4[number] == 4:
                ui.gridLayout_4.addWidget(ui.pushButton_3_1, 0, 2)

    cpu1 = Process(target=distribution_of_tasks, name="CPU1", args=(task_mas1,))
    cpu2 = Process(target=distribution_of_tasks, name="CPU2", args=(task_mas2,))
    cpu3 = Process(target=distribution_of_tasks, name="CPU3", args=(task_mas3,))
    cpu4 = Process(target=distribution_of_tasks, name="CPU4", args=(task_mas4,))
    cpu1.start()
    cpu2.start()
    cpu3.start()
    cpu4.start()
    cpu1.join()
    cpu2.join()
    cpu3.join()
    cpu4.join()


def start_wave_for_options(criterion):
    task_mas1 = [[0], [0, 0], [0]]
    task_mas2 = [[0], [0, 0], [0]]
    task_mas3 = [[0], [0, 0], [0]]
    task_mas4 = [[0], [0, 0], [0]]
    for wave1 in (permutations([1, 0, 0, 0])):
        task_mas1[0][0] = wave1[0]
        task_mas2[0][0] = wave1[1]
        task_mas3[0][0] = wave1[2]
        task_mas4[0][0] = wave1[3]
        for wave21 in set(permutations([2, 0, 0, 0])):
            task_mas1[1][0] = wave21[0]
            task_mas2[1][0] = wave21[1]
            task_mas3[1][0] = wave21[2]
            task_mas4[1][0] = wave21[3]
            for wave22 in set(permutations([3, 0, 0, 0])):
                task_mas1[1][1] = wave22[0]
                task_mas2[1][1] = wave22[1]
                task_mas3[1][1] = wave22[2]
                task_mas4[1][1] = wave22[3]
                for wave31 in set(permutations([4, 0, 0, 0])):
                    task_mas1[2][0] = wave31[0]
                    task_mas2[2][0] = wave31[1]
                    task_mas3[2][0] = wave31[2]
                    task_mas4[2][0] = wave31[3]

                    timer = time.time()

                    cpu1 = Process(target=distribution_of_tasks, name="CPU1", args=(task_mas1[0],))
                    cpu2 = Process(target=distribution_of_tasks, name="CPU2", args=(task_mas2[0],))
                    cpu3 = Process(target=distribution_of_tasks, name="CPU3", args=(task_mas3[0],))
                    cpu4 = Process(target=distribution_of_tasks, name="CPU4", args=(task_mas4[0],))
                    cpu1.start()
                    cpu2.start()
                    cpu3.start()
                    cpu4.start()
                    cpu1.join()
                    cpu2.join()
                    cpu3.join()
                    cpu4.join()

                    cpu1 = Process(target=distribution_of_tasks, name="CPU1", args=(task_mas1[1],))
                    cpu2 = Process(target=distribution_of_tasks, name="CPU2", args=(task_mas2[1],))
                    cpu3 = Process(target=distribution_of_tasks, name="CPU3", args=(task_mas3[1],))
                    cpu4 = Process(target=distribution_of_tasks, name="CPU4", args=(task_mas4[1],))
                    cpu1.start()
                    cpu2.start()
                    cpu3.start()
                    cpu4.start()
                    cpu1.join()
                    cpu2.join()
                    cpu3.join()
                    cpu4.join()

                    cpu1 = Process(target=distribution_of_tasks, name="CPU1", args=(task_mas1[2],))
                    cpu2 = Process(target=distribution_of_tasks, name="CPU2", args=(task_mas2[2],))
                    cpu3 = Process(target=distribution_of_tasks, name="CPU3", args=(task_mas3[2],))
                    cpu4 = Process(target=distribution_of_tasks, name="CPU4", args=(task_mas4[2],))
                    cpu1.start()
                    cpu2.start()
                    cpu3.start()
                    cpu4.start()
                    cpu1.join()
                    cpu2.join()
                    cpu3.join()
                    cpu4.join()

                    finish_timer = time.time() - timer

                    if finish_timer > criterion:
                        print("TOO LONG %s seconds" % finish_timer)
                    else:
                        print("CPU1 (first wave):", task_mas1[0], end='   ')
                        print("CPU1 (second wave):", task_mas1[1], end='   ')
                        print("CPU1 (third wave):", task_mas1[2])

                        print("CPU2 (first wave):", task_mas2[0], end='   ')
                        print("CPU2 (second wave):", task_mas2[1], end='   ')
                        print("CPU2 (third wave):", task_mas2[2])

                        print("CPU3 (first wave):", task_mas3[0], end='   ')
                        print("CPU3 (second wave):", task_mas3[1], end='   ')
                        print("CPU3 (third wave):", task_mas3[2])

                        print("CPU4 (first wave):", task_mas4[0], end='   ')
                        print("CPU4 (second wave):", task_mas4[1], end='   ')
                        print("CPU4 (third wave):", task_mas4[2])

                        print("%s seconds" % finish_timer)
                        print()


def factorial(n):
    n *= 10000
    number = 1
    while n > 1:
        number *= n
        n -= 1


def start_test():
    criterion = ui.doubleSpinBox.value()
    print("\n" * 80)
    timer = time.time()
    current_wave = [1]
    start_wave(current_wave)
    current_wave = [2, 3]
    start_wave(current_wave)
    current_wave = [4]
    start_wave(current_wave)
    finish_timer = time.time() - timer
    print("%s seconds" % finish_timer)
    if finish_timer > criterion:
        ui.label.setStyleSheet('color: rgb(255, 0, 0);')
    else:
        ui.label.setStyleSheet('color: rgb(0, 255, 0);')


def searching_for_options():
    criterion = ui.doubleSpinBox_2.value()
    print("\n" * 80)
    start_wave_for_options(criterion)

def start_canvas():
    ui.figure = plt.figure()
    ui.canvas = FigureCanvas(ui.figure)
    if ui.verticalLayout_graph.count() > 0:
        ui.verticalLayout_graph.takeAt(0)
        plt.cla()
    ui.verticalLayout_graph.addWidget(ui.canvas)
    plot(ui.spinBox_count_of_tasks.value(), ui.doubleSpinBox_connection_probability.value())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    # Начало кода

    ui.pushButton_start.clicked.connect(start_test)
    ui.pushButton_search.clicked.connect(searching_for_options)
    ui.pushButton.clicked.connect(start_canvas)
    #Конец кода
    sys.exit(app.exec_())