
import pandas as pd

# import the library
from pandas_profiling import ProfileReport

# read the data 
data = pd.read_csv('Housing.csv')

# view the analysis result inside jupyter
prof = ProfileReport(data,  minimal=True, title="DATA ANALYSIS REPORT")
prof

# save the analysis to html
prof.to_file(output_file='PANDAS_PROFILING_ANALYSIS.html')