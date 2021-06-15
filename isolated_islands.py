from collections import deque


def get_possible_movements():
    return [[1, 0], [-1, 0], [0, 1], [0, -1]]


def is_valid_movement(node, matrix):
    node_x = node[0]
    node_y = node[1]

    if node_x >= len(matrix) or node_x < 0 or node_y >= len(matrix[0]) or node_y < 0:
        return False
    return True


def get_border_islands(matrix):
    border_islands = {}

    top_down_rows = [0, len(matrix) - 1]
    for rowId in top_down_rows:
        for col in range(0, len(matrix[rowId])):
            if matrix[rowId][col] == 1:
                border_islands[(rowId, col)] = True

    for rowId in range(1, len(matrix) - 1):
        if matrix[rowId][0] == 1:
            border_islands[(rowId, 0)] = True

        if matrix[rowId][len(matrix[rowId]) - 1] == 1:
            border_islands[(rowId, len(matrix[rowId]) - 1)] = True

    return border_islands


def get_islands_connected_to_boder(matrix):
    visited_nodes = {}

    possible_moves = get_possible_movements()

    border_islands = get_border_islands(matrix)

    q = deque()

    for border in border_islands:
        q.append(border)

    while q:
        node = q.popleft()

        if node not in visited_nodes and is_valid_movement(node, matrix):
            visited_nodes[node] = True

            current_x = node[0]
            current_y = node[1]

            if matrix[current_x][current_y] == 1:
                border_islands[(current_x, current_y)] = True

            for move in possible_moves:
                next_x = node[0] + move[0]
                next_y = node[1] + move[1]
                new_node = (next_x, next_y)

                if is_valid_movement(new_node, matrix) and matrix[next_x][next_y] == 1:
                    q.append((next_x, next_y))

    return border_islands


def clean_not_connected_islands(matrix, border_islands):
    for [i, _] in enumerate(matrix):
        for [j, _] in enumerate(matrix[i]):
            if (i, j) not in border_islands:
                matrix[i][j] = 0


if __name__ == "__main__":
    matrix = [[1, 0, 0, 0, 1], [0, 1, 0, 0, 0], [0, 0, 0, 0, 1]]

    border_islands = get_islands_connected_to_boder(matrix)

    clean_not_connected_islands(matrix, border_islands)

    print(matrix)
