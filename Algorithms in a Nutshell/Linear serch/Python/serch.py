def serch_list(A,t):
    for i in range(len(A)):
        if A[i]==t:
            return i
        #It return the index where the element is located
    return False
    # If the are not in the list it return false

A=[3,4,5,6,7,2,1]
# For linear serch it is nor nessery to sorted the list in assending order
print(serch_list(A,1))# it return 6
print(serch_list(A,0))# it return False
S=[2,3,4,5,6,7,1]
# Not nessery to same both function list name and declered list name.
# Declred list passes through the function ,Function parameter accept the list.
print(serch_list(S,3))# it return 1
print(serch_list(S,8))# it return False