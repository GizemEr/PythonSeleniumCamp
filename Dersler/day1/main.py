print("Kodlama.io")
baslik = "Taşıt Kredisi"
print(baslik)
#string => metinsel ifade 
baslik = "İhtiyaç Kredisi"
print(baslik)
#int, integer => tam sayı (değişken türü)
vade = 36 #numeric bir ifade, işlem yapabiliriz
ekVade = 6
vade2 = "36" #metinsel bir ifade

#float, decimal, double 
aylikOdeme = 200.50 

#bool, boolean=> karar yapılarında yani true, false için kullandığımız
yukselisteMi = False

#matematiksel operatörler 

# +
print(5 + 5)
print(vade + 12)
print(vade + ekVade)
print(36 + 6)

# -
print(5-5)
print(vade-12)
print(vade - ekVade)
print(36-6)

# *
print(5*5)
print(vade * 2)
print(vade * ekVade)
print(10*10)

# /
print(5/5)
print(vade / 2)
print(vade / ekVade)
print(10/2)


yeniVade = vade / 2
fiyat = 100
indirimliFiyat = fiyat - 20

print(yeniVade)
print(indirimliFiyat)

# % => mod operatörü
print(10 % 2)
print(vade % 5)
print(vade % ekVade)
print(30 % 10)


#mantıksal operatörler
print(1 == 1) #sonuç true yada false olarak geliyor
print(1 == 2)

# CTRL K + CTRL C Birden fazla satırı yorum satırı yapmak için, yorum satırında çıkarmak için o satırlar seçili iken edit=>toggle line comment
print(1 > 2)
print(3 > 1)
print(1 > 1)
print(1 >= 1)

print(1 < 2)
print(3 < 1)
print(1 < 1)
print(1 <= 1) 


print(1 != 1) #sonuç istenilen durum sağlanıyorsa true, sağlanmıyorsa false 
print(1 != 2)

# or, and operatörleri
# and => ve : true olması için koşulların hepsinin doğru olması gerekmekte
# or => veya : true olması için birinin doğru olması yeterli
print(1 > 2 or 5 > 2)
print(1 > 2 and 5 > 2)
print(1 > 2 or 5 > 2 and 3 > 2)

print(1 > 2 and 5 > 2 and 3 > 2)

print(2 > 1 or 1 > 2 and 3 > 2)


# karar yapıları
# if else if  else yapıları (pythonda else if genel olarak elif olarak ele alınıyor )
sayi1 = 15
sayi2 = 15
# sayi1 sayi2'den büyükse ekrana sayi1 daha büyük yazdır
#condition : şart

#indent (girinti)
if sayi1 <= sayi2 :
    print("Sayi1 sayi2'den küçüktür.")
elif sayi1 == sayi2:
    print("İki sayı eşittir")
#eğer if ve else if bloklarından hiç birine girmez ise
else:
    print("Sayi1 sayi2'den büyüktür.")

print("*****************************************")

if sayi1 <= sayi2 :
    print("Sayi1 sayi2'den küçüktür.")
if sayi1 == sayi2:
    print("İki sayı eşittir.")
else:
    print("Sayi1 sayi2'den büyüktür.")

print("Burası if bloğunun dışıdır.")
