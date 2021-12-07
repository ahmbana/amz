class Person:
    def __init__(self, name):
        self.name=name
    def say_hi(self):
        print("hallo, my name is",self.name)
p=Person("ahmed")
p.say_hi()

class Human:
    #person='human'
    def __init__(self, nationality,size,eye_color):
        self.nationality= nationality
        self.size= size
        self.eye_color= eye_color
    def get_details(self):
        print(self.nationality)
        print(self.size)
        return self.eye_color
Ahmed=Human("yemen","178cm","brown")
Belal=Human("palstain","178cm","brown")
print("details list of Ahmed & Belal:")
print("\nAhmed's details:")
print("nationality:",Ahmed.nationality)
print("size:",Ahmed.size)
print("eye colore:",Ahmed.eye_color)

print("\nBelal's details:")
print("nationality:",Belal.nationality)
print ("size:",Belal.size)
print("eye colore:",Belal.eye_color)

#print("\nAccessing class variable using class name")
#print(Human.person)  
print(Ahmed.get_details())


      
