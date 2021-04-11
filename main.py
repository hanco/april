import itertools
from tqdm import tqdm

n = 20
k = n - 7
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
    trys = 10_000_000
    t = tqdm(range(1, trys))
    for q in t:
        t.set_description("# combinations: %s at n: %d" % (len(combinations), n))
        wheel = list(wheel_of_choice)
        pos = -1
        while len(wheel) > k:
            wheel = step(q, wheel)
        if tuple(wheel) in combinations:
            combinations.remove(tuple(wheel))
            if not combinations:
                return


    rest = [item for item in combinations if item not in winnings]

    return rest


find_combinations()

rest = all_spins()

print(rest)
print(len(rest))



