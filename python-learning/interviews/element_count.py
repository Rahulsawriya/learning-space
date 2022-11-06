#ip: aaabbccccdddddeefffff
#op: 3abb4c5dee5f
lst = 'aaabbccccdddddeefffff'
#'abaabbbbccddffgggg'
ls = list(set(lst))
op = {}
for i in lst:
	if i in op:
		op[i]+=1
	else:
		op[i] = 1
	"""xy = lst.count(i)
	if xy > 2:
		#print(xy)
		#print(i)
		op.append(xy)
		op.append(i)
	else:
		op.append(i)"""
#print(op)
print(op)

li1 = [1, 1, 2, 2, 2, 3, 4, 4, 4, 4]
li2 = [2, 4, 5]
for i in li2:
    print("count of {} =".format(i), li1.count(i))

#second method
count_occurance = {i: li1.count(i) for i in li1}
print(count_occurance.get(1))






