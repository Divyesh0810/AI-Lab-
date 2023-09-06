#8-puzzle solution with heuristic values of each state in the state space tree
#required inputs 1.only the level till which the user desires to print the state spaces
from collections import deque

GOAL_STATE = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def is_valid_move(x, y):
    return 0 <= x < 3 and 0 <= y < 3

def calculate_heuristic(state):
    misplaced_tiles = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != GOAL_STATE[i][j]:
                misplaced_tiles += 1
    return misplaced_tiles

def create(initial_state, level):
    initial_state = [list(row) for row in initial_state]
    queue = deque([(initial_state, 0)]) 

    while queue:
        current_state, current_level = queue.popleft()
        if current_level > level:
            break
        print("Level:", current_level)
        for row in current_state:
            print(" ".join(map(str, row)))
        heuristic_value = calculate_heuristic(current_state)
        print("Heuristic Value:", heuristic_value)
        print()
        for i in range(3):
            for j in range(3):
                if current_state[i][j] == 0:
                    empty_x, empty_y = i, j
        for dx, dy in MOVES:
            new_x, new_y = empty_x + dx, empty_y + dy
            if is_valid_move(new_x, new_y):
                new_state = [list(row) for row in current_state]
                new_state[empty_x][empty_y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[empty_x][empty_y]
                queue.append((new_state, current_level + 1))

initial_state = [
    [1, 2, 3],
    [4, 5, 6],
    [8, 7, 0]
]
level_number = int(input("Enter the max level required for the state space tree to be produced: "))
create(initial_state, level_number)
