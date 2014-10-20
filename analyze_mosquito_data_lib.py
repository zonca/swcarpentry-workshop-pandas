import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

def fahr_to_celsius(tempF):
    """Convert fahrenheit to celsius"""
    tempC = (tempF - 32) * 5 / 9.0
    return tempC

def analyze(data):
    """Perform regression analysis on mosquito data
    
    Takes a dataframe as input that includes columns named 'temperature',
    'rainfall', and 'mosquitos'.
        
    For consistency, always use temperature in Celsius.
    
    Performs a multiple regression to predict the number of mosquitos.
    Creates an observed-predicted plot of the result and
    returns the parameters of the regression.
    
    """
    regr_results = sm.OLS.from_formula('mosquitos ~ temperature + rainfall', data).fit()
    parameters = regr_results.params
    predicted = parameters['Intercept'] + parameters['temperature'] * data['temperature'] + parameters['rainfall'] * data['rainfall']
    plt.figure()
    plt.plot(predicted, data['mosquitos'], 'ro')
    min_mosquitos, max_mosquitos = min(data['mosquitos']), max(data['mosquitos'])
    plt.plot([min_mosquitos, max_mosquitos], [min_mosquitos, max_mosquitos], 'k-')
    return parameters
