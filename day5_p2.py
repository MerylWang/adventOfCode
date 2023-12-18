# example_input = """Time:      7  15   30
# Distance:  9  40  200"""

# time_str, distance_str = example_input.split("\n")
# time_str = ''.join(time_str.split(":")[1].strip().split())

import math

example_time, example_dist = 71530 , 940200
time, dist = 53717880, 275118112151524

def part_2(t, d):
    """
    t: max time allowed 
    d: min distance need to cover
    """
    lower = math.ceil(d/t)
    higher = t - 1

    # find lower range of k 
    while lower < t:
        if (t - lower) * lower > d:
            break
        else: 
            lower += 1

    # find higher range of k
    while higher > 0:
        if (t - higher) * higher > d:
            break
        else: 
            higher -= 1

    # number of possible ways = higher - lower + 1
    return higher - lower + 1
    # print(f'race {i} lower: {lower} higher: {higher} num_ways: {num_ways}')

print(part_2(example_time, example_dist))
print(part_2(time, dist))


    

    