# 3-gönderilen 2 sayı arasındaki tüm asal sayıları bulun

sayi1=int(input('sayi1 gir: '))
sayi2 =int(input('sayi2 gir: '))

for num in range(sayi1, sayi2+1):
    asallmi = True
    for i in range(2,num):
        if(num%i==0):
            break
    else:
         print(num)