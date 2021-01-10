sayi = int(input("sayı gir : "))
sayi2 = int(input("sayı gir : ")) 

for i in range(sayi,sayi2 + 1):
   if i > 1:
       for j in range(2,i):
           if (i % j) == 0:
               break
       else:
           print(i)
