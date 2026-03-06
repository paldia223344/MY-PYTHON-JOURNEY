'''
Write a code to generates a complete multiplication table for numbers 1 through 10.
'''
n = int(input("Enter a number"))
for i in range (1,n+1):
    print(f"MULTIPLICATION TABLE OF {i}:")
    for j in range (1,11):
        print(f"{i} X {j} = {i*j}")
  