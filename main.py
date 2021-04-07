import itertools

n = 12
k = 7
wheel_of_choice = list(range(1, n+1))
pos = -1

def find_combinations():
    global combinations
    combinations = []
    for i in itertools.combinations(range(1,n+1), k):
        combinations.append(i)

    return combinations

def step(q, wheel):
    global pos

    new_pos = (pos + q) % (len(wheel))
    del wheel[new_pos]
    pos = new_pos - 1

    return wheel

def all_spins():
    global pos
    winnings = []
    for q in range(1, 100000):
        wheel = list(wheel_of_choice)
        pos = -1
        while len(wheel) > k:
            wheel = step(q, wheel)
        if wheel not in winnings:
            winnings.append(tuple(wheel))

    rest = [item for item in combinations if item not in winnings]

    return rest

print(find_combinations())

rest = all_spins()

print(rest)
print(len(rest))



