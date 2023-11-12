import pandas as pd


# import the library
from autoviz import AutoViz_Class
# from autoviz.AutoViz_Class import AutoViz_Class


# read the data 
data = pd.read_csv('Housing.csv')

av = AutoViz_Class()
avt = av.AutoViz("",dfte = data,header = 0,verbose = 1,lowess = False,
      chart_format = "server",max_rows_analyzed = 10000,max_cols_analyzed = 10,
      save_plot_dir=None)


