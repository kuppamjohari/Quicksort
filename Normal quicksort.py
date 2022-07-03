import random as r
from time import time as T
a=int(input("Enter the range of starting no: "))
b=int(input("Enter the range of End no: "))
c=int(input("Enter Number of Elements in list: "))
k=r.sample(range(a,b),c)
print(f"Randomly generated list :{k}")
begin=T()
def quicksort(my_list):
    # recursion base case - empty list
    if not my_list:
        return []
    # first element is pivot
    pivot = my_list[0]
    # break up problem
    smaller = [x for x in my_list[1:] if x < pivot]
    greater = [x for x in my_list[1:] if x >= pivot]
    # recursively solve problem and recombine solutions
    return quicksort(smaller) + [pivot] + quicksort(greater)
print(f"Randomly generated list after Sorting : {quicksort(k)}")
end=T()
print(f"Time taken to sort the Elements : {begin-end}")
