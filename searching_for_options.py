import copy
from system_operation import system_operation, search_for_a_winner


def searching_for_options(number_of_devices, number_of_processors,
                          labels, connection,
                          systems, gateways, gateways_memory,
                          device_memory, throughput,
                          labels_memory, labels_speed,
                          communication_type):
    best_time = -1
    all_options = [[[] for processor in range(number_of_devices*number_of_processors)] for device in range(len(labels))]
    indexes = [0 for device in range(len(labels))]
    for number in range(len(labels)):
        space_systems = 0
        space_processor = 0
        for space in range(number_of_devices*number_of_processors):
            all_options[number][space].append(space_systems)
            all_options[number][space].append(space_processor)
            space_processor += 1
            if space_processor >= number_of_processors:
                space_processor = 0
                space_systems += 1

    for number_space in range((number_of_processors*number_of_devices)**len(labels)):

        index_options = []
        for number in range(len(labels)):
            index_options.append(all_options[number][indexes[number]])

        option = copy.deepcopy(systems)
        for number in range(len(labels)):
            for system in range(number_of_devices):
                if system == index_options[number][0]:
                    for processor in range(number_of_processors):
                        if processor == index_options[number][1]:
                            option[system][processor][number] = labels[number]

        finish_timer = system_operation(connection, option, gateways, gateways_memory,
                                        device_memory, throughput, labels_memory, labels_speed,
                                        communication_type)
        best_time = search_for_a_winner(finish_timer, best_time)

        index = 0
        count = number_of_devices*number_of_processors
        if number_space != (number_of_processors*number_of_devices)**len(labels) - 1:
            index_selection(indexes, index, count)

    return best_time

def index_selection(indexes, index, count):
    indexes[index] += 1
    if indexes[index] >= count:
        indexes[index] = 0
        index_selection(indexes, index + 1, count)

