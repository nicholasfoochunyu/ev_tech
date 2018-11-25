
# coding: utf-8

# In[ ]:


import pandas as pd


# In[ ]:


# function for initial correction of data, will then update loaded dataframe:-
# 1. Correct 0 odometer reading(@ start of journey) to correct reading (use last odometer reading from previous journey)
# Note: If is first entry of list, then will take first available odometer reading
# 2. Correct charge reading @start of every new journey (use charge reading from 1st available reading of that journey)
# Note: If is first entry of list, will take first available reading
# Note: didn't use last charge reading from previous journey as assume drainage of battery level overtime even
# when vehicle not used
# 3. Correct 102.737 charge reading (will be Nan for now, later interpolate)
def reading_corrections(df, odometer, charge):
    
    '''
    Function for initial correction of known data errors with:-
    1. odometer (reading of 0 at start of journey)
    2. charge (occasional reading of 102.737)
    
    Dataframe (df) is then updated with corrected odometer and charge values
    
    
    Parameters
    ----------
    df = a pandas dataframe
        Pandas dataframe produced as output from read_extract_data()
    
    odometer = a list
        List of raw odometer readings (extracted from pandas dataframe produced in read_extract_data())
        
    charge = a list
        List of raw charge readings (extracted from pandas dataframe produced in read_extract_data())
        
    Returns
    -------
    Updated odometer and charge list is returned. Dataframe (df) is also updated but not returned as an output
    '''
    
    remove = []
    for a in range(len(odometer)): # only need to use odometer data as is same length as charge data
        if odometer[a] == 0: # when odometer[a] = 0, is always start of new journey
            remove.append(a)
    for b in remove:
        if b == 0:
            odometer[b] = odometer[b+2] # takes odometer reading from 1st available reading
            charge[b] = charge[b+1] # takes charge reading from 1st available reading
        else:
            odometer[b] = odometer[b-1] # takes odometer reading from when vehicle last moved
            charge[b] = charge[b+1]     # takes charge reading from when vehicle first started up again
                                        # assume that when vehicle not used & not charging, battery level slowly drops
                                        # hence not taking last charge level when vehicle last moved
    # replacing 102.737 charge reading with real charge value (will be Nan for now, later interpolated)
    for c in range(len(charge)):
        check_value = round(charge[c], 3)
        if check_value > 100:
            charge[c] = 'Nan'
            
    # updating dataframe with new odometer & charge values
    non_zero_odometer = {'Odometer' : odometer}
    non_zero_odometer_df = pd.DataFrame(data=non_zero_odometer)
    non_zero_charge = {'Charge' : charge}
    non_zero_charge_df = pd.DataFrame(data=non_zero_charge)

    df.update(non_zero_odometer_df)
    df.update(non_zero_charge_df) 
    
    return odometer, charge

