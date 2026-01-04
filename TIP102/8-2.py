from collections import deque 

# Tree Node class
# class TreeNode:
#   def __init__(self, value, key=None, left=None, right=None):
#       self.key = key
#       self.val = value
#       self.left = left
#       self.right = right

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

"""
Problem 1: Monstera Madness

Given the root of a binary tree where each node represents the number of splits in a leaf of a Monstera plant, return the number of Monstera leaves 🍃 that have an odd number of splits.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.

Note: The term leaf in this problem refers to the plant leaf 🍃 of a Monstera plant, not the type of node leaf nodes which are nodes with no children.
"""
# Time Complexity: O(N) -> grows with each node, O(1) time for comparison

# class TreeNode():
#      def __init__(self, value, left=None, right=None):
#          self.val = value
#          self.left = left
#          self.right = right
         
# def count_odd_splits(root):
#     if not root:
#         return 0
    
#     count = 0
#     if root.val % 2 != 0:
#         count = 1
    
#     # left_count = count_odd_splits(root.left)


#     return (1 if root.val % 2 else 0) + count_odd_splits(root.left) + count_odd_splits(root.right)
#     # if root.val % 2 == 1 


# """
#       2
      
       
#    3     5
        
#  6   7     12
# """

# """
# Using build_tree() function included at top of page
# Example 1 Explanation: Three Monstera leaves (nodes) have an odd number of fenestrations (3, 5, and 7).
# 0
# """
# values = [2, 3, 5, 6, 7, None, 12]
# monstera = build_tree(values)

# print(count_odd_splits(monstera)) # expected 3
# print(count_odd_splits(None)) # expected 0


"""
Problem 2: Flower Finding

You are looking to buy a new flower plant for your garden. The nursery you visit stores its inventory in a binary search tree (BST) where each node represents a plant in the store. The plants are organized according to their names (vals) in alphabetical order in the BST.

Given the root of the binary search tree inventory and a target flower name, write a function find_flower() that returns True if the flower is present in the garden and False otherwise.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.
"""

# Time complexity: O(log N)

class TreeNode():
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right
         

"""
         Rose
        /    
      Lily   Tulip
     /         
  Daisy  Lilac  Violet
"""

def find_flower(inventory, name):
    # base case
    if not inventory:
        return False
    
    if(inventory.val == name):
        return True
    elif(inventory.val < name):
        return find_flower(inventory.right, name)
    else:
        return find_flower(inventory.left, name)
    

# using build_tree() function at top of page
values = ["Rose", "Lilac", "Tulip", "Daisy", "Lily", None, "Violet"]
garden = build_tree(values)

print(find_flower(garden, "Lilac")) # expected True
print(find_flower(garden, "Sunflower")) # expected False