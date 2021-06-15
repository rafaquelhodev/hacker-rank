def getQueenPossibilities():
    possibilities = [
        [1, 1],
        [1, -1],
        [-1, 1],
        [-1, -1],
        [0, 1],
        [0, -1],
        [1, 0],
        [-1, 0],
    ]
    return possibilities


def isValidPosition(x, y, n, obstaclesMap):
    if x <= n and y <= n and x >= 1 and y >= 1 and (x, y) not in obstaclesMap:
        return True
    return False


def getObstaclesMap(obstacles):
    obstaclesMap = {}
    for obstacle in obstacles:
        obstaclesMap[(obstacle[0], obstacle[1])] = 1


def queensAttack(n, k, r_q, c_q, obstacles):
    positions = 0

    possibilities = getQueenPossibilities()

    obstaclesMap = getObstaclesMap(obstacles)
    for possibility in possibilities:
        x = r_q
        y = c_q

        validPosition = True
        while validPosition:
            x += possibility[0]
            y += possibility[1]

            validPosition = isValidPosition(x, y, n, obstaclesMap)

            if validPosition:
                positions += 1

    return positions


if __name__ == "__main__":

    print(queensAttack(4, 1, 4, 4, []))
