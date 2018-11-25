
# coding: utf-8

# In[ ]:


# function that looks for where within viable charge indexes to interpolate journey without charging are made
def charge_journeys(refined_index_range, charge): 
    
    '''
    Function that breaks charge list up into sublists based on whether a car has been recharged. 
    All charge readings before a recharge event are considered to be part of a single journey.
    Third step in filling in interpolable charge values.
    
    Parameters
    ----------
    refined_index_range = a list of lists
        A list of list, specifying viable charge indixes that can be interpolated. Produced as output from 
        number_interpolations()
    
    charge = a list
        A list of updated charge values (after applying reading_corrections() in charge)
        
    Returns
    -------
    A list of lists, specifying index locations of each new journey for a car (based on recharge events)
    '''
    
    divided_charge_list = []
    for remove in refined_index_range:
        
        # generate charge values within each remove list in refined_index_range
        first_index = remove[0]
        last_index = remove[1]
        charge_values = charge[first_index:last_index]
        
        # generate list for storing index position of when car has not been charged
        journey_no_charge = []
        for i in range(len(charge_values)):
            # special case since always starting with charged car
            if i == 0:
                journey_no_charge.append(i)
            # checking if car has been charged yet
            elif abs(float(charge_values[i]) - float(charge_values[i-1])) > 5 or             abs(float(charge_values[i]) - float(charge_values[i-3])) > 5:
                journey_no_charge.append(i) 
            elif i == len(charge_values) - 1:
                journey_no_charge.append(i+1)
                
        # putting information into a list
        grouped_charges = []
        for e in range(len(journey_no_charge)):
            if e != max(range(len(journey_no_charge))):
                if e == 0:
                    starting_index = 0
                    ending_index = journey_no_charge[e+1]
                    index_range = [starting_index, ending_index]
                    grouped_charges.append(index_range)
                else:
                    starting_index = journey_no_charge[e]+1
                    ending_index = journey_no_charge[e+1]-1
                    index_range = [starting_index, ending_index]
                    grouped_charges.append(index_range)
                    
        # removal of redundant items to interpolate, note for 1st list will remove first 2 values, these are not needed
        for g_charges in (grouped_charges):
            start_index = g_charges[0] # staring index value for sublist
            end_index = g_charges[1] # ending index value for sublist
            # check if is sensible list to interpolate, if not then remove
            if end_index - start_index < 3: # use value of 3 as normally charge value (& odometer) have repeated value 3 times at most
                list_index = grouped_charges.index(g_charges)
                del grouped_charges[list_index]# remove item from list
        divided_charge_list.append(grouped_charges)
        # manual correction for first value of first sublist
        divided_charge_list[0][0][0] = 0
    return divided_charge_list

