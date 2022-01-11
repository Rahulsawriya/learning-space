my_list = [[10,20,30],[40,50,60],[70,80,90]]
output = [10, 20, 30, 40, 50, 60, 70, 80, 90]
t = [[10,20,30],[40,50,60],[70,80,90]]
flat = [item for sublist in t for item in sublist]
print(flat)