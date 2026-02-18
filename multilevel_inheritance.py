class employee:
    a = 1

class manager(employee):
    b = 3
    
class worker(manager,employee):
    c = 8

p = employee()
j= manager()
k= worker()
print(k.c,k.b,k.a)
print(j.b,j.a)
print(p.a)