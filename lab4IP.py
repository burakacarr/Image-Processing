#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
im1=plt.imread("1.jpg")
im1.setflags(write=1) # resim sadece read-only özelliğine sahipti üzerinde değişiklik yapabilmek için değiştirdim
get_ipython().run_line_magic('matplotlib', 'inline')
plt.imshow(im1)
plt.show()


# In[2]:


def get_distance(v,w=[1/3,1/3,1/3]):   #w ağırlık değeri
    a,b,c=v[0],v[1],v[2]
    w1,w2,w3=w[0],w[1],w[2]
    #d=((a*w1)**2+(b*w2)**2+(c*w3)**2)**.5 #sqrt işlemi var
    d=((a**2)*w1+(b**2)*w2+(c**2)*w3)**.5
    return d


# In[3]:


my_RGB=[1,2,3]
gray_level=get_distance(my_RGB)
print(gray_level)


# In[4]:



my_RGB=[10,20,3]
gray_level=get_distance(my_RGB,[.6,.3,.1])
print(gray_level)


# In[5]:


#hocanın convert kodu
def convert_rgb_to_gray_level(im_1):
    m=im_1.shape[0]
    n=im_1.shape[1]
    im_2=np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            im_2[i,j]=get_distance(im_1[i,j,:])
    return im_2


# In[6]:



im2=convert_rgb_to_gray_level(im1)
type(im2)
im1.shape,im2.shape


# In[12]:



plt.imshow(im2,cmap='gray')
plt.show()


# In[8]:


def convert_rgb_to_BW(image_gray_level):
    m=image_gray_level.shape[0]
    n=image_gray_level.shape[1]
    im_bw=np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            if image_gray_level[i,j]>120:
                im_bw[i,j]=1
            else:
                im_bw[i,j]=0
    return im_bw


# In[20]:


im3=convert_rgb_to_BW(im2)


# In[10]:



plt.subplot(1,3,1),plt.imshow(im1)
plt.subplot(1,3,2),plt.imshow(im2,cmap='gray')
plt.subplot(1,3,3),plt.imshow(im3,cmap='gray')  #histogram ödev kendin bak


# In[ ]:



plt.imshow(im3,cmap='gray')
plt.show()


# In[21]:


#black-white yapma kodu : denemelerim


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
from scipy import misc
import matplotlib.pyplot as plt

image=im1
x,y,z=image.shape
image[:] = image.mean(axis=-1,keepdims=1) 

plt.figure(figsize=(10,20))
plt.imshow(image)

photo_data = misc.imread("1.jpg")
photo_data[495:505,390:405]


for i in range(x):
    for j in range(y):
        if (photo_data[i,j,0]<210 and photo_data[i,j,1]<160):
            photo_data[i,j]= np.mean(photo_data[i,j])
plt.imshow(photo_data)


# In[ ]:




