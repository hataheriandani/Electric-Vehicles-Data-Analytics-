import pandas as pd
from lightningchart import Themes, Chart3D

# Set license key
my_license_key = 'Your license key'

# Load data
file_path = 'C:/Users/Taheri/Desktop/darsi/m8.5/workplacement/project 8/ElectricCarData_Clean.csv'
data = pd.read_csv(file_path)

# Select relevant columns (Top Speed, Range, and Price)
columns = ['Brand', 'Model', 'TopSpeed_KmH', 'Range_Km', 'PriceEuro']
filtered_data = data[columns].dropna()

# Get lists for each axis
brands = filtered_data['Brand'].tolist()
top_speeds = filtered_data['TopSpeed_KmH'].tolist()
ranges = filtered_data['Range_Km'].tolist()
# Divide prices by 1000
prices = (filtered_data['PriceEuro'] / 1000).tolist()

# Create 3D chart
chart_3d = Chart3D(
    theme=Themes.Dark,
    title='Comparison of Cars on Top Speed, Range, and Price',
    license=my_license_key
)

# Add box series for Top Speed
box_series_speed = chart_3d.add_box_series()
box_series_speed.set_name('Top Speed (Km/h)')

data_boxes_speed = [
    {
        'xCenter': i * 4 + 1,
        'yCenter': top_speeds[i] / 2,
        'zCenter': 0,
        'xSize': 4,
        'ySize': top_speeds[i],
        'zSize': 0.1
    }
    for i in range(len(brands))
]

box_series_speed.add(data_boxes_speed)

# Add box series for Range
box_series_range = chart_3d.add_box_series()
box_series_range.set_name('Range (Km)')

data_boxes_range = [
    {
        'xCenter': i * 4 + 2,
        'yCenter': ranges[i] / 2,
        'zCenter': 1,
        'xSize': 4,
        'ySize': ranges[i],
        'zSize': 0.1
    }
    for i in range(len(brands))
]

box_series_range.add(data_boxes_range)

# Add box series for Price
box_series_price = chart_3d.add_box_series()
box_series_price.set_name('Price (1000 Euro)')

data_boxes_price = [
    {
        'xCenter': i * 4 + 3,
        'yCenter': prices[i] / 2,
        'zCenter': 2,
        'xSize': 4,
        'ySize': prices[i],
        'zSize': 0.1
    }
    for i in range(len(brands))
]

box_series_price.add(data_boxes_price)

# Open the chart in browser
chart_3d.open(method='browser')
