from pprint import pprint 

example_input = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

example_arr = [[char for char in line] for line in example_input.split("\n")]
pprint(example_arr)

"""
gear: symbol that is adjacent to exactly 2 numbers 
gear ratio: product of those 2 numbers
return: sum of gear ratios 

for every elt in arr, if elt is symbol 
    find number of adjacent numbers (for top and bottom, look at 3 above & below and see if 1 or 2 numbers)
    if adjancency = 2, multiply those 2 numbers and add to sum

...*......
.53.67....

...*......
..345.....


.*...
56...
"""

def check_top_or_bottom(arr, i, j, top_or_bottom="top"):
    m,n = len(arr), len(arr[0])

    s = ""
    for temp_j in [j-1, j, j+1]:
        if temp_j < 0 or temp_j >= n:
            continue 
        if top_or_bottom == "top":
            s += arr[i-1][temp_j]
        elif top_or_bottom == "bottom":
            s += arr[i+1][temp_j]

    if len(s) < 3 and [char.isdigit() for char in s].count(True) > 0:
        num_adj += 1
    else: # len(top_s) === 3
        # x.., xx., xxx, x.x, .x., .xx, ..x, ... 
        s = s.strip('.')
        if s.isdigit():
            return 1
        elif len(s) < 1:
            return 0 
        elif len(s) == 3:
            return 2
    return 
    

  
def find_sum(arr):
    result = 0 
    m,n = len(arr), len(arr[0])

    for i in range(m):
        for j in range(n):
            val = arr[i][j]
            if val.isdigit() or val == '.':
                continue 
            # is symbol 
            # check if 2 numbers adjacent
            num_adj = 0 

            # check top 3 values 
            if i != 0: # skip first row             
                num_adj += check_top_or_bottom(arr, i, j, top_or_bottom="top")

            # check left and right adjacent values 
            if j-1 >= 0 and arr[i][j-1].isdigit():
                num_adj += 1
            if j+1 < n and arr[i][j+1].isdigit():
                num_adj += 1

            # check bottom 3 values
            if j != n-1: # skip last row 
                num_adj += check_top_or_bottom(arr, i, j, top_or_bottom="bottom")
            
            if num_adj == 2:
                # gear_ratio = 
                # todo: gahh need to find the actual numbers - might come back to this later

                
            
                





    return result 