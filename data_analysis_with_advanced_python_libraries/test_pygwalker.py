# import the library
import pygwalker as pyg

import pandas as pd

# read the data 
data = pd.read_csv('Housing.csv')

# run the code
pyg.walk(data)