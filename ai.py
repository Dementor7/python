#!/bin/python3

import matplotlib.pyplot as plt 
import numpy as np 

x = np.array(['PhoneTime','LaptopTime','EatTime','YoutubeTime','SleepingTime','RoundTime' ,'HomeWork'])
y = np.array([3,5,1,3,9,1,2])
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'red','size':20}
font3 = {'family':'serif','color':'green','size':20}
plt.title("Life_Of_Lv7",fontdict=font1)
plt.xlabel('LifeTime',fontdict=font2)
plt.ylabel('hours',fontdict=font3)
plt.bar(x,y)
plt.show()


