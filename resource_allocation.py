from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from main_window import Ui_MainWindow

import xlwt
import time

from system import system_construction
from graph_construction import graph_construction
from scientific_poke_method import scientific_poke_method
from searching_for_options import searching_for_options
from evolutionary_method import evolutionary_method
from annealing_method import annealing_method


def beginning_of_work(method):
    labels, connection, labels_memory, labels_speed = graph_construction(ui.spinBox_count_of_nodes.value(),
                                                                         ui.doubleSpinBox_connection_probability.value())
    systems, gateways, gateways_memory = system_construction(ui.spinBox_number_of_devices.value(),
                                                             ui.spinBox_number_of_processors.value(),
                                                             ui.comboBox_communication_type.currentIndex())
    if method == 1:
        timer = time.time()
        best_time = scientific_poke_method(ui.spinBox_number_of_devices.value(),
                                           ui.spinBox_number_of_processors.value(),
                                           labels, connection,
                                           systems, gateways, gateways_memory,
                                           ui.comboBox_device_memory.currentIndex(),
                                           ui.comboBox_throughput.currentIndex(),
                                           labels_memory, labels_speed)
        total_timer = time.time() - timer
        print("%s seconds" % best_time)
        print("Working hours %s seconds" % total_timer)
        ui.label_scientific_poke_method.setStyleSheet('color: rgb(0, 255, 0);')
        ui.label_searching_for_options.setStyleSheet('color: rgb(255, 0, 0);')
        ui.label_evolutionary_method.setStyleSheet('color: rgb(255, 0, 0);')
        ui.label_annealing_method.setStyleSheet('color: rgb(255, 0, 0);')
        ui.label_full_test.setStyleSheet('color: rgb(255, 0, 0);')
    elif method == 2:
        timer = time.time()
        best_time = searching_for_options(ui.spinBox_number_of_devices.value(),
                                          ui.spinBox_number_of_processors.value(),
                                          labels, connection,
                                          systems, gateways, gateways_memory,
                                          ui.comboBox_device_memory.currentIndex(),
                                          ui.comboBox_throughput.currentIndex(),
                                          labels_memory, labels_speed)
        total_timer = time.time() - timer
        print("%s seconds" % best_time)
        print("Working hours %s seconds" % total_timer)
        ui.label_scientific_poke_method.setStyleSheet('color: rgb(255, 0, 0);')
        ui.label_searching_for_options.setStyleSheet('color: rgb(0, 255, 0);')
        ui.label_evolutionary_method.setStyleSheet('color: rgb(255, 0, 0);')
        ui.label_annealing_method.setStyleSheet('color: rgb(255, 0, 0);')
        ui.label_full_test.setStyleSheet('color: rgb(255, 0, 0);')
    elif method == 3:
        timer = time.time()
        best_time = evolutionary_method(ui.spinBox_number_of_devices.value(),
                                           ui.spinBox_number_of_processors.value(),
                                           labels, connection,
                                           systems, gateways, gateways_memory,
                                           ui.comboBox_device_memory.currentIndex(),
                                           ui.comboBox_throughput.currentIndex(),
                                           labels_memory, labels_speed,
                                           ui.spinBox_number_of_generations.value(),
                                           ui.spinBox_number_of_individuals.value(),
                                           ui.doubleSpinBox_mutation_probability.value(),
                                           ui.comboBox_selection.currentIndex())
        total_timer = time.time() - timer
        print("%s seconds" % best_time)
        print("Working hours %s seconds" % total_timer)
        ui.label_scientific_poke_method.setStyleSheet('color: rgb(255, 0, 0);')
        ui.label_searching_for_options.setStyleSheet('color: rgb(255, 0, 0);')
        ui.label_evolutionary_method.setStyleSheet('color: rgb(0, 255, 0);')
        ui.label_annealing_method.setStyleSheet('color: rgb(255, 0, 0);')
        ui.label_full_test.setStyleSheet('color: rgb(255, 0, 0);')
    elif method == 4:
        timer = time.time()
        best_time = annealing_method(ui.spinBox_number_of_devices.value(),
                                        ui.spinBox_number_of_processors.value(),
                                        labels, connection,
                                        systems, gateways, gateways_memory,
                                        ui.comboBox_device_memory.currentIndex(),
                                        ui.comboBox_throughput.currentIndex(),
                                        labels_memory, labels_speed,
                                        ui.spinBox_temperature.value(),
                                        ui.spinBox_temperature_stop.value(),
                                        ui.spinBox_number_of_iterations.value(),
                                        ui.comboBox_cooling.currentIndex())
        total_timer = time.time() - timer
        print("%s seconds" % best_time)
        print("Working hours %s seconds" % total_timer)
        ui.label_scientific_poke_method.setStyleSheet('color: rgb(255, 0, 0);')
        ui.label_searching_for_options.setStyleSheet('color: rgb(255, 0, 0);')
        ui.label_evolutionary_method.setStyleSheet('color: rgb(255, 0, 0);')
        ui.label_annealing_method.setStyleSheet('color: rgb(0, 255, 0);')
        ui.label_full_test.setStyleSheet('color: rgb(255, 0, 0);')
    else:
        data_collection(labels, connection, systems, gateways, gateways_memory)
        ui.label_scientific_poke_method.setStyleSheet('color: rgb(255, 0, 0);')
        ui.label_searching_for_options.setStyleSheet('color: rgb(255, 0, 0);')
        ui.label_evolutionary_method.setStyleSheet('color: rgb(255, 0, 0);')
        ui.label_annealing_method.setStyleSheet('color: rgb(255, 0, 0);')
        ui.label_full_test.setStyleSheet('color: rgb(0, 255, 0);')


def data_collection(labels, connection, systems, gateways, gateways_memory):
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

    sheet.write(1, 0,
                xlwt.Formula("(" + str(ui.spinBox_number_of_tests.value()) + "-" + "COUNTBLANK(A4:A"
                             + str(ui.spinBox_number_of_tests.value() + 3) + "))/"
                             + str(ui.spinBox_number_of_tests.value())))
    sheet.write(1, 1,
                xlwt.Formula("(" + str(ui.spinBox_number_of_tests.value()) + "-" + "COUNTBLANK(B4:B"
                             + str(ui.spinBox_number_of_tests.value() + 3) + "))/"
                             + str(ui.spinBox_number_of_tests.value())))
    sheet.write(1, 2,
                xlwt.Formula("(" + str(ui.spinBox_number_of_tests.value()) + "-" + "COUNTBLANK(C4:C"
                             + str(ui.spinBox_number_of_tests.value() + 3) + "))/"
                             + str(ui.spinBox_number_of_tests.value())))
    sheet.write(1, 3,
                xlwt.Formula("(" + str(ui.spinBox_number_of_tests.value()) + "-" + "COUNTBLANK(D4:D"
                             + str(ui.spinBox_number_of_tests.value() + 3) + "))/"
                             + str(ui.spinBox_number_of_tests.value())))
    sheet.write(1, 4,
                xlwt.Formula("(" + str(ui.spinBox_number_of_tests.value()) + "-" + "COUNTBLANK(E4:E"
                             + str(ui.spinBox_number_of_tests.value() + 3) + "))/"
                             + str(ui.spinBox_number_of_tests.value())))
    sheet.write(1, 5,
                xlwt.Formula("(" + str(ui.spinBox_number_of_tests.value()) + "-" + "COUNTBLANK(F4:F"
                             + str(ui.spinBox_number_of_tests.value() + 3) + "))/"
                             + str(ui.spinBox_number_of_tests.value())))
    sheet.write(1, 6,
                xlwt.Formula("(" + str(ui.spinBox_number_of_tests.value()) + "-" + "COUNTBLANK(G4:G"
                             + str(ui.spinBox_number_of_tests.value() + 3) + "))/"
                             + str(ui.spinBox_number_of_tests.value())))
    sheet.write(1, 7,
                xlwt.Formula("(" + str(ui.spinBox_number_of_tests.value()) + "-" + "COUNTBLANK(H4:H"
                             + str(ui.spinBox_number_of_tests.value() + 3) + "))/"
                             + str(ui.spinBox_number_of_tests.value())))
    sheet.write(1, 8,
                xlwt.Formula("(" + str(ui.spinBox_number_of_tests.value()) + "-" + "COUNTBLANK(I4:I"
                             + str(ui.spinBox_number_of_tests.value() + 3) + "))/"
                             + str(ui.spinBox_number_of_tests.value())))
    sheet.write(1, 9,
                xlwt.Formula("(" + str(ui.spinBox_number_of_tests.value()) + "-" + "COUNTBLANK(J4:J"
                             + str(ui.spinBox_number_of_tests.value() + 3) + "))/"
                             + str(ui.spinBox_number_of_tests.value())))
    sheet.write(1, 10,
                xlwt.Formula("(" + str(ui.spinBox_number_of_tests.value()) + "-" + "COUNTBLANK(K4:K"
                             + str(ui.spinBox_number_of_tests.value() + 3) + "))/"
                             + str(ui.spinBox_number_of_tests.value())))
    sheet.write(1, 11,
                xlwt.Formula("(" + str(ui.spinBox_number_of_tests.value()) + "-" + "COUNTBLANK(L4:L"
                             + str(ui.spinBox_number_of_tests.value() + 3) + "))/"
                             + str(ui.spinBox_number_of_tests.value())))


    sheet.write(2, 0,
                xlwt.Formula("AVERAGE(A4:A" + str(ui.spinBox_number_of_tests.value() + 3) + ")"))
    sheet.write(2, 1,
                xlwt.Formula("AVERAGE(B4:B" + str(ui.spinBox_number_of_tests.value() + 3) + ")"))
    sheet.write(2, 2,
                xlwt.Formula("AVERAGE(C4:C" + str(ui.spinBox_number_of_tests.value() + 3) + ")"))
    sheet.write(2, 3,
                xlwt.Formula("AVERAGE(D4:D" + str(ui.spinBox_number_of_tests.value() + 3) + ")"))
    sheet.write(2, 4,
                xlwt.Formula("AVERAGE(E4:E" + str(ui.spinBox_number_of_tests.value() + 3) + ")"))
    sheet.write(2, 5,
                xlwt.Formula("AVERAGE(F4:F" + str(ui.spinBox_number_of_tests.value() + 3) + ")"))
    sheet.write(2, 6,
                xlwt.Formula("AVERAGE(G4:G" + str(ui.spinBox_number_of_tests.value() + 3) + ")"))
    sheet.write(2, 7,
                xlwt.Formula("AVERAGE(H4:H" + str(ui.spinBox_number_of_tests.value() + 3) + ")"))
    sheet.write(2, 8,
                xlwt.Formula("AVERAGE(I4:I" + str(ui.spinBox_number_of_tests.value() + 3) + ")"))
    sheet.write(2, 9,
                xlwt.Formula("AVERAGE(J4:J" + str(ui.spinBox_number_of_tests.value() + 3) + ")"))
    sheet.write(2, 10,
                xlwt.Formula("AVERAGE(K4:K" + str(ui.spinBox_number_of_tests.value() + 3) + ")"))
    sheet.write(2, 11,
                xlwt.Formula("AVERAGE(L4:L" + str(ui.spinBox_number_of_tests.value() + 3) + ")"))

    all_time = time.time()
    for graphs in range(ui.spinBox_number_of_tests.value()):
        labels, connection, labels_memory, labels_speed = graph_construction(ui.spinBox_count_of_nodes.value(),
                                                                             ui.doubleSpinBox_connection_probability.value())
        systems, gateways, gateways_memory = system_construction(ui.spinBox_number_of_devices.value(),
                                                                 ui.spinBox_number_of_processors.value(),
                                                                 ui.comboBox_communication_type.currentIndex())

        if ui.checkBox_scientific_poke_method.checkState():
            timer = time.time()
            best_time = scientific_poke_method(ui.spinBox_number_of_devices.value(),
                                               ui.spinBox_number_of_processors.value(),
                                               labels, connection,
                                               systems, gateways, gateways_memory,
                                               ui.comboBox_device_memory.currentIndex(),
                                               ui.comboBox_throughput.currentIndex(),
                                               labels_memory, labels_speed)
            total_timer = time.time() - timer
            if best_time == -1:
                sheet.write(graphs + 3, 0, "")
                sheet.write(graphs + 3, 1, "")
            else:
                sheet.write(graphs + 3, 0, best_time)
                sheet.write(graphs + 3, 1, total_timer)

        if ui.checkBox_searching_for_options.checkState():
            timer = time.time()
            best_time = searching_for_options(ui.spinBox_number_of_devices.value(),
                                              ui.spinBox_number_of_processors.value(),
                                              labels, connection,
                                              systems, gateways, gateways_memory,
                                              ui.comboBox_device_memory.currentIndex(),
                                              ui.comboBox_throughput.currentIndex(),
                                              labels_memory, labels_speed)
            total_timer = time.time() - timer
            if best_time == -1:
                sheet.write(graphs + 3, 2, "")
                sheet.write(graphs + 3, 3, "")
            else:
                sheet.write(graphs + 3, 2, best_time)
                sheet.write(graphs + 3, 3, total_timer)

        if ui.checkBox_evolutionary_method.checkState():
            timer = time.time()
            best_time = evolutionary_method(ui.spinBox_number_of_devices.value(),
                                            ui.spinBox_number_of_processors.value(),
                                            labels, connection,
                                            systems, gateways, gateways_memory,
                                            ui.comboBox_device_memory.currentIndex(),
                                            ui.comboBox_throughput.currentIndex(),
                                            labels_memory, labels_speed,
                                            ui.spinBox_number_of_generations.value(),
                                            ui.spinBox_number_of_individuals.value(),
                                            ui.doubleSpinBox_mutation_probability.value(),
                                            0)
            total_timer = time.time() - timer
            if best_time == -1:
                sheet.write(graphs + 3, 4, "")
                sheet.write(graphs + 3, 5, "")
            else:
                sheet.write(graphs + 3, 4, best_time)
                sheet.write(graphs + 3, 5, total_timer)

            timer = time.time()
            best_time = evolutionary_method(ui.spinBox_number_of_devices.value(),
                                            ui.spinBox_number_of_processors.value(),
                                            labels, connection,
                                            systems, gateways, gateways_memory,
                                            ui.comboBox_device_memory.currentIndex(),
                                            ui.comboBox_throughput.currentIndex(),
                                            labels_memory, labels_speed,
                                            ui.spinBox_number_of_generations.value(),
                                            ui.spinBox_number_of_individuals.value(),
                                            ui.doubleSpinBox_mutation_probability.value(),
                                            1)
            total_timer = time.time() - timer
            if best_time == -1:
                sheet.write(graphs + 3, 6, "")
                sheet.write(graphs + 3, 7, "")
            else:
                sheet.write(graphs + 3, 6, best_time)
                sheet.write(graphs + 3, 7, total_timer)

        if ui.checkBox_annealing_method.checkState():
            timer = time.time()
            best_time = annealing_method(ui.spinBox_number_of_devices.value(),
                                         ui.spinBox_number_of_processors.value(),
                                         labels, connection,
                                         systems, gateways, gateways_memory,
                                         ui.comboBox_device_memory.currentIndex(),
                                         ui.comboBox_throughput.currentIndex(),
                                         labels_memory, labels_speed,
                                         ui.spinBox_temperature.value(),
                                         ui.spinBox_temperature_stop.value(),
                                         ui.spinBox_number_of_iterations.value(),
                                         0)
            total_timer = time.time() - timer
            if best_time == -1:
                sheet.write(graphs + 3, 8, "")
                sheet.write(graphs + 3, 9, "")
            else:
                sheet.write(graphs + 3, 8, best_time)
                sheet.write(graphs + 3, 9, total_timer)

            timer = time.time()
            best_time = annealing_method(ui.spinBox_number_of_devices.value(),
                                         ui.spinBox_number_of_processors.value(),
                                         labels, connection,
                                         systems, gateways, gateways_memory,
                                         ui.comboBox_device_memory.currentIndex(),
                                         ui.comboBox_throughput.currentIndex(),
                                         labels_memory, labels_speed,
                                         ui.spinBox_temperature.value(),
                                         ui.spinBox_temperature_stop.value(),
                                         ui.spinBox_number_of_iterations.value(),
                                         1)
            total_timer = time.time() - timer
            if best_time == -1:
                sheet.write(graphs + 3, 10, "")
                sheet.write(graphs + 3, 11, "")
            else:
                sheet.write(graphs + 3, 10, best_time)
                sheet.write(graphs + 3, 11, total_timer)

    all_time = time.time() - all_time
    print(all_time)

    book.save("Full test.xls")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    # Начало кода

    ui.pushButton_scientific_poke_method.clicked.connect(lambda: beginning_of_work(1))
    ui.pushButton_searching_for_options.clicked.connect(lambda: beginning_of_work(2))
    ui.pushButton_evolutionary_method.clicked.connect(lambda: beginning_of_work(3))
    ui.pushButton_annealing_method.clicked.connect(lambda: beginning_of_work(4))
    ui.pushButton_full_test.clicked.connect(lambda: beginning_of_work(0))
    # Конец кода
    sys.exit(app.exec_())
