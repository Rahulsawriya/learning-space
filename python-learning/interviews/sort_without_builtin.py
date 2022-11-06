old_list = [5, 7, 2, 1]
new_list = []
while old_list:
	minimum = old_list[0]
	for item in old_list:
		if item < minimum:
			minimum = item
	new_list.append(minimum)
	old_list.remove(minimum)
print(new_list)

#=====================================
from operator import itemgetter
arr = [{"name": "Nandini", "age": 20}, {"name": "Manjeet", "age": 20}, {"name": "Nikhil", "age": 19}]
result = sorted(arr, key=itemgetter('age'), reverse=True)
print(result)

# using sorted and lambda to print list sorted
# by age
print("The list printed sorting by age: ")
print(sorted(arr, key=lambda i: i['age']))

# using sorted and lambda to print list sorted
# by both age and name. Notice that "Manjeet"
# now comes before "Nandini"
print("The list printed sorting by age and name: ")
print(sorted(arr, key=lambda i: (i['age'], i['name'])))

#========================================
"""You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions."""

# Examples => Expected Output
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
# [5, 3, 2, 8, 1, 4] => [1, 3, 2, 8, 5, 4]
# [5, 3, 1, 8, 0] => [1, 3, 5, 8, 0]

def sort_array(source_array):
    sort_odd_array = sorted([num for num in source_array if num%2 != 0 ])
    result = []
    i = 0
    for num in source_array:
    	if num%2!=0:
    		result.append(sort_odd_array[i])
    		i+=1
    	else:
    		result.append(num)
    return result
    #return sort_odd_array

print(sort_array([5, 8, 6, 3, 4]))
#print(sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))
