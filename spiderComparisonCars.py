import pandas as pd
import lightningchart as lc

# Set your license key
lc.set_license('my_license_key')

# Load the dataset
file_path = '/ElectricCarData_Clean.csv'
data = pd.read_csv(file_path)

columns = ['Brand', 'Model', 'TopSpeed_KmH', 'Range_Km', 'Efficiency_WhKm', 'FastCharge_KmH', 'PriceEuro']

filtered_data = data[columns].dropna()

# Convert columns to numeric, forcing errors to NaN (Not a Number)
filtered_data['TopSpeed_KmH'] = pd.to_numeric(filtered_data['TopSpeed_KmH'], errors='coerce')
filtered_data['Range_Km'] = pd.to_numeric(filtered_data['Range_Km'], errors='coerce')
filtered_data['Efficiency_WhKm'] = pd.to_numeric(filtered_data['Efficiency_WhKm'], errors='coerce')
filtered_data['FastCharge_KmH'] = pd.to_numeric(filtered_data['FastCharge_KmH'], errors='coerce')
filtered_data['PriceEuro'] = pd.to_numeric(filtered_data['PriceEuro'], errors='coerce')

# Drop rows where any conversion resulted in NaN
filtered_data = filtered_data.dropna()

# Normalize data to fit in the radar chart
filtered_data['TopSpeed_KmH'] = (filtered_data['TopSpeed_KmH'] / filtered_data['TopSpeed_KmH'].max()) * 100
filtered_data['Range_Km'] = (filtered_data['Range_Km'] / filtered_data['Range_Km'].max()) * 100
filtered_data['Efficiency_WhKm'] = (filtered_data['Efficiency_WhKm'].max() - filtered_data['Efficiency_WhKm']) / (filtered_data['Efficiency_WhKm'].max() - filtered_data['Efficiency_WhKm'].min()) * 100
filtered_data['FastCharge_KmH'] = (filtered_data['FastCharge_KmH'] / filtered_data['FastCharge_KmH'].max()) * 100
filtered_data['PriceEuro'] = (filtered_data['PriceEuro'].max() - filtered_data['PriceEuro']) / (filtered_data['PriceEuro'].max() - filtered_data['PriceEuro'].min()) * 100


# Adding top 25 cars to the radar chart
top_cars = filtered_data.head(25)

# Create Radar (Spider) Chart
chart = lc.SpiderChart(
    theme=lc.Themes.Dark,
    title='Comparison of Cars on Top Speed, Range, Efficiency, Fast Charge, and Price'
)
chart.set_web_mode('circle')

for index, row in top_cars.iterrows():
    series = chart.add_series()  
    series.set_name(f"{row['Brand']} {row['Model']}") 
    series.add_points([
        {'axis': 'Top Speed (Km/h)', 'value': row['TopSpeed_KmH']},
        {'axis': 'Range (Km)', 'value': row['Range_Km']},
        {'axis': 'Efficiency (Wh/Km)', 'value': row['Efficiency_WhKm']},
        {'axis': 'Fast Charge (Km/h)', 'value': row['FastCharge_KmH']},
        {'axis': 'Price (Euro)', 'value': row['PriceEuro']},
    ])

chart.open()
