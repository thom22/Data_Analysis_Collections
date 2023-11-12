# import the library

import pandas as pd
import numpy as np
from IPython.core.display import display, HTML
import dtale


#display(HTML("<style>.container { width:90% !important; }</style>"))

# read the data 
data = pd.read_csv('Housing.csv')
# data.columns = data.columns.str.upper()   #convert the columns to uppercase 
# data



#view the data analysis result inside your editor 
dtale.show(data)

# open the analysis in browser
dtale.show(data).open_browser()