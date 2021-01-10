# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 17:25:22 2021

@author: furkan
"""
"""
Buradaki problemin çözümünü derslerimizde özellikle öğrenmedik. 
Burada mantık yürüterek ve 
list comprehension kullanarak 1'den 100'e kadar olan sayılardan 
sadece çift sayıları bir listeye atmayı yapmayı çalışın.

Not: Programlamada her detayı öğrenemeyiz. 
Bunun için bazı yerlerde deneme yanılma yoluyla da öğrendiğimiz şeyler olur. 
Bu problemde deneme yanılma yoluyla 
list comprehension'ın koşullu durumlarla kullanımını öğreneceksiniz.

İpucu: Basit düşünmeye çalışın.
"""

liste = list(range(1,101))
liste2 = [i for i in liste if i%2 == 0 ]
print(liste2)