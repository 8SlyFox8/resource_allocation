from itertools import combinations
import random


def graph_construction(count_of_tasks, connection_probability): #Количество задач и вероятность взаимосвязи
    number_of_tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  #Тип задачи

    nodes = list(range(0, count_of_tasks))
    tasks_mixing = random.choices(number_of_tasks, k=count_of_tasks)
    labels = dict(zip(nodes, tasks_mixing))
    tasks_mixing = random.choices(number_of_tasks, k=count_of_tasks)
    labels_memory = dict(zip(nodes, tasks_mixing))
    tasks_mixing = random.choices(number_of_tasks, k=count_of_tasks)
    labels_speed = dict(zip(nodes, tasks_mixing))

    connection = set()
    for combination in combinations(nodes, 2):
        a = random.random()
        if a < connection_probability:
            connection.add(combination)

    return labels, connection, labels_memory, labels_speed
