# Given a string s consisting of English letters (lowercase and/or uppercase) and digits, return all possible strings that can be formed by changing the case of the letters in s. You may not alter the order of characters in the string, and digits should remain unchanged.
Input: s = "a1b2"
Output: ["a1b2", "A1b2", "a1B2", "A1B2"]
Input: s = "3z4"
Output: ["3z4", "3Z4"]
Input: s = "12345"
Output: ["12345"]

# understand: loop thru strings, looking for char; if character, if upper/lower, switch case

lst_string = [""]

"""
temp_string = ""
for char in s:
    if char.alpha():
        if uppercase
            tolower
            str add
        else
            toupper
            str add
    else:
        str add

add temp to list string
return lst_string
"""

results = [""]
for char in s:
    temp_results = ""

    if char.isalpha()
        for string in results:
            temp_results.append(string + char.lower())
            temp_results.append(string + char.upper())
