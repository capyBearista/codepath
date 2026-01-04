from collections import deque 

# Tree Node class
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root


"""
Problem 1: Merging Cookie Orders

You run a local bakery and are given the roots of two binary trees order1 and order2 where each node in the binary tree represents the number of a certain cookie type the customer has ordered. To maximize efficiency, you want to bake enough of each type of cookie for both orders together.

Given order1 and order2, merge the order together into one tree and return the root of the merged tree. To merge the orders, imagine that when place one tree on top of the other, some nodes of the two trees are overlapped while others are not. If two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the not None node will be used as the node of the new tree.

Start the merging process from the root of both orders.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.
"""

# time complexity: O(n + m) or O(n), should say "n + m" in an interview setting

def merge_orders(order1, order2):
    if not order1 and not order2:
        return None
    
    if not order1:
        return order2
    
    if not order2:
        return order1
    
    new_tree = TreeNode(order1.val + order2.val)

    new_tree.left = merge_orders(order1.left, order2.left)
    new_tree.right = merge_orders(order1.right, order2.right)

    return new_tree


# Example 'order1' and 'order2' trees and their merged result
"""
     1             2         
    /           /          
   3    2       1     3   
 /                        
5                 4      7   
"""

# Using build_tree() function included at top of page
cookies1 = [1, 3, 2, 5]
cookies2 = [2, 1, 3, None, 4, None, 7]
order1 = build_tree(cookies1)
order2 = build_tree(cookies2)

# Using print_tree() function included at top of page
print_tree(merge_orders(order1, order2))

"""
[3, 4, 5, 5, 4, None, 7]
Explanation:
Merged Tree:
     3
    /  
  4     5  
 /       
5   4      7
"""


"""
Problem 2: Croquembouche

You are designing a delicious croquembouche (a French dessert composed of a cone-shaped tower of cream puffs 😋), for a couple's wedding. They want the cream puffs to have a variety of flavors. You've finished your design and want to send it to the couple for review.

Given a root of a binary tree design where each node in the tree represents a cream puff in the croquembouche, that prints a list of the flavors (vals) of each cream puff in level order (i.e., from left to right, level by level).

Note: The build_tree() and print_tree() functions both use variations of a level order traversal. To get the most out of this problem, we recommend that you reference these functions as little as possible while implementing your solution.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.
"""

# time complexity: O(n), traversing each node
# space complexity: O(log n), due to recursion of balanced tree

from collections import deque
class Puff():
     def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

def print_design(design):
    if design is None:
        return []
    
    queue_design = deque([design])

    result = []
    
    while queue_design:
        node = queue_design.popleft()
        result.append(node.val)
        if node.left:
            queue_design.append(node.left)
        if node.right:
            queue_design.append(node.right)
    
    print(result)


"""
            Vanilla
           /       
      Chocolate      Strawberry
      /     
  Vanilla   Matcha  
"""
croquembouche = Puff("Vanilla", 
                    Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), 
                    Puff("Strawberry"))
print_design(croquembouche) # expected ['Vanilla', 'Chocolate', 'Strawberry', 'Vanilla', 'Matcha']


"""
Problem 3: Maximum Tiers in Cake

You have entered your bakery into a cake baking competition and for your entry have decided build a complicated pyramid shape cake, where different sections have different numbers of tiers. Given the root of a binary tree cake where each node represents a different section of your cake, return the maximum number of tiers in your cake.

The maximum number of tiers is the number of nodes along the longest path from the root node down to the farthest leaf node.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.
"""

# time complexity: O(n)
# space complexity: O(log n), due to recursion of balanced tree
# this uses DFS

# class TreeNode():
#      def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def max_tiers(cake):
#     if cake is None:
#         return 0
    
#     left = max_tiers(cake.left)
#     right = max_tiers(cake.right)

#     return 1 + max(left, right)
    
# """
#         Chocolate
#         /        
#     Vanilla    Strawberry
#                 /     
#          Chocolate    Coffee
# """
# # Using build_tree() function included at top of page
# cake_sections = ["Chocolate", "Vanilla", "Strawberry", None, None, "Chocolate", "Coffee"]
# cake = build_tree(cake_sections)

# print(max_tiers(cake)) # expected 3


"""
Problem 4: Maximum Tiers in Cake II

If you solved max_tiers() in the previous problem using a depth first search approach, reimplement your solution using a breadth first search approach. If you implemented it using a breadth first search approach, use a depth first search approach.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.
"""
from collections import deque

class TreeNode():
     def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def max_tiers(cake):
    if not cake:
        return 0
    
    queue = deque([cake])

    levels = 0
    while queue:
        len_queue = len(queue)

        for i in range(len_queue):
            node = queue.popleft()
        
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        levels+=1
    
    return levels

"""
        Chocolate
        /        
    Vanilla    Strawberry
                /     
         Chocolate    Coffee
"""
# Using build_tree() function included at top of page
cake_sections = ["Chocolate", "Vanilla", "Strawberry", None, None, "Chocolate", "Coffee"]
cake = build_tree(cake_sections)

print(max_tiers(cake)) # expected 3