'''
printing the pattern
1
12
123
1234
12345 
'''
row = int(input("Enter number of rows"))
for i in range (1,row+1):
    for j in range (1,i+1):
        print(j,end = '')
    
    print("")
