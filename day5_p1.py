# basically: how many ms should you spend holding button? 
# let t = time allowed for current race 
# for i in 1...t, distance travelled = (t - k) * k, where k = ms spent holding button = speed 

"""
Determine the number of ways you could beat the record in each race. 
What do you get if you multiply these numbers together?

Time:      7  15   30
Distance:  9  40  200

lower - you need to go at least 9mm in at most 7ms; 9/7 = ceil(1.28) = 2 mm/ms is lowest speed required 
 - ceil(distance/time) = min_k
   - k should only be higher than this, since time is cut short by k 
higher - you run out of time to travel, despite high speed 
  - max possible k = time allowed - 1
"""

import math


example_input = """Time:      7  15   30
Distance:  9  40  200"""

input = """Time:        53     71     78     80
Distance:   275   1181   1215   1524"""

example_arr = example_input.split("\n")
arr = input.split("\n")

def part_1(arr):
    race_time_limits = arr[0].split(":")[1].strip().split()
    race_record_dist = arr[1].split(":")[1].strip().split()

    if len(race_time_limits) != len(race_record_dist):
        raise Exception("Input not formatted correctly")
    
    n = len(race_time_limits)
    res = 1

    # for each race 
    for i in range(n):
        t, d = int(race_time_limits[i]), int(race_record_dist[i])
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
        num_ways = higher - lower + 1
        # print(f'race {i} lower: {lower} higher: {higher} num_ways: {num_ways}')

        # multiply this for each race 
        res *= num_ways

    return res 

# expected: 288 (4 * 8 * 9)
print(part_1(example_arr))
print(part_1(arr))
