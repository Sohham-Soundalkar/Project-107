import pandas as pd
import csv
import plotly.express as pe

data = pd.read_csv('data.csv')
student_info = data.groupby(['student_id', 'level'],as_index=False)['attempt'].mean()
graph = pe.scatter(student_info, x='student_id', y='level', size='attempt', color='attempt')
graph.show()

