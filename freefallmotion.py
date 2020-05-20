import matplotlib.pyplot as plt
from PIL import Image
import glob
import os.path
import math 
#Inisialisasi Variable
v0 = 0
t0 = 0
g = -9.8
y0 = 100
delta_t = 0.01

TimesOfNumerik = []
PlotsOfNumerik = []
TimesOfAnalitik= []
PlotsOfAnalitik = []

V = 0
y = y0
t = 0
while y > 0 :
    V = V + (g * delta_t) #Kecepatan
    y = y + (V * delta_t) #Posisi
    PlotsOfNumerik.append(y)
    TimesOfNumerik.append(t)
    t+=delta_t
# Analitik
y = y0
t = 0
while y > 0 :
    y = y0 + (0.5 * g * t  * t)
    PlotsOfAnalitik.append(y)
    TimesOfAnalitik.append(t)
    t+=delta_t

timeNumerik = TimesOfNumerik[len(TimesOfNumerik)-1] #Menampilkan waktu ketika menyentuh tanah
timeAnalitik = TimesOfAnalitik[len(TimesOfAnalitik)-1] #Menampilkan waktu ketika menyentuh tanah
plt.xlabel('Time') #Label pada axis X
plt.ylabel('Height') #Label pada axis Y
plt.plot(TimesOfAnalitik, PlotsOfAnalitik,'r')
plt.plot(TimesOfNumerik, PlotsOfNumerik,'b')
plt.legend(['Analitik Time {}s'.format(timeAnalitik),'Numerik Time {}s'.format(timeNumerik)], loc = 'upper right')
plt.ylim(0,y0+10)
plt.show()