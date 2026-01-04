"""
Problem 1: Can Rebook Flight

Oh no! Your flight has been cancelled and you need to rebook. Given an adjacency matrix of today's
 flights flights where each flight is labeled 0 to n-1 and flights[i][j] = 1 indicates that there 
 is an available flight from location i to location j, return True if there exists a path from your
   current location source to your final destination dest. Otherwise return False.

Evaluate the time complexity of your function. Define your variables and provide a rationale for
 why you believe your solution has the stated time complexity.
"""
from collections import deque

# def can_rebook(flights, source, dest):
#     if source == dest:
#         return True

#     queue = deque([source])
#     n = len(flights)
#     visited = [False] * n
#     visited[source] = True
    
#     while queue:
#         current = queue.popleft()

#         if current == dest:
#             return True
    
#         for flight in range(n):
#             if flights[current][flight] == 1 and not visited[flight]:
#                 if flight == dest:
#                     return True
            
#                 visited[flight] = True
#                 queue.append(flight)
    
#     return False


flights1 = [
    [0, 1, 0], # Destination 0
    [0, 0, 1], # Destination 1
    [0, 0, 0]  # Destination 2
]

flights2 = [
    [0, 1, 0, 1, 0], # Destination 0
    [0, 0, 0, 1, 0], # Destination 1
    [0, 0, 0, 0, 1], # Destination 2
    [0, 0, 0, 0, 0], # Destination 3
    [0, 0, 0, 0, 0]  # Destination 4
]

# print(can_rebook(flights1, 0, 2)) # True
# print(can_rebook(flights2, 0, 2)) # False


"""
Problem 2: Can Rebook Flight II

If you solved the above problem can_rebook() using Breadth First Search, try solving it using Depth First Search. If you solved it using Depth First Search, solve it using Breadth First Search.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.
"""

def can_rebook(flights, source, dest):
    n = len(flights)
    visited = [False] * n
    
    # HELPER FUNCTION
    def flight_traverse(current):
        if current == dest:
            return True
        visited[current] = True

        
        
        
    
flights1 = [
    [0, 1, 0], # Flight 0
    [0, 0, 1], # Flight 1
    [0, 0, 0]  # Flight 2
]

flights2 = [
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

print(can_rebook(flights1, 0, 2)) # expected True
print(can_rebook(flights2, 0, 2)) # expected False