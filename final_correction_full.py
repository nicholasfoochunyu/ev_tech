
# coding: utf-8

# In[ ]:


import pandas as pd
import math


# In[ ]:


# function to format csv file & save it:-
# 1. add '' around DateTime, 2. add'' around TimeofData,
# 3. insert corrected UID value, 4. correct lattitude to 8 significant figures (2 + 6)
# 5. correct longitude to 7 significant figures (1 + 6), 6. assign Null to 0 values in speed
# 7. change odometer values float to integers, 8. correct charge to 6 significant figures (2+4)
# 9. add additional column to input ',' for line seperation, 
# 10. replace NaN values in charge column with NULL
def final_correction_full(df, file_name):
    '''
    Function for formating dataframe for export as a sql text file. Allows for direct creating of
    table in MySQL Workbench/loading data into existing table in MySQL Workbench.
    
    Parameters
    ----------
    df = a pandas dataframe
        A dataframe, where all possible Nan values have been filled in.
        
    file_name = a string
        Filename to be modified, acting as file name for function output
        
    Returns
    -------
    A SQL text file that can be imported into MySQL Workbench. 
    Warning!!! Depending on file size exported, may be too large for direct read in
    
    '''
    # 1. insert '(' and '' around DateTime
    datetime_change = df['DateTime'].tolist() # extracting information from dataframe
    corrected_datetime = [] # empty list to store corrected values for DateTime
    for datetime in datetime_change:
        correct_dt = "('%s'"%str(datetime) # insert ( and ''
        corrected_datetime.append(correct_dt) # appending to empty list
    corrected_datetime = {'DateTime':corrected_datetime} # making dictionary for dataframe storage
    corrected_datetime_df = pd.DataFrame(data=corrected_datetime) # store corrected values in dataframe
    df.update(corrected_datetime_df) # updating existing dataframe with newly generated dataframe
    
    # 2. insert '' around TimeofData, essentially the same steps as for DateTime
    timeofdata_change = df['TimeOfData'].tolist()
    corrected_timeofdata = []
    for timeofdata in timeofdata_change :
        correct_tod = "'%s'"%str(timeofdata)
        corrected_timeofdata.append(correct_tod)
    corrected_timeofdata = {'TimeOfData':corrected_timeofdata}
    corrected_timeofdata_df = pd.DataFrame(data=corrected_timeofdata)
    df.update(corrected_timeofdata_df)
    
    # 3. assign correct UID
    UID_change= df['UID'].tolist() # extract information from dataframe
    UID_correction = file_name[13:-9]# extract exact UID for replacement
    if UID_correction[0] == '_':
        UID_correction = str(file_name[14:-9])
    corrected_UID = []
    for a in range(len(UID_change)):
        corrected_UID.append("'%s'"%str(UID_correction)) # update empty list with correct UID for replacement
    corrected_UID = {'UID':corrected_UID}
    corrected_UID_df = pd.DataFrame(data=corrected_UID)
    df.update(corrected_UID_df) # updating dataframe
    
    #4. correct latitude values to 6 decimal places
    latitude_change = df['Latitude'].tolist()
    corrected_latitude = []
    for latitude in latitude_change:
        correct_latitude = '%.6f'%(latitude) # taking 6 decimal places only
        corrected_latitude.append(correct_latitude)
    corrected_latitude = {'Latitude':corrected_latitude}
    corrected_latitude_df = pd.DataFrame(data=corrected_latitude)
    df.update(corrected_latitude_df)
    
    # 5. correct longitude values to 6 decimal places, essentially same steps for lattitude
    longitude_change = df['Longitude'].tolist()
    corrected_longitude = []
    for longitude in longitude_change:
        correct_longitude = '%.6f'%(longitude)
        corrected_longitude.append(correct_longitude)
    corrected_longitude = {'Longitude':corrected_longitude}
    corrected_longitude_df = pd.DataFrame(data=corrected_longitude)
    df.update(corrected_longitude_df)
    
    # 6. set NaN values in speed to 'NULL' string
    speed_change = df['Speed'].tolist()
    corrected_speed = []
    for speed in speed_change:
        if math.isnan(speed) == True: # if speed is NaN
            speed_nan = 'NULL'
            corrected_speed.append(str(speed_nan))
        else: # speed has real value 
                corrected_speed.append(speed)
    corrected_speed = {'Speed':corrected_speed}
    corrected_speed_df = pd.DataFrame(data=corrected_speed)
    df.update(corrected_speed_df)
    
    # 7. adjust odometer readings to have no decimal places
    odometer_change = df['Odometer'].tolist()
    corrected_odometer = []
    for odometer in odometer_change:
        correct_odometer = str(int(odometer)) # convert to integer, then string to remove final .0
        corrected_odometer.append(correct_odometer)
    corrected_odometer = {'Odometer':corrected_odometer}
    corrected_odometer_df = pd.DataFrame(data=corrected_odometer)
    df.update(corrected_odometer)
    
    # 8. add ')' to charge values
    charge_change = df['Charge'].tolist()
    corrected_change = []
    for change in charge_change:
        try:
            correct_change = '%f'%(change)  # correction to 4 decimal places, 
        except TypeError:
            correct_change = change
        corrected_change.append(correct_change)
    corrected_change = {'Charge':corrected_change}
    corrected_change_df = pd.DataFrame(data=corrected_change)
    df.update(corrected_change_df)
    
    # 9 add '' around WeatherDesc
    weatherdesc_change = df['WeatherDesc'].tolist()
    corrected_weatherdesc = []
    for weatherdesc in weatherdesc_change :
        correct_weather = "'%s'"%str(weatherdesc)
        corrected_weatherdesc.append(correct_weather)
    corrected_weatherdesc = {'WeatherDesc':corrected_weatherdesc}
    corrected_weatherdesc_df = pd.DataFrame(data=corrected_weatherdesc)
    df.update(corrected_weatherdesc_df)
    
    # 10 ')' for end of row 
    elevation = df['Elevation'].tolist()
    corrected_elev = []
    for elev in elevation:
        try:
            correct_elev = '%f'%(elev) + ')'
        except TypeError:
            correct_elev = elev
        corrected_elev.append(correct_elev)
    corrected_elev = {'Elevation':corrected_elev}
    corrected_elev_df = pd.DataFrame(data=corrected_elev)
    df.update(corrected_elev_df)
    
    # 11 add additional column to input ',' for line seperation
    line_seperator = []
    for c in range(len(df)):
        line_seperator.append('') # add in ''
    line_seperator = {'Seperator':line_seperator}
    line_seperator_df = pd.DataFrame(data=line_seperator) # adds in ',' to every end of line
    df['Seperator'] = line_seperator_df # adding new column to dataframe
    
    # 12. replace NaN values in charge column with NULL
    charge_nan_change = df['Charge'].tolist()
    corrected_charge_nan = []
    for i_charge in charge_nan_change:
        try:
            if math.isnan(int(i_charge[0])) == False: # if charge is not NaN
                corrected_charge_nan.append(i_charge)
        except ValueError: # if charge is NaN
            charge_nan = 'NULL'
            corrected_charge_nan.append(str(charge_nan))
    corrected_charge_nan = {'Charge':corrected_charge_nan}
    corrected_charge_nan_df = pd.DataFrame(data=corrected_charge_nan)
    df.update(corrected_charge_nan_df)
    
    # saving as csv_file 
    df.to_csv('interp_tele_1' + file_name, index=False, header=False)
    
    # accessing csv_file to create sql text file with inserted table code for SQL
    starting_string = "SET NAMES utf8;\nSET time_zone = '+00:00';\nSET foreign_key_checks = 0;\nSET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';\n\nDROP TABLE IF EXISTS `Trakm8_full_int`;\nCREATE TABLE `Trakm8_full_int` (\n  `DateTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,\n  `TimeOfData` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',\n `UID` bigint(11) NOT NULL,\n  `Latitude` double NOT NULL,\n  `Longitude` double NOT NULL,\n \t`Speed` tinyint(3) unsigned DEFAULT NULL,\n \t`Odometer` bigint(20) unsigned DEFAULT NULL,\n \t`Charge` float unsigned DEFAULT NULL,\n \t`WeatherDesc` varchar(100) DEFAULT NULL,\n \t`Temp` tinyint(4) DEFAULT NULL,\n  \t`Humidity` smallint(5) unsigned DEFAULT NULL,\n  \t`Elevation` int(11) NOT NULL)\n \tENGINE=MyISAM DEFAULT CHARSET=latin1;\n\nINSERT INTO `Trakm8_full_int` (`DateTime`, `TimeOfData`, `UID`, `Latitude`, `Longitude`, `Speed`, `Odometer`, `Charge`, `WeatherDesc`, `Temp`, `Humidity`, `Elevation`) VALUES\n"
    with open('interp_tele.sql', 'w') as file:
        file.write(starting_string)
        with open('interp_tele.sql', 'r') as data: # writing data from csv into sql file
            data_text = data.read()[:-2]
        data.close()
        file.write(data_text)
        file.write(';') # insert ; at end of file
    file.close()

