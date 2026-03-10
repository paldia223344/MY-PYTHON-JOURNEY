'''
Use a lambda with the map() function to double each element in a list
Given:

numbers = [1, 2, 3, 4, 5]
'''

numbers = [1,2,3,4,5]
double_values = list(map(lambda x: x*2,numbers))
print(f"Double values of th numbers list id given by {double_values}")
