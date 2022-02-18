from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from main_window import Ui_MainWindow
from multiprocessing import Process
import random
import time


def distribution_of_tasks(task_mas):
    if task_mas is not None:
        for number in range(len(task_mas)):
            if task_mas[number] == 1:
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


def factorial(n):
    n *= 10000
    number = 1
    while n > 1:
        number *= n
        n -= 1


def start_test():
    x = ui.doubleSpinBox.value()
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
    if finish_timer > x:
        ui.label.setStyleSheet('color: rgb(255, 0, 0);')
    else:
        ui.label.setStyleSheet('color: rgb(0, 255, 0);')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    # Начало кода

    ui.pushButton_start.clicked.connect(start_test)
    #Конец кода
    sys.exit(app.exec_())