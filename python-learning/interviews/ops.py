#example:1
#dict1 = {1:"a","str":2,1:("c",2),(9,99):"tuple",{7:77}:"dict"}
#print(dict1)
#Error: TypeError: unhashable type: 'dict'

#example:2
tuple1 = (1,"string",(9,99),[7,77],)
print(tuple1) # (1, 'string', (9, 99), [7, 77])
tuple1[-1].append(1999) 
print(tuple1) #(1, 'string', (9, 99), [7, 77, 1999])

example:3
class Teacher:
	def printme(self):
		print("Hi From Teacher")

class Student:
	def printme(self):
		print("Hi From Student")

class Principal(Teacher, Student):
	pass

p = Principal()
p.printme() #MRO: Method resolution order
#Hi from Student
