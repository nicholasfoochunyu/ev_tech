
# coding: utf-8

# In[ ]:


# import modules for linear regression model
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.sandbox.regression.predstd import wls_prediction_std

# modules for handling dataset
import glob
import pandas as pd
import numpy as np
from sklearn import preprocessing


# In[ ]:


# creating function for extracting information on statistical results of OLS
# usable on raw, standardized and normalized data

def OLS_results(dataframe):
    
    # define dependent variable to explain
    dep_var = ['ChargeUsed', 'KilowattsUsed', 'MilesPerKW']
    
    # define headings of dataframe
    heading = dataframe.columns.values.tolist()
    
    # begin linear regression using Ordinary Least Squares
    for i, var in enumerate(dep_var):
        
        # working with first dependent variable
        if i == 0:
            for j, head in enumerate(heading):

                # checking that not running dependent variable against itself
                if var != head:
                    if head!= 'UID':

                        # run the Ordinary Least SQuares
                        model = ols(f"{var} ~ {head}", data=dataframe).fit()

                        # extract specific information from OLS results
                        r_sq = model.rsquared_adj
                        coef = model.params[1]
                        std_e = model.bse[1]
                        p_val = model.pvalues[1]

                        # putting information into a nice dataframe

                        if j == 1: # if first time creating dataframe
                            column_name = ['Paramaters','Adj-R-squared', 'Regression Coefficient', 'Standard Error',                                           'p-value']
                            row_insert = np.array([head, r_sq, coef, std_e, p_val]).reshape(1,5)
                            table_1 = pd.DataFrame(data= row_insert,
                                                  columns=column_name)

                        else: # after created dataframe
                            table_1.loc[j] = [head, r_sq, coef, std_e, p_val]

            # working with second dependent variable
        elif i == 1:
            for j, head in enumerate(heading):

                # checking that not running dependent variable against itself
                if var != head:
                    if head!= 'UID':

                        # run the Ordinary Least SQuares
                        model = ols(f"{var} ~ {head}", data=dataframe).fit()

                        # extract specific information from OLS results
                        r_sq = model.rsquared_adj
                        coef = model.params[1]
                        std_e = model.bse[1]
                        p_val = model.pvalues[1]

                        # putting information into a nice dataframe

                        if j == 1: # if first time creating dataframe
                            column_name = ['Paramaters','Adj-R-squared', 'Regression Coefficient', 'Standard Error',                                           'p-value']
                            row_insert = np.array([head, r_sq, coef, std_e, p_val]).reshape(1,5)
                            table_2 = pd.DataFrame(data= row_insert,
                                                  columns=column_name)

                        else: # after created dataframe
                            table_2.loc[j] = [head, r_sq, coef, std_e, p_val]
            
        # working with third dependent variable
        else:
            for j, head in enumerate(heading):

            # checking that not running dependent variable against itself
                if var != head:
                    if head!= 'UID':

                        # run the Ordinary Least SQuares
                        model = ols(f"{var} ~ {head}", data=dataframe).fit()

                        # extract specific information from OLS results
                        r_sq = model.rsquared_adj
                        coef = model.params[1]
                        std_e = model.bse[1]
                        p_val = model.pvalues[1]

                        # putting information into a nice dataframe

                        if j == 1: # if first time creating dataframe
                            column_name = ['Paramaters','Adj-R-squared', 'Regression Coefficient', 'Standard Error',                                           'p-value']
                            row_insert = np.array([head, r_sq, coef, std_e, p_val]).reshape(1,5)
                            table_3 = pd.DataFrame(data= row_insert,
                                                  columns=column_name)

                        else: # after created dataframe
                            table_3.loc[j] = [head, r_sq, coef, std_e, p_val]
    
    return table_1, table_2, table_3

