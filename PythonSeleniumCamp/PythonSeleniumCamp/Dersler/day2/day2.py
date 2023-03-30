faiz = 1.59
vade = "36"
krediAdi = "İhtiyaç Kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))


print(int(vade) + 12)
#print(int(krediAdi)) bu şekilde hata alınır, int değere çevrilemez
faiz = str(faiz)
print(type(faiz))
#Kullanıcıdan alınan input pythonda defalt olarak string değerine sahip oluyor.
vade =  36 #int(input("Lütfen istediğiniz vade sayısını giriniz: "))
print(type(vade))
vade = vade + 12

# string interpolation 
# Seçtiğiniz vade sonucu ortaya çıkan vade: 
print("Seçtiğiniz vade sonucu ortaya çıkan vade: " + str(vade))
print("Seçtiğiniz vade sonucu ortaya çıkan vade: {vadeSayisi}".format(vadeSayisi=vade))
print(f"Seçtiğiniz vade sonucu ortya açıkan vade: {vade}")

isim = "Gizem" #input("İsminizi giriniz : ")
metin = "Merhaba {name}".format(name = 123)
print(metin)


# f-string
metin = f"Hoşgeldiniz {1+1}"
print(metin)


#listeler : programlamada verileri set, koleksiyon olarak saklamamızı sağlayan bir veri türüdür. Elemanlarımızı [] içine yazarız.
#döngüler
#fonksiyonlar 

dizi = ["İhtiyaç Kredisi", 10, 5.2, True] #hem string hem int, hem boolean hemde float değerlerimiz var, yani bütün değerleri barındırabilir list
print(dizi)

krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
print(type(krediler))

print(krediler[0])

print(len(krediler)) #lenght
#print(krediler[3]) => hata verir, çünkü saymaya 0'dan başlanır

krediler.append("Özel Kredi") #append içerisine aldığı değeri o listenin SON elemanına ekler
print(krediler)

krediler.append("X Kredisi")
print(krediler)

krediler.pop(0) #verilen indexteki elemanı siler ama bir index belirtmek zorunda değilsin, index belirtilmezse son elemanı siler
print(krediler)

krediler.append("Taşıt Kredisi")
print(krediler)


krediler.remove("Taşıt Kredisi") #index değil değer bazlı çalışıyor, içerisine yazılan değeri bulduğu İLK elemanı siliyor
print(krediler)

krediler.extend(["Y Kredisi", "Z Kredisi"]) #birden fazla eleman eklemek istersek 
print(krediler)

# for döngüsü , döngü bir condition vererek, bu condition sağlandığı sürece bir kod bloğunu tekrar tekrar çalıştırdığımız yapılardır
# i=0 i<10 i++
x = 10
for i in range (x) : # range kısmı i değerini alıp verilen değere ulaşana kadar arttırır burada i 0'dan başlar 10'a kadar, 10 dahil olmayacak şekilde sayar
    print("xx")
    print(i)
print("********************************")

for i in range(5,10): # 5'ten başlayıp 10'a kadar devam eder
    print(i)

print("***************************")
for i in range(0,51,10):
    print(i)
print("***************************")
# for i in range(0.1,0.5): bu durumda hata alırdık range içinde integer istediğini söylüyor
#     print(i)
krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
for kredi in krediler :
    print(kredi) # her elemanın teker teker yazıldığın görürüz bunun sonucunda 
print("*******************************")
for i in range(len(krediler)):
    print(krediler[i]) # yukarıdaki gibi hepsini teker teker yazdırır ama bunu indexi kullanarak yapar
print("*********************")


# sonsuz döngü
i = 0
while i < 10 : #yanındaki condition true olduğu sürece içerisindeki bloğu çalıştıran bir yapıdır
    print("x")
    i +=1 # i = i + 1 demektir yani i'yi bir arttır, i++ yazarsan hata alırsın bu syntax pythonda mevcut değildir
print("y")

print("******************************")


while True :
    print("X")
    break # döngüyü kırmak için kullanılır 

print("************ Son Döngü ******************")

krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
i = 0
while i < len(krediler):
    i +=1
    print(i)
    print(krediler[i])
    if krediler[i] == "Konut Kredisi" :
        break

# fonksiyonlar , yapıcağımız işlemleri bir fonksiyona atadığımız ve çağırdığımız sürece içerisindeki bloğu çalıştırabildiğimiz yapılardır

fiyat = 100
indirim = 20
#definition define 
def calculate(): # Pythonda bir fonksiyon tanımlamak için def kullanırız
    print(100-20)

def calculateWithParams(fiyat,indirim): # fonksiyonlara parametre atamak için pythonda ilgili fonksiyonu tanımlarken parantezin içerisine bu parametreleri sırasıyla, virgülle ayırarak yazıyoruz.
    print(fiyat-indirim)

def sayHello(name):
    print(f"Merhaba {name}")


calculate() #print satırı ben calculate()'i ne kadar çağırırsam o kadar çalışıcak
calculateWithParams(50,10)
calculateWithParams(100,30)
sayHello("Halit")
sayHello("Arif")
sayHello("Mevlüt")


def calculateAndReturn(fiyat,indirim): #bunun içindeki isimler farklı olmak zorunda değil her fonksiyon kendi bloğunda çalışır
    return fiyat-indirim #ilgili fonksiyonun geriye döneceğini belirttiğimiz alan

yeniFiyat = calculateAndReturn(200,50) #fonksiyonda verdiğimiz sırayla bu değerleri vermek zorundayız, sıra önemli
print(yeniFiyat + 10)

#void, return yazılmadığında geriye değer dönmeyen, void olarak isimlendirilen fonksiyon türü olarak düşünebiliriz
def calculatePrice (price, discount):
    print(price-discount) #return yerine print olduğu için çıkan sonucu başka yerde kullanamıyorum sadece bu fonksiyon içinde kulanabiliyorum

def calculatePriceAndReturn (price, discount):
    return price - discount

print("****************************")
fonk1 = calculatePrice(100,50) #return olmadığı için fonk1'e bir değer ataması yapamadık
fonk2 = calculatePriceAndReturn(300,100)
print(f"159.satır + {fonk1}")
print(f"160.satır + {fonk2+100}")
print("*************************************")
