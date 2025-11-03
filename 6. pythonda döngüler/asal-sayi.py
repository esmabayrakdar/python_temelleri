'''
soru: girilen bir sayinin asal olup olmadigini bulun.
** sasl sayi 1 ve kendisi hariç 
tam böleni olmayan sayilara denir.
'''

sayi = int(input('sayi giriniz: '))

if sayi <= 1:
    print('{} sayisi asal değildir'.format(sayi))
else:
    for i in range(2,sayi):
        if(sayi%i==0):
            print("{} sayisi asal degil.".format(sayi))
            break
    else:
         print("{}sayisi asal sayidir.".format(sayi))






