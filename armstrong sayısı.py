# -*- coding: utf-8 -*-
"""
Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.

Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin
4. kuvvetinin toplamı( 3 basamaklı sayılar için 3.kuvveti ) 
o sayıya eşitse bu sayıya "Armstrong" sayısı denir.

Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4
"""

sayi = (input("bir sayı gir :"))
liste = list(sayi)
basamak = len(liste)
toplam = 0
for i in liste :
    toplam += int(i)**basamak

print(toplam)
if toplam == int(sayi) :
    print("\n{} sayısı armstrong sayısı".format(int(sayi)))
else :
    print("\n{} sayısı armstrong sayısı değil".format(int(sayi)))
    