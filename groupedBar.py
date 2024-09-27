import pandas as pd
import lightningchart as lc

# Set your license key
lc.set_license('my_license_key')

# Load the dataset
file_path = 'C:/Users/Taheri/Desktop/darsi/m8.5/workplacement/project 8/revenue1.xlsx'
df = pd.read_excel(file_path)
years = df['year'].astype(str).tolist() 
battery_ev = df['Battery Electric Vehicles'].tolist()
plug_in_hybrid_ev = df['Plug-in Hybrid Electric Vehicles'].tolist()
total_revenue = df['Total'].tolist()

# Prepare the data in the format for grouped bar chart
data = [
    {'subCategory': 'Battery Electric Vehicles', 'values': battery_ev},
    {'subCategory': 'Plug-in Hybrid Electric Vehicles', 'values': plug_in_hybrid_ev},
    {'subCategory': 'Total Revenue', 'values': total_revenue},
]

# Create the grouped bar chart
chart = lc.BarChart(
    vertical=True,
    theme=lc.Themes.Dark,
    title='Electric Vehicles Revenue (2016-2029)'
)
chart.set_sorting('disabled')
# Set the data to be grouped by year
chart.set_data_grouped(
    years,
    data
)
# Add a legend and open the chart
chart.add_legend(x=18,y=44).add(chart)
chart.open()
