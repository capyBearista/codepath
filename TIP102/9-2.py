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
Problem 1: Balanced Baked Goods Display

Given the root of a binary tree display representing the baked goods on display at your store, return True if the tree is balanced and False otherwise.

A balanced display is a binary tree in which the difference in the height of the two subtrees of every node never exceeds one.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.
"""

#using DFS
#find height of both the right and left subtrees.
#if differene in the height>1  then we'll return false, otherwise go to the children

# time complexity: O(N^2)
# space complexity: O(log N)

def is_balanced(display):    
    # HELPER FUNCTION
    def get_height(node):
        if not node:
            return 0
         
        left_height = get_height(node.left)
        right_height = get_height(node.right)
        height = max(left_height, right_height) + 1

        return height

    if display is None:
        return True
    
    left_height_out = get_height(display.left)
    right_height_out = get_height(display.right)

    if abs(left_height_out - right_height_out) > 1:
        return False
    
    return is_balanced(display.left) and is_balanced(display.right)

"""
      🎂
     /  
   🥮   🍩
       /    
     🥖    🧁

"""
# Using build_tree() function included at top of page
baked_goods = ["🎂", "🥮", "🍩", None, None, "🥖", "🧁"] 
display1 = build_tree(baked_goods)

"""
          🥖
         /  
       🧁    🧁
       /       
      🍪       🍪
     /           
    🥐           🥐  

"""
baked_goods = ["🥖", "🧁", "🧁", "🍪", None, None, "🍪", "🥐", None, None, "🥐"]
display2 = build_tree(baked_goods)


print(is_balanced(display1)) # expected True
print(is_balanced(display2)) # expected False