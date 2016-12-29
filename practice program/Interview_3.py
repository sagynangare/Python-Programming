class Person(object):
    def __init__(self,name):
        self.name = name
    def reveal_identity(self):
        print "My name is {}".format(self.name)

class SuperHero(Person):
    def __init__(self,name,hero_name):

        super(SuperHero,self).__init__(name)
        self.hero_name = hero_name

    def reveal_identity(self):
        print ".....And I am{}".format(self.hero_name)

Corey = Person("Corey")
Corey.reveal_identity()

wade = SuperHero('Wade Wilson','Deadpool')
wade.reveal_identity()

        
