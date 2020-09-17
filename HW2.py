import matplotlib.pyplot as plt
import functools as ft
import numpy as np
import pandas as pd

#%% load data
measles = pd.read_csv('Measles.csv', header = None).values
mumps = pd.read_csv('Mumps.csv', header = None).values
chickenPox=pd.read_csv('chickenPox.csv', header = None).values

plt.close('all') # close all existing figures

#%%  Total number of measles cases in each year
measlesData = np.array(measles) # Convert to numpy array

# get years from measles data
years = measlesData[:,0] # All rows x 0th column
# create array for X-axis data
totalMeaslesCases = np.array(years[:]) 

# For each year add all columns from index 1 to 12; add Sum to a numpy array
for year in range(len(years)): 
    totalMeaslesCases[year] = ft.reduce(lambda x,y: x+y, measlesData[year, 1:12]) 

# Plot Measles data
plt.figure(1)
plt.title('Fig 1: NYC measles cases')
plt.xlabel('Year')
plt.ylabel('Number of cases')
plt.plot(years, totalMeaslesCases, 'b*-') 
plt.show()

#%%  Total number of measles and mumps cases in each year in logarithm scale

mumpsData = np.array(mumps) # Convert to numpy array
# Create array for X-axis data
totalMumpsCases = np.array(years[:])  

# For each year add all columns from index 1 to 12; add Sum to a numpy array
for year in range(len(years)):
    totalMumpsCases[year] = ft.reduce(lambda x,y: x+y, mumpsData[year, 1:12])

# Plot Measles and Mumps data
plt.figure(2)
plt.title('Fig 2: Measles and mumps cases in NYC')
plt.xlabel('Year')
plt.ylabel('Number of cases')
plt.yscale('log') # logarithmic scale the y-axis
plt.plot(years, totalMeaslesCases, 'bx-',
         years, totalMumpsCases, 'go:')
plt.legend(['Measles', 'Mumps'])
plt.show()

#%% Average number of mumps cases for each month of the year
sums = np.sum(mumpsData[:, 1:] , axis=0) # sum each column (month) along 0th axis
sums = sums / 41 # calculate average of each month

plt.figure(3)
plt.title('Fig 3: Average monthly mumps cases')
plt.xlabel('Months')
plt.ylabel('Average number of cases')
plt.bar(range(1,13), sums)
plt.show()

#%% Monthly mumps cases against the measles cases
plt.figure(4)
plt.title('Fig 4: Monthly mumps vs measles cases')
plt.xlabel('Number of Mumps cases')
plt.ylabel('Number of Measles cases')
plt.scatter(mumpsData[:, 1:], measlesData[:, 1: ])

#%% Monthly mumps cases against measles cases (Logarithmic scale)
plt.figure(5)
plt.title('Fig 5: Monthly mumps vs measles cases (log scale)')
plt.xlabel('Number of Mumps cases')
plt.ylabel('Number of Measles cases')
plt.xscale('log')
plt.yscale('log')
plt.scatter(mumpsData[:, 1:], measlesData[:, 1:])
plt.axis([10**1.5, 10**3.5, .5, 10**5])

