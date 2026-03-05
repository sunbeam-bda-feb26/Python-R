# matplotlib
# - used for data visualization
# - visualization
#   - converting the data into graphs/charts/diagrams/tables
# - graph vs chart
#   - graph: has a proper scale and drawn on graph paper
#   - chart: does not have any proper scale and does not require graph paper

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def function1():
    # data source
    salaries = np.array([20, 30, 35, 45, 49, 80, 84, 90, 87, 96])
    positions = np.arange(len(salaries))

    # create a scatter chart
    plt.scatter(positions, salaries, label="Salary")

    # add title on x axis
    plt.xlabel("position of a person")

    # add title on y axis
    plt.ylabel("Salary")

    # add a title for the chart
    plt.title("Salaries")

    # show the grid lines
    plt.grid()

    # show the legend
    plt.legend()

    # render and show the chart
    plt.show()

# function1()


def function2():
    # read the data from csv file
    df = pd.read_csv('Salary_Data.csv')
    
    # create a scatter plot
    plt.scatter(df['YearsExperience'], df['Salary'], label="Salary", color="green")

    # set the labels
    plt.xlabel("Experience in years")
    plt.ylabel("Salary")
    plt.title("Experience vs Salary")

    # enable grid lines
    plt.grid()
    
    # enable legend
    plt.legend()

    # render and show the chart
    plt.show()

# function2()

def function3():
    # read the data from csv file
    df = pd.read_csv('Salary_Data.csv')
    
    # create a line chart / plot
    plt.plot(df['YearsExperience'], df['Salary'], label="Salary", color="green")

    # create a scatter plot
    plt.scatter(df['YearsExperience'], df['Salary'], label="Salary", color="green")

    # set the labels
    plt.xlabel("Experience in years")
    plt.ylabel("Salary")
    plt.title("Experience vs Salary")

    # enable grid lines
    plt.grid()
    
    # enable legend
    plt.legend()

    # render and show the chart
    plt.show()

# function3()

def function4():
    # data source for bar plot
    marks = [20, 45, 10, 50, 39]
    positions = np.arange(len(marks))

    # create a bar chart
    plt.bar(positions, marks, color="orange", label="Marks")

    # create a scatter plot
    plt.scatter(positions, marks, color="blue")

    # create a line plot
    plt.plot(positions, marks, color="blue")

    # set the labels
    plt.xlabel("Position")
    plt.ylabel("Marks")
    plt.title("Student Exam Score Card")

    # enable grid lines
    plt.grid()
    
    # enable legend
    plt.legend()

    # save the chart to the disk
    plt.savefig("chart.jpg")

    # show the chart
    plt.show()

# function4()

def function5():
    # data source for bar plot
    marks = [20, 45, 10, 50, 39]
    
    # create the labels
    subjects = ["computers", "maths", "english", "science", "social science"]

    # explod values
    explod_values = [0.0, 0.0, 0.1, 0.0, 0.0]

    # create a pie chart
    plt.pie(marks, explode=explod_values, labels=subjects)

    # set the labels
    plt.title("Student Exam Score Card")

    # save the chart to the disk
    # NOTE: call this function before the show()
    plt.savefig("chart.jpg")

    # show the chart
    plt.show()

function5()