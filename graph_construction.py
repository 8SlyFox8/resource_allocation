import networkx as nx
from itertools import combinations
import random
import numpy as np


def plot(count_of_tasks, connection_probability): #Количество задач и вероятность взаимосвязи
    number_of_tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  #Тип задачи

    nodes = list(range(0, count_of_tasks))
    number_of_tasks = random.choices(number_of_tasks, k=count_of_tasks)
    labels = dict(zip(nodes, number_of_tasks))

    connection = set()
    for combination in combinations(nodes, 2):
        a = random.random()
        if a < connection_probability:
            connection.add(combination)

    graph = nx.DiGraph()

    graph.add_nodes_from(nodes)
    graph.add_edges_from(connection)

    nx.draw_networkx(graph, pos=nx.circular_layout(graph), labels=labels, node_color='y', node_size=1000, edge_color='black', arrows=True, arrowsize=10,  width=2)

    return labels, connection
