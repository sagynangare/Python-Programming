from parent import *

class Child(Person):

    def __init__(self,name,age,address,mobile_no):
        
        Person.__init__(self,name,age,address,mobile_no)
        self.str = str
        self.int = int
result = Child("Sagar",24,"chavanwadi",9975340919)
