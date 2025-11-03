#1-100 e kadar
x = 0
while x<=100:
    print(x)
    x=x+1

print('bitti...')


#çift sayilar
x = 1
while x <= 100:
    if x%2==0:
        print(x)
    x+=1

print('bitti')

#tek sayilar
x = 1
while x <= 100:
    if x%2==1:
        print(x)
    x+=1

print('bitti')


name = ''
while not name.strip():
    name = input('isminizi giriniz: ')

print(f'Merhaba {name}')