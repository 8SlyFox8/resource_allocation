import random
import copy
from system_operation import system_operation, search_for_a_winner


def evolutionary_method(number_of_devices, number_of_processors,
                        labels, connection,
                        systems, gateways, gateways_memory,
                        device_memory, throughput,
                        labels_memory, labels_speed,
                        number_of_generations, number_of_individuals, mutation_probability, selection,
                        communication_type):
    best_time = -1
    individuals = []
    for individual in range(number_of_individuals):
        individuals.append(first_gen(number_of_devices, number_of_processors, labels, systems))
    for gen in range(number_of_generations):
        results = {}
        for individual in range(number_of_individuals):
            finish_timer = system_operation(connection, individuals[individual], gateways, gateways_memory,
                                            device_memory, throughput, labels_memory, labels_speed,
                                            communication_type)
            results[individual] = finish_timer
        if selection == 0:
            individuals = analysis_roulette(results, individuals, labels, systems, number_of_individuals)
        else:
            individuals = analysis_ranging(results, individuals, labels, systems, number_of_individuals)
        individuals = mutation(individuals, labels, systems, mutation_probability)
    for individual in range(number_of_individuals):
        finish_timer = system_operation(connection, individuals[individual], gateways, gateways_memory,
                                        device_memory, throughput, labels_memory, labels_speed,
                                        communication_type)
        best_time = search_for_a_winner(finish_timer, best_time)
    return best_time


def first_gen(number_of_devices, number_of_processors, labels, systems):
    individual = copy.deepcopy(systems)
    for number in range(len(labels)):
        system_dice = random.randint(0, number_of_devices - 1)
        processor_dice = random.randint(0, number_of_processors - 1)
        for system in range(number_of_devices):
            for processor in range(number_of_processors):
                if system == system_dice and processor == processor_dice:
                    individual[system][processor][number] = labels[number]
    return individual


# Метод рулетки
def analysis_roulette(results, individuals, labels, systems, number_of_individuals):
    all_time = 0
    max_result = max(results.values())
    for result in results:
        if results[result] == -1:
            results[result] = max_result*2
    for individual in range(number_of_individuals):
        all_time += max_result - results[individual]
    if all_time == 0:
        for individual in range(number_of_individuals):
            results[individual] = 1 / number_of_individuals
    else:
        for individual in range(number_of_individuals):
            results[individual] = (max_result - results[individual]) / all_time
    new_individuals = []
    for couple in range(
            (number_of_individuals // 2) + (number_of_individuals % 2)):
        parents = []
        for i in range(2):
            dice = results[0]
            a = random.random()
            for individual in range(number_of_individuals):
                if a < dice:
                    parents.append(individuals[individual])
                    break
                else:
                    if individual != range(number_of_individuals - 1):
                        dice += results[individual + 1]
        if number_of_individuals % 2 == 1:
            if couple == number_of_individuals // 2:
                new_individuals.append(crossing(parents, labels, systems)[0])
            else:
                new_individuals.append(crossing(parents, labels, systems)[0])
                new_individuals.append(crossing(parents, labels, systems)[1])
        else:
            new_individuals.append(crossing(parents, labels, systems)[0])
            new_individuals.append(crossing(parents, labels, systems)[1])
    return new_individuals


#Метод ранжирования
def analysis_ranging(results, individuals, labels, systems, number_of_individuals):
    all_time = {}
    max_result = max(results.values())
    for result in results:
        if results[result] == -1:
            results[result] = max_result*2
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
    for couple in range((number_of_individuals // 2) + (number_of_individuals % 2)):
        parents = []
        for i in range(2):
            dice = {}
            a = random.randint(1, save_max_result)
            for individual, result in results.items():
                if (a <= result[0]) and (a > result[1]):
                    dice[individual] = result
            parents.append(individuals[random.choice(list(dice))])
        if number_of_individuals % 2 == 1:
            if couple == number_of_individuals // 2:
                new_individuals.append(crossing(parents, labels, systems)[0])
            else:
                new_individuals.append(crossing(parents, labels, systems)[0])
                new_individuals.append(crossing(parents, labels, systems)[1])
        else:
            new_individuals.append(crossing(parents, labels, systems)[0])
            new_individuals.append(crossing(parents, labels, systems)[1])
    return new_individuals


def crossing(parents, labels, systems):
    children = [[[dict() for processor in range(len(systems[0]))] for device in range(len(systems))] for child in range(2)]
    for nodes in range(len(labels)):
        a = random.random()
        for i in range(len(systems)):
            for j in range(len(systems[0])):
                for number in parents[0][i][j]:
                    if a < 0.5 and number == nodes:
                        children[1][i][j][number] = parents[0][i][j][number]
                    if a >= 0.5 and number == nodes:
                        children[0][i][j][number] = parents[0][i][j][number]
                for number in parents[1][i][j]:
                    if a < 0.5 and number == nodes:
                        children[0][i][j][number] = parents[1][i][j][number]
                    if a >= 0.5 and number == nodes:
                        children[1][i][j][number] = parents[1][i][j][number]
    return children


def mutation(individuals, labels, systems, mutation_probability):
    new_individuals = []
    for individual in individuals:
        a = random.random()
        if a < mutation_probability:
            mutant = [[dict() for processor in range(len(systems[0]))] for device in range(len(systems))]
            dice = random.randint(0, len(labels) - 1)
            for nodes in range(len(labels)):
                for i in range(len(systems)):
                    for j in range(len(systems[0])):
                        for number in individual[i][j]:
                            if number == nodes:
                                if number == dice:
                                    cpu = j
                                    machine = i
                                    while machine == i:
                                        while cpu == j:
                                            cpu = random.randint(0, len(systems[0])-1)
                                        machine = random.randint(0, len(systems)-1)
                                    mutant[machine][cpu][number] = individual[i][j][number]
                                else:
                                    mutant[i][j][number] = individual[i][j][number]
            new_individuals.append(mutant)
        else:
            new_individuals.append(individual)
    return new_individuals
