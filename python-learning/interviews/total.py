def total_list_sum(lst1):
    total = 0  # don't use `sum` as a variable name
    for i in lst1:
        if isinstance(i, list):  # checks if `i` is a list
            total += total_list_sum(i)
        else:
            total += i
    return total

lst1 = [2, 5, [3, 4, 7],[4, 6, 2, [7, 3]]]
print(total_list_sum(lst1))

#=========================================
list1 = [1, 2, 3, 4]
 
total = 0
for i in list1:
    total = total + i
print(total)



    