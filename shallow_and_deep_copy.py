"""
In Python, we use = operator to create a copy of an object. You may think that this creates a new object; it doesn't.
It only creates a new variable that shares the reference of the original object.
"""

# Create a list
old_list = [[1, 'ram', 31], [2, 'Charan', 30], [3, 'grcm', 33]]
old_list[2][2] = 31
print(f'Old list - {old_list} and ID {id(old_list)}')

# Copy old_list to new_list
new_list = old_list
print(f"New list elements {new_list} and ID: {id(new_list)}")

# now ID of both list are same even though we have updated the values, as python reference the same memory
# reference to the other variable

# In some cases you don't want changes happened to the old to apply into the new_list, in that case we need to
# use deepcopy by importing copy() module

import copy

# Deep copy exercise
deep_new_list = copy.deepcopy(new_list)
new_list[1][2] = 28
new_list[1][1] = "Rakshith"
new_list.append([4, 'Rian', '1'])
print(f"New list elements {new_list} and ID: {id(new_list)}")
print(f"Deep copy list elements {deep_new_list} and ID: {id(deep_new_list)}")

# Here you don't see the updates happened to new_list as it is a deep copy and ID of the list gets changed
# shallow copy

shallow_new_list = copy.copy(new_list)
new_list.append([5, 'Rudransh', '1'])
print(f"New list elements {new_list} and ID: {id(new_list)}")
print(f"shallow copy list elements {shallow_new_list} and ID: {id(shallow_new_list)}")

# Here you can see shallow_new_list gets the updates made to existing elements but when we .append values it won't get
# changes, ID also differs
