import copy


def search_for_a_winner(current_time, best_time):
    if best_time == -1:
        best_time = current_time
    if current_time < best_time and current_time != -1:
        best_time = current_time
    return best_time


def system_operation(connection, systems, gateways, gateways_memory, device_memory, throughput, labels_memory, labels_speed):
    link_list = connection.copy()
    distribution = copy.deepcopy(systems)
    finish_timer = 0
    time_counter = [[0 for processor in range(len(systems[0]))] for device in range(len(systems))]

    if device_memory == 0:
        device_memory = 10
    elif device_memory == 1:
        device_memory = 20
    elif device_memory == 2:
        device_memory = 30
    elif device_memory == 3:
        device_memory = 40
    elif device_memory == 4:
        device_memory = 50
    elif device_memory == 5:
        device_memory = 60
    elif device_memory == 6:
        device_memory = 70
    elif device_memory == 7:
        device_memory = 80
    elif device_memory == 8:
        device_memory = 90
    else:
        device_memory = 100

    if throughput == 0:
        throughput = 10
    elif throughput == 1:
        throughput = 11
    elif throughput == 2:
        throughput = 12
    elif throughput == 3:
        throughput = 13
    elif throughput == 4:
        throughput = 14
    elif throughput == 5:
        throughput = 15
    elif throughput == 6:
        throughput = 16
    elif throughput == 7:
        throughput = 17
    elif throughput == 8:
        throughput = 18
    elif throughput == 9:
        throughput = 19
    else:
        throughput = 20

    del_tasks = []
    task_in_gateways_memory = []
    exitflag1 = False
    while exitflag1 != True:
        for system in range(len(distribution)):
            device_memory_error = 0
            for processor in range(len(distribution[system])):
                if distribution[system][processor] != {}:
                    for task1 in distribution[system][processor]:
                        for task_memory in labels_memory:
                            if task1 == task_memory:
                                device_memory_error += labels_memory[task_memory]
                        break
                    if device_memory_error > device_memory:
                        print("ERROR: Not enough memory")
                        return -1

        counter = 0
        for system in range(len(distribution)):
            for processor in range(len(distribution[system])):
                if distribution[system][processor] != {}:
                    exitflag2 = False
                    for task in distribution[system][processor]:
                        for number_in_matrix in link_list:
                            if number_in_matrix[1] == task:
                                time_counter[system][processor] += 1
                                break
                        else:
                            exitflag2 = True

                        if exitflag2 == False:
                            break

                        time_counter[system][processor] += 1
                        distribution[system][processor][task] -= 1
                        if distribution[system][processor][task] == 0:
                            del_tasks.append(task)
                        break
                else:
                    counter += 1

        del_gateways_memory = copy.deepcopy(gateways_memory)
        for gateway in gateways_memory:
            throughput_error = 0
            for task in del_gateways_memory[gateway]:
                throughput_error += gateways_memory[gateway][task]
                if throughput_error > throughput:
                    break
                gateways_memory[gateway][task] -= 1
                if gateways_memory[gateway][task] == 0:
                    del gateways_memory[gateway][task]

        for task in del_tasks:
            for system in range(len(distribution)):
                for processor in range(len(distribution[system])):
                    if distribution[system][processor] != {}:
                        if task in distribution[system][processor]:
                            del distribution[system][processor][task]

            find_connect(task, link_list, systems, gateways, gateways_memory, task_in_gateways_memory, labels_speed)

        if counter == len(distribution)*len(distribution[0]):
            exitflag1 = True

    for system in time_counter:
        for time in system:
            if time > finish_timer:
                finish_timer = time

    return finish_timer


def find_connect(current_task, link_list, systems, gateways, gateways_memory, task_in_gateways_memory, labels_speed):
    current_system = -1
    for system in range(len(systems)):
        for processor in range(len(systems[system])):
            if current_task in systems[system][processor]:
                current_system = system

    if current_task not in task_in_gateways_memory:
        for number_in_matrix in link_list:
            if number_in_matrix[0] == current_task:
                find_task = number_in_matrix[1]
                for system in range(len(systems)):
                    for processor in range(len(systems[system])):
                        if systems[system][processor] != {}:
                            if find_task in systems[system][processor]:
                                find_system = system
                                if find_system != current_system:
                                    for gateway in gateways:
                                        if gateways[gateway][0] == current_system \
                                                and gateways[gateway][1] == find_system:
                                            for task_speed in labels_speed:
                                                if current_task == task_speed:
                                                    gateways_memory[gateway][current_task] = labels_speed[task_speed]
                                            task_in_gateways_memory.append(current_task)

                                        elif gateways[gateway][1] == current_system \
                                                and gateways[gateway][0] == find_system:
                                            for task_speed in labels_speed:
                                                if current_task == task_speed:
                                                    gateways_memory[gateway][current_task] = labels_speed[task_speed]
                                            task_in_gateways_memory.append(current_task)

    exitflag3 = False
    while exitflag3 != True:
        for number_in_matrix in link_list:
            if number_in_matrix[0] == current_task:

                find_task = number_in_matrix[1]
                find_system = -1
                for system in range(len(systems)):
                    for processor in range(len(systems[system])):
                        if systems[system][processor] != {}:
                            if find_task in systems[system][processor]:
                                find_system = system
                exitflag4 = True
                for gateway in gateways_memory:
                    if current_task in gateways_memory[gateway]:
                        if current_system != find_system:
                            exitflag4 = False

                if exitflag4 == False:
                    continue

                link_list.remove(number_in_matrix)
                break
        else:
            exitflag3 = True