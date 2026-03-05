# data frame
# - 2d array
# - it has rows and columns
# - constructed using multiple columns (which are series)
# - every column in data frame is a series object

# pre-defined values
# - NaN: not a number (considered as a missing value -> NA)
# - Inf: infinity

import pandas as pd


def function1():
    # data frame with 2d collection
    df = pd.DataFrame([
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]
    ])
    print(df)

# function1()

def function2():
    # data frame using list of dictionaries
    df = pd.DataFrame([
        {"name": "person1", "age": 30, "address": "pune", "email": "person1@test.com"},
        {"name": "person2", "age": 20, "address": "mumbai"},
        {"name": "person3", "age": 60, "address": "satara", "email": "person3@test.com"},
        {"name": "person4", "age": 40, "address": "nashik", "email": "person4@test.com"},
        {"name": "person5", "age": 89,  "email": "person5@test.com"}
    ])
    print(df)
    print("-" * 80)

    print(f"#dimension     = {df.ndim}")
    print(f"shape          = {df.shape}")
    print(f"columns        = {df.columns}")
    
    # separate the rows and cols
    rows, cols = df.shape
    print(f"rows           = {rows}")
    print(f"cols           = {cols}")
    print('-' * 80)

    # object: string
    print(f"data types")
    print(df.dtypes)

# function2()

def function3():
    # read the data from csv file
    df = pd.read_csv("nba.csv")
    print(df)
    print('-' * 80)

    # attributes
    print(f"columns     = {df.columns}")
    print(f"shape       = {df.shape}")
    print('-' * 80)

    # methods

    # get only first 5 rows
    # print(df.head())

    # get only first 10 rows
    # print(df.head(10))

    # get only last 5 rows
    # print(df.tail())

    # get only last 10 rows
    # print(df.tail(10))

    # get all the information (summary) about the data frame
    # df.info()

    # get statistical information about the df
    # print(df.describe())

# function3()

def function4():
    # read the data from csv file
    df = pd.read_csv("nba.csv")
    
    # get name of all the players (series object)
    # read a column values
    # print(df['Name'])

    # get the column Team
    # print(df['Team'])

    # get multple columns at once (returns a df)
    # print(df[['Name', 'Salary', 'Team']])

# function4()

def function5():
    # read the data from csv file
    df = pd.read_csv("nba.csv")

    # iloc
    # - used to read the data from a data frame
    # - syntax
    #   - df.iloc[<row>, <col>]

    # read the values using column and row index positions
    # use iloc (ith location) to read the values
    # print(df.iloc[0, 0])

    # read all information about the first player
    # read entire row at 0th position
    # print(df.iloc[0, [0, 1, 2, 3, 4, 5, 7, 8]])
    # print(df.iloc[0, 0:9])
    # print(df.iloc[0, :9])
    # print(df.iloc[0, :])

    # find name, team and salary of 2nd, 5th and 10th player
    # print(df.iloc[[1, 4, 9], [0, 1, 8]])

    # find name, team, number and position of first 10 players
    # print(df.iloc[:10, :4])

# function5()

def function6():
    # read the data from csv file
    df = pd.read_csv("nba.csv")

    print(df.columns)
    print('-' * 80)

    # add a new column named Bonus
    df['Bonus'] = df['Salary'] * 0.10

    print(df.columns)
    print('-' * 80)

    # add a new column named New Salary
    df['New Salary'] = df['Salary'] + df['Bonus']

    print(df.columns)
    print('-' * 80)

    print(df)

    # save the updated df to the disk
    df.to_csv("nba_new.csv")

# function6()

def function7():
    # read the data from csv file
    df = pd.read_csv("nba.csv")
    print(df.columns)
    print('-' * 80)

    # remove a column
    # using del keyword only one column can be deleted at a time
    del df['College']
    print(df.columns)
    print('-' * 80)

    # remove multiple columns
    # axis = 0 => row
    # axis = 1 => column
    # by default, drop method does not modify the existing df
    # instead it returns a new df performing the operation
    # new_df = df.drop(['Team', 'Position', 'Number'], axis=1)
    # print(new_df.columns)
    # print('-' * 80)

    # remove multiple columns from existing df
    # do not return the newly modifed df
    df.drop(['Team', 'Position', 'Number'], axis=1, inplace=True)
    print(df.columns)
    print('-' * 80)

    # save the updated df to the disk
    df.to_csv("nba_new.csv")
    df.to_excel('new_nba.xlsx')

# function7()

def function8():
    # read data from json file
    persons = pd.read_json('persons.json')
    print(persons)
    print('-' * 80)

    # drop a row at 1st position
    persons.drop([1], axis=0, inplace=True)
    print(persons)
    print('-' * 80)

    # save the contents into excel file
    persons.to_excel('persons.xlsx')

function8()