import matplotlib.pyplot as plt
import numpy as np


#%% load data
import pandas as pd 
measles=pd.read_csv('Measles.csv',header=None).values
mumps=pd.read_csv('Mumps.csv',header=None).values
chickenPox=pd.read_csv('chickenPox.csv',header=None).values

# close all existing floating figures
plt.close('all')

#%% Q1. plot annual total measles cases in each year

plt.figure()
plt.title('Fig 1: NYC measles cases')

# complete this part

plt.show()

#%% Q2 plot annual total measels and mumps cases in log scale

plt.figure()
plt.title('Fig 2: Measles and mumps cases in NYC')

# complete this part

plt.show()

#%% Q3 plot average mumps cases for each month of the year

plt.figure()
plt.title('Fig 3: Average monthly mumps cases')

# complete this part

plt.show()


#%% Q4 plot monthly mumps cases against measles cases 
mumpsCases = mumps[:, 1:].reshape(41*12)
measlesCases = measles[:, 1:].reshape(41*12)

plt.figure()
plt.title('Fig 4: Monthly mumps vs measles cases')

# complete this part

plt.show()


#%% Q5 plot monthly mumps cases against measles cases in log scale
plt.figure()
plt.title('Fig 5: Monthly mumps vs measles cases (log scale)')

# complete this part

plt.show()


#%% Q6 plot annual total chicken pox cases in each year

plt.figure()
plt.title('Fig 6: NYC chicken pox cases')

# complete this part

plt.show()
