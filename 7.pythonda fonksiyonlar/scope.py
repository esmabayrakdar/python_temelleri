x= 'global x'

def function():
    x = 'local x'
    print(x)

function()
print(x)

print("--------------------------")

x= 'global x'

def function():
    
    print(x)

function()
print(x)


print("-----------------------------------------")
######################################
name = 'Esma'

def changeName(new_name):
    #global name olarak tanımlarsak dışardaki Esma stringi de Ada stringi ile değiştirilir
    name=new_name
    print(name)
changeName('Ada')
print(name)

print("---- iç içe fonksiyon tanımladığımız zaman----")

name='global string'

def greeting():
    #name='Esma'

    def hello():
        #name = 'Ada'
        print('hello ' + name)
    
    hello()
greeting()


print("-----")
x= 50
def test(x):
    print(f'x: {x} ')

    x= 100
    print(f'changed x to {x}')

test(x)
print(f'global x: {x}')