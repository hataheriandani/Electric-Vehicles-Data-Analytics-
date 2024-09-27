import pandas as pd
import lightningchart as lc
import time

# Set LightningChart license
lc.set_license('my_license_key')

# Data for company production in 2023
data_2023 = {
    'company': ['BYD', 'Hyundai', 'Mercedes-Benz', 'MG', 'Nissan', 'Other', 'Tesla', 'Toyota', 'Volkswagen', 'Wuling'],
    '2023': [15.6, 1.9, 1.6, 1.7, 2.5, 19.5, 39.4, 4.2, 4.5, 3.4]
}

# Convert data to DataFrame
df_2023 = pd.DataFrame(data_2023)
df_2023.set_index('company', inplace=True)

# Create dashboard with 2 rows
dashboard = lc.Dashboard(theme=lc.Themes.Dark, rows=2, columns=1)

# Row 1: Vertical BarChart for 2023 production data
bar_chart_2023 = dashboard.BarChart(row_index=0, column_index=0, vertical=True)

# Prepare data for BarChart 2023
bar_data_2023 = [
    {"category": company, "value": value}
    for company, value in zip(df_2023.index, df_2023['2023'].values)
]

# Set data and title for 2023 BarChart
bar_chart_2023.set_data(bar_data_2023)
bar_chart_2023.set_title("Company Production in 2023")

# Disable sorting to prevent automatic sorting of bars
bar_chart_2023.set_sorting('disabled')

# Apply color palette to the 2023 BarChart
bar_chart_2023.set_palette_colors(
    steps=[
        {'value': 0, 'color': lc.Color('blue')}, 
        {'value': 0.5, 'color': lc.Color('yellow')}, 
        {'value': 1, 'color': lc.Color('red')}
    ],
    percentage_values=True
)

# Data for live BarChart (Row 2)
data = {
    'Brands': ['Tesla', 'BYD Auto', 'Geely Holdings', 'Others'],
    'Q3 2022': [17, 13, 5, 65],
    'Q4 2022': [17, 14, 7, 62],
    'Q1 2023': [22, 14, 8, 56],
    'Q2 2023': [20, 15, 6, 59],
    'Q3 2023': [17, 17, 6, 60],
    'Q4 2023': [16, 18, 6, 60],
    'Q1 2024': [20, 15, 8, 57],
    'Q2 2024': [17, 17, 7, 59]
}

# Convert data to DataFrame
df = pd.DataFrame(data)
df.set_index('Brands', inplace=True)

# Convert DataFrame values to standard int type
df = df.applymap(int)

# Row 2: Horizontal BarChart for live data
bar_chart_live = dashboard.BarChart(row_index=1, column_index=0, vertical=False)

# Apply color palette to the live BarChart
bar_chart_live.set_palette_colors(
    steps=[
        {'value': 0, 'color': lc.Color('blue')}, 
        {'value': 0.5, 'color': lc.Color('yellow')}, 
        {'value': 1, 'color': lc.Color('red')}
    ],
    percentage_values=True
)

# Function to update live BarChart for each quarter
def update_bar_chart_for_quarter(quarter):
    data_for_quarter = df[quarter]

    # Prepare data for BarChart
    bar_data = [
        {"category": brand, "value": int(value)} 
        for brand, value in zip(data_for_quarter.index, data_for_quarter.values)
    ]

    # Update BarChart data
    bar_chart_live.set_data(bar_data)
    
    bar_chart_live.set_title(f"Global EV Market Share by Brand - {quarter}")

    bar_chart_live.set_palette_colors(
       steps=[
           {'value': 0, 'color': lc.Color('green')}, 
           {'value': 0.33, 'color': lc.Color('yellow')},
           {'value': 0.66, 'color': lc.Color('orange')},
           {'value': 1, 'color': lc.Color('green')}  
       ],
       percentage_values=True
   )


# Function to simulate real-time updates for the live BarChart
def update_dashboard():
    quarters = ['Q3 2022', 'Q4 2022', 'Q1 2023', 'Q2 2023', 
                'Q3 2023', 'Q4 2023', 'Q1 2024', 'Q2 2024']
    for quarter in quarters:
        print(f"Updating data for quarter: {quarter}")
        update_bar_chart_for_quarter(quarter)
        time.sleep(2)  # Simulate real-time updates with a 2-second delay

# Open dashboard and start real-time updates
dashboard.open(live=True)
update_dashboard()
