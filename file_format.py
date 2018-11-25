
# coding: utf-8

# In[ ]:


import pandas as pd
from final_correction_full import *
import glob
import os


# In[ ]:


# function for formating file
# decide if want to save as csv or as sql

def file_format(df, file_name, csv=True):
    
    '''
    A function for saving the dataframe as either a csv file or a sql file.
    csv files do not require further formating.
    sql files are for each car individually, with may require file splitting if too large (can't be loaded in MySQL Workbench)
    
    Parameters
    ----------
    i: an integer
        An integer indicating car number working with
    
    df: a pandas dataframe
        A dataframe where missing values have been filled in.
    
    file_name: a string
        Filename to be modified, acting as file name for function output
    
    csv: a boolean value
        If True, then data saved as a csv file & all data for all cars saved under 1 csv file.
        If False, data for each car saved as a seperate sql file, which may require file splitting if too large
        to be read at once in MySQL Workbench
    
    Returns
    -------
    Either a single csv file or multiple sql files    
    '''
    # creating a csv file
    if csv:
        df.to_csv(f'interp_tele.csv', index=False, header=True)
    
    # creating a sql text file/files
    else:
        final_correction_full(df, file_name) # returning a sql text file
        
        # checking size of returned sql text file 
        file_check = glob.glob('interp_tele.sql') 
        fileinfo = os.stat(file_check[0])
        
        # if exceed file size loadable in MySQL Workbench, split file
        if fileinfo.st_size > 3000000:
            fs = FileSplit(file=fileinfo, splitsize=3000000)
            fs.split()
        
            # grabbing back split files
            divided_files = glob.glob(f'interp_tele_*.sql')
            
            # ensure grabbing correct file
            for files in divided_files:
                    file_open = open(files, 'r')
                    file_content = file_open.read()
                    
                    # check if is the first file of series
                    if files[-6:] == '_1.sql':
                        with open(files, 'w') as file:
                            file.write(file_content[:-2] + ';')
                            file.close()
                            
                    # checking if have ; at end of file
                    elif file_content[-1] != ';':
                        
                        # create new sql files to insert into final_revision the desired content
                        with open(files, 'w') as file:
                            file.write('INSERT INTO `Trakm8_full_int` (`DateTime`, `TimeOfData`, `UID`, `Latitude`,`Longitude`, `Speed`, `Odometer`, `Charge`, `WeatherDesc`, `Temp`, `Humidity`, `Elevation`) VALUES')
                            file.write(file_content[:-2] + ';')
                            file.close()
                            
                    else:
                        with open(files, 'w') as file:
                            file.write('INSERT INTO `Trakm8_full_int` (`DateTime`, `TimeOfData`, `UID`, `Latitude`,`Longitude`, `Speed`, `Odometer`, `Charge`, `WeatherDesc`, `Temp`, `Humidity`, `Elevation`) VALUES')
                            file.write(file_content)
                            file.close()

