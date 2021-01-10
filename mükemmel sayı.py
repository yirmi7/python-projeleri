sayi = int(input("bir sayı gir :"))
liste = []
toplam = 0

for i in range(1,sayi):
    if sayi % i == 0 :
        liste.append(i)
        print("{} sayısı {} sayısının böleni".format(i,sayi))
    else :
        print("{} sayısı {} sayısının böleni değil".format(i,sayi))
        
for i in liste:
    toplam += i


if toplam == sayi :
    print("\n{} sayısı mükemmel sayı".format(sayi))
else :
    print("\n{} sayısı mükemmel sayı değil".format(sayi))