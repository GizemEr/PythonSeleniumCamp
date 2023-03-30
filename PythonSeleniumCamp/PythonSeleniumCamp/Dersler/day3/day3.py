# sınıflar => classlar
# modules
# paket yönetimi


# instance => örnek
from human import Human


human1 = Human("Enes")
#human1.name = "Enes" #Eğer self kalırsa Enes yazar, self kalmazsa Ercan yazar, talk fonk. üstünde olması önemli 
human1.talk("Merhaba")
human1.walk()
print(human1)


human2 = Human("Halit") #ben burada isim belirtmezsem parametre yollanmadığı için hata alırız
human2.talk("Selam")
human2.walk()
print(human2)