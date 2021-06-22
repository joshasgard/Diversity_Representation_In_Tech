import pandas as pd
from collections import defaultdict
import numpy as np



def total_count(df, col1, col2, look_for):
    '''
    INPUT:
    df - the pandas dataframe you want to search
    col1 - the column name you want to look through
    col2 - the column you want to count values from
    look_for - a list of strings you want to search for in each row of df[col]

    OUTPUT:
    new_df - a dataframe of each look_for with the count of how often it shows up
    '''
    new_df = defaultdict(int)
    #loop through list of ed types
    for val in look_for:
        #loop through rows
        for idx in range(df.shape[0]):
            #if the ed type is in the row add 1
            if val in df[col1][idx]:
                new_df[val] += int(df[col2][idx])
    new_df = pd.DataFrame(pd.Series(new_df)).reset_index()
    new_df.columns = [col1, col2]
    new_df.sort_values('count', ascending=False, inplace=True)
    return new_df




def clean_race(race_item):
    possible_race = ['White or of European descent', 'South Asian', 'Hispanic or Latino/Latina', 
                 'East Asian', 'Middle Eastern','Native American, Pacific Islander, or Indigenous Australian',
                 'I prefer not to say','Black or of African descent','I don\'t know']
    '''
    INPUT
    race_item - line item of the dataframe column
    
    OUTPUT
    val - cleaned and streamlined data
    
    '''
    race_item = str(race_item)
    for val in possible_race:
        if val in race_item:
            return val 
        else:
            pass



