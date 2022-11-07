#A static method is a method which is bound to the class and not the object of the class. It can’t access or modify class state.
class Maths():
      
    @staticmethod
    def addNum(num1, num2):
        return num1 + num2
          
# Driver's code
if __name__ == "__main__":
      
    # Calling method of class
    # without creating instance
    res = Maths.addNum(1, 2)
    print("The result is", res)

