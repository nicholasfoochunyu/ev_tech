
# coding: utf-8

# In[ ]:


import pandas as pd


# In[ ]:


# function for interpolating Odometer readings, uses pchip (PCHIP 1-d monotonic cubic interpolation)
# essentially a smoothing function
def odometer_interpolation(df, odometer):
    
    '''
    Function for filling in missing odometer readings (currently NULL) with interpolated values.
    Uses pchip interpolation method (essentially a polynomial smoothing function)
    
    Parameters
    ----------
    df = a pandas dataframe
        Updated pandas dataframe (df), updated by reading_corrections()
    
    odometer = a list
        List of updated odometer readings, returned output from reading_corrections()
    
    Returns
    -------
    No printed output. df is updated, now with no more missing/incorrect odometer values
    '''
    
    odo_df= pd.DataFrame(odometer)
    new_odo= odo_df.interpolate(method='pchip')
    new_odo.columns = ['Odometer'] # rename column heading

    # updating dataframe for Odometer = Finish Odometer adjustment
    df.update(new_odo)

