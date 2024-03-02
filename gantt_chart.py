import plotly.express as px
import pandas as pd

# Load the CSV file
df = pd.read_csv('data.csv')

# Convert the date columns to datetime format
df['Start Date'] = pd.to_datetime(df['Start Date'])
df['End Date'] = pd.to_datetime(df['End Date'])

# Create the Gantt chart with reversed order
fig = px.timeline(df, x_start="Start Date", x_end="End Date", y="Task", title="Reversed Gantt Chart",
                   labels={'Task': 'Task', 'Start Date': 'Start Date', 'End Date': 'End Date'},
                   category_orders={"Task": df['Task'][::-1]})

# Show the reversed Gantt chart
fig.show()
