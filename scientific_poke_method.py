import random
import copy
from system_operation import system_operation, search_for_a_winner


def scientific_poke_method(number_of_devices, number_of_processors,
                           labels, connection,
                           systems, gateways, gateways_memory,
                           device_memory, throughput,
                           labels_memory, labels_speed):
    best_time = -1
    poke = copy.deepcopy(systems)
    for number in range(len(labels)):
        system_dice = random.randint(0, number_of_devices - 1)
        processor_dice = random.randint(0, number_of_processors - 1)
        for system in range(number_of_devices):
            for processor in range(number_of_processors):
                if system == system_dice and processor == processor_dice:
                    poke[system][processor][number] = labels[number]

    finish_timer = system_operation(connection, poke, gateways, gateways_memory,
                                    device_memory, throughput, labels_memory, labels_speed)
    best_time = search_for_a_winner(finish_timer, best_time)

    return best_time
