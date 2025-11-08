# Inheritance (Kalıtım): Miras alma

#Person => name, lastname, age, eat(), run(), drink()

#Student(Person), Teacher(Person)

#Animal => Dog(), Cat()

class Person():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        print('Person Created')


    def who_am_i(self):
        print('I am a person')

    def eat(self):
        print('I am eating')

class Student(Person):
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname,lname)
        self.studentNumber=number
        print('Student Created')

    
    #override
    def who_am_i(self):
        print('I am a student')
    
    def sayHello(self):
        print('Hello I am student')

class Teacher(Person):
    def __init__ (self,fname,lname,branch):
        #Person.__init__ 
        super().__init__(fname,lname)
        self.branch = branch
    
    def who_am_i(self):
        print(f'I am a {self.branch} teacher')


p1 = Person('Esma', 'Bayrakdar')
s1=Student('Ayşe' ,'Yilmaz',847)
t1= Teacher('Sadık','Turan','Python')

print(p1.firstName+' '+p1.lastName)
print(s1.firstName+' '+s1.lastName+ ' '+ str(s1.studentNumber))

p1.who_am_i()
s1.who_am_i()
t1.who_am_i()

p1.eat()
s1.eat()
s1.sayHello()
