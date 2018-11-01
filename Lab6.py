#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np  #resmimizi gray level daha sonra bw aktarıcaz   t için e - 6   t için i - 2
import matplotlib.pyplot as plt
image=plt.imread("2.png")
plt.imshow(image)
plt.show()


# In[2]:


def get_distance(v,w=[1/3,1/3,1/3]):
    a,b,c=v[0],v[1],v[2]
    w1,w2,w3=w[0],w[1],w[2]
    d=((a**2)*w1+(b**2)*w2+(c**2)*w3)**.5
    return d


# In[3]:


def convert_rgb_to_gray_level(image):
    m=image.shape[0]
    n=image.shape[1]
    image2=np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            image2[i,j]=get_distance(image[i,j,:])
    return image2
im1=convert_rgb_to_gray_level(image)
plt.imshow(im1,cmap='gray')
plt.show()


# In[4]:


def convert_rgb_to_bw(image):
    m=image.shape[0]
    n=image.shape[1]
    image_bw=np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            if(image[i,j]==0):
                image_bw[i,j]=0
            else:
                image_bw[i,j]=1
    return image_bw
im2=convert_rgb_to_bw(im1)
plt.imshow(im2,cmap='gray')
plt.show()


# In[5]:


def pixel_compenent(image):
    m=image.shape[0]
    n=image.shape[1]
    internal=0
    external=0
    for i in range(1,m-1):
        for j in range(1,n-1):
            poi=image[i:i+2,j:j+2]
            white=0
            black=0
            for k in range(2):
                for l in range(2):
                    if poi[k,l]==1:
                        white=white+1
                    else:
                        black=black+1
            if(black>white and white>0):
                internal=internal+1
            elif(white>black and black>0):
                external= external+1
    print("dış kenar ",external)
    print("iç kenar ",internal)
    print("Nesne sayisi",(external-internal)/4)


# In[6]:


pixel_compenent(im2)


# In[7]:


def pixel_compenent2(resim):     #evde pixel compenenti ayrı fonksiyon yap ayır daha güzel olur
    m=resim.shape[0]   # siyah 0  beyaz 1 
    n=resim.shape[1]
    external=0
    internal=0
    for i in range (1,m-1):
        for j in range(1,n-1):
            poi=resim[i:i+2,j:j+2]
            siyah=0
            beyaz=0
            for k in range(2):
                for l in range(2):
                    if poi[k][l]==1:
                        beyaz=beyaz+1
                    else:
                        siyah=siyah+1
            if(siyah>beyaz and beyaz>0):
                internal=internal+1
            elif(beyaz>siyah and siyah>0):
                external=external+1
                
    print("dış kenar ",external)
    print("iç kenar ",internal)
    print("Nesne sayisi",(external-internal)/4)


# In[8]:


pixel_compenent2(im2)


# In[10]:


im=plt.imread("adsız.png")
im3=convert_rgb_to_gray_level(im)
ima=convert_rgb_to_bw(im3)
pixel_compenent(ima)


# In[ ]:




