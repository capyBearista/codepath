# Problem 1: Final Costs After a Supply Discount

# You are managing the budget for a global expedition, where the cost of supplies is represented by an integer array costs, where costs[i] is the cost of the ith supply item.

# There is a special discount available during the expedition. If you purchase the ith item, 
# you will receive a discount equivalent to costs[j], where j is the minimum index such that j > i and costs[j] <= costs[i]. If no such j exists, you will not receive any discount.

# Return an integer array final_costs where final_costs[i] is the final cost you will pay for the ith supply item, considering the special discount.


"""
def final_supply_costs(costs):
    final_costs = costs
    
    # quadratic time complexity O(n^2)
    for i in range(0, len(costs) + 1):    
        for j in range(i+1, len(costs)):
            if costs[j] <= costs[i]:
                final_costs[i] = (costs[i] - costs[j])
                break
                
    return final_costs
"""

def final_supply_costs(costs):
    n = len(costs)
    final_costs = costs[:]
    stack = []

    for i in range(n):
        # time complexity O(n)
        while stack and costs[stack[-1]] >= costs[i]:
            j = stack.pop()
            final_costs[j] -= costs[i]
        stack.append(i)

    return final_costs

# Example Usage:

print(final_supply_costs([8, 4, 6, 2, 3])) 
print(final_supply_costs([1, 2, 3, 4, 5])) 
print(final_supply_costs([10, 1, 1, 6])) 

# Example Output:

# [4, 2, 4, 2, 3]
# [1, 2, 3, 4, 5]
# [9, 0, 1, 6]

"""OUTPUT"""
# [4, 2, 4, 2, 3]
# [1, 2, 3, 4, 5]
# [9, 0, 1, 6]

print("\nProblem 2")

# Problem 2: Find First Symmetrical Landmark Name

# During your global expedition, you encounter a series of landmarks, each represented by a string in the array landmarks. Your task is to find and return the first symmetrical landmark name. If there is no such name, return an empty string "".

# A landmark name is considered symmetrical if it reads the same forward and backward.
def find_palindrome(word):
    left = 0
    right = len(word)- 1 
    
    while left < right:
        if word[left] != word[right]:
            return False
        else:
            left += 1
            right -= 1
    
    return True

def first_symmetrical_landmark(landmarks):
    for landmark in landmarks:
        if find_palindrome(landmark) == True:
            return landmark
    else:
        return ""


# Example Usage:
print(first_symmetrical_landmark(["canyon","forest","rotor","mountain"])) 
print(first_symmetrical_landmark(["plateau","valley","cliff"])) 

# Example Output:
# rotor



# Problem 3: Terrain Elevation Match

# During your global expedition, you are mapping out the terrain elevations, where the elevation of each point is represented by an integer. You are given a string terrain of length n, where:

#     terrain[i] == 'I' indicates that the elevation at the ith point is lower than the elevation at the i+1th point (elevation[i] < elevation[i + 1]).
#     terrain[i] == 'D' indicates that the elevation at the ith point is higher than the elevation at the i+1th point (elevation[i] > elevation[i + 1]).

# Your task is to reconstruct the elevation sequence and return it as a list of integers. If there are multiple valid sequences, return any of them.

# Hint: Try using two variables: one to track the smallest available number and one for the largest. As you process each character in the string, assign the smallest number when the next elevation should increase ('I'), and assign the largest number when the next elevation should decrease ('D').

def terrain_elevation_match(terrain):
    lowest = 0
    highest = len(terrain)

    for letter in terrain:
        if letter == "I":
            lowest += 1
        elif letter == "D":
            highest -= 1

    else:
        return "Invalid"

# Example Usage:
print(terrain_elevation_match("IDID")) 
print(terrain_elevation_match("III")) 
print(terrain_elevation_match("DDI")) 

# Example Output:
# [0, 4, 1, 3, 2]
# [0, 1, 2, 3]
# [3, 2, 0, 1]
