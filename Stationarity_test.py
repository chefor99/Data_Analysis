#!/usr/bin/env python
# coding: utf-8

# In[ ]:



#
# ********************** Checking for Stationarity *****************************
#


import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from datetime import datetime
from matplotlib.pylab import rcParams # rc = runtime configuration (linewidth, color, style, etc)
rcParams['figure.figsize'] = 8, 6
from statsmodels.tsa.stattools import adfuller
from IPython.display import display

def stats_test_by_stor_nbr(time_series, store_number, last_number, Stationary_Data):
    
   #
   # Rolling Statistics 
   # Moving Average (MA) and Varaince (Standard Deviation) over a 30-days cycle
   #
    plt.figure()
    plt.plot(time_series, color = 'blue', label = 'Store_nbr: {}'.format(store_number))
    plt.plot(pd.Series(time_series).rolling(window = 30).mean(), color  = 'red', label = 'MA_30 Days')   
    plt.plot(pd.Series(time_series).rolling(window = 30).std(),color = 'black', label = 'Standard_Deviation')
   
    plt.xlabel('Date')
    plt.ylabel('Transactions')
    plt.legend(loc = 'best')
    plt.show(block = False)
    
    #  
    # Dickey-Fuller Test
    # H_0: Time series is not sationary:If p-vale < 0.5, discard H_0;
    # Capmpare Test Statistic to Critical value @ 1%, 5% and 10%
    # NB: AIC estimates the quality of each model(error), relative to alternative ones->Aids for best model selection
    #    

#     print('\nDickey Fuller Test Results')
    
    df_test   = adfuller(time_series, autolag = 'AIC')                          # AIC == Akaike Infomation Criteria
    
    test_sts = df_test[0]
    p_value = format(df_test[1])
    critical_values = df_test[4]                                               # df_test[4] == a Dictionary  
#     print('p-value = {}'.format(p_value))

#     print('Test Statistic =', test_sts)   
#     print('Critical values =', critical_values)


    #
    # Re-arrange the output
    #
   
    
    df_output = pd.Series(df_test[0:4], index = ['Test Statistic: ', 'p-value: ', '#Lags Used: ', '#Observations Used:'])     
    for key, value in df_test[4].items():                                              
        df_output['Critical value: {%s}' %key] = value
        
    #
    # Construct a Stationrity Table (DataFrame)
    #

    print("Stationary")

    if test_sts < critical_values.get('1%'):
        Stationarity = 'Yes'
        Confidence = 99

    elif test_sts < critical_values.get('5%'):
        Stationarity = 'Yes'
        Confidence = 95

    elif test_sts < critical_values.get('10%'):
        Stationarity = 'Yes'
        Confidence = 90

    else:
        Stationarity = 'No'
        Confidence = ' '
    Stationary_Data.loc[store_number] = [store_number, p_value, Stationarity, Confidence] 

    if store_number == last_number:
        display(Stationary_Data)
    
    return df_output

#________________________________________________________________________________________________________________________________________

def stats_test_by_prdtFamily(time_series,  family_prdt, Stationary_Data, last_family_prdt):
    
   #
   # Rolling Statistics 
   # Moving Average (MA) and Varaince (Standard Deviation) over a 30-days cycle
   #
    plt.figure()
    plt.plot(time_series, color = 'blue', label = family_prdt)
    plt.plot(pd.Series(time_series).rolling(window = 30).mean(), color  = 'red', label = 'MA_30 Days')   
    plt.plot(pd.Series(time_series).rolling(window = 30).std(),color = 'black', label = 'Standard_Deviation')
   
    plt.xlabel('Date')
    plt.ylabel('Transactions')
    plt.legend(loc = 'best')
    plt.show(block = False)
    
    #  
    # Dickey-Fuller Test
    # H_0: Time series is not sationary:If p-vale < 0.5, discard H_0;
    # Capmpare Test Statistic to Critical value @ 1%, 5% and 10%
    # NB: AIC estimates the quality of each model(error), relative to alternative ones->Aids for best model selection
    #    

#     print('\nDickey Fuller Test Results')
    
    df_test   = adfuller(time_series, autolag = 'AIC')                          # AIC == Akaike Infomation Criteria
    
    test_sts = df_test[0]
    p_value = format(df_test[1])
    critical_values = df_test[4]                                               # df_test[4] == a Dictionary  
#     print('p-value = {}'.format(p_value))

#     print('Test Statistic =', test_sts)   
#     print('Critical values =', critical_values)


    #
    # Re-arrange the output
    #
   
    
    df_output = pd.Series(df_test[0:4], index = ['Test Statistic: ', 'p-value: ', '#Lags Used: ', '#Observations Used:'])     
    for key, value in df_test[4].items():                                              
        df_output['Critical value: {%s}' %key] = value
        
    #
    # Construct a Stationrity Table (DataFrame)
    #
        
    if test_sts < critical_values.get('1%'):
        Stationarity = 'Yes'
        Confidence = 99
        
    elif test_sts < critical_values.get('5%'):
        Stationarity = 'Yes'
        Confidence = 95
        
    elif test_sts < critical_values.get('10%'):
        Stationarity = 'Yes'
        Confidence = 90
        
    else:
        Stationarity = 'No'
        Confidence = ' '
    Stationary_Data.loc[family_prdt] = [family_prdt, p_value, Stationarity, Confidence] 
            
    if family_prdt == last_family_prdt:
        display(Stationary_Data)
