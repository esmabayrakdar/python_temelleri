def add(a,b,c,d = 0):
    return sum((a,b,c,)) #sum fonksiyonu

print(add(10,20,40))
print(add(10,20,30))
print(add(10,20,30,40))


def add(a,b,c=0,d = 0):
    return sum((a,b,c,)) #sum fonksiyonu

print(add(10,20,))
print(add(10,20,30))
print(add(10,20,30,40))

def add(*params):
    print(params) #tuple liste olarak yazar
    print(params[0]) #0.indexte olanı yazdırır
    return sum((params))

print(add(10,20)) #toplamları yazar
print(add(10,20,30))
print(add(10,20,30,40))


def add(*params):
    print(type(params))
    sum = 0

    for n in params:
        sum = sum + n

    return sum 

print(add(10,20,30))
print(add(10,20,30,40))

def displayUser(**params):
    print(type(params))
    for key,value in params.items():
        print('{}is{}'.format(key,value))
displayUser(name='çinar',age=2,city='istanbul')
displayUser(name='esma',age=21,city='bursa', phone='123456789')
displayUser(name='mustafa',age=12,city='bursa', phone='19234567', email='mustafa@gmail.com')


def myfunc(a,b,c, *params, **kwargs):
    print(a)
    print(b)
    print(c)
    print(params)
    print(kwargs)

myfunc(10,20,30,40,50, key1='value 1', key2 = ' value 2')