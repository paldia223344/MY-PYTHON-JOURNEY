'''
Write a program to calculate the sum of this series up to terms terms.
For example, if the number is 2 and the number of terms is 5,
then the series will be 2+22+222+2222+22222=2469

'''
total = 0
terms = int(input("Enter a number"))
num = 2
for i in range(terms):
    print(num,end= "+")
    total+= num
    num = num*10 + 2
    
print("Sum is : ",total)