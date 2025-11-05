
# 4-kendisine gönderilen bir sayının tam bölenlerini bir liste
#  seklinde döndüren fonksiyon

sayi=int(input('sayi gir: '))
for i in range(1,sayi+1):
    if (sayi%i==0):
        print(i)

def tamBolenleriBul(say):
    tamBolenler=[]

    for i in range(2,say):
        if(say%i==0):
            tamBolenler.append(i)

    return tamBolenler
print(tamBolenleriBul(20))
        