# 1-gönderilen bir kelimeyi belirtilen kez ekranda gösteren 
# fonksiyonu yazın

kelime = input('kelime gir: ')
sayac = int(input('sayac gir: '))
def yazdir(kelime, sayac):

    while sayac>0:
        print(kelime)
        sayac-=1

yazdir(kelime,sayac)

def yaz(kelime, adet):
    print(kelime*adet)

yaz('merhaba\n',5)
