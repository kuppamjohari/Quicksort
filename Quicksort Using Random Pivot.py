import random as r
from time import time as T
a=int(input("Enter the range of starting no: "))
b=int(input("Enter the range of End no: "))
c=int(input("Enter Number of Elements in list: "))
k=r.sample(range(a,b),c)
print(f"Randomly generated list :{k}")
begin=T()
def quicksort(my_list):
    if len(my_list)==0:
        return []
    list_pivot=r.randint(0,len(my_list)-1)
    print(f"Random pivot of Quicksort: {list_pivot}")
    pivot = my_list[list_pivot]
    smaller = filter(lambda x: x < pivot,my_list)
    greater = filter(lambda x: x > pivot,my_list)
    return quicksort(list(smaller)) + [pivot] + quicksort(list(greater))
print(f"Randomly generated list after Sorting : {quicksort(k)}")
end=T()
print(f"Time taken to sort the Elements : {begin-end}")
