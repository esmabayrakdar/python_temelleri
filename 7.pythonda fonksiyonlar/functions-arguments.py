def changeName(n):
    n = 'ada'
   
name = 'yigit'

changeName(name)
print(name)


def change(n):
    n[0]='istanbul'


sehirler = ['ankara', 'izmir']

change(sehirler)

print(sehirler)


def change(n):
    n[0]='istanbul'


sehirler = ['ankara', 'izmir']
n = sehirler[:] #slicing

n[0]= 'istanbul'
print(sehirler)
print(n)


def change(n):
    n[0]='istanbul'


sehirler = ['ankara', 'izmir']
change(sehirler[:])

print(sehirler)