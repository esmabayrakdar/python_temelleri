#BANKAMATİK UYGULAMASI

EsmaHesap = {
    'ad': 'Esma Bayrakdar',
    'hesapNo':'14562892',
    'bakiye':5000,
    'ekHesap':2000
}

AhmetHesap = {
    'ad': 'Ahmet Bayrakdar',
    'hesapNo':'87235149',
    'bakiye':2000,
    'ekHesap':1000
}

def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")

    if(hesap['bakiye']>= miktar):
        hesap['bakiye']-=miktar
        print('paranızı alabilirsiniz.')
        bakiyeSorgula(hesap)
    else:
        toplam=hesap['bakiye'] + hesap['ekHesap']
        if (toplam >= miktar):
            ekHesapKullanimi = input('ek hesap kullanılsın mı?(e/h)')

            if ekHesapKullanimi == 'e':
                bakiye= hesap['bakiye']
                ekHesapKullanilacakMiktar=miktar-bakiye
                hesap['bakiye']=0
                hesap['ekHesap']-=ekHesapKullanilacakMiktar
                
                print('paranızı alabilirsiniz..')
                bakiyeSorgula(hesap)
            else:
                print(f'{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır')
        else:
            print('üzgünüz bakiye yetersiz')
            bakiyeSorgula(hesap)

    
def bakiyeSorgula(hesap):
    print(f'{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz ise {hesap['ekHesap']} bulunmaktadır')


def paraYatir(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")
    hesap['bakiye']+=miktar
    print(f"{miktar} TL hesabınıza yatırlımıştır.")
    bakiyeSorgula(hesap)


paraCek(EsmaHesap,4000)

paraCek(EsmaHesap,3000)

paraCek(EsmaHesap,100)

paraYatir(EsmaHesap,2000)

