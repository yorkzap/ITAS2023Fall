import random
import math

def run_random_experiment(iterations):
    count0 = 0
    count1 = 0

    for _ in range(iterations):
        getRandom = random.randint(0, 1)
        
        if getRandom == 0:
            count0 += 1
        else:
            count1 += 1

    print(f"{count0} times 0")
    print(f"{count1} times 1")

run_random_experiment(1000)
