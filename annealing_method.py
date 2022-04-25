import numpy as np
from system_operation import system_operation
from evolutionary_method import first_gen, mutation


def annealing_method(number_of_devices, number_of_processors,
                     labels, connection,
                     systems, gateways, gateways_memory,
                     device_memory, throughput,
                     labels_memory, labels_speed,
                     initial_temperature, temperature_stop, number_of_iterations, cooling,
                     communication_type):
    option = first_gen(number_of_devices, number_of_processors, labels, systems)
    finish_timer = system_operation(connection, option, gateways, gateways_memory,
                                    device_memory, throughput, labels_memory, labels_speed,
                                    communication_type)
    temperature = initial_temperature
    new_option = []
    new_option.append(option)
    for iterator in range(1, number_of_iterations):
        new_option = mutation(new_option, labels, systems, 1)
        new_timer = system_operation(connection, new_option[0], gateways, gateways_memory,
                                     device_memory, throughput, labels_memory, labels_speed,
                                     communication_type)

        delta_timer = new_timer - finish_timer
        if (delta_timer < 0 and new_timer != -1) or finish_timer == -1:
            finish_timer = new_timer
            option = new_option
        else:
            dice = np.exp(-delta_timer / temperature)
            if np.random.rand() <= dice:
                finish_timer = new_timer
                option = new_option
        if cooling == 0:
            temperature = reverse_linear_cooling(initial_temperature, iterator)
        else:
            temperature = linear_cooling(initial_temperature, iterator, number_of_iterations)

        if temperature <= temperature_stop:
            break

    return finish_timer


# схема обратного линейного охлаждения
def reverse_linear_cooling(current_temperature, iterator):
    return current_temperature / iterator


# схема линейного охлаждения
def linear_cooling(current_temperature, iterator, number_of_iterations):
    return current_temperature - (current_temperature/number_of_iterations) * iterator