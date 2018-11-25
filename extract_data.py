
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# function to open csv file and extract dataframe & desired columns (Odometer, Charge)
# file_name must be a csv file and in '', example = 'sample_interpolation.csv'
# must assign 2 variable_names to get function output
def extract_data(df):
    
    '''
    Reads loaded file as a pandas dataframe,
    organizes the data inside in ascending order by UID, then TimeOfData,
    and extracts the odometer and charge values as a list from the dataframe.
    
    Parameters
    ----------
    file_name = a string
        Single file want to read and extract data from. Must be in csv format
    
    Returns
    -------
    1. a correctly organized pandas dataframe of file loaded (df)
    2. a list of odometer readings (odometer)
    3. a list of charge readings (charge)
    '''
    # extract odometer and charge data as a list, to return
    odometer = df['Odometer'].tolist()
    charge = df['Charge'].tolist()
    
    return df, odometer, charge 

