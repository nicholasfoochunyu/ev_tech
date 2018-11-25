
# coding: utf-8

# In[ ]:


import pandas as pd


# In[ ]:


# function for integrating charge values and updating charge columns in dataframe
# uses pchip interpolation
def update_charge_column(df, refined_index_range, divided_charge_list):
    
    '''
    A function to interpolate viable charge values.
    Final step in filling in interpolable charge values.
    
    Parameters
    ----------
    df =  a pandas dataframe
        Updated df, after interpolated odometer values have been inserted
    
    refined_index_range = a list of lists
        Specifies where viable charge values can be interpolated (avoiding excessive Nans)
        
    divided_charge_list = a list of lists
        Specified indices in charge that can be grouped together as a single journey (without a recharge event) for interpolation
    
    Returns
    An updated dataframe, with previously Nan charge values that could be interpolated filled with interpolated values.
    '''
    
    charge = df['Charge'].tolist() # pull out updated charge list each time
    charge_df = pd.DataFrame(charge) # converts charge list into a dataframe
    charge_df.columns = ['Charge']
    charge_df['Charge'] = pd.to_numeric(charge_df['Charge'], errors='coerce')
    for h in range(len(refined_index_range)):
        journey_removed_Nan = refined_index_range[h] # pick out each journey without excess Nan
        start_journey = journey_removed_Nan[0] # picks out starting index of journey
        journey_charge = divided_charge_list[h] # pick out corresponding travel within each journey with no charge events
        
        # identifying the location of each event in journey_charge, within length_journey
        for events in journey_charge:
            event_start = events[0] + start_journey
            event_end = events[1]-3 + start_journey # applying interpolation to values
                                                    # excludes last 2 NaN values (should be the same as last real value).
            # getting specific rows from charge column to apply interpolation
            updated_charge = charge_df.loc[event_start:event_end]
            try:
                new_charge = updated_charge.interpolate(method='pchip')
            except IndexError: # if can't use pchip method
                new_charge = updated_charge.interpolate(method='linear')
            except TypeError:
                new_charge = updated_charge.interpolate(method='linear')
            # updating dataframe for Charge = Finish Charge adjustment
            df.update(new_charge)

