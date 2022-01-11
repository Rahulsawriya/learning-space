test_list = [1, 1, 3, 4, 4, 4, 5, 6, 6, 7, 8, 8, 6, 9, 9, 1]
#old_list = [3,5,7,6]

dupe = False
i=0
old_list = []
while i < len(test_list) - 1:
    if test_list[i] == test_list[i+1]:
        del test_list[i]
        dupe = True
    elif dupe:
        del test_list[i]
        dupe = False
        old_list.append(test_list[i])
    else:
        i+=1
print(old_list)