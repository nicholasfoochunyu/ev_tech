
# coding: utf-8

# In[ ]:


# function that looks for where in charge list to interpolate, avoiding excess Nan values
def number_interpolations(points_interpolation):
    
    '''
    Function for identifying indexes for interpolable charge values within the charge list.
    Uses indexes of single Nan values specified in points_interpolation (an output from single_Nan())
    to  identify segments of charge list where <5 consecutive Nan values found.
    Second step in filling in interpolable charge values.
    
    Parameters
    ----------
    points_interpolation: a list
        List of indexes that indicate where within charge list single Nan readings found
    
    Returns
    -------
    A list that indicates where within charge list, Nan values can be interpolated
    
    '''

    list_within_interpolation_list = []
    interpolation_list = []
    for h in range(len(points_interpolation)):
        if h == 0: # first value of list
            list_within_interpolation_list.append(points_interpolation[h])
        else:
            if points_interpolation[h] <= points_interpolation[h-1]+10: # within 5 empty values (Nan)
                list_within_interpolation_list.append(points_interpolation[h])
                if h == len(points_interpolation)-1: # if come to last value of list to interpolate
                    list_within_interpolation_list.append(points_interpolation[h])
                    interpolation_list.append(list_within_interpolation_list)
            else:
                interpolation_list.append(list_within_interpolation_list) # appending series of index positions for interpolation
                list_within_interpolation_list = [points_interpolation[h]] # begin a new list
                
    # now indicating the range of each index list within the larger list
    refined_index_range = [] # final list for storing index range for each interpolation
    for j in range(len(interpolation_list)):
        index_range = []
        min_index, max_index = min(interpolation_list[j]), max(interpolation_list[j])
        index_range.append(min_index)
        index_range.append(max_index)
        refined_index_range.append(index_range)
        
    return refined_index_range

