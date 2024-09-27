import pandas as pd
import lightningchart as lc
import time

lc.set_license('my_license_key')
file_path = '/project 8/IEA Global EV Data 2024.csv'
df = pd.read_csv(file_path)

regions_of_interest = ['Norway', 'China', 'Europe', 'USA', 'India','Brazil','Rest of the world','Sweden','Japan','Korea','Germany','France','Finland','Canada','Denmark','Turkiye']
filtered_data = df[(df['region'].isin(regions_of_interest)) &
                   (df['powertrain'] == 'PHEV') &
                   (df['year'].between(2011, 2023)) &
                   (df['unit'] == 'Vehicles')]

# Create a pivot table to show the PHEV values for each region by year
pivot_data = filtered_data.pivot_table(index='year', columns='region', values='value', aggfunc='sum').fillna(0)
# Setup the dashboard with 1 row and 1 column
dashboard = lc.Dashboard(theme=lc.Themes.Dark, rows=1, columns=1)
# Create a horizontal Bar Chart for each region
bar_chart = dashboard.BarChart(row_index=0, column_index=0, vertical=False)
# Function to update the chart for each year
def update_bar_chart_for_year(year):
    data_for_year = pivot_data.loc[year]

    bar_data = [
        {"category": region, "value": value}
        for region, value in zip(data_for_year.index, data_for_year.values)
    ]

    bar_chart.set_data(bar_data)
    bar_chart.set_title(f"PHEV Vehicles by Country - Year {year}")


# Function to simulate real-time updates
def update_dashboard():
    for year in range(2011, 2024):
        print(f"Updating data for year: {year}")
        update_bar_chart_for_year(year)
        time.sleep(2)

# Open the dashboard and start real-time updates
dashboard.open(live=True)
update_dashboard()
