#Listeler
krediler = ["Hızlı Kredi","Maaşını Halkbank'tan alanlara özel","Mutlu emekli ihtiyaç kredisi"] #köşeli parantez görünce liste olduğunu bilicez
#Bir çok programlama dilinde diziler 0'dan başlar
print(krediler)
print(krediler[0])
print(krediler[1])
print(krediler[2])

print(len(krediler)) #len = lenght listenin kaç elemandan oluştuğunun bilgisini verir

krediler[0] = "Çabuk kredi" #kredilerin 0. elamanına atama yapmış olduk
print(krediler)

print(krediler[2])

print("*************************")

#Döngüler : bizim birbirine benzeyen işleri tekrar etmememiz için kullandığımız yapılardır.
krediler = ["Hızlı Kredi","Maaşını Halkbank'tan alanlara özel","Mutlu emekli ihtiyaç kredisi"]

for kredi in krediler : #for bir döngü çeşididir, en çok kullanılandır/ kredi yazan yere istenilen isim verilebilir o kısım takma addır(alias)
    print("<option>"+kredi+"<option>")

for i in range(len(krediler)) :
    print (krediler[i])

for i in range(3,10): #saymaya 3'ten başla demek, 3 dahil 10 dahil değil!
    print(i)

for i in range(0,11,2): #0'dan başla 10'a kadar, 11 dahil değil, 2'şer arttır
    print(i)