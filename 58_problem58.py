print("Number Pattern:")

# Outer loop for the number of rows
for i in range(1, 6):
    # Inner loop to print numbers in each row
    for j in range(1, i + 1):
        print(j, end=' ')
    # Move to the next line after each row is printed
    print("")