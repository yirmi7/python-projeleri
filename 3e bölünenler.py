# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 17:19:17 2021

@author: furkan



1'den 100'e kadar olan sayılardan sadece 3'e bölünen sayıları ekrana bastırın. 
Bu işlemi continue ile yapmaya çalışın.
"""

for i in range(1,101) :
    if i % 3 == 0 :
        print("{} sayısı 3 sayısına tam bölünüyor".format(i))
    else :
        continue

