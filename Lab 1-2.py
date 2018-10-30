#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

liste=[0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1]

for i in liste:
    print(int(i)+1)
    
for i in rane(0,len(liste)):
    liste[i]=liste[i]+1


# In[9]:


import matplotlib.pyplot as plt

im1= plt.imread("1.jpg")
im1.setflags(write=1)
plt.imshow(im1)
plt.show()
im1.shape

type(im1)
im1[:,:,2]=im1[:,:,2]+100

plt.imshow(im1)
plt.show()
def fonk1(image_1):
    print("Resmin boyutu = ",image_1.ndim,"\n") 
    print("Resmin Shape değeri = ",image_1.shape,"\n")
    print("Red için min değer = ",image_1[:,:,0].min(),"\n") #':' hangi yerde kullanıldıysa oranın tamamından bahsediyor örneğin burada tüm satırlar ve sütünlar
    print("Red için max değer = ",image_1[:,:,0].max(),"\n") # şuan kırmızı için olan değerlere bakıyoruz 1 olsa yeşil 2 olursa mavi
    
fonk1(im1)


# In[ ]:





# In[ ]:




