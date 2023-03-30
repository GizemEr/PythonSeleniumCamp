class Human : # Bir class içerisinde fonksiyon kullanıyorsak self parametresini kullanıcaz. İsmi self olarak vermek zorunda değiliz humanObj vs de diyebilirdik. 
    #name = "Gizem" init olan kısma self yanına name ile sonraki satıra self.name = name yazdığımızda artık bu name'e ihtiyacımız olmaz
    # built-in 
    # constructor : yapıcı
    # initialize
    def __init__(self,name):
        self.name = name #self'in içine name alanını at, değerini de gelen name yap
        print("Bir human instance'i üretildi")
    def __str__(self) :
        return f"STR Fonksiyonundan dönen değer: {self.name}"
    def talk(self,sentence): # Burada bizim verdiğimiz ilk alanı self'ten sonraki kısma vererek parametre sıranızı o şekilde devam ettiricektir.
        #name = "Ercan" 
        print(f"{self.name}: {sentence}") #name kısmına self verirsem Gizem'i vermezsem Ercan'ı görür
    def walk(self):
        print(f"{self.name} is walking..")