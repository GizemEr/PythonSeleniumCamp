#1 - Python'da veri tiplerini araştırınız :

#Veri tipi çeşitleri : 

# string : str, Metinsel verilerin, yazı ver karakter, tutulduğu veri tipidir. 
# string = "Python"

# int : integer, Tam sayıların tutulduğu veri tipidir.
# int = 10

# float : Ondalıklı sayıların tutulduğu veri tipidir.
# float = 10.8

# complex : Karmaşık sayılar için kullanılan veri tipidir.
# complex = 1 + i

# boolean : Sadece true yada false değerleri için kullanılabilir. 
# boolean = True

# list : Dizi halindeki veriler için kullanılır. (Sıralı, Değiştirilebilir, farklı tip veri tutabilir.)
# list = ["p","y","t","h","o","n"]

# tuple : Dizi halindeki veriler için kullanılır. (Sıralı, Değiştirilemez, farklı tip veri tutabilir.)
# tuple = ("s","e","l","e","n","i","u","m")

# range : Aralık belirtmek için kullanılan veri tipidir.(Diziler içerisinde yer alır.)
# range = range(2,8)

#2 - Kodlama.io sitesinde değişken olarak düşündüğünüz verileri, veri tipleriyle birlikte örneklendiriniz.

# string : Kurslarım, Tüm Kurslar, Kariyer, Sık Sorulan Sorular kısmı için string kullanılmıştır.
# integer : Kursların tamamlanma oranları yani sayılar için in veri tipi kullanılmıştır.
# list : Kategori ve eğitmen kısımları için kullanılmıştır.

#3 - Kodlama.io sitesinde şart blokları kullanıldığını düşündüğünüz kısımları örneklendiriniz ve Python dilinde bu örnekleri koda dökünüz.

#Kodlama.io sitesine giriş yaparken mail ve şifre istenmektedir. 

mail = input("Lütfen mail adresinizi giriniz.")
sifre = input("Lütfen şifrenizi giriniz.")
#input() fonksiyonu kullanıcıdan bilgi almak için kullanılır.

if mail == ("abc@mail.com") and sifre == (12345):
   print("Giriş başarılı")
else :
   print("Giriş başarısız")

#Ayrıca eğitmenler kategorisi için 
egitmen = input("Lütfen eğitmen seçiniz")
if egitmen == ("Engin Demiroğ"):
   print("Java", "C#", "JavaScript", ".NET")
elif egitmen == ("Halit Enes Kalaycı"):
   print("Python")
else:
   print("Java", "C#", "JavaScript", ".NET", "Python")



