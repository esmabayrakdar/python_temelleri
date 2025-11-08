#Object Oriented Programming(OOP)

#class

class Person:
    pass
    #attributes
    adress='no information'

    #constuctor ( yapıcı metod)
    def __init__(self, name, year):
        self.name = name
        self.year = year
        print('init metodu çalıştı')


    #methods

#object, instance
p1 = Person('Esma',2004)
p2 = Person('Ahmet',2025)

#updating
p1.name = 'Mustafa'
p1.adress = 'Bursa'
#accessing object attributes
print(f'p1: name:{p1.name} year: {p1.year} adres: {p1.adress}')
print(f'p2: name:{p2.name} year: {p2.year} adres: {p2.adress}')

print(p1)
print(p2)
print(type(p1))
print(type(p2))
print(p1==p2) #farklı objeler