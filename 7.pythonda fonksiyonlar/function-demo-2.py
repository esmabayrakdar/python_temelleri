# 2-kendine gönderilen sınırsız sayıdaki parametreyi bir
#listeye ceviren fonksiyonu yaz

def cevir(*params):
    return list(params)

def listeyeCevir(*params):
    liste=[]

    for param in params:
        liste.append(param)

    return liste
result= listeyeCevir(10,20,30, 'merhaba')
print(result)