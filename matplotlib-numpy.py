#!/bin/python3.8

import numpy as np 
import matplotlib.pyplot as plt 

#1st plot
x = np.array(['front-end','back-end','full-stack','pentesting','error-fixing','system-skill'])
y = np.array([ 80,50,60,75,70,90])

plt.subplot(1,2,1)
plt.bar(x,y)

plt.title('welcome') 

#second plot

x = np.array(['hello_world','linux','windows', 'vscode' , 'games' , 'youtube'])
y = np.array([10,20,30,40,50,60])
plt.subplot(1,2,2)
plt.bar(x,y)
plt.title('nothing')

plt.show()
