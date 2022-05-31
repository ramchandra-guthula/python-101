sample_list = ['a', 'b', 'c', 'c', 'a', 'd']

for i in range(len(sample_list)): # Looping through index
    for p in range(i+1, len(sample_list)):
        if sample_list[i] == sample_list[p]: # Taking first element in sample_list and compare with all the elements
            print(sample_list[i])