#abstraction  is the process of hiding the complex implementation details and showing only the essential features of the object.
#hiding unnecessary details and showing only what is important.
#hiding the complexity,showing what the user needs.
#why abstract is needed: modify,enables userability, improves security.


from abc import ABC, abstractmethod
class vechile(ABC):             #INHERIT FROM ABC
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year =year
    
    
    @abstractmethod
    def display_info(self):       #no code here 
        pass
    
class car(vechile):
    def __init__(self, make, model, year, num_doors):
            super().__init__(make, model, year)      #
            self.num_doors = num_doors
     
    def display_info(self):
        print("car information")
        print("make :",self.make)
        print("model",self.model)
        print("year", self.year)
        print("doors:",self.num_doors)

car=car("toyota","hilax", 2002, 8)

car.display_info()