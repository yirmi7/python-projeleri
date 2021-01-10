"""
Her bir while döngüsünde kullanıcıdan bir sayı alın ve 
kullanıcının girdiği sayıları "toplam" isimli bir değişkene ekleyin. 
Kullanıcı "q" tuşuna bastığı zaman döngüyü sonlandırın ve 
ekrana "toplam değişkenini" bastırın.

İpucu : while döngüsünü sonsuz koşulla başlatın ve 
kullanıcı q'ya basarsa döngüyü break ile sonlandırın.
"""

toplam = 0

while True :
    sayi = (input("bir sayı gir veya çıkmak için q harfine bas : \n"))
    if sayi != "q" :
        toplam += int(sayi)
    else :
        break
    
print("\ntoplam : {}".format(toplam))