# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list
sample_list = ['apple', 'orange', 'chickoo', 'pomegranate']
new_list = []
for i in sample_list:
    new_list.append(i)
print(f"Old list -> {sample_list}")
print(f"New list -> {new_list}")

# Here we created 'for' loop to create a new list, instead we can create a list with a single line using list comprehension

new_list1 = [i for i in sample_list]
print(new_list1)


new_list2 = [i for i in sample_list if 'a' in i ]
print(new_list2)

new_list3 = [i if 'a' in i else 'No Fruit' for i in sample_list]
print(new_list3)

print(sample_list.sort())
