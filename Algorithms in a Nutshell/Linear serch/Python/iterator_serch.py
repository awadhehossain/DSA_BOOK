# It simply called While loop use insted for loop
# Using try except
def serch_iterator(C,t):
    iter_c=iter(C)
    index=0
    while True:
        try:
            e=next(iter_c)
            if e==t:
                return index # it return the index 
            index+=1
        except StopIteration:
            break
    return False
A=[1,2,3,4,5,6,8,9,0]
print(serch_iterator(A,0))# It return 8