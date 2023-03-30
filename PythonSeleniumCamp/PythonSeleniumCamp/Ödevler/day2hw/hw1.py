# ÖDEV TANIMI:
# Bir öğrenci kayıt sistemi yazdığımızı düşünelim. Sistemimizdeki öğrencileri bir listede sadece ad soyad olacak şekilde tutalım.
# Bu öğrenci kayıt sistemine;
# -Aldığı isim soy isim ile listeye öğrenci ekleyen
# -Aldığı isim soy isim ile eşleşen değeri listeden kaldıran
# -Listeye birden fazla öğrenci eklemeyi mümkün kılan
# -Listedeki tüm öğrencileri tek tek ekrana yazdıran
# -Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan
# -Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız)
# Fonksiyonları geliştiriniz ve her bir fonksiyonu en az bir kere çağırarak konsolda test ediniz.
# Ödevde kullanacağınız döngülerin bir tanesi for bir tanesi while döngüsü olması istenmektedir.

ogrenciler = []
    
def ogrenciEkle():
    ogrenci = (input("Lütfen öğrencinin ad ve soyadını giriniz : "))
    ogrenciler.append(ogrenci)
    print("Öğrenci listeye eklendi.")
    print(ogrenciler)

def ogrenciSilme():
    ogrenci = (input("Lütfen öğrencinin ad ve soyadını giriniz : "))
    if ogrenci in ogrenciler:
       ogrenciler.remove(ogrenci)
       print("Öğrenci listeden silindi.")
    else :
        print("Öğrenci listede bulunamadı")

def ogrenciTopluEkle():
    while True:
        ogrenci = input("Öğrencinin ad ve soyadını giriniz, daha fazla öğrenci eklemeyecekseniz bitir yazınız. ")
        if ogrenci == "bitir":
            break
        ogrenciler.append(ogrenci)
    print("Öğrenciler listeye eklendi.")
    print(ogrenciler)

def ogrenciListele():
    if len(ogrenciler) !=0:
      for ogrenci in ogrenciler:
          print(ogrenci)
    else : 
        print("Listede öğrenci bulunmamaktadır.")

def ogrenciNoBul() :
    ogrenci = str(input("Lütfen numarasını öğrenmek istediğiniz öğrencinin ad ve soyadını giriniz : "))
    i = 0
    while i <= len(ogrenciler):
        if ogrenciler[i] == ogrenci :
            print(i, ogrenciler[i])
            break
        i +=1

def ogrenciTopluSil():
    while True:
        ogrenci = input("Silmek istediğiniz öğrencinin adını yazınız, daha fazla öğrenci silmek istemiyorsanız bitir yazınız. ")
        if ogrenci == "bitir" :
            break
        ogrenciler.remove(ogrenci)
    print("Öğrenciler listeden silindi.")
    print(ogrenciler)


while True:
    print("Öğrenci Kayıt Sistemi : 1- Öğrenci Ekle, 2- Öğrenci Silme, 3- Birden Fazla Öğrenci Ekleme, 4- Tüm öğrencileri listele, 5- Öğrenci Numarası Öğrenme, 6-Birden Fazla Öğrenci Silme, 0-Programdan çıkış")
    choice = int(input("Yapmak istediğiniz işlemi seçiniz : "))

    if choice == 1:
        ogrenciEkle()
    elif choice == 2:
        ogrenciSilme()
    elif choice == 3:
        ogrenciTopluEkle()
    elif choice == 4:
        ogrenciListele()
    elif choice == 5:
        ogrenciNoBul()
    elif choice == 6:
        ogrenciTopluSil()
    elif choice == 0:
        break
    else :
        print("Geçersiz seçim, lütfen tekrar deneyin.")
    