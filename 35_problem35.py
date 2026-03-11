'''

Use a lambda with the sorted() function to sort a list of tuples based on the second element
Given:

data = [('apple', 5), ('banana', 2), ('cherry', 8), ('date', 1)]
'''

data = [('apple', 5), ('banana', 2), ('cherry', 8), ('date', 1)]
sorted_list= sorted(data,key = lambda item:item[1])
print(f"The sorted list of tuples based on the second element is: {sorted_list}")
