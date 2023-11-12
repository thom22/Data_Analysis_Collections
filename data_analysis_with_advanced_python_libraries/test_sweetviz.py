import pandas as pd
# analysis report with sweetviz
import sweetviz as sv


# read the data 
data = pd.read_csv('Housing.csv')

# make analysis and assign the target feature
sweet_report = sv.analyze(data , target_feat='PRICE') 

# view the analysis result in browser 
sweet_report.show_html()

# save the analysis result into html
sweet_report.show_html('analysis_with_sweetviz.html', scale=0.92)