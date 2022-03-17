from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from main_window import Ui_MainWindow

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import random
import pandas as pd
from openpyxl import load_workbook
import xlrd
import xlwt


from graph_construction import plot


def processor_operation(task_mas1, task_mas2, task_mas3, task_mas4):
    link_list = global_connection.copy()
    finish_timer = 0
    time_counter = [0, 0, 0, 0]

    tasks = [task_mas1.copy(), task_mas2.copy(), task_mas3.copy(), task_mas4.copy()]

    exitflag1 = False
    while exitflag1 != True:
        counter = 0
        del_tasks = []
        for cpu in range(len(tasks)):
            if tasks[cpu] != {}:
                exitflag2 = False
                for task in tasks[cpu]:
                    for number_in_matrix in link_list:
                        if number_in_matrix[1] == task:
                            time_counter[cpu] += 1
                            break
                    else:
                        exitflag2 = True

                    if exitflag2 == False:
                        break

                    time_counter[cpu] += 1
                    tasks[cpu][task] -= 1
                    if tasks[cpu][task] == 0:
                        del_tasks.append(task)
                    break
            else:
                counter += 1

        for task in del_tasks:
            exitflag3 = False
            while exitflag3 != True:
                for number_in_matrix in link_list:
                    if number_in_matrix[0] == task:
                        link_list.remove(number_in_matrix)
                        break
                else:
                    exitflag3 = True
            for cpu in range(len(tasks)):
                if tasks[cpu] != {}:
                    if task in tasks[cpu]:
                        del tasks[cpu][task]

        if counter == 4:
            exitflag1 = True

    for time in time_counter:
        if time > finish_timer:
            finish_timer = time
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
    ui.label_4.setStyleSheet('color: rgb(255, 0, 0);')
    total_timer = finish_timer
    print("Working hours %s seconds" % total_timer)
    return finish_timer, total_timer


def searching_for_options():
    total_timer = 0
    task_mas1 = {}
    task_mas2 = {}
    task_mas3 = {}
    task_mas4 = {}
    best_time = 0
    labels = global_labels
    best_time, total_timer = enumeration(0, labels, task_mas1, task_mas2, task_mas3, task_mas4, best_time, total_timer)
    print("%s seconds" % best_time)
    ui.label_1.setStyleSheet('color: rgb(255, 0, 0);')
    ui.label_2.setStyleSheet('color: rgb(0, 255, 0);')
    ui.label_3.setStyleSheet('color: rgb(255, 0, 0);')
    ui.label_4.setStyleSheet('color: rgb(255, 0, 0);')
    print("Working hours %s seconds" % total_timer)
    return best_time, total_timer


def enumeration(communication_number, labels, task_mas1, task_mas2, task_mas3, task_mas4, best_time, total_timer):
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
            best_time, total_timer = enumeration(communication_number + 1, labels, task_mas1, task_mas2, task_mas3, task_mas4, best_time, total_timer)
        else:
            finish_timer = processor_operation(task_mas1, task_mas2, task_mas3, task_mas4)
            total_timer += finish_timer
            best_time = search_for_a_winner(finish_timer, best_time, task_mas1, task_mas2, task_mas3, task_mas4)
        if index == 0:
            task_mas1.pop(communication_number)
        elif index == 1:
            task_mas2.pop(communication_number)
        elif index == 2:
            task_mas3.pop(communication_number)
        else:
            task_mas4.pop(communication_number)
    return best_time, total_timer


def evolutionary_method():
    total_timer = 0
    best_time = 0
    individuals = []
    for individual in range(ui.spinBox_number_of_individuals.value()):
        individuals.append(first_gen())

    for gen in range(ui.spinBox_number_of_generations.value()):
        results = {}
        for individual in range(ui.spinBox_number_of_individuals.value()):
            finish_timer = processor_operation(individuals[individual][0], individuals[individual][1], individuals[individual][2], individuals[individual][3])
            results[individual] = finish_timer
            total_timer += finish_timer
        individuals = analysis(results, individuals)
        individuals = mutation(individuals)

    for individual in range(ui.spinBox_number_of_individuals.value()):
        finish_timer = processor_operation(individuals[individual][0], individuals[individual][1], individuals[individual][2], individuals[individual][3])
        total_timer += finish_timer
        best_time = search_for_a_winner(finish_timer, best_time, individuals[individual][0], individuals[individual][1], individuals[individual][2], individuals[individual][3])

    print("%s seconds" % best_time)
    ui.label_1.setStyleSheet('color: rgb(255, 0, 0);')
    ui.label_2.setStyleSheet('color: rgb(255, 0, 0);')
    ui.label_3.setStyleSheet('color: rgb(0, 255, 0);')
    ui.label_4.setStyleSheet('color: rgb(255, 0, 0);')
    print("Working hours %s seconds" % total_timer)
    return best_time, total_timer


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
    if all_time == 0:
        for individual in range(ui.spinBox_number_of_individuals.value()):
            results[individual] = 1 / ui.spinBox_number_of_individuals.value()
    else:
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
                    if individual != range(ui.spinBox_number_of_individuals.value()-1):
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


def full_test():
    book = xlwt.Workbook(encoding="utf-8")
    sheet = book.add_sheet("Full test")
    sheet.write(0, 0, "Scientific poke method (Best time)")
    sheet.write(0, 1, "Scientific poke method (Total time)")
    sheet.write(0, 2, "Searching for options (Best time)")
    sheet.write(0, 3, "Searching for options (Total time)")
    sheet.write(0, 4, "Evolutionary method (Best time)")
    sheet.write(0, 5, "Evolutionary method (Total time)")

    for graphs in range(ui.spinBox_number_of_graphs.value()):
        start_canvas()

        best_time, total_timer = scientific_poke_method()
        sheet.write(graphs + 1, 0, best_time)
        sheet.write(graphs + 1, 1, total_timer)

        best_time, total_timer = searching_for_options()
        sheet.write(graphs + 1, 2, best_time)
        sheet.write(graphs + 1, 3, total_timer)

        best_time, total_timer = evolutionary_method()
        sheet.write(graphs + 1, 4, best_time)
        sheet.write(graphs + 1, 5, total_timer)
    book.save("Full test.xls")

    ui.label_1.setStyleSheet('color: rgb(255, 0, 0);')
    ui.label_2.setStyleSheet('color: rgb(255, 0, 0);')
    ui.label_3.setStyleSheet('color: rgb(255, 0, 0);')
    ui.label_4.setStyleSheet('color: rgb(0, 255, 0);')


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
    ui.pushButton_full_test.clicked.connect(full_test)
    #Конец кода
    sys.exit(app.exec_())