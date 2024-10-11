#  Heuristique de Recherche A*
import heapq


class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Distance du départ au nœud actuel
        self.h = 0  # Distance heuristique du nœud actuel à la destination
        self.f = 0  # Coût total g + h


def astar(maze, start, end):
    open_list = []
    closed_list = set()
    start_node = Node(start)
    end_node = Node(end)
    heapq.heappush(open_list, (start_node.f, start_node))

    while open_list:
        _, current_node = heapq.heappop(open_list)
        closed_list.add(current_node.position)

        if current_node.position == end_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # Adjacent squares
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[0]) - 1) or \
                    node_position[1] < 0:
                continue

            if maze[node_position[0]][node_position[1]] != 0:
                continue

            new_node = Node(node_position, current_node)
            children.append(new_node)

        for child in children:
            if child.position in closed_list:
                continue

            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + (
                        (child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            if len([i for i in open_list if child.position == i[1].position and child.g > i[1].g]):
                continue

            heapq.heappush(open_list, (child.f, child))

    return None


# Exemple d'utilisation
maze = [[0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]]

start = (0, 0)
end = (4, 4)
path = astar(maze, start, end)
print(path)

#  Heuristique Gloutonne pour le Problème du Sac à Dos
def knapsack_greedy(items, max_weight):
    items = sorted(items, key=lambda x: x[1] / x[0], reverse=True)
    total_value = 0
    total_weight = 0
    knapsack = []

    for weight, value in items:
        if total_weight + weight <= max_weight:
            knapsack.append((weight, value))
            total_weight += weight
            total_value += value

    return knapsack, total_value


# Exemple d'utilisation
items = [(2, 3), (3, 4), (4, 5), (5, 8)]
max_weight = 8
knapsack, total_value = knapsack_greedy(items, max_weight)
print("Items in knapsack:", knapsack)
print("Total value:", total_value)

#  Heuristique de Descente de Gradient pour la Régression Linéaire

import numpy as np

def gradient_descent(X, y, learning_rate=0.01, iterations=1000):
    m = len(y)
    theta = np.zeros(X.shape[1])
    for _ in range(iterations):
        predictions = X.dot(theta)
        errors = predictions - y
        theta -= (learning_rate / m) * np.dot(X.T, errors)
    return theta

# Exemple d'utilisation
X = np.array([[1, 1], [1, 2], [1, 3], [1, 4]])
y = np.array([2, 2.5, 3, 3.5])
theta = gradient_descent(X, y)
print("Optimal theta:", theta)
