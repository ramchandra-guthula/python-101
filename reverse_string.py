"""
Reverse a given list
Input:- 'peter piper picked a peck of pickled peppers.'
Output:- 'peppers. pickled of peck a picked piper peter'
"""


str_input = 'peter piper picked a peck of pickled peppers.'
input_list = str_input.split(' ')
print(input_list[::-1])

"""
Reverse every string a list 
Input:- 'peter piper picked a peck of pickled peppers.'
Output:- 
"""

str_input = 'peter piper picked a peck of pickled peppers.'
input_list = str_input.split(' ')
rev_text_list = []
rev_text = ""
for i in input_list:
    rev_text_list.append(i[::-1])
    join_string = rev_text.join(rev_text_list)
    join_string += " "

print(join_string)