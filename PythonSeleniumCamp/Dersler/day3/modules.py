#alias (takma ad)
#import matematik  as m # Başka bir dosyadan bir kod bloğu, alan kullanabilmek için o modulü import etmemiz lazım print(m.topla(10,20))
# built-in modules
from matematik import topla as toplamaIslemi #matematik modülünden hangi alanı/alanları kullanıcaksan 
from day2 import sayHello
from day3 import Human
from human import Human
import random # rastgele sayı üretebildiğimiz bir modül
from selenium import webdriver
#package

print(toplamaIslemi(10,20))

print(random.randint(0,100)) # 0 ile 100 dahil

human1 = Human("Mirza")
human1.talk("Merhaba")

chromeDriver = webdriver.Chrome()
#packages