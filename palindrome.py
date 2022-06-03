"""
A palindrome is nothing but any number or a string which remains unaltered when reversed.
"""

# Input:- ['ab', 'abc', 'aba', 'xyz', '1991']
# Output:- 2

input_list = ['ab', 'abc', 'aba', 'xyz', '1991']
count = 0
for i in input_list:
    if i[::-1] == i:
        count += 1
print(count)


def palindrome(inputList):
    pal_count = 0
    for i in inputList:
        if i[::-1] == i:
            pal_count += 1
    return pal_count


palindrome_test = palindrome(input_list)
print(palindrome_test)
