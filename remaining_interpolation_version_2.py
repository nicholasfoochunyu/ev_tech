
# coding: utf-8

# In[ ]:


import pandas as pd


# In[ ]:


# filling in values for weather, temperature, and humidity
def remaining_interpolation(df):
    
    '''
    Function for filling in values for weather, temperature and humidity in dataframe.
    Weather is filled in based on most weather of closest available real reading (from previous timestep).
    Temperature and humidity values are filled in through interpolation
    
    Parameters
    ----------
    df = pandas dataframe
        df can be either the raw dataframe (before the odometer and charge values are updated) or the updated dataframe.
    
    Returns
    -------
    An updated df, with all values for weather, temperature and humidity filled in.
    
    '''
    
    # loop over weather desc to fill in values
    for i in range(len(df)):
    # check weather at row i
            weather_report = df.loc[i,'WeatherDesc'] # 
            if isinstance(weather_report, float) == True: # check if weather is a floating point number
                                                          # since only nan has floating point number
                df.loc[i, 'WeatherDesc'] = df.loc[i-1, 'WeatherDesc']
    
    # temperature interpolation
    temperature = df['Temp'].tolist() # extract temperature values as a list
    temperature_df = pd.DataFrame(temperature) # construct datafrane
    temperature_df.columns = ['Temp'] # rename column
    new_temperature = temperature_df.interpolate(method='pchip') # apply pchip interpolation
    df.update(new_temperature) # update existing loaded dataframe

    # humidity interpolation
    humidity = df['Humidity'].tolist() # extract temperature values as a list
    humidity_df = pd.DataFrame(humidity) # construct datafrane
    humidity_df.columns = ['Humidity'] # rename column
    new_humidity = humidity_df.interpolate(method='pchip') # apply pchip interpolation
    df.update(new_humidity) # update existing loaded dataframe

