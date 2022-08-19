"""
Add a key and value to dictionary
"""
sample_dictionary1 = {"id": 1, "author": "ram", "book_name": "Life is a Lie"}
sample_dictionary1["rating"] = 5
print(f"Dictionary after adding a value: {sample_dictionary1}")

# So, instead of the del statement you can use the pop method. This method takes in the key as the parameter.
# As a second argument, you can pass the default value if the key is not present.
sample_dictionary1.pop("id", none)



"""
Delete a key from a  dictionary
"""

sample_dictionary2 = {"id": 1, "author": "ram", "book_name": "Life is a Lie"}
del sample_dictionary2['id']
# del sample_dictionary2['rating'] # this throws an error because this key is not exist  KeyError: 'rating'
print(sample_dictionary2)


# Using pop(), pop will be
sample_dictionary2 = {"id": 1, "author": "ram", "book_name": "Life is a Lie"}
remove_key1 = sample_dictionary2.pop("author")
print(f"remove existing key with pop: {sample_dictionary2}")
remove_key2 = sample_dictionary2.pop('rating', 'Key not exists')
print(f"remove key which is not exists with pop: {sample_dictionary2}")


"""
Loop through dictionary using FOR loop
"""
sample_dictionary = {"id": 1, "author": "ram", "book_name": "Life is a Lie"}
for key, value in sample_dictionary.items():
    print(key, ":", value)


"""
Dictionaries inside a list
"""
multiple_dic = [
    {"id": 1, "author": "Ram", "book_name": "Life is a Lie"},
    {"id": 2, "author": "Raji", "book_name": "Truth of life"},
    {"id": 3, "author": "Rian", "book_name": "Worth to live"}
]

"""
Looping through list of dictionaries
"""

for i in multiple_dic:
    print(i)
"""
Print only authors from the dictionaries
"""

for i in multiple_dic:
    print(i['author'])
    
"""
Delete one dictionary form the list based on the key matches
"""

counter = 0
for i in multiple_dic:
    counter += 1
    if i['id'] == 3:
        del multiple_dic[counter - 1]  # Here -1 is because of list index starts at 0, if iteration is 2, 2-1

print(multiple_dic)


"""
Updating a value of dictionary
"""

counter = 0
for i in multiple_dic:
    counter += 1
    print(i)
    if i['id'] == 3:
        multiple_dic[counter - 1]['id'] = 4 

print(multiple_dic)


"""
Finding and remove duplicates from the given list, https://www.w3schools.com/python/python_howto_remove_duplicates.asp
"""

sample_list = ['a', 'b', 'a', 'c', 'c', 'd']
duplicates = list(dict.fromkeys(sample_list)) # while creating a dictionary it removes the duplicates
print(duplicates)

"""
Reverse string 
"""

txt = "Hello World"[::-1]
print(txt)

def reverse_string(given_string):
    return given_string[::-1]

print(reverse_string("reverse this string"))



"""
Find a duplicates in list
"""
sample_list1 = ['a', 'b', 'a', 'c', 'c', 'd']
for i in sample_list1:
    if sample_list1.count(i) > 1:
        print(i)
