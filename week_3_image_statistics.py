#!/usr/bin/env python
# coding: utf-8

# In[8]:


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
img=mpimg.imread('1.jpg')
get_ipython().run_line_magic('matplotlib', 'inline')

plt.subplot(1,2,1),plt.imshow(img)
plt.subplot(1,2,2),plt.imshow(255-img)    


# In[9]:


def my_histogram(image):
    
    my_H0={}
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if(image[i,j,0] in my_H0.keys()):
                my_H0[image[i,j,0]]+=1
            else:
                my_H0[image[i,j,0]]=1
    
    my_H1={}
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if(image[i,j,1] in my_H1.keys()):
                my_H1[image[i,j,1]]+=1
            else:
                my_H1[image[i,j,1]]=1
    my_H2={}
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if(image[i,j,2] in my_H2.keys()):
                my_H2[image[i,j,2]]+=1
            else:
                my_H2[image[i,j,2]]=1
    return (my_H0,my_H1,my_H2)


# In[15]:


my_histogram2=my_histogram(img)

x=[]
y=[]
for i in my_histogram2[0].keys():
    x.append(i)
    y.append(my_histogram2[0][i])
plt.subplot(1,3,1),plt.plot(x,y, color='r')   

x=[]
y=[]
for i in my_histogram2[1].keys():
    x.append(i)
    y.append(my_histogram2[1][i])
plt.subplot(1,3,2),plt.plot(x,y, color='g') 

x=[]
y=[]
for i in my_histogram2[2].keys():
    x.append(i)
    y.append(my_histogram2[2][i])
plt.subplot(1,3,3),plt.plot(x,y, color='b') 


# In[ ]:




