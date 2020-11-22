import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import math
import random
import pylab
from itertools import combinations

##########################################################
class Agent():      

  def agents(self):   #speed and parameter
      self.speed=[round(random.uniform(0,3),2)] #speed between 0 and 3 with 2 decimal
      self.agent=[round(random.uniform(1,3),1)] #define a parameter that agent will be satified
      return self.speed, self.agent

  def maps(self,mapSize):
      self.x=[round(random.uniform(0,mapSize),2)]
      self.y=[round(random.uniform(0,mapSize),2)]
      return self.x, self.y

  def connection(self,pointNumber,mapSize):

      return
  
  
  
#####################################################
pointNumber=5
mapSize=200



positions=[]

positions=Agent().maps(mapSize)

print(positions[0])


for i in range(pointNumber):
  objects.maps(mapSize)
  print(objects)


fig = plt.figure(figsize=(16,8))
ax1 = fig.add_subplot(11)
ax1.set_ylim(0, mapSize) 
ax1.set_xlim(0, mapSize) 
colors = ['red','brown','orange','yellow','blue'] #5 attractions
attractions=['little red','little brown','little orange','little yellow','little blue']
plt.ion() #make code continue
fig.show() 


for p in range(pointNumber):
        
    ax1.plot(x[p],y[p], c=colors[p], label=f'attractions={attractions[p]}')
         
    ax1.scatter(x[p],y[p], c=colors[p])

ax1.plot(0,0, c='black', label=f'entry/exit') #entry/exit
         
ax1.scatter(0,0, c='black')
    

fig.canvas.draw()
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('map')
ax1.legend() 
