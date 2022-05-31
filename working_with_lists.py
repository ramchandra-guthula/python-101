"""
Create a sample list
"""
sample_list = ["Name", "Location", 30, "devops12"]

"""
Adding and updating Elements to list 
"""
sample_list.append("Bangalore")

sample_list[2] = "Cloud" # Updating element 2 with 'cloud'

another_list = ["linux", "centos", "suse", "ubuntu"]

sample_list.append(another_list)

print(f"List after adding Bangalore: {sample_list}")
sample_list[1:4] = ["Ocean", "hills", "Desert"]


"""
Adding several elements to a list
"""

sample_list.extend([15, 25, "raji"])

"""
Adding elements at a specific index using insert() method
"""
sample_list.insert(3, "Ram")

"""
Printing a Elements from the list like last, middle etc
"""
print(f"Last Elements in a list: {sample_list[-1]}") # If you staring using index Elements with '-' it start prints in reverse order

print(f"Last but one from a list: {sample_list[-2]}")

print(f"Elements between index 1 to 3: {sample_list[1:3]}")

print(f"Elements beginning to end: {sample_list[:]}")

print(f"Elements from index 2 onwards: {sample_list[2:]}")

"""
Getting a length of a list
"""
print(f"length of a list: {len(sample_list)}")

"""
Delete a value from the list
"""
del sample_list[2]
print(f"List after deleting a Elements: {sample_list}")

print(f"Delete elements using pop: {sample_list.pop(2)}")

"""
Looping through list
"""
for _i in sample_list:
    print(_i)


"""
Sorting and reversing the elements in list
"""
print(f"Sorted list: {sample_list.sort()}")

"""
Clear the entire list elements
"""
sample_list.clear()
print(f"List elements after clearing the list: {sample_list}")
