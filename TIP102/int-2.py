# PASTED
class TreeNode():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

"""
Problem #2 (Same Tree)

Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

edge cases:
if both empty, true
if one empty, false

plan:
traverse each node and compare value at that node

base case:
root.left and root.right None
"""

def sameTree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    
    if p.value != q.value:
        return False
    
    return sameTree(p.left, q.left) and sameTree(p.right, q.right)

p = TreeNode(5, 6, 7)
q = TreeNode(5, 6, 7)

print(sameTree(p, q))

x = TreeNode(5, 6, 7)
y = TreeNode(5, 6)

print(sameTree(x, y))
