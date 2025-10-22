# Problem 1: Reverse Sentence

# Write a function reverse_sentence() that takes in a string sentence and returns the sentence with the order of the words reversed. The sentence will contain only alphabetic characters and spaces to separate the words. If there is only one word in the sentence, the function should return the original string.

# Example Usage:

# sentence = "tubby little cubby all stuffed with fluff"
# reverse_sentence(sentence)

# sentence = "Pooh"
# reverse_sentence(sentence)

# Example Output:

# "fluff with stuffed all cubby little tubby"
# "Pooh"

def reverse_sentence(sentence):
    # list_words = sentence.split(" ")
    # if len(list_words) == 1:
    #     return sentence
    
    # print(list_words)
    
    # output_list = []
    
    # for _ in range(len(list_words)):
    #     output_list.append(list_words.pop())

    # return " ".join(output_list)

    return " ".join(sentence.split()[::-1])

sentence = "tubby little cubby all stuffed with fluff"
print(reverse_sentence(sentence))

# Problem 2: Goldilocks Number

# In the extended universe of fictional bears, Goldilocks finds an enticing list of numbers in the Three Bears' house. She doesn't want to take a number that's too high or too low - she wants a number that's juuust right. Write a function goldilocks_approved() that takes in the list of distinct positive integers nums and returns any number from the list that is neither the minimum nor the maximum value in the array, or -1 if there is no such number.

# Return the selected integer.

# Example Usage

# nums = [3, 2, 1, 4]
# goldilocks_approved(nums)

# nums = [1, 2]
# goldilocks_approved(nums)

# nums = [2, 1, 3]
# goldilocks_approved(nums)

# Example Output:

# 2
# -1
# 2

def goldilocks_approved(nums):
    if len(nums) <=2:
        return -1
    nums.sort()

    return nums[1]
    
    # maximum = max(nums)
    # minimum = min(nums)

    # for num in nums:
    #     if num != maximum and num != minimum:
    #         return num
        
nums = [3, 2, 1, 4]
print(goldilocks_approved(nums))

nums = [1, 2]
print(goldilocks_approved(nums))

nums = [2, 1, 3]
print(goldilocks_approved(nums))


# Problem 3: Delete Minimum

# Pooh is eating all of his hunny jars in order of smallest to largest. Given a list of integers hunny_jar_sizes, write a function delete_minimum_elements() that continuously removes the minimum element until the list is empty. Return a new list of the elements of hunny_jar_sizes in the order in which they were removed.

# Example Usage

# hunny_jar_sizes = [5, 3, 2, 4, 1]
# delete_minimum_elements(hunny_jar_sizes)

# hunny_jar_sizes = [5, 2, 1, 8, 2]
# delete_minimum_elements(hunny_jar_sizes)

# Example Output:

# [1, 2, 3, 4, 5]
# [1, 2, 2, 5, 8]

def delete_minimum_elements(hunny_jar_sizes):
    output_list = []
    while hunny_jar_sizes:
        minimum = min(hunny_jar_sizes)
        hunny_jar_sizes.remove(minimum)
        output_list.append(minimum)
    return output_list

hunny_jar_sizes = [5, 3, 2, 4, 1]
print(delete_minimum_elements(hunny_jar_sizes))

hunny_jar_sizes = [5, 2, 1, 8, 2]
print(delete_minimum_elements(hunny_jar_sizes))

# Problem 4: Sum of Digits

# Write a function sum_of_digits() that accepts an integer num and returns the sum of num's digits.

# Example Usage

# num = 423
# sum_of_digits(num)

# num = 4
# sum_of_digits(num)

# Example Output:

# 9 # Explanation: 4 + 2 + 3 = 9
# 4 

def sum_of_digits(num):
    number = str(num)

    sum = 0
    for char in number:
        sum += int(char)
    
    return sum

print(sum_of_digits(423))  # expected 9

# Problem 5: Bouncy, Flouncy, Trouncy, Pouncy

# Tigger has developed a new programming language Tiger with only four operations and one variable tigger.

#     bouncy and flouncy both increment the value of the variable tigger by 1.
#     trouncy and pouncy both decrement the value of the variable tigger by 1.

# Initially, the value of tigger is 1 because he's the only tigger around! Given a list of strings operations containing a list of operations, return the final value of tigger after performing all the operations.

# def final_value_after_operations(operations):
# 	pass

# Example Usage

# operations = ["trouncy", "flouncy", "flouncy"]
# final_value_after_operations(operations)

# operations = ["bouncy", "bouncy", "flouncy"]
# final_value_after_operations(operations)

# Example Output:

# 2
# 4

def final_value_after_operations(operations):
    tigger = 1

    for op in operations:
        if op == "trouncy" or op == "pouncy":
            tigger -= 1
        if op == "bouncy" or op == "flouncy":
            tigger += 1

    return tigger

operations = ["trouncy", "flouncy", "flouncy"]
print(final_value_after_operations(operations))

operations = ["bouncy", "bouncy", "flouncy"]
print(final_value_after_operations(operations))

# Problem 6: Acronym

# Given an array of strings words and a string s, implement a function is_acronym() that returns True if s is an acronym of words and returns False otherwise.

# The string s is considered an acronym of words if it can be formed by concatenating the first character of each string in words in order. For example, "pb" can be formed from ["pooh"", "bear"], but it can't be formed from ["bear", "pooh"].

# Example Usage

# words = ["christopher", "robin", "milne"]
# s = "crm"
# is_acronym(words, s)

# Example Output:

# True

def is_acronym(words, s):
    if len(s) != len(words):
        return False

    output_s = ""
    for word in words:
        output_s += word[0]

    return output_s == s
    # ALSO WORKS: return "".join(w[0] for w in words if w) == s

words = ["christopher", "robin", "milne"]
s = "crm"
print(is_acronym(words, s))

words = ["dog", "robin", "milne"]
s = "crm"
print(is_acronym(words, s))

# Problem 7: Good Things Come in Threes

# Write a function make_divisible_by_3() that accepts an integer array nums. In one operation, you can add or subtract 1 from any element of nums. Return the minimum number of operations to make all elements of nums divisible by 3.

# def make_divisible_by_3(nums):
#     pass

# Example Usage

# nums = [1, 2, 3, 4]
# make_divisible_by_3(nums)

# nums = [3, 6, 9]
# make_divisible_by_3(nums)

# Example Output:

# 3
# 0

def make_divisible_by_3(nums):
    count = 0
    for num in nums:
        if num % 3 != 0:
            count += 1
    return count

nums = [1, 2, 3, 4]
print(make_divisible_by_3(nums))

nums = [3, 6, 9]
print(make_divisible_by_3(nums))

# Problem 8: Exclusive Elements

# Given two lists lst1 and lst2, write a function exclusive_elemts() that returns a new list that contains the elements which are in lst1 but not in lst2 and the elements that are in lst2 but not in lst1.

# Example Usage

# lst1 = ["pooh", "roo", "piglet"]
# lst2 = ["piglet", "eeyore", "owl"]
# exclusive_elemts(lst1, lst2)

# lst1 = ["pooh", "roo"]
# lst2 = ["piglet", "eeyore", "owl", "kanga"]
# exclusive_elemts(lst1, lst2)

# lst1 = ["pooh", "roo", "piglet"]
# lst2 = ["pooh", "roo", "piglet"]
# exclusive_elemts(lst1, lst2)

# Example Output:

# ["pooh", "roo", "eeyore", "owl"]
# ["pooh", "roo", "piglet", "eeyore", "owl", "kanga"]
# []

def exclusive_elemts(lst1, lst2):
	pass

lst1 = ["pooh", "roo", "piglet"]
lst2 = ["piglet", "eeyore", "owl"]
print(exclusive_elemts(lst1, lst2))

lst1 = ["pooh", "roo"]
lst2 = ["piglet", "eeyore", "owl", "kanga"]
print(exclusive_elemts(lst1, lst2))

lst1 = ["pooh", "roo", "piglet"]
lst2 = ["pooh", "roo", "piglet"]
print(exclusive_elemts(lst1, lst2))