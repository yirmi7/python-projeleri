# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 10:05:42 2020

@author: furkan
"""

"""
taş kağıt makas denemesi
"""

"""
kullanıcıdan veri al (tamamlandı)
veriyi değerlendir (tamamlandı)
random sayıları tanımla (tamamlandı)
bilgisayarla kullanıcıyı karşılaştır (tamamlandı)
skor sistemini düzenle (tamamlandı)
tekrar ve çıkış menüsü yaz (tamamlandı)
"""
skor = 0
import time
print("oyun başlıyor. 2 saniye bekle")
time.sleep(2)

def oyun():
    
    global skor
    import random
    import time
    
    kullanc=int(input("taş kağıt makas ? (taş : 1 - kağıt : 2 - makas : 3) : "))

    if kullanc < 1 or kullanc > 3:
        print("hatalı seçim. tekrardan seç !")
        time.sleep(1)
        while kullanc < 1 or kullanc > 3:
            kullanc=int(input("taş : 1 - kağıt : 2 - makas : 3 : "))
            continue
        
    elif kullanc == 1:
        print("")
        kullanc = 1
        time.sleep(1)
                                
    elif kullanc == 2:
        print("")
        kullanc = 2
        time.sleep(1)

    elif kullanc == 3:
        print("")
        kullanc = 3
        time.sleep(1)
    
    liste=[]
    liste.append(random.randint(1,3))    
    bilgisayar = liste[0]
    if bilgisayar == 1:
        print("bilgisayar taş seçti")
        time.sleep(1)
        if kullanc == 1:
            print("")
            print("sen taş seçtin")
            time.sleep(1)
            print("berabere. 1 puan kazandın")
            time.sleep(1)
            liste=[]
            skor +=1
        if kullanc == 2:
            print("")
            print(("sen kağıt seçtin"))
            time.sleep(1)
            print("sen kazandın. 3 puan kazandın")
            time.sleep(1)
            liste=[]
            skor +=3
        if kullanc == 3:
            print("")
            print(("sen makas seçtin"))
            time.sleep(1)
            print("kaybettin. puan kazanamadın")
            time.sleep(1)
            liste=[]

    if bilgisayar == 2:
        print("bilgisayar kağıt seçti")
        time.sleep(1)
        if kullanc == 1:
            print("")
            print("sen taş seçtin")
            time.sleep(1)
            print("kaybettin. puan kazanamadın")
            time.sleep(1)
            liste=[]
        if kullanc == 2:
            print("")
            print(("sen kağıt seçtin"))
            time.sleep(1)
            print("berabere. 1 puan kazandın")
            time.sleep(1)
            liste=[]
            skor +=1
        if kullanc == 3:
            print("")
            print(("sen makas seçtin"))
            time.sleep(1)
            print("sen kazandın. 3 puan kazandın")
            time.sleep(1)
            liste=[]
            skor +=3

    if bilgisayar == 3:
        print("bilgisayar makas seçti")
        time.sleep(1)
        if kullanc == 1:
            print("")
            print("sen taş seçtin")
            time.sleep(1)
            print("sen kazandın. 3 puan kazandın")
            time.sleep(1)
            liste=[]
            skor +=3
        if kullanc == 2:
            print("")
            print(("sen kağıt seçtin"))
            time.sleep(1)
            print("kaybettin. puan kazanamadın")
            time.sleep(1)
            liste=[]
        if kullanc == 3:
            print("")
            print(("sen makas seçtin"))
            time.sleep(1)
            print("berabere. 1 puan kazandın")
            time.sleep(1)
            liste=[]
    
    print("")
    print(skor, "puanın var ")
    print("")
    time.sleep(1)
    karar = input("tekrar oynamak için 'e' harfine, çıkmak için herhangi bir tuşa bas ve enterla :")
    if karar == "e":
        print("")
        print("ortalık toparlanıyor lütfen 2 saniye bekle")
        time.sleep(2)
        oyun()
    
    else:
        print("")
        print("sonlandırmak istedin. etrafı toparlıyorum biraz bekle")
        time.sleep(2)
        son()
    
def son():
    global skor
    print("")
    print(skor, "puan aldın")
    

oyun()
