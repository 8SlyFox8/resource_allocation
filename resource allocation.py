from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from main_window import Ui_MainWindow

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import random
import time
import xlwt
import numpy as np

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
    timer = time.time()
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
    total_timer = time.time() - timer
    print("CPU1", task_mas1)
    print("CPU2", task_mas2)
    print("CPU3", task_mas3)
    print("CPU4", task_mas4)
    print("%s seconds" % finish_timer)
    ui.label_1.setStyleSheet('color: rgb(0, 255, 0);')
    ui.label_2.setStyleSheet('color: rgb(255, 0, 0);')
    ui.label_3.setStyleSheet('color: rgb(255, 0, 0);')
    ui.label_4.setStyleSheet('color: rgb(255, 0, 0);')
    ui.label_5.setStyleSheet('color: rgb(255, 0, 0);')
    print("Working hours %s seconds" % total_timer)
    return finish_timer, total_timer


def searching_for_options():
    print("\n" * 80)
    timer = time.time()
    task_mas1 = {}
    task_mas2 = {}
    task_mas3 = {}
    task_mas4 = {}
    best_time = 0
    labels = global_labels
    best_time = enumeration(0, labels, task_mas1, task_mas2, task_mas3, task_mas4, best_time)
    total_timer = time.time() - timer
    print("%s seconds" % best_time)
    ui.label_1.setStyleSheet('color: rgb(255, 0, 0);')
    ui.label_2.setStyleSheet('color: rgb(0, 255, 0);')
    ui.label_3.setStyleSheet('color: rgb(255, 0, 0);')
    ui.label_4.setStyleSheet('color: rgb(255, 0, 0);')
    ui.label_5.setStyleSheet('color: rgb(255, 0, 0);')
    print("Working hours %s seconds" % total_timer)
    return best_time, total_timer


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


def evolutionary_method(method):
    print("\n" * 80)
    timer = time.time()
    best_time = 0
    individuals = []
    for individual in range(ui.spinBox_number_of_individuals.value()):
        individuals.append(first_gen())

    for gen in range(ui.spinBox_number_of_generations.value()):
        results = {}
        for individual in range(ui.spinBox_number_of_individuals.value()):
            finish_timer = processor_operation(individuals[individual][0], individuals[individual][1], individuals[individual][2], individuals[individual][3])
            results[individual] = finish_timer
        if method == 1:
            individuals = analysis_roulette(results, individuals)
        else:
            individuals = analysis_ranging(results, individuals)
        individuals = mutation(individuals)

    for individual in range(ui.spinBox_number_of_individuals.value()):
        finish_timer = processor_operation(individuals[individual][0], individuals[individual][1], individuals[individual][2], individuals[individual][3])
        best_time = search_for_a_winner(finish_timer, best_time, individuals[individual][0], individuals[individual][1], individuals[individual][2], individuals[individual][3])

    total_timer = time.time() - timer
    print("%s seconds" % best_time)
    ui.label_1.setStyleSheet('color: rgb(255, 0, 0);')
    ui.label_2.setStyleSheet('color: rgb(255, 0, 0);')
    ui.label_3.setStyleSheet('color: rgb(0, 255, 0);')
    ui.label_4.setStyleSheet('color: rgb(255, 0, 0);')
    ui.label_5.setStyleSheet('color: rgb(255, 0, 0);')
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


#Метод рулетки
def analysis_roulette(results, individuals):
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


#Метод ранжирования
def analysis_ranging(results, individuals):
    all_time = {}
    for result in results:
        if results[result] not in all_time.values():
            all_time[result] = results[result]

    max_result = 0
    for rank in range(len(all_time)+1):
        max_result += rank

    new_results = {}
    results_keys = sorted(results, key=results.get)
    for result in results_keys:
        new_results[result] = results[result]

    save_max_result = max_result
    rank = len(all_time)
    for result in new_results:
        results[result] = max_result, max_result - rank
        if new_results[result] not in results.values():
            max_result -= rank
            rank -= 1

    new_individuals = []
    for couple in range((ui.spinBox_number_of_individuals.value() // 2) + (ui.spinBox_number_of_individuals.value() % 2)):
        parents = []
        for i in range(2):
            dice = {}
            a = random.randint(1, save_max_result)
            for individual, result in results.items():
                if (a <= result[0]) and (a > result[1]):
                    dice[individual] = result
            parents.append(individuals[random.choice(list(dice))])
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


def annealing_method(method):
    print("\n" * 80)
    timer = time.time()
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

    option = [task_mas1, task_mas2, task_mas3, task_mas4]

    temperature = ui.spinBox_temperature.value()

    for iterator in range(1, ui.spinBox_iteration.value()):

        new_option = option_changes(option)
        new_timer = processor_operation(new_option[0], new_option[1], new_option[2], new_option[3])
        delta_timer = new_timer - finish_timer

        if delta_timer < 0:
            finish_timer = new_timer
            option = new_option
        else:
            dice = np.exp(-delta_timer / temperature)
            if np.random.rand() <= dice:
                finish_timer = new_timer
                option = new_option

        if method == 1:
            temperature = reverse_linear_cooling(ui.spinBox_temperature.value(), iterator)
        else:
            temperature = linear_cooling(ui.spinBox_temperature.value(), iterator)

        if temperature <= ui.spinBox_temperature_stop.value():
            break

    total_timer = time.time() - timer
    print("CPU1", task_mas1)
    print("CPU2", task_mas2)
    print("CPU3", task_mas3)
    print("CPU4", task_mas4)
    print("%s seconds" % finish_timer)
    ui.label_1.setStyleSheet('color: rgb(255, 0, 0);')
    ui.label_2.setStyleSheet('color: rgb(255, 0, 0);')
    ui.label_3.setStyleSheet('color: rgb(255, 0, 0);')
    ui.label_4.setStyleSheet('color: rgb(0, 255, 0);')
    ui.label_5.setStyleSheet('color: rgb(255, 0, 0);')
    print("Working hours %s seconds" % total_timer)
    return finish_timer, total_timer


# схема обратного линейного охлаждения
def reverse_linear_cooling(current_temperature, iterator):
    return current_temperature / iterator


# схема линейного охлаждения
def linear_cooling(current_temperature, iterator):
    return max(0.1, current_temperature - 0.1 * iterator)


def option_changes(option):
    new_option = [{}, {}, {}, {}]
    dice = random.randint(0, len(global_labels) - 1)
    for nodes in range(len(global_labels)):
        for i in range(4):
            for number in option[i]:
                if number == nodes:
                    if number == dice:
                        cpu = i
                        while (cpu == i):
                            cpu = random.randint(0, 3)
                        if cpu == 0:
                            new_option[0][number] = option[i][number]
                        elif cpu == 1:
                            new_option[1][number] = option[i][number]
                        elif cpu == 2:
                            new_option[2][number] = option[i][number]
                        else:
                            new_option[3][number] = option[i][number]
                    else:
                        new_option[i][number] = option[i][number]
    return new_option


def full_test():
    book = xlwt.Workbook(encoding="utf-8")
    sheet = book.add_sheet("Full test")
    sheet.write(0, 0, "Scientific poke method (Best time)")
    sheet.write(0, 1, "Scientific poke method (Total time)")
    sheet.write(0, 2, "Searching for options (Best time)")
    sheet.write(0, 3, "Searching for options (Total time)")
    sheet.write(0, 4, "Evolutionary method (Roulette method)(Best time)")
    sheet.write(0, 5, "Evolutionary method (Roulette method)(Total time)")
    sheet.write(0, 6, "Evolutionary method (Ranking method)(Best time)")
    sheet.write(0, 7, "Evolutionary method (Ranking method)(Total time)")
    sheet.write(0, 8, "Annealing method (Reverse linear cooling)(Best time)")
    sheet.write(0, 9, "Annealing method (Reverse linear cooling)(Total time)")
    sheet.write(0, 10, "Annealing method (Linear cooling)(Best time)")
    sheet.write(0, 11, "Annealing method (Linear cooling)(Total time)")

    all_time = time.time()
    for graphs in range(ui.spinBox_number_of_graphs.value()):
        start_canvas()

        best_time, total_timer = scientific_poke_method()
        sheet.write(graphs + 1, 0, best_time)
        sheet.write(graphs + 1, 1, total_timer)

        best_time, total_timer = searching_for_options()
        sheet.write(graphs + 1, 2, best_time)
        sheet.write(graphs + 1, 3, total_timer)

        best_time, total_timer = evolutionary_method(1)
        sheet.write(graphs + 1, 4, best_time)
        sheet.write(graphs + 1, 5, total_timer)

        best_time, total_timer = evolutionary_method(2)
        sheet.write(graphs + 1, 6, best_time)
        sheet.write(graphs + 1, 7, total_timer)

        best_time, total_timer = annealing_method(1)
        sheet.write(graphs + 1, 8, best_time)
        sheet.write(graphs + 1, 9, total_timer)

        best_time, total_timer = annealing_method(2)
        sheet.write(graphs + 1, 10, best_time)
        sheet.write(graphs + 1, 11, total_timer)

    all_time = time.time() - all_time
    print(all_time)

    sheet.write(ui.spinBox_number_of_graphs.value() + 1, 0,
                xlwt.Formula("AVERAGE(A2:A" + str(ui.spinBox_number_of_graphs.value() + 1) + ")"))
    sheet.write(ui.spinBox_number_of_graphs.value() + 1, 1,
                xlwt.Formula("AVERAGE(B2:B" + str(ui.spinBox_number_of_graphs.value() + 1) + ")"))
    sheet.write(ui.spinBox_number_of_graphs.value() + 1, 2,
                xlwt.Formula("AVERAGE(C2:C" + str(ui.spinBox_number_of_graphs.value() + 1) + ")"))
    sheet.write(ui.spinBox_number_of_graphs.value() + 1, 3,
                xlwt.Formula("AVERAGE(D2:D" + str(ui.spinBox_number_of_graphs.value() + 1) + ")"))
    sheet.write(ui.spinBox_number_of_graphs.value() + 1, 4,
                xlwt.Formula("AVERAGE(E2:E" + str(ui.spinBox_number_of_graphs.value() + 1) + ")"))
    sheet.write(ui.spinBox_number_of_graphs.value() + 1, 5,
                xlwt.Formula("AVERAGE(F2:F" + str(ui.spinBox_number_of_graphs.value() + 1) + ")"))
    sheet.write(ui.spinBox_number_of_graphs.value() + 1, 6,
                xlwt.Formula("AVERAGE(G2:G" + str(ui.spinBox_number_of_graphs.value() + 1) + ")"))
    sheet.write(ui.spinBox_number_of_graphs.value() + 1, 7,
                xlwt.Formula("AVERAGE(H2:H" + str(ui.spinBox_number_of_graphs.value() + 1) + ")"))
    sheet.write(ui.spinBox_number_of_graphs.value() + 1, 8,
                xlwt.Formula("AVERAGE(I2:I" + str(ui.spinBox_number_of_graphs.value() + 1) + ")"))
    sheet.write(ui.spinBox_number_of_graphs.value() + 1, 9,
                xlwt.Formula("AVERAGE(J2:J" + str(ui.spinBox_number_of_graphs.value() + 1) + ")"))
    sheet.write(ui.spinBox_number_of_graphs.value() + 1, 10,
                xlwt.Formula("AVERAGE(K2:K" + str(ui.spinBox_number_of_graphs.value() + 1) + ")"))
    sheet.write(ui.spinBox_number_of_graphs.value() + 1, 11,
                xlwt.Formula("AVERAGE(L2:L" + str(ui.spinBox_number_of_graphs.value() + 1) + ")"))

    sheet.write(0, 12, xlwt.Formula(
        "AVERAGE(A" + str(ui.spinBox_number_of_graphs.value() + 2) +
                ";C" + str(ui.spinBox_number_of_graphs.value() + 2) +
                ";E" + str(ui.spinBox_number_of_graphs.value() + 2) +
                ";G" + str(ui.spinBox_number_of_graphs.value() + 2) +
                ";I" + str(ui.spinBox_number_of_graphs.value() + 2) +
                ";K" + str(ui.spinBox_number_of_graphs.value() + 2) + ")"))

    book.save("Full test.xls")

    ui.label_1.setStyleSheet('color: rgb(255, 0, 0);')
    ui.label_2.setStyleSheet('color: rgb(255, 0, 0);')
    ui.label_3.setStyleSheet('color: rgb(255, 0, 0);')
    ui.label_4.setStyleSheet('color: rgb(255, 0, 0);')
    ui.label_5.setStyleSheet('color: rgb(0, 255, 0);')


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
    ui.pushButton_roulette.clicked.connect(lambda: evolutionary_method(1))
    ui.pushButton_ranging.clicked.connect(lambda: evolutionary_method(2))
    ui.pushButton_reverse.clicked.connect(lambda: annealing_method(1))
    ui.pushButton_linear.clicked.connect(lambda: annealing_method(2))
    ui.pushButton.clicked.connect(start_canvas)
    ui.pushButton_full_test.clicked.connect(full_test)
    #Конец кода
    sys.exit(app.exec_())