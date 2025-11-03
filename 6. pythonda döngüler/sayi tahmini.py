'''
1-100 arasinda rastgele üretilecek bir sayiyi a
şagi yukari ifadeleri ile buldurmaya çalisin. (hak=5)

** random modulu icin python random seklinde arama yapin.
** 100 üzerinden puanlama yapin. her soru 20p.
*** hak bilgisini kullanicidan alin ve her soru belirtilen 
can sayisi üzerinden hesaplansin.
'''

import random

sayi = random.randint(1,10)


hak = int(input('hak sayinizi giriniz: '))
sayac = 0
while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input('tahmin: '))

    if sayi==tahmin:
        print(f'tebrikler {sayac} . defada bildiniz. Toplam puaniniz: {100-(100/hak)*(sayac-1)}')
        break
    elif sayi > tahmin:
        print('yukari')
    else:
        print('asagi')


    if hak == 0:
        print(f'hakkiniz bitti. tutulan sayi : {sayi}')


