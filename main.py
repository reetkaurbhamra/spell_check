def spellCheck():
    return 0

list_1 = ['aa', 'bb', 'bb1', 'cc', 'dd']
list_2 = ['bb', 'u2', 'c', 'ad']
potential = []

for i in list_1:
    if i not in list_2:
        potential.append(i)

print(potential)