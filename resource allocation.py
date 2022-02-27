from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from main_window import Ui_MainWindow

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from multiprocessing import Process, Manager
import random
import time

from graph_construction import plot
from tasks import factorial


"""def start_wave_for_options(criterion):
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
                        print()"""


"""def start_test():
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
        ui.label.setStyleSheet('color: rgb(0, 255, 0);')"""

def task_completion(task_mas, link_list):
    if task_mas != {}:
        for key in task_mas:
            exitflag = False
            while exitflag != True:
                exitflag = False
                for number_in_matrix in link_list:
                    if number_in_matrix[1] == key:
                        exitflag = False
                        break
                else:
                    exitflag = True

            if task_mas[key] == 1:
                factorial(1)
            elif task_mas[key] == 2:
                factorial(2)
            elif task_mas[key] == 3:
                factorial(3)
            elif task_mas[key] == 4:
                factorial(4)
            elif task_mas[key] == 5:
                factorial(5)
            elif task_mas[key] == 6:
                factorial(6)
            elif task_mas[key] == 7:
                factorial(7)
            elif task_mas[key] == 8:
                factorial(8)
            elif task_mas[key] == 9:
                factorial(9)
            else:
                factorial(10)

            exitflag = False
            while exitflag != True:
                exitflag = False
                for number_in_matrix in link_list:
                    if number_in_matrix[0] == key:
                        link_list.remove(number_in_matrix)
                        exitflag = False
                        break
                else:
                    exitflag = True


def processor_operation(task_mas1, task_mas2, task_mas3, task_mas4):
    link_matrix_searching_for_options = Manager().list(global_connection)
    timer = time.time()
    cpu1 = Process(target=task_completion, name="CPU1", args=(task_mas1, link_matrix_searching_for_options,))
    cpu2 = Process(target=task_completion, name="CPU2", args=(task_mas2, link_matrix_searching_for_options,))
    cpu3 = Process(target=task_completion, name="CPU3", args=(task_mas3, link_matrix_searching_for_options,))
    cpu4 = Process(target=task_completion, name="CPU4", args=(task_mas4, link_matrix_searching_for_options,))
    cpu1.start()
    cpu2.start()
    cpu3.start()
    cpu4.start()
    cpu1.join()
    cpu2.join()
    cpu3.join()
    cpu4.join()
    finish_timer = time.time() - timer
    print("CPU1", task_mas1)
    print("CPU2", task_mas2)
    print("CPU3", task_mas3)
    print("CPU4", task_mas4)
    print("%s seconds" % finish_timer)


def scientific_poke_method():
    print("\n" * 80)
    task_mas1 = {}
    task_mas2 = {}
    task_mas3 = {}
    task_mas4 = {}
    labels = global_labels
    for number in range(len(labels)):
        dice = random.randint(1, 4)
        if dice == 1:
            task_mas1[number] = labels[number]
        elif dice == 2:
            task_mas2[number] = labels[number]
        elif dice == 3:
            task_mas3[number] = labels[number]
        else:
            task_mas4[number] = labels[number]
    task_mas1 = {0: 2, 1: 3, 3: 5}
    task_mas2 = {2: 2}
    task_mas3 = {4: 9}
    task_mas4 = {}
    processor_operation(task_mas1, task_mas2, task_mas3, task_mas4)
    ui.label_1.setStyleSheet('color: rgb(0, 255, 0);')
    ui.label_2.setStyleSheet('color: rgb(255, 0, 0);')


def searching_for_options():
    print("\n" * 80)
    task_mas1 = {}
    task_mas2 = {}
    task_mas3 = {}
    task_mas4 = {}
    labels = global_labels
    enumeration(0, labels, task_mas1, task_mas2, task_mas3, task_mas4)
    ui.label_1.setStyleSheet('color: rgb(255, 0, 0);')
    ui.label_2.setStyleSheet('color: rgb(0, 255, 0);')


def enumeration(communication_number, labels, task_mas1, task_mas2, task_mas3, task_mas4):
    for index in range(4):
        if index == 0:
            task_mas1[communication_number] = labels[communication_number]
        elif index == 1:
            task_mas2[communication_number] = labels[communication_number]
        elif index == 2:
            task_mas3[communication_number] = labels[communication_number]
        else:
            task_mas4[communication_number] = labels[communication_number]
        if communication_number < len(labels) - 1:
            enumeration(communication_number + 1, labels, task_mas1, task_mas2, task_mas3, task_mas4)
        else:
            processor_operation(task_mas1, task_mas2, task_mas3, task_mas4)
        if index == 0:
            task_mas1.pop(communication_number)
        elif index == 1:
            task_mas2.pop(communication_number)
        elif index == 2:
            task_mas3.pop(communication_number)
        else:
            task_mas4.pop(communication_number)


def start_canvas():
    global global_labels, global_connection
    ui.figure = plt.figure()
    ui.canvas = FigureCanvas(ui.figure)
    if ui.verticalLayout_graph.count() > 0:
        ui.verticalLayout_graph.takeAt(0)
        plt.cla()
    ui.verticalLayout_graph.addWidget(ui.canvas)
    global_labels, global_connection = plot(ui.spinBox_count_of_tasks.value(),
                                            ui.doubleSpinBox_connection_probability.value())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    # Начало кода

    ui.pushButton_poke.clicked.connect(scientific_poke_method)
    ui.pushButton_options.clicked.connect(searching_for_options)
    ui.pushButton.clicked.connect(start_canvas)
    #Конец кода
    sys.exit(app.exec_())