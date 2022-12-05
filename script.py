print('Hello, World!')
def has_duplicates(lst):
    return len(lst) != len(set(lst))
    
x = [1,2,3,4,5,5]
has_duplicates(x) 			# True
