import numpy as np
from itertools import combinations


def system_construction(number_of_devices, number_of_processors, communication_type):
    systems = [[dict() for processor in range(number_of_processors)] for device in range(number_of_devices)]
    gateways = dict()
    gateways_memory = dict()

    if communication_type == 0:
        system_construction = mesh_topology(number_of_devices)
    else:
        system_construction = passive_star(number_of_devices)

    number_of_gateway = 0
    for gateway in system_construction:
        gateways[number_of_gateway] = gateway
        gateways_memory[number_of_gateway] = {}
        number_of_gateway += 1

    return systems, gateways, gateways_memory


def mesh_topology(number_of_devices):
    devices = np.arange(number_of_devices)
    connection = set()
    for combination in combinations(devices, 2):
        connection.add(combination)
    return connection


def passive_star(number_of_devices):
    connection = set()
    for combination in range(number_of_devices):
        connection.add((-1, combination))
    return connection
