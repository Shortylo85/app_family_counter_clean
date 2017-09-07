class PersonTree():
    
    def __init__(self, firstname, lastname, gender, parent = False):
        
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.parent = parent
        
    def createPerson(self):
        
        
        
        array_person = []
        
        json_person = {
                'firstname': self.firstname,
                'lastname': self.lastname,
                'gender': self.gender,
                'parent': self.parent,
        }
        array_person.append(json_person)
        print(array_person)
        
        
        
    
person1 = PersonTree("Danijel","Petrovic","musko")

person1.createPerson()
