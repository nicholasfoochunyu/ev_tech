
# coding: utf-8

# In[ ]:


import pandas as pd
import math


# In[ ]:


# 2nd round of interpolation of charge values
# essentially packaging steps 1 to 4 for interpolating charge values from above methods
def second_update_charge_column(df):
    '''
    A function for interpolating charge readings. Done after running first 3 steps at least once before
    (hence,  single_Nan(), number_interpolations(), charge_journeys() & update_charge_column())
    
    Parameters
    ----------
    df = a pandas dataframe
        An updated df, after running the odometer interpolation and charge interpolation(must be done before using
        this function)
    
    Returns
    -------
    An updated dataframe, with viable charge values inside interpolated
    '''
    
    charge = df['Charge'].tolist() # pull out updated charge list each time
    odometer = df['Odometer'].tolist() # pull out updated odometer list
    # create empty list to store values to interpolate and values to replace for charge
    charge_interpolate = [] # index positions in charge to interpolate
    charge_replace = [] # index position in charge to replace using previous index position
    
    # identify segments of charge column requiring further interpolation
    for index, value in enumerate(charge):
        if math.isnan(float(value)) == True: # if charge value is NaN
            if math.isnan(float(charge[index - 1])) == True: # if previous charge value is NaN
                if odometer[index] != odometer[index - 1]: # if current and previous odometer are not equal
                    charge_interpolate.append(index) # add to charge values to be interpolated (since can't directly use value above it)
            else:
                if odometer[index] == odometer[index-1]:
                    charge_replace.append(index) # able to use charge value in position above to replace since have same odometer value
                else:
                    charge_interpolate.append(index)
    
    # create charge dataframe for interpolation
    charge_df = pd.DataFrame(charge) # converts charge list into a dataframe
    charge_df.columns = ['Charge']
    charge_df['Charge'] = pd.to_numeric(charge_df['Charge'], errors='coerce')
    
    # start to interpolate values in dataframe
    for i in charge_interpolate:
        updated_charge = charge_df.loc[i-2:i+1]
        try:
            new_charge = updated_charge.interpolate(method='pchip')
        except IndexError: # if can't use pchip method
            new_charge = updated_charge.interpolate(method='linear')
        except TypeError:
            new_charge = updated_charge.interpolate(method='linear')
         # updating dataframe for Charge = Finish Charge adjustment
        df.update(new_charge)

    # replace charge values specified in charge_replace with charge value in above position
    charge = df['Charge'].tolist()
    for j in charge_replace:
        charge[j] = charge[j-1]
    charge_df = pd.DataFrame(charge) # converts charge list into a dataframe
    charge_df.columns = ['Charge']
    charge_df['Charge'] = pd.to_numeric(charge_df['Charge'], errors='coerce')
    df.update(charge_df)
    
    # final correction for charge, based on if have same odometer value
    charge = df['Charge'].tolist()
    for a in range(len(odometer)):
        if a != 0:
            if odometer[a] == odometer[a-1]:
                if abs(float(charge[a]) - float(charge[a-1])) < 5:
                    charge[a] == charge[a-1]
    charge_df = pd.DataFrame(charge) # converts charge list into a dataframe
    charge_df.columns = ['Charge']
    charge_df['Charge'] = pd.to_numeric(charge_df['Charge'], errors='coerce')
    df.update(charge_df)

