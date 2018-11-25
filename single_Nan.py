
# coding: utf-8

# In[ ]:


import math


# In[ ]:


# function for identifying single Nan values in charge list for interpolation by pchip
def single_Nan(charge):
    
    '''
    Function for identifying location of single Nan values (avoiding consecutive Nan readings) in the charge list.
    First step in filling in interpolable charge values.
    
    Parameters
    ----------
    charge = a list
    
    Returns
    -------
    list (points_interpolation) of locations of single Nan values in the charge list.
    
    '''
    
    points_interpolation = []
    for d in range(len(charge)-1):
        if d <= len(charge):
            if math.isnan(float(charge[d])) == False and math.isnan(float(charge[d+1])) == True:
                points_interpolation.append(d)
                
    return points_interpolation

