#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#a-28*28 bıyutlarında içeriği 0 ve 1 olan bir matris üretiniz.
#b- a'da üretilen matristebirleri içeren MBR dikdörtgeni üreten fonksiyonu yazınız.
#c- kendisine aktarılan 2 vektörün benzerliğini return eden fonksiyonu yazınız
#d- a şıkkında yazdığımız fonksiyonu kullanarak 100 farklı matris elde edin birinci üretilen ile diğerlerini karşılaştırıp yakınlığını ve benzerliğini listeleyiniz


# In[ ]:


#a da 29*28 lik 0 ve 1 olan bir matris
# b'de matrisi alıp 1 leri içeren en küçük dikdörtgeni geri döndürecek
# def my(a,b) skaler çarpoım verecek
#d a fonk 100 kere çağıracak ve 100 sayıyı 1 ile karşılaştırıp c ile karşılaştıracak


# In[ ]:





# In[21]:


import matplotlib.pyplot as plt
import numpy as np
import random as random

def my_create_m():
    matris=np.random.randint(0,2,(28,28))
    return matris


# In[22]:


print(my_create_m())


# In[27]:


def MBR_create_28_by_28_with_0_1(matris_a):
    m=matris_a.shape[0]
    n=matris_a.shape[1]
    x_min=m
    x_max=0    #başlangıç değerleri olası en olumsuz durum
    y_min=n
    y_max=0
    for i in range(m):
        for j in range(n):
            if (matris_a[i,j]==1 and x_min>i):    # resim/matris üzerinden 
                x_min=i                          # x_min, .... güncelleniyor
            if (matris_a[i,j]==1 and x_max<i):
                x_max=i
            if (matris_a[i,j]==1 and y_min>j):
                y_min=j
            if (matris_a[i,j]==1 and y_max<j):
                y_max=j
    return (x_min,x_max,y_min,y_max)


# In[41]:


def get_similarity(character_a,character_b):
    m=character_a.shape[0]
    n=character_a.shape[1]
    my_similarity=0
    for i in range(m):
        for j in range(n):
            my_similarity=my_similarity+character_a[i,j]*character_b[i,j]
    return my_similarity


# In[36]:


MBR_create_28_by_28_with_0_1(my_create_m())


# In[40]:


print(get_similarity(my_create_m(),my_create_m()))


# In[50]:


a=my_create_m()
plt.imshow(a, cmap='gray')
plt.show()
max=0
for i in range(99):
    b=my_create_m()
    #print(get_similarity(a,b))
    if(get_similarity(a,b)>max):
        max=get_similarity(a,b)
        c=b
plt.imshow(b, cmap='gray')
plt.show()
print("En yüksek benzerlik :", max)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




