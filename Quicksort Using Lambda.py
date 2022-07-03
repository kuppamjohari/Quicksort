import random as r
from time import time as T
a=int(input("Enter the range of starting no: "))
b=int(input("Enter the range of End no: "))
c=int(input("Enter Number of Elements in list: "))
k=r.sample(range(a,b),c)
print(f"Randomly generated list :{k}")
begin=T()
q = lambda l: q([x for x in l[1:] if x <= l[0]]) + [l[0]] + q([x for x in l if x > l[0]]) if l else []
print(f"Randomly generated list after Sorting : {q(k)}")
end=T()
print(f"Time taken to sort the Elements : {begin-end}")
