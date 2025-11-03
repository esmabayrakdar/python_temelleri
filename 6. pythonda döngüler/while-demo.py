sayilar = [1,3,5,7,9,12,19,21]

#1- sayilar listesini while ile ekrana yazdır
i=0
while(i<len(sayilar)):
   print(sayilar[i])
   i+=1

#2-başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki 
# tüm tek sayıları ekrana yazdır.
baslangic = int(input('baslangic degeri giriniz:'))
bitis = int(input('bitis degerini giriniz:'))


i=baslangic
while i<bitis:
    i+=1
    if(i%2==1):
        print(i)

#3-1-100 arasındaki sayıları azalan şekilde yaz
i=100
while i>0:
    print(i)
    i-=1


#4-kullanıcıcdan alacağınız
#  5 sayıyı ekranda sıralı şekilde yazdır.

numbers=[]

i=0
while i<5:
    sayi = int(input('sayi: '))
    numbers.append(sayi)
    i+=1

numbers.sort() #sıralı şekilde sıralar
print(numbers)


#5-kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi
# içinde sakla
#ürün sayınsını kullanıcıya sor
#dictionary listesi yapısı (name, price) şeklinde olsun
#ürün ekleme işlemi bittiğinde ürünleri ekranda 
# while döngüsü ile listele

urunler = []

adet = int(input('kaç ürün eklemek istiyorsunuz: '))

i=0

while(i<adet):
    name = input('ürün ismi: ')
    price = input('ürün fiyati:')
    urunler.append({
        'name': name,
        'price': price
    })
     i+=1

for urun in urunler:
    print(f'ürün adi: {urun["name"]} ürün fiyati: {urun["price"]}')