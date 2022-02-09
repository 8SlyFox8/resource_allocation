from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from main_window import Ui_MainWindow
from multiprocessing import Process, current_process
import random
import time

def distribution_of_tasks(task_mas):
    timer = time.time()
    if task_mas != None:
        for number in range(len(task_mas)):
            if task_mas[number] == 1:
                factorial(1)
            elif task_mas[number] == 2:
                factorial(2)
            elif task_mas[number] == 3:
                factorial(3)
            elif task_mas[number] == 4:
                factorial(4)
            elif task_mas[number] == 5:
                factorial(5)
            elif task_mas[number] == 6:
                factorial(6)
            elif task_mas[number] == 7:
                factorial(7)
            elif task_mas[number] == 8:
                factorial(8)
            elif task_mas[number] == 9:
                factorial(9)
            elif task_mas[number] == 10:
                factorial(10)
    print(current_process().name, "%s seconds" % (time.time() - timer))

def start_test():
    print("\n" * 80)
    tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    task_mas1 = []
    task_mas2 = []
    task_mas3 = []
    task_mas4 = []
    random.shuffle(tasks)
    for number in range(len(tasks)):
        dice = random.randint(1, 4)
        if dice == 1:
            task_mas1.append(tasks[number])
        elif dice == 2:
            task_mas2.append(tasks[number])
        elif dice == 3:
            task_mas3.append(tasks[number])
        else:
            task_mas4.append(tasks[number])

    if task_mas1 != None:
        for number in range(len(task_mas1)):
            if task_mas1[number] == 1:
                ui.horizontalLayout_1.addWidget(ui.pushButton_1)
            elif task_mas1[number] == 2:
                ui.horizontalLayout_1.addWidget(ui.pushButton_2)
            elif task_mas1[number] == 3:
                ui.horizontalLayout_1.addWidget(ui.pushButton_3)
            elif task_mas1[number] == 4:
                ui.horizontalLayout_1.addWidget(ui.pushButton_4)
            elif task_mas1[number] == 5:
                ui.horizontalLayout_1.addWidget(ui.pushButton_5)
            elif task_mas1[number] == 6:
                ui.horizontalLayout_1.addWidget(ui.pushButton_6)
            elif task_mas1[number] == 7:
                ui.horizontalLayout_1.addWidget(ui.pushButton_7)
            elif task_mas1[number] == 8:
                ui.horizontalLayout_1.addWidget(ui.pushButton_8)
            elif task_mas1[number] == 9:
                ui.horizontalLayout_1.addWidget(ui.pushButton_9)
            elif task_mas1[number] == 10:
                ui.horizontalLayout_1.addWidget(ui.pushButton_10)

    if task_mas2 != None:
        for number in range(len(task_mas2)):
            if task_mas2[number] == 1:
                ui.horizontalLayout_2.addWidget(ui.pushButton_1)
            elif task_mas2[number] == 2:
                ui.horizontalLayout_2.addWidget(ui.pushButton_2)
            elif task_mas2[number] == 3:
                ui.horizontalLayout_2.addWidget(ui.pushButton_3)
            elif task_mas2[number] == 4:
                ui.horizontalLayout_2.addWidget(ui.pushButton_4)
            elif task_mas2[number] == 5:
                ui.horizontalLayout_2.addWidget(ui.pushButton_5)
            elif task_mas2[number] == 6:
                ui.horizontalLayout_2.addWidget(ui.pushButton_6)
            elif task_mas2[number] == 7:
                ui.horizontalLayout_2.addWidget(ui.pushButton_7)
            elif task_mas2[number] == 8:
                ui.horizontalLayout_2.addWidget(ui.pushButton_8)
            elif task_mas2[number] == 9:
                ui.horizontalLayout_2.addWidget(ui.pushButton_9)
            elif task_mas2[number] == 10:
                ui.horizontalLayout_2.addWidget(ui.pushButton_10)

    if task_mas3 != None:
        for number in range(len(task_mas3)):
            if task_mas3[number] == 1:
                ui.horizontalLayout_3.addWidget(ui.pushButton_1)
            elif task_mas3[number] == 2:
                ui.horizontalLayout_3.addWidget(ui.pushButton_2)
            elif task_mas3[number] == 3:
                ui.horizontalLayout_3.addWidget(ui.pushButton_3)
            elif task_mas3[number] == 4:
                ui.horizontalLayout_3.addWidget(ui.pushButton_4)
            elif task_mas3[number] == 5:
                ui.horizontalLayout_3.addWidget(ui.pushButton_5)
            elif task_mas3[number] == 6:
                ui.horizontalLayout_3.addWidget(ui.pushButton_6)
            elif task_mas3[number] == 7:
                ui.horizontalLayout_3.addWidget(ui.pushButton_7)
            elif task_mas3[number] == 8:
                ui.horizontalLayout_3.addWidget(ui.pushButton_8)
            elif task_mas3[number] == 9:
                ui.horizontalLayout_3.addWidget(ui.pushButton_9)
            elif task_mas3[number] == 10:
                ui.horizontalLayout_3.addWidget(ui.pushButton_10)

    if task_mas4 != None:
        for number in range(len(task_mas4)):
            if task_mas4[number] == 1:
                ui.horizontalLayout_4.addWidget(ui.pushButton_1)
            elif task_mas4[number] == 2:
                ui.horizontalLayout_4.addWidget(ui.pushButton_2)
            elif task_mas4[number] == 3:
                ui.horizontalLayout_4.addWidget(ui.pushButton_3)
            elif task_mas4[number] == 4:
                ui.horizontalLayout_4.addWidget(ui.pushButton_4)
            elif task_mas4[number] == 5:
                ui.horizontalLayout_4.addWidget(ui.pushButton_5)
            elif task_mas4[number] == 6:
                ui.horizontalLayout_4.addWidget(ui.pushButton_6)
            elif task_mas4[number] == 7:
                ui.horizontalLayout_4.addWidget(ui.pushButton_7)
            elif task_mas4[number] == 8:
                ui.horizontalLayout_4.addWidget(ui.pushButton_8)
            elif task_mas4[number] == 9:
                ui.horizontalLayout_4.addWidget(ui.pushButton_9)
            elif task_mas4[number] == 10:
                ui.horizontalLayout_4.addWidget(ui.pushButton_10)

    CPU1 = Process(target=distribution_of_tasks, name="CPU1", args=(task_mas1,))
    CPU2 = Process(target=distribution_of_tasks, name="CPU2", args=(task_mas2,))
    CPU3 = Process(target=distribution_of_tasks, name="CPU3", args=(task_mas3,))
    CPU4 = Process(target=distribution_of_tasks, name="CPU4", args=(task_mas4,))
    CPU1.start()
    CPU2.start()
    CPU3.start()
    CPU4.start()
    CPU1.join()
    CPU2.join()
    CPU3.join()
    CPU4.join()

def factorial(n):
    n *= 10000
    factorial = 1
    while n > 1:
        factorial *= n
        n -= 1

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