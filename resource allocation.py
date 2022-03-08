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


def task_completion(task_mas, link_list):
    if task_mas != {}:
        for key in task_mas:
            exitflag = False
            while exitflag != True:
                exitflag = False
                for number_in_matrix in link_list:
                    if number_in_matrix[1] == key:
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

            save_link_list = []
            save_link_list.extend(link_list)
            exitflag = False
            while exitflag != True:
                for number_in_matrix in save_link_list:
                    if number_in_matrix[0] == key:
                        link_list.remove(number_in_matrix)
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
    return finish_timer


def search_for_a_winner(current_time, best_time, task_mas1, task_mas2, task_mas3, task_mas4):
    if best_time == 0:
        best_time = current_time
        print("\n" * 80)
        print("CPU1", task_mas1)
        print("CPU2", task_mas2)
        print("CPU3", task_mas3)
        print("CPU4", task_mas4)
    if current_time < best_time:
        best_time = current_time
        print("\n" * 80)
        print("CPU1", task_mas1)
        print("CPU2", task_mas2)
        print("CPU3", task_mas3)
        print("CPU4", task_mas4)
    return best_time


def scientific_poke_method():
    total_timer = time.time()
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
    finish_timer = processor_operation(task_mas1, task_mas2, task_mas3, task_mas4)
    print("CPU1", task_mas1)
    print("CPU2", task_mas2)
    print("CPU3", task_mas3)
    print("CPU4", task_mas4)
    print("%s seconds" % finish_timer)
    ui.label_1.setStyleSheet('color: rgb(0, 255, 0);')
    ui.label_2.setStyleSheet('color: rgb(255, 0, 0);')
    ui.label_3.setStyleSheet('color: rgb(255, 0, 0);')
    total_timer = time.time() - total_timer
    print("Working hours %s seconds" % total_timer)


def searching_for_options():
    total_timer = time.time()
    task_mas1 = {}
    task_mas2 = {}
    task_mas3 = {}
    task_mas4 = {}
    best_time = 0
    labels = global_labels
    best_time = enumeration(0, labels, task_mas1, task_mas2, task_mas3, task_mas4, best_time)
    print("%s seconds" % best_time)
    ui.label_1.setStyleSheet('color: rgb(255, 0, 0);')
    ui.label_2.setStyleSheet('color: rgb(0, 255, 0);')
    ui.label_3.setStyleSheet('color: rgb(255, 0, 0);')
    total_timer = time.time() - total_timer
    print("Working hours %s seconds" % total_timer)


def enumeration(communication_number, labels, task_mas1, task_mas2, task_mas3, task_mas4, best_time):
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
            best_time = enumeration(communication_number + 1, labels, task_mas1, task_mas2, task_mas3, task_mas4, best_time)
        else:
            finish_timer = processor_operation(task_mas1, task_mas2, task_mas3, task_mas4)
            best_time = search_for_a_winner(finish_timer, best_time, task_mas1, task_mas2, task_mas3, task_mas4)
        if index == 0:
            task_mas1.pop(communication_number)
        elif index == 1:
            task_mas2.pop(communication_number)
        elif index == 2:
            task_mas3.pop(communication_number)
        else:
            task_mas4.pop(communication_number)
    return best_time


def evolutionary_method():
    total_timer = time.time()
    best_time = 0
    individuals = []
    for individual in range(ui.spinBox_number_of_individuals.value()):
        individuals.append(first_gen())

    for gen in range(ui.spinBox_number_of_generations.value()):
        results = {}
        for individual in range(ui.spinBox_number_of_individuals.value()):
            finish_timer = processor_operation(individuals[individual][0], individuals[individual][1], individuals[individual][2], individuals[individual][3])
            results[individual] = finish_timer
        individuals = analysis(results, individuals)
        individuals = mutation(individuals)

    for individual in range(ui.spinBox_number_of_individuals.value()):
        finish_timer = processor_operation(individuals[individual][0], individuals[individual][1], individuals[individual][2], individuals[individual][3])
        best_time = search_for_a_winner(finish_timer, best_time, individuals[individual][0], individuals[individual][1], individuals[individual][2], individuals[individual][3])
    print("%s seconds" % best_time)

    ui.label_1.setStyleSheet('color: rgb(255, 0, 0);')
    ui.label_2.setStyleSheet('color: rgb(255, 0, 0);')
    ui.label_3.setStyleSheet('color: rgb(0, 255, 0);')
    total_timer = time.time() - total_timer
    print("Working hours %s seconds" % total_timer)


def first_gen():
    labels = global_labels
    individual = [{}, {}, {}, {}]
    for number in range(len(labels)):
        dice = random.randint(1, 4)
        if dice == 1:
            individual[0][number] = labels[number]
        elif dice == 2:
            individual[1][number] = labels[number]
        elif dice == 3:
            individual[2][number] = labels[number]
        else:
            individual[3][number] = labels[number]
    return individual


def analysis(results, individuals):
    all_time = 0
    max_result = max(results.values())
    for individual in range(ui.spinBox_number_of_individuals.value()):
        all_time += max_result - results[individual]
    for individual in range(ui.spinBox_number_of_individuals.value()):
        results[individual] = (max_result - results[individual]) / all_time

    new_individuals = []
    for couple in range((ui.spinBox_number_of_individuals.value() // 2) + (ui.spinBox_number_of_individuals.value() % 2)):
        parents = []
        for i in range(2):
            dice = results[0]
            a = random.random()
            for individual in range(ui.spinBox_number_of_individuals.value()):
                if a < dice:
                    parents.append(individuals[individual])
                    break
                else:
                    if individual != range(ui.spinBox_number_of_individuals.value() - 1):
                        dice += results[individual+1]
        if ui.spinBox_number_of_individuals.value() % 2 == 1:
            if couple == ui.spinBox_number_of_individuals.value() // 2:
                new_individuals.append(crossing(parents)[0])
            else:
                new_individuals.append(crossing(parents)[0])
                new_individuals.append(crossing(parents)[1])
        else:
            new_individuals.append(crossing(parents)[0])
            new_individuals.append(crossing(parents)[1])
    return new_individuals


def crossing(parents):
    children = [[{}, {}, {}, {}], [{}, {}, {}, {}]]
    for nodes in range(len(global_labels)):
        a = random.random()
        for i in range(4):
            for number in parents[0][i]:
                if a < 0.5 and number == nodes:
                    children[1][i][number] = parents[0][i][number]
                if a >= 0.5 and number == nodes:
                    children[0][i][number] = parents[0][i][number]
            for number in parents[1][i]:
                if a < 0.5 and number == nodes:
                    children[0][i][number] = parents[1][i][number]
                if a >= 0.5 and number == nodes:
                    children[1][i][number] = parents[1][i][number]
    return children


def mutation(individuals):
    new_individuals = []
    for individual in individuals:
        a = random.random()
        if a < ui.doubleSpinBox_mutation_probability.value():
            mutant = [{}, {}, {}, {}]
            dice = random.randint(0, len(global_labels)-1)
            for nodes in range(len(global_labels)):
                for i in range(4):
                    for number in individual[i]:
                        if number == nodes:
                            if number == dice:
                                cpu = i
                                while(cpu == i):
                                    cpu = random.randint(0, 3)
                                if cpu == 0:
                                    mutant[0][number] = individual[i][number]
                                elif cpu == 1:
                                    mutant[1][number] = individual[i][number]
                                elif cpu == 2:
                                    mutant[2][number] = individual[i][number]
                                else:
                                    mutant[3][number] = individual[i][number]
                            else:
                                mutant[i][number] = individual[i][number]
            new_individuals.append(mutant)
        else:
            new_individuals.append(individual)
    return new_individuals



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
    ui.pushButton_evolution.clicked.connect(evolutionary_method)
    ui.pushButton.clicked.connect(start_canvas)
    #Конец кода
    sys.exit(app.exec_())