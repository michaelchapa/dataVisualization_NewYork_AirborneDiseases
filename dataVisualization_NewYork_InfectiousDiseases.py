import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

font = {'family': 'lucinda', 
        'color':  'black',
        'weight': 'normal', 
        'size': 14
        }

def plot_Line_Cases_Years(disease, diseaseName):
    years = disease.index.values
    totals = disease.sum(axis = 1)
    
    plt.figure()
    plt.title('New York ' + diseaseName + ' cases', fontdict = font)
    plt.xlabel('Years')
    plt.ylabel('Total cases')
    plt.bar(years, totals)
    plt.show()

def plot_Line_Log_Cases_Years(disease1, disease2, names):
    years = disease1.index.values
    disease1Totals = disease1.sum(axis = 1)
    disease2Totals = disease2.sum(axis = 1)
    
    plt.figure()
    plt.title(names[0] + ' and ' + names[1] + ' cases in New York City')
    plt.xlabel('Year')
    plt.ylabel('Total cases')
    plt.yscale('log')
    plt.plot(years, disease1Totals, 'b.-', 
             years, disease2Totals, 'r.-')
    plt.legend(names)
    plt.show()
    
def plot_Bar_Cases_Month(disease, name):
    months = disease.columns.values
    monthAvgs = disease.mean()
    
    plt.figure()
    plt.title(name + ' Average cases by Month (1931 - 1971)', fontdict = font)
    plt.ylabel('Average Cases')
    plt.bar(months, monthAvgs, color = '#FF6ACE')
    plt.xticks(months, rotation = -70)
    plt.show()
    
def plot_Scatter_Cases_Versus(disease1, disease2, names):
    label = ' cases (log)'
    plt.figure()
    plt.xscale('log')
    plt.yscale('log')
    plt.title('Monthly ' + names[0] + ' cases vs ' + names[1] + ' cases ' \
              + '(1931 - 1971)')
    plt.xlabel(names[0] + label)
    plt.ylabel(names[1] + label)
    plt.axis([5, 10**4.7, 10, 10**4])
    plt.scatter(disease1, disease2, color = '#FF6ACE')
    plt.show()
    
#%% load data
months = ['January', 'February', 'March', 'April', 'May', 'June', 
           'July', 'August', 'September', 'October', 'November', 'December']

measles = pd.read_csv('Measles.csv', index_col = 0, names = months)
mumps = pd.read_csv('Mumps.csv', index_col = 0, names = months)

chickenpox = pd.read_csv('chickenPox.csv', index_col = 0, names = months)
chickenpox.sort_index(inplace = True)

plt.close('all') # close all existing figures

#%%
plot_Line_Cases_Years(measles, "Measles")
plot_Line_Cases_Years(mumps, "Mumps")
plot_Line_Cases_Years(chickenpox, "Chickenpox")

#%% 
plot_Line_Log_Cases_Years(measles, chickenpox, ['Measles', 'Chickenpox'])

#%% Average number of mumps cases for each month of the year
plot_Bar_Cases_Month(measles, 'Measles')

#%% Log plot of Measles agains Mumps cases
plot_Scatter_Cases_Versus(measles, mumps, ['Measles', 'Mumps'])
