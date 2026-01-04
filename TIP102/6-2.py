"""
Problem 1: Wild Goose Chase

You're a detective and have been given an anonymous tip on your latest case, but something about it seems fishy - you suspect the clue might be a red herring meant to send you around in circles. Write a function is_circular() that accepts the head of a singly linked list clues and returns True if the tail of the linked list points at the head of the linked list. Otherwise, return False.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
"""
# understand, accept head, return true/false

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def is_circular(clues):
    current = clues

    first = clues # clue1
    if current is None:
        return False
    while current:
        if current.next == first:
            return True

        current = current.next

    return False

# Example Usage:
# Circular linked list of 3 clues where 3rd clue points to 1st clue

clue1 = Node("The stolen goods are at an abandoned warehouse")
clue2 = Node("The mayor is accepting bribes")
clue3 = Node("They dumped their disguise in the lake")
clue1.next = clue2
clue2.next = clue3
clue3.next = clue1

print(is_circular(clue1))

# Example Output:
# True

print()
"""
Problem 2: Breaking the Cycle

All the clues that lead us in circles are false evidence we need to purge! Given the head of a linked list evidence, clean up the evidence list by identifying any false clues. Write a function collect_false_evidence() that returns an array containing all values that are part of any cycle in evidence. Return the values in any order.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
"""

# understand: accept head of linked list, return nodes that are part of cycle

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def collect_false_evidence(evidence):
    if (evidence is None) or (evidence.next is None): 
        return []
    
    visited = []
    fake = []

    current = evidence
    temp = current

    while current:
        if current.value in fake:
            break
        if current in visited:
            fake.append(current.value) 
        else:
            visited.append(current)
        
        current = current.next
    
    return fake


# Example Usage:
# Linked list with 4 clues where 4th clue points to 2nd clue

clue1 = Node("Unmarked sedan seen near the crime scene")
clue2 = Node("The stolen goods are at an abandoned warehouse")
clue3 = Node("The mayor is accepting bribes")
clue4 = Node("They dumped their disguise in the lake")
clue1.next = clue2
# cycle below
clue2.next = clue3
clue3.next = clue4
clue4.next = clue2

clue5 = Node("A masked figure was seen fleeing the scene")
clue6 = Node("Footprints lead to the nearby woods")
clue7 = Node("A broken window was found at the back")
clue5.next = clue6
clue6.next = clue7

print(collect_false_evidence(clue1))
print(collect_false_evidence(clue5))

# Example Output:

# ['The stolen goods are at an abandoned warehouse', 'The mayor is accepting bribes', 'They dumped their disguise in the lake']

# []