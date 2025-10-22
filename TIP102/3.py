# You are managing a social media platform and need to ensure that posts are properly formatted. 
# Each post must have balanced and correctly nested tags, such as () for mentions, [] for hashtags, 
# and {} for links. You are given a string representing a post's 
# content, and your task is to determine if the tags in the post are correctly formatted.

# A post is considered valid if:

#     Every opening tag has a corresponding closing tag of the same type.
#     Tags are closed in the correct order.  as soon as we see a bracket we immediately see the closing  version of it


# U: Check for tags and closing brackets/parenthesis 
# we have have an empty list at the end to check for balancenesss
# we can check for this at the end of function 

# P:  using a stack a store the seen elements 
#   looping throught the string pushing elements and checking for closing parenthesis
#  return false if stack in non-empty or if stack is empty and next is closing parenthesis
 

def is_valid_post_format(posts):
    stack = []
    lookup = {
        ')':'(',
        '}':'{',
        ']':'['
    }

    for c in posts:
        if c in lookup.values():
                stack.append(c)
        elif stack and lookup[c] == stack[-1]:
                stack.pop()
        else:
            return False
        
    return stack == [] # check if the stack is empty 

# def is_valid_post_format(posts):
#     stack = []

#     for c in posts:
#         if c == "(":
#             stack.append(c)
#         elif c == '[':
#             stack.append(c)
#         elif c == '{':
#             stack.append(c)

#         if len(stack) != 0:
#             if stack[-1] == '(' and c == ')':
#                 stack.pop()
#             if stack[-1] == '[' and c == ']':
#                 stack.pop()
#             if stack[-1] == '{' and c == '}':
#                 stack.pop()

#     return len(stack) == 0


print("1", is_valid_post_format("()"))    # expected True
print("2", is_valid_post_format("()[]{}"))    # expected True
print("3", is_valid_post_format("(]"))    # expected False
print("4", is_valid_post_format("(([]))"))    # expected True


# PROBLEM 2     
# On your platform, comments on posts are displayed in the order they are received.
# However, for a special feature, you need to reverse the order of comments before 
# displaying them. Given a queue of comments represented as a list of strings,
# reverse the order using a stack.

# U: Reverse the order of elements string in the list
# empty list, for condition 

# P: traverse the list to fill a  stack, and the we print it
# use pop to print the reverse order of the element in the 


def reverse_comments_queue(comments):
    stack = []
    for elem in comments:
        stack.append(elem)
    
    reverse_stack = []
    while stack:
        reverse_stack.append(stack.pop())
    
    return reverse_stack 

# expected ['Thanks for sharing.', 'Love it!', 'Great post!']
print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing"]))
# expected ['Well written.', 'Interesting read.', 'First!']
print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))


# PROBLEM 3
# As part of a new feature on your social media platform, you want to highlight post titles 
# that are symmetrical, meaning they read the same forwards and backwards when ignoring spaces,
# punctuation, and case. Given a post title as a string, use a new algorithmic technique the 
# two-pointer method to determine if the title is symmetrical.

# U: problem doesn't care about spaces, 
# we need the string to have the same characters in reverse order as in parameter
# doesn't care about casing

# I: Need to use two-pointer method
# Check if the element of the left is equal to the element on the right 
# lower all the casing of the characters in new variable 
# can be either even length or odd 

def is_symmetrical_title(title):
    lower_title = title.lower() # this step make the string all lower case
    left = 0 # looks at the left index of the string
    right = len(lower_title) - 1 # looks at the right element of the string

    
    while left < right:
        if lower_title[left] == ' ':
             left += 1
        elif lower_title[right] == ' ':
             right -= 1
       
        if lower_title[left] != lower_title[right]:
            return False
        left += 1
        right -= 1
    
    return True
         


print(is_symmetrical_title("A Santa at NASA"))    # expected True
print(is_symmetrical_title("Social Media"))    # expected False
print(is_symmetrical_title("racecar"))
print(is_symmetrical_title("raCE cAR"))

# Problem 4: Engagement Boost

# You track your daily engagement rates as a list of integers, sorted in non-decreasing order. 
# To analyze the impact of certain strategies, you decide to square each engagement rate and then 
# sort the results in non-decreasing order.

# Given an integer array engagements sorted in non-decreasing order, return an array of the squares of 
# each number sorted in non-decreasing order.

# Your Task:
#     Read through the existing solution and add comments so that everyone in your pod understands how it works.
#     Modify the solution below to use the two-pointer technique.

def engagement_boost(engagements):
    squared_engagements = [] # declare a list(stack)
    
    for i in range(len(engagements)): #looping through the elements in order 
        squared_engagement = engagements[i] * engagements[i] # local variable to store the squared value in the element at index i
        squared_engagements.append((squared_engagement, i)) # append the squared amount to stack
    
    squared_engagements.sort(reverse=True) # sort the element in the stack in the reverse
    
    result = [0] * len(engagements) # initializing a list with a default value repeated a certain amount of times, this is 
    # 0 default with length of engagement amount of times
    position = len(engagements) - 1 # pointer to the last element
    
    for square, original_index in squared_engagements:
        result[position] = square
        position -= 1
    
    return result