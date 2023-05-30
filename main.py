def spellCheck():
    return 0

# A Naive recursive Python program to find minimum number
# operations to convert str1 to str2


def editDistance(str1, str2, m, n):
    if m == 0:
        return n
    if n == 0:
        return m
    if str1[m-1] == str2[n-1]:
        return editDistance(str1, str2, m-1, n-1)

    return 1 + min(editDistance(str1, str2, m, n-1), # Insert
				editDistance(str1, str2, m-1, n), # Remove
				editDistance(str1, str2, m-1, n-1) # Replace
				)

# This code is contributed by Bhavya Jain

list_1 = ['aa', 'bb', 'bb1', 'cc', 'dd']
list_2 = ['bb', 'u2', 'c', 'ad']
potential = []

for i in list_1:
    if i not in list_2:
        potential.append(i)

print(potential) #all elements of list1 that are not in list2

for j in potential:
    for k in list_2:
        l = editDistance(j,k,len(j),len(k))
        if l!=0 and l!=len(j):
            print(j,l,k)