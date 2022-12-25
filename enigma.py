import random
from datetime import datetime
import pyfiglet
from colorama import init, Fore, Back, Style

init(autoreset=True)
ascii_banner = pyfiglet.figlet_format("Enigma          by   Libuntu")
print(Style.BRIGHT + Back.RED + Fore.WHITE + ascii_banner)

giris = True
while giris:
    time = datetime.now()
    saat = int(time.strftime("%H"))
    dakika = int(time.strftime("%M"))
    anlik_sifre = saat*dakika*31*13
    giris_sifre = int(input("Giriş Şifresi Nedir?: "))
    if giris_sifre==anlik_sifre:
        giris = False

if giris==False:
    print("Giriş Yapıldı! Enigmaya Hoşgeldiniz!")
    print(" ")
ayar_1 = int(input("Enigma Cihazının 1. Ayarını Giriniz!: "))
ayar_2 = int(input("Enigma Cihazının 2. Ayarını Giriniz!: "))
ayar_3 = int(input("Enigma Cihazının 3. Ayarını Giriniz!: "))
ayar_4 = int(input("Enigma Cihazının 4. Ayarını Giriniz!: "))
ayar_5 = int(input("Enigma Cihazının 5. Ayarını Giriniz!: "))
ayar_6 = int(input("Enigma Cihazının 6. Ayarını Giriniz!: "))
print("-"*50)
ayar = 1
while ayar==1:
    time = datetime.now()
    saat = int(time.strftime("%H"))
    yil = int(time.strftime("%Y"))
    genel_ayar = ayar_1*ayar_3/ayar_2*ayar_4/ayar_6*ayar_5/saat*yil
    normal_alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', " "]
    random.seed(genel_ayar)
    alph = random.sample(normal_alph, len(normal_alph))
    mesaj_var = 1

    while mesaj_var==1:
        mesaj = input("Mesajınız: ")
        print("-"*50)
        mesaj_list =[i for i in mesaj]
        sonuc = []
        tersine_sonuc = []
        index = 0

        for i in range(len(mesaj_list)):
            sonuc.append(alph[normal_alph.index(mesaj_list[index])])
            tersine_sonuc.append(normal_alph[alph.index(mesaj_list[index])])
            index += 1
        print("Şifrelenmiş Hali: ", "".join(map(str,sonuc)))
        print("Çözülmüş Hali: ", "".join(map(str,tersine_sonuc)))
        print("-"*50)
        mesaj_var = 0


    

