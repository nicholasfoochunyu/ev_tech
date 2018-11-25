##########################################################
##########################################################
# BASE CALCULATION MODULE FOR RUNNING BATTERY PREDICTION #
##########################################################
##########################################################

###########
# IMPORTS #
###########
import numpy as np


#############
# CONSTANTS #
#############
LOW_BASE = 2.75                                                               # Set low baseline of Miles Per kWh

########################
# CALCULATE END CHARGE #
#######################################################################
# FUNCTION: Predicts End charge                                       # 
# INPUT: Start Charge, Battery Size in KW, (No of) Journeys,          #
#        Average Miles Per kWh (Weighted for Distance),               # 
#        Standard Deviation in Miles Per kWh (Weighted for Distance), #
#        Distance (in Metres) of this Journey                         #
# OUTPUT: End Charge                                                  #
#######################################################################
def calculate_end_charge(start_charge, battery_kw, journeys, avg_mpkw, std_dev_mpkw, distance):
    # INPUTS
    # start_charge - current battery % of vehicle
    # battery_kw - size of car battery in kw
    # journeys - number of journeys made by driver and vehicle for which mpkw has been recorded
    # avg_mpkw - average miles per kwh recorded for those journeys (weighted by distance not number)
    # std_dev_mpkw - standard deviation of miles per kwn recorded for journeys (weighted by distance not number)
    # distance - distance of planned journey in metres
    
    # CALCULATE MILES PER KWH
    if (journeys >= 1 and journeys < 6):                                     # If number of journeys between 1 and 5...
        mpkw = LOW_BASE                                                          # Miles Per kWh = Low Baseline MPKW
    elif(journeys >=6 and journeys < 11):                                    # If number of journeys between 6 and 10...
        mpkw = (LOW_BASE + (avg_mpkw - (std_dev_mpkw * 0.5))) / 2                # Calculate Avg of Low Baseline and (Avg MPKW - Half SD) 
    elif(journeys > 10):                                                     # If number of journeys greater than 10...
        mpkw = avg_mpkw - (std_dev_mpkw * 0.5)                                   # Calculate Avg MPKW - Half SD
    
    # CALCULATE END CHARGE
    dist_km = (distance/1000)                                                # Calculate Distance in KM
    dist_miles = dist_km * 0.6214                                            # Calculate Distance in Miles
    kw_used = dist_miles / mpkw                                              # Calculate KW Used for Journey
    batt_one_percent = battery_kw / 100                                      # Calculate 1% of Battery        
    charge_used = kw_used / batt_one_percent                                 # Calculate Charge Used for Journey
    end_charge = start_charge - charge_used                                  # Calculate End Charge
    return end_charge                                                        # Return End Charge