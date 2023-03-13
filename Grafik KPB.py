#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as Axes3D


# In[3]:


# Persamaan Garis y = mx
m = float(input("masukan gradien garis "))
n = 100
x = np.linspace(-5,5, n)

y = x

plt.grid()
plt.plot(x,y)
plt.xlim((-5,5))
plt.ylim((-5,5))
plt.show()


# In[4]:


# Persamaan Kuadrat y = mx^2 + c
m = float(input("masukan koefisien x^2 (m) "))
c = float(input("masukan nilai kostan c "))
n = 100
x = np.linspace(-5,5, n)

y = (m*x**2) + c

plt.grid()
plt.plot(x,y)
plt.xlim((-5,5))
plt.ylim((-1,25))
plt.show()


# In[5]:


# Persamaan Kuadrat y = akar x
n = 100
x = np.linspace(-5,5, n)

y = np.sqrt(x)

plt.axis('equal')
plt.grid()
plt.plot(x,y)
plt.show()


# In[6]:


# Persamaan Trigonometri
# y = sin x
n = 1000
m = float(input("Masukan konstanta pi: "))
x = np.linspace(-m*np.pi,m*np.pi, n)

y = np.sin(x)

plt.grid()
plt.plot(x,y)
plt.xlim((-m*np.pi, m*np.pi))
plt.ylim((-1.5, 1.5))
plt.show()


# In[7]:


# Persamaan Trigonometri
# y = cos x
n = 1000
m = float(input("Masukan konstanta pi: "))
x = np.linspace(-m*np.pi,m*np.pi, n)

y = np.cos(x)

#plt.axis('equal')
plt.grid()
plt.plot(x,y)
plt.xlim((-m*np.pi, m*np.pi))
plt.ylim((-1.5, 1.5))
plt.show()


# In[8]:


m = float(input("Masukan konstanta pi: "))
x = np.linspace(-m*np.pi,m*np.pi, n)

y = np.tan(x)

#plt.axis('equal')
plt.grid()
plt.plot(x,y)
plt.xlim((-m*np.pi, m*np.pi))
plt.ylim((-3, 3))
plt.show()


# In[9]:


# Persamaan Lingkaran dengan Parameter t
r = float(input("Masukkan jari-jari lingkaran "))
n = 100
t = np.linspace(0,2*np.pi, n)

x = r*np.cos(t)
y = r*np.sin(t)

plt.axis('equal')
plt.grid()
plt.plot(x,y)
plt.show()


# In[11]:


# Persamaan Lingkaran x^2 + y^2 = r^2
r = float(input("Masukkan jari-jari lingkaran "))
n = 100
x = np.linspace(-r-1,r+1, n)

y = np.sqrt(r**2-x**2)
y1 = -np.sqrt(r**2-x**2)

plt.axis('equal')
plt.grid('equal')
plt.plot(x,y,x,y1)
plt.show()


# In[13]:


a = float(input("Jari-jari lingkaran adalah "))
t = np.linspace(0, 10* np.pi, 100)

x = a*t - a*np.sin(t)
y = a - a*np.cos(t)

plt.grid()
plt.plot(x,y)
plt.xlim((0,10*np.pi))
plt.ylim((-1, a+2))
plt.show()


# In[24]:


# Persamaan Hiposikloid
a = float(input("Jari-jari lingkaran besar adalah "))
b = float(input("Jari-jari lingkaran kecil adalah "))
t = np.linspace(0, 10* np.pi, 100)

x = (a-b)*np.cos(t) + b*np.cos(((a-b)/b)*t)
y = (a-b)*np.sin(t) + b*np.sin(((a-b)/b)*t)

plt.axis('equal')
plt.grid()
plt.plot(x,y)
#plt.xlim((-a,a))
#plt.ylim((-a,a))
plt.show()


# # 

# In[25]:


# Persamaan Helix
r = 1
t = np.linspace(0, 10* np.pi, 100)
# Parameter
x = r* np.cos(t)
y = r* np.sin(t)
z = t

# Pengaturan figure
fig = plt.figure('Parametric curves')
ax = fig.add_subplot(111, projection= '3d')

# Plot
ax.plot(x, y, z, '-r', linewidth = 3)

# Label koordinat
ax.set_xlabel('X', fontweight = 'bold', fontsize = 14)
ax.set_xlabel('Y', fontweight = 'bold', fontsize = 14)
ax.set_xlabel('Z', fontweight = 'bold', fontsize = 14)

#Judul
plt.title('Parametric Curve', fontweight = 'bold', fontsize = 16)

plt.show()


# In[ ]:




