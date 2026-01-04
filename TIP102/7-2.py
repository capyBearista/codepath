# Problem 1
"""
It's vacation time! Given an integer vacation_length and a list of integers cruise_lengths sorted in ascending order, use binary search to return True if there is a cruise length that matches vacation_length and False otherwise.
"""
def find_cruise_length(cruise_lengths, vacation_length):
    low = 0
    high = len(cruise_lengths) - 1

    while low <= high:
        mid = (low + high) // 2
        
        if cruise_lengths[mid] == vacation_length:
            return True
        elif cruise_lengths[mid] > vacation_length:
            high = mid - 1
        else:
            low = mid + 1
        
    return False

print("\nPROBLEM 1")
print(find_cruise_length([9, 10, 11, 12, 13, 14, 15], 13)) # expected True
print(find_cruise_length([8, 9, 12, 13, 13, 14, 15], 11)) # expected False


# Problem 2
"""
As part of your cruise planning, you have a list of available cabins sorted in ascending order by their deck level. Given the list of available cabins represented by deck level, cabins, and an integer preferred_deck, write a recursive function find_cabin_index() that returns the index of preferred_deck. If a cabin with your preferred_deck does not exist in cabins, return the index where it would be if it were added to the list to maintain the sorted order.

Your algorithm must have O(log n) time complexity.
"""

# time complexity: O(log n)
# space complexity: O(log n)

def find_cabin_index(cabins, preferred_deck):
    def helper(low,high):
   
        if low>high:
            return low
    
        mid = (low + high) // 2

        if cabins[mid] == preferred_deck:
            return mid
        elif cabins[mid] > preferred_deck:
            return helper(low,mid-1)
        else:
            return helper(mid + 1, high)

    return helper(0, len(cabins) - 1)

print("\nPROBLEM 2")

print(find_cabin_index([1, 3, 5, 6], 5)) # expected 2
print(find_cabin_index([1, 3, 5, 6], 2)) # expected 1
print(find_cabin_index([1, 3, 5, 6], 7)) # expected 4


# Problem 3
"""As a cruise ship worker, you're in charge of tracking how many passengers have checked in to their rooms thus far. You are given a list of rooms where passengers are either checked in (represented by a 1) or not checked in (represented by a 0). The list is sorted, so all the 0s appear before any 1s.

Write a function count_checked_in_passengers() that efficiently counts and returns the total number of checked-in passengers (1s) in the list in O(log n) time.
"""
# if mid is 0, we can ignore left subsection
    # rooms[mid + 1, high]
# if mid is 1, we have to check left
# if last is 0, then the whole list is 0
# if first is 1, then the whole list is 1

# time complexity: O(log n)
# space complexity: O(1)

def count_checked_in_passengers(rooms):
    low = 0
    high = len(rooms) - 1

    if rooms[low] == 1:
        return len(rooms)
    if rooms[high] == 0:
        return 0

    while low <= high:
        mid = (low + high) // 2

        if rooms[mid] == 0:
            low = mid + 1
        else: # rooms[mid] == 1
            high = mid - 1

    return (len(rooms) - low)


rooms1 = [0, 0, 0, 1, 1, 1, 1]
rooms2 = [0, 0, 0, 0, 0, 1]
rooms3 = [0, 0, 0, 0, 0, 0]

print("PROBLEM 3")
print(count_checked_in_passengers(rooms1)) # expected 4
print(count_checked_in_passengers(rooms2)) # expected 1
print(count_checked_in_passengers(rooms3)) # expected 0


# Problem 4
"""
As the activities director on a cruise ship, you’re organizing excursions for the passengers. You have a sorted list of non-negative integers excursion_counts, where each number represents the number of passengers who have signed up for various excursions at your next cruise destination. The list is considered profitable if there exists a number x such that there are exactly x excursions that have at least x passengers signed up.

Write a function that detrmines whether excursion_counts is profitable. If it is profitable, return the value of x. If it is not profitable, return -1. It can be proven that if excursion_counts is profitable, the value for x is unique.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
"""

def is_profitable(excursion_counts):
    pass


print(is_profitable([3, 5]))
print(is_profitable([0, 0]))
