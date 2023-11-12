# import the necessary libraries
import pandas as pd
import numpy as np
from IPython.core.display import display, HTML
display(HTML("<style>.container { width:90% !important; }</style>"))

# read the data 
data = pd.read_csv('Housing.csv')
data.columns = data.columns.str.upper()   #convert the columns to uppercase 
data