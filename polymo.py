class animal:                                 #parent class
    def __init__(self, name):                #constructor
        self.name = name                     # instance variable

    def speak(self):                      
        print ("animal speaks")             
class dog(animal):
    def speak(self):
        print (" barks barks!")

  class cat(animal):
    def speak(self):
        print (" meows meows!")

def animal_sound(animal):
    animal.speak()
    pets = [dog(), cat()]
    for pet in pets:
        animal_sound(pet)
animal_sound(dog())
animal_sound(cat())




class shape:
    def area(self):
     print ("area is 0")

class rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    print("Area of rectangle:", rectangle(5, 3).area())
    
class circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
    print("Area of circle:", circle(4).area())

    #one loop through shapes
shapes = [recangle(5, 3), circle(4)]   # create shape objects
for sh in shapes:                      # loop through shape objects
    print("Area:", sh.area())          # each print its own area



    
        


        