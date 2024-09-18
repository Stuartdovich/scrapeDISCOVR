#scrapeDISCOVR
#Webscraping script for DISCOVR data using json Python library.

#Realtime update of induced Electric field model using DISCOVR solar parameters. 

#Based on the paper "Regression-based forecast model of induced geoelectric field" (http://onlinelibrary.wiley.com/doi/10.1002/2016SW001518/full)
#Excerpt: 'Regression-based (i.e., empirical) model for quantitatively predicting the upper envelope of induced E field components, 
#using near-Earth measurements of solar wind plasma and magnetic field parameters as input arguments to the model'

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import numpy as np
import json
import urllib2
import csv

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

#Initialise arrays
x = []
score = []
pressure = np.zeros(11)

# Specify url
# Get date&time and Bt every 1 min
urlmag = 'http://services.swpc.noaa.gov/products/solar-wind/mag-5-minute.json'
# Get density and speed every 1 min
urlplas = 'http://services.swpc.noaa.gov/products/solar-wind/plasma-5-minute.json'


def animate(i):

    getmag = np.asarray(json.load(urllib2.urlopen(urlmag)))
    getplas = np.asarray(json.load(urllib2.urlopen(urlplas)))
    # extract mag
    Bt = float(getmag[2,6])	
    #extract density
    roh = float(getplas[2,1])	
    #extract speed
    Vsw = float(getplas[2,2])
    #determine Pd
    Pd = roh*Vsw**2
    # append data to keep delta_t-10
    np.append(pressure,Pd)
    # calculate electric field
    E_chi = 0.06*( Pd-pressure[-11] )**0.38 * Bt**0.39 * Vsw**0.51 - 0.53
    E_gamma = 0.06*( Pd-pressure[-11])**0.58 * Bt**0.38 * Vsw**0.55 - 0.85     
      
    x.append(i)
    score.append(E_chi)

    ax1.clear()
    ax1.plot(x, score)

ani = animation.FuncAnimation(fig, animate, interval=60000)
plt.show()






	
