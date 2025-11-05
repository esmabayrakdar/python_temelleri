def sayHello():
    print('Hello')

sayHello()

def sayHello(name):
    print('Hello '+ name)

sayHello('Esma')
 

def sayHello(name = 'user'):
    print('Hello '+ name)

sayHello('Esma')
sayHello()

def sayHello(name = 'user'):
    return 'Hello ' + name

msg = sayHello('Çınar')
print(msg)
 

def total(num1,num2):
    return num1+num2
result = total(10,20)
print(result)


def yasHesapla(dogumYili):
    return 2025-dogumYili
ageEsma= yasHesapla(2004)
ageMustafa= yasHesapla(2013)
ageBelinay = yasHesapla(2015)
ageAhmet = yasHesapla(2025)

print(ageEsma, ageMustafa, ageBelinay, ageAhmet)

def EmekliligeKacYilKaldi(dogumYili, isim):
    '''
    DOCSTRİNG: Doğumm yiliniza göre emekliliğinize kaç yil kaldi
    INPUT: doğum yılı
    OUTPUT: hesaplanan yıl bilgisi
    '''
    yas = yasHesapla(dogumYili)
    emeklilik = 65-yas
    if emeklilik>0:
        print(f'{isim} emekliliginize {emeklilik} yil kaldi')
    else:
        print(f'zaten emekli oldunuz')


EmekliligeKacYilKaldi(1968, 'Hasan')

print(help(EmekliligeKacYilKaldi))

list = [1,2,3]
print(help(list.append))