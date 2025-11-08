class Person:
    def __init__(self, name, year):
        self.name = name
        self.year = year
    #instance methods
    def intro(self):
        print(f'Hello there. I am '+ self.name)
    #instance methods
    def calculateAge(self):
        return 2025-self.year
        print('I am '+self.year + ' years old.')

p1 = Person('Esma', 2004)
p2 = Person('Ahmet', 2025)


p1.intro()
p2.intro()

print(f'adım: {p1.name} yaşım: {p1.calculateAge()}')




class Circle:
    #Class object attributes
    pi = 3.14

    def __init__(self, yaricap=1):
        self.yaricap=yaricap

    #methods
    def cevre_hesapla(self):
        return 2 * self.pi * self.yaricap

    def alan_hesapla(self,yaricap=1):
        return self.pi*(self.yaricap**2)

c1=Circle()
c2=Circle(5)

print(f'c1: alan= {c1.alan_hesapla()} cevre= {c1.cevre_hesapla()} ')
print(f'c2: alan= {c2.alan_hesapla()} cevre= {c2.cevre_hesapla()}')