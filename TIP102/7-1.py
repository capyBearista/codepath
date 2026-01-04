# PROBLEM 1
"""
Tony Stark, aka Iron Man, has designed many different suits over the years. Given a list of strings suits where each string is a suit in Stark's collection, count the total number of suits in the list.

    Implement the solution iteratively without the use of the len() function.
    Implement the solution recursively.
    Discuss: what are the similarities between the two solutions? What are the differences?
"""
def count_suits_recursive(suits):
    if not suits:
        return 0
    else:
        # suits.pop()
        return 1 + count_suits_recursive(suits[1:])


# PROBLEM 2
"""
Thanos is collecting Infinity Stones. Given an array of integers stones representing the power of each stone, return the total power using a recursive approach.

Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.
"""
def sum_stones(stones):
    if not stones:
        return 0
    else:
        return stones[0] + sum_stones(stones[1:])

print(sum_stones([5, 10, 15, 20, 25, 30]))
print(sum_stones([12, 8, 22, 16, 10]))


# PROBLEM 3
"""
Some of Iron Man's suits are duplicates. Given a list of strings suits where each string is a suit in Stark's collection, count the total number of distinct suits in the list.

    Implement the solution iteratively.
    Implement the solution recursively.
    Discuss: what are the similarities between the two solutions? What are the differences?
    Evaluate the time complexity of each solution. Are they the same? Define your variables and provide a rationale for why you believe your solution has the stated time complexity.

"""
def count_suits_iterative(suits):
    return  len(set(suits))

def count_suits_recursive(suits, uniq = None):
    if uniq is None:
        uniq = set()
    if not suits:
        return len(uniq)
    
    uniq.add(suits[0])
    return count_suits_recursive(suits[1:],uniq)

print(count_suits_iterative(["Mark I", "Mark I", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III",  "Mark I", "Mark III", "Mark II"]))


# PROBLEM 4
"""
Groot grows according to a pattern similar to the Fibonacci sequence. Given n, find the height of Groot after n months using a recursive method.

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.

Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.
"""
def fibonacci_growth(n):
    if n == 0:
        return 0
    elif n == 1: # if n <= 1: retir
        return 1
    else:
        return fibonacci_growth(n - 1) + fibonacci_growth(n - 2)

print(fibonacci_growth(5))
print(fibonacci_growth(8))


# PROBLEM 5
"""
The superhero team, The Fantastic Four, are training to increase their power levels. Their power level is represented as a power of 4. Write a recursive function that calculates the result of 4 raised to the nth power to determine their training level.

Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.
"""
def power_of_four(n):
    # return 4 ** n

    if n is None:
        return None
    if n == 0:
        return 1
    if n > 0:
        return 4 * power_of_four(n - 1)
    else:
        return 1/(4 * 1/power_of_four(n + 1))

print(power_of_four(2)) # 16
print(power_of_four(-2)) # 1/16