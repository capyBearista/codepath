from collections import deque 

# Tree Node class
# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

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
Problem 1: Grafting Apples

You are grafting different varieties of apple onto the same root tree can produce many different varieties of apples! Given the following TreeNode class, create the binary tree depicted below. The text representing each node should should be used as the value.

The root, or topmost node in the tree TreeNode("Trunk") has been provided for you.

             Trunk
                   
      Mcintosh   Granny Smith
                       
    Fuji   Opal   Crab   Gala
"""
# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# root = TreeNode("Trunk")
# root.left = TreeNode("Mcintosh")
# root.right = TreeNode("Granny Smith")
# root.left.left = TreeNode("Fuji")
# root.left.right = TreeNode("Opal")
# root.right.left = TreeNode("Crab")
# root.right.right = TreeNode("Gala")

# print_tree(root)

# Example Output:

# ['Trunk', 'Mcintosh', 'Granny Smith', 'Fuji', 'Opal', 'Crab', 'Gala']


"""
Problem 2: Calculating Yield

You have a fruit tree represented as a binary tree with exactly three nodes: the root and its two children. Given the root of the tree, evaluate the amount of fruit your tree will yield this year. The tree has the following form:

    Leaf nodes have an integer value.
    The root has a string value of either "+", "-", "*", or "-".

The yield of a the tree is calculated by applying the mathematical operation to the two children.

Return the result of evaluating the root node.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.
"""
# TIME COMPLEXITY: O(1)

# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def calculate_yield(root):
#     if root.val == "+":
#         return root.left.val + root.right.val
#     if root.val == "-":
#         return root.left.val - root.right.val
#     if root.val == "*":
#         return root.left.val * root.right.val
#     if root.val == "/":
#         return root.left.val / root.right.val
    
# """
#     +
#  7     5
# """
# apple_tree = TreeNode("+", TreeNode(7), TreeNode(5)) # expected 12
# print(calculate_yield(apple_tree))

# apple_tree = TreeNode("*", TreeNode(7), TreeNode(5)) # expected 35
# print(calculate_yield(apple_tree))


"""
Problem 3: Ivy Cutting

You have a trailing ivy plant represented by a binary tree. You want to take a cutting to start a new plant using the rightmost vine in the plant. Given the root of the plant, return a list with the value of each node in the path from the root node to the rightmost leaf node. If there is no right child, return only the root node value (the rightmost path in this case is just the root node).

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.
"""

# TIME COMPLEXITY O(n)

# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def right_vine(root):
#     temp = root
#     val_list = []
    
#     while temp is not None:
#         val_list.append(temp.val)
#         temp = temp.right

#     return val_list

# """
#         Root
            
#     Node1    Node2
               
# Leaf1    Leaf2  Leaf3
# """
# ivy1 = TreeNode("Root", 
#                 TreeNode("Node1", TreeNode("Leaf1")),
#                 TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

# """
#       Root
#       /  
#     Node1
#     /
#   Leaf1  
# """
# ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

# print(right_vine(ivy1)) # expected ['Root', 'Node2', 'Leaf3']
# print(right_vine(ivy2)) # expected ['Root']


"""
Problem 4: Ivy Cutting II

If you implemented right_vine() iteratively in the previous problem, implement it recursively. If you implemented it recursively, implement it iteratively.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.
"""
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def right_vine(root):
    if root is None:
        return []

    return [root.val] + right_vine(root.right) 
    
    
"""
        Root
            
    Node1    Node2
               
Leaf1    Leaf2  Leaf3
"""
ivy1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

print(right_vine(ivy1)) # expected ['Root', 'Node2', 'Leaf3']
print(right_vine(ivy2)) # expected ['Root']


"""
    # Base case: node is None or we find the key
    if node is None or node.key == key:
        return node

    # If the key to be found is less than the current node's key, search in the left subtree
    if key < node.key:
        return search_bst(node.left, key)

    # If the key to be found is greater than the current node's key, search in the right subtree
    return search_bst(node.right, key)
"""