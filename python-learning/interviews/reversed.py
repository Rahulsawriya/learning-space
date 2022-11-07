input = ['xyz', 'abc', '123']
#output = ['zyx', 'cba', '321']
result = [i[::-1] for i in input]
print(result)

input = [[1,1,0],[1,0,1],[0,0,0]]
#Output: [[1,0,0],[0,1,0],[1,1,1]]
output = []
for n in input:
    new_list = []
    out = n[::-1]
    #print(out)
    #print("="*20)
    for i in out:
        if out[i] == 0:
            out[i] = 1
            new_list.append(out[i])
        else:
            out[i] = 0
            new_list.append(out[i])
print(output)