# -*- coding: utf-8 -*-
"""
Created on Thu May 21 17:53:20 2020

@author: moham
"""

import pandas as pd
people = {
    "first": ["Corey", 'Jane', 'John'],
    "last":  ["Shafer", 'Doe', 'Bull'],
    "email": ["coshafer@gmail.com", "Janedo@email.com", "Jobull@mail.com"]
}
df = pd.DataFrame(people)
df
df['email']
df.set_index('email') # sets 'email' as the index of the dataframe (first column), only fo this command
df.set_index('email', inplace=True) # permanent form of previous command
df.index # shows index for the dataframe
df.loc['Jobull@mail.com']
df.loc['Jobull@mail.com', 'last']
df.reset_index(inplace=True) # restes the index to its original form (0,1,2,...)

df['last'] == 'Doe' #gives a series object that yields True (if ‘last’ is ‘Doe’ in that row) or False(if ‘last’ is not ‘Doe’ in that row)
filt = (df["last"] == 'Doe') #creates a series varibale named filt with True and False values based on the defined condition  
df[filt]
df.loc[filt] #same as df[filt]. locates and shows data based on True values defined by filt.
df.loc[~filt] # same as df[filt]. locates and shows data based on False values defined by filt.
df.loc[filt, ['first', 'last']] # locates data based on filter, but only shows the 'first' and 'last' columns data.
df.columns #shows column names and type
df.columns = ['first_name', 'last_name', 'email'] #rename the columns to these ones
df.columns = [x.upper() for x in df.columns] #comprehension: changes column name letters to capital letters.
df.columns = [x.lower() for x in df.columns] #changes column name letters to small/non-capital letters
df
df.columns = df.columns.str.replace('_', ' ') #replaces all the '_' with ' ' in column names
df.columns = df.columns.str.replace(' ', '_') #reverse the above command
df
df.rename(columns={'first_name':'first', 'last_name':'last'})#renames the selected columns to the ones assigned inside the dicitonary in {} 
df.rename(columns={'first_name':'first', 'last_name':'last'}, inplace=True) #permanent form of the above command
df.loc[2] #shows information for row 2(third row)
df.loc[0]=['Corey', 'Schafer', 'Corey.schafer@mail.com']
df.loc[1]=['Jane', 'Doe', 'JaneDoe@gmail.com']
df.loc[2]=['John', 'Smith', 'Johnsmith@email.com'] #assigns new values to row 2. Need to match the number of dimensions inside row 2. for example cannot assign two values when row 2 has 3 dimensions.
df.loc[2, ['last', 'email']]=['Doe', 'JohnDoe@email.com']
df.loc[2, 'last'] = 'Smith' #assigns/changes the value in row 2 under 'last' column to 'Smith'.
df.at[2, 'last'] = 'Smith' # same as above. less common
# now choosing a data point like above, this time using a filter
filt = (df['email']=='JohnDoe@email.com')
df[filt]
df[filt]['last'] #chooses the data row using the defined filter(filt) and then shows only its value under the 'last' column. However for changing values use .loc 
df.loc[filt, 'last'] = 'Smith' #changes the value for row defined by filt and under 'last' column to 'Smith'.
df['email'].str.lower() #returns the values under 'email' column in lower case.
df['email'] = df['email'].str.lower() # makes the above change permanent
#apply is used to call a function on our values, it can be applied to either a dataframe or a series object
df['email'].apply(len) #applies the length function to the 'email' column in 'df' data frame.
#instead of len() function any function can be used, you can even define functions and call them into the above command. for example:
def update_email(email):
    return email.upper() # creates a function that receives 'email' in the form of a series and returns its upper case version.
df['email'].apply(update_email) #applies the update_email function to 'email' column.
#now doing the same thing using lambda, which is anonymous function
df['email'] = df['email'].apply(lambda x: x.lower()) #changes 'email' column values to lower case.
df.apply(len) #since df is a dataframe this gives the length of each column (first:3; last: 3; email:3)
df.apply(len, axis = 'columns') # same thing as above, but changes the default from rows to columns and counts the columns, so now gives the length of rows(0:3; 1:3; 2:3)
df.apply(pd.Series.min) # finds the minimum under each column, which due to the string format of the example here gives strings with the alphabetic order (a is minimum and z is max)
df.apply(lambda x: x.min()) #same as above using labda
df.apply(pd.Series.min, axis = 'columns') #same as above, just changes default to columns so shows min for each row.
#running apply in a series applies the function to every data in the series, while running apply in a dataframe, applies the function to every series in the dataframe.
df.applymap(len) #applymap applies the function to every individual value in the dataframe. it is only used with dataframes.
#applies the len function to every individual value in a dataframe.
df.applymap(str.lower) #applies lower letter function to every individual value in the dataframe.
#map is only used with series, to substitute a value in a series with another value.
df['first'].map({'Corey': 'Chris', 'Jane':'Mary'})#changes individual values in a dataframe, getting new values in a dictionary format.
#However above example changes the thrid value 'John' to NaN since we didn't specify a new value for that. To solve this problem we can use replace.
df['first'].replace({'Corey': 'Chris', 'Jane':'Mary'}) #changes the assigned values and keep the unassigned ones unchanged.
df['first'] = df['first'].map({'Corey': 'Chris', 'Jane':'Mary'}) # same as above but makes the changes permanent.
df['first'] + ' ' + df['last'] #gives first name and last name with a apce between them.
df['full_name'] = df['first'] + ' ' + df['last'] # creates a new column named 'full_name' which is first name and last name with a space between them.
df
df.drop(columns=['first' , 'last']) #drops columns named 'first' and 'last' temporarily
df.drop(columns = ['first' , 'last'], inplace=True) #makes the above change PERMANENTLY.
df['full_name'].str.split(' ', expand = True) #splits the full_name column values from a space
df[['first' ,'last']] = df['full_name'].str.split(' ', expand = True)#create two columns named first and last with first and last name extracted from the full_name column.
df.append({'first': 'Tony'}, ignore_index=True) #adds a row with first name as Tony.
#Now let's add a dataframe to the current dataframe
people2 = {
    'first' : ['Tony', 'Steve'],
    'last' : ['Stark', 'Rogers'],
    'email' : ['Tonystark@email.com', 'Steverogers@mail.com']
    }
df2 = pd.DataFrame(people2) #created a dataframe (df2) from the newly defined dictionary (people2)
df2
df.append(df2, ignore_index = True, sort = False) #adds the new dataframe (df2) to the first dataframe (df)
df = df.append(df2, ignore_index = True, sort = False) #makes the above attachment permanent, inplace=true can't be used here!
df
df.drop(index=4) #drops the last row from the df dataframe (last row index is 4)
df.drop(index=df[df['last'] == 'Doe'].index) #uses a conditional to drop a row. Condition is 'last'='Doe'
#cleaner way of doing above is as follow:
filt = df['last'] == 'Doe'
df.drop(index=df[filt].index)    
df.sort_values(by='last') # sort rows based on the 'last' column, in ascending order.
df.sort_values(by='last', ascending=False) #same as above, just descending order.
df.sort_values(by=['last', 'first'], ascending=False) #sorts based on first 'last' and then 'first', all of them in descending order.
df.sort_values(by=['last', 'first'], ascending=False, inplace=True) # same as above but PERMANENT
df.sort_values(by=['last', 'first'], ascending=[False, True]) # sorts by 'last' in descending order and then by 'first' in ascending order.
df.sort_values(by=['last', 'first'], ascending=[False, True], inplace=True) #same as above, but PERMANENT.
df.sort_index() #sorts dataframe based on index.
df['last'].sort_values() #sorts and gives just the 'last' column, like a series.
##Cleaning data
import pandas as pd
import numpy as np
people3 = { 'first': ['Corey', 'Jane', 'John', 'Chris', np.nan, None, 'NA'],
            'last': ['Schafer', 'Doe', 'Doe', 'Schafer', np.nan, np.nan, 'Missing'],
            'email' : ['CoreyMSchafer@gmail.com', 'JaneDoe@gmail.com', 'JohnDoe@gmail.com', None, np.nan, 'Anonymous@email.com', 'NA'],
            'age' : ['33', '55', '63', '36', None, None, 'Missing']
    }
df3 = pd.DataFrame(people3)

df3.replace('NA', np.nan, inplace=True) #replaces 'NA' values with NaN
df3.replace('Missing', np.nan, inplace=True) #replaces all 'Missing' values with NaN
df3
#for example if they don't have first, last, and email we can't use their data and have to delete it:
df3.dropna() #deletes rows with missing values
df3.dropna(axis='index', how='any') #these are default settings for dropna, so this does the
#same as above(dropna()).
df3.dropna(axis = 'index', how='all') #drop rows if all of the values in that row is missing.
df3.dropna(axis='columns', how='any') #changes the default axis to columns, so drops any column that has a missing/no value in it.
df3.dropna(axis='columns') #same as above, since default is 'any'.
#Now I want to drop rows that don't include an email address.
df3.dropna(axis='index', how='any', subset=['email'])
df3.dropna(axis='index', how='all', subset=['last', 'email']) #drops the rows that have missing/no value for 'last' AND 'email' value.
#to make the above changes permanent, need to use inplace=true.
df3.dropna(axis=0)#drops the entire row.
df3.dropna(axis=1)#drops the entire column.
df3.isna() #detects missing values
df3.fillna('MISSING') #changes all NA values to 'MISSING'.
df3.fillna(0) #changes all NA values to 0.
##CASTING
df3.dtypes #shows data types for the dataframe.
type(np.nan) #shows data type for NaN which is float.
#now let's calculate the age average for 'age' column. Howeever, running above command shows 
#'age' data is object (in this case string). So we need to change data type first.
df['age'].replace(np.nan, mean) #replaces the missing values in column 'age' with 'mean' of the column.
df3['age'] = df3['age'].astype(int) # if our column does not have any missing values this would work fine.
# here since there are missing values, we have to either replace NaN values with 0,
# or just cast that column to 'float'.
df3['age'] = df3['age'].astype(float) #changes 'age' type from object to float.
df3.dtypes
df3['age'].mean() #now with float type we can use mean function to see mean for 'age' column.

