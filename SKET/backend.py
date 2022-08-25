# importing necessary packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# reading dataset
global df, graphs, x_variable, y_variable


# = pd.read_csv("california_housing_test.csv")

def readcsv(filename):
    global df
    df = pd.read_csv("california_housing_test.csv")


def clean():
    global df
    print("Cleaning")
    # handling missing values
    df.isnull().sum()

    df.dropna
    df.isnull().sum()


def getcolumns():
    global df
    print("got columns")
    # displaying the columns available
    return df.columns


def xandy(x_val, y_val):
    global df, x_variable, y_variable
    print(f"incoming x {x_val} y {y_val}")
    # determining x and y variables
    var_list = []
    a = 1
    for x in df.columns:
        print(str(a) + "." + str(x))
        var_list.append(x)
        a = a + 1
    columns = df.shape[1]
    x_variable = x_val  # int(input("\nchoose x variable from 1 to " + str(columns) + ":"))
    # this should be replaced with the dropdown selection
    y_variable = y_val  # int(input("\nchoose y variable from 1 to " + str(columns) + ":"))
    # this should also be replaced with the dropdown selection


def det_graph():
    global df, graphs
    # determining the type of graph
    graphs = ['scatter plot', 'bar graph', 'line graph']
    a = 1
    for x in graphs:
        print(str(a) + "." + str(x))
        a = a + 1
    graph_type = 2  # int(input("\nchoose the graph type from 1 to " + str(len(graphs)) + ":"))


"""print(df.columns[x_variable - 1])
print(df.columns[y_variable - 1])
print(graphs[graph_type - 1])"""


def plot_graph(x, y, gtype):
    global df, graphs, x_variable, y_variable
    print(f"incoming x {x} y {y} g {gtype}")
    x_variable = df.columns[x - 1]
    y_variable = df.columns[y - 1]
    graph_type = gtype  # graphs[graph_type - 1]

    if graph_type == 'scatter plot':
        sns.relplot(x=x_variable, y=y_variable, data=df)
    elif graph_type == 'bar graph':
        sns.barplot(x=x_variable, y=y_variable, data=df)
    elif graph_type == 'line graph':
        sns.lineplot(x=x_variable, y=y_variable, data=df)

    plt.savefig('output.png')
