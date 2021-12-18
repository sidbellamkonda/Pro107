import csv
import plotly.express as px
import pandas as pd

df = pd.read_csv('class107.csv')
mean = df.groupby(["student_id", "level"], as_index = False)["attempt"].mean()
print(mean)

fig = px.scatter(mean, x = "student_id", y = "level", size = "attempt", color = "attempt")

fig.show()