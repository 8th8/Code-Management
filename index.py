a = int(input("nhap so a :"))
b = int(input("nhap so b :"))

class Calculator():
    def add (self,a,b):
        return a + b
    
    def subtract (self,a,b):
        return a - b
    def Multiply (self,a,b):
        return a * b
    def Divide (self,a,b):
        if b != 0:
            return a / b
        else:
            return " khong chia duoc "
cals = Calculator()
print("add :",cals.add(a,b))
print("subtract :",cals.subtract(a,b))
print("Multiply :",cals.Multiply(a,b))
print("Divide :",cals.Divide(a,b))