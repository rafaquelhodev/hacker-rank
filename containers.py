import operator

def organizingContainers(container):
    status = "Possible"
    
    total_containers = len(container)
    ball_types = len(container[0])
    
    balls_per_container = []
    total_balls_per_type = ball_types*[0]
    
    for container_i in range(len(container)):
        sum_container = 0
        for ball_type_i in range(len(container[container_i])):
            balls_type = container[container_i][ball_type_i]
            balls_per_container[ball_type_i] += balls_type
            sum_container += balls_type
            
        balls_per_container.append(sum_container)
    
    balls_per_container = sorted(balls_per_container)
    total_balls_per_type = sorted(total_balls_per_type)
    
    if (len(balls_per_container) != len(total_balls_per_type)):
        return "Impossible"
    
    for index in range(len(total_balls_per_type)):
        if (balls_per_container[index] != total_balls_per_type[index]):
            return "Impossible"

    return "Possible"
    
if __name__ == "__main__":
    containers = [[0, 2, 1], [1, 1, 1], [2, 0, 0]]
    status = organizingContainers(containers)
    print(status)