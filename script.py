print('Hello, World!')
def has_duplicates(lst):
    return len(lst) != len(set(lst))
    
x = [1,2,3,4,5,5]
has_duplicates(x) 			# True
first = [1, 2, 3, 4, 5]
print(first)
second = first
print(second)
second.append(6)
print(second)
print(first)
if first == second :
    print("bug! you will get hacked!")
