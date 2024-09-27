import pandas as pd
import lightningchart as lc
import time

lc.set_license('my_license_key')
file_path = '/IEA Global EV Data 2024.csv'
df = pd.read_csv(file_path)

regions_of_interest = ['Norway', 'China', 'Europe', 'USA', 'India','Brazil','Rest of the world','Sweden','Japan','Korea','Germany','France','Finland','Canada','Denmark','Turkiye']

# Create filtered data for PHEV
filtered_data_phev = df[(df['region'].isin(regions_of_interest)) & 
                        (df['powertrain'] == 'PHEV') & 
                        (df['year'].between(2011, 2023)) & 
                        (df['unit'] == 'Vehicles')]

# Create filtered data for BEV
filtered_data_bev = df[(df['region'].isin(regions_of_interest)) & 
                       (df['powertrain'] == 'BEV') & 
                       (df['year'].between(2011, 2023)) & 
                       (df['unit'] == 'Vehicles')]

# Create pivot tables to show the PHEV and BEV values for each region by year
pivot_data_phev = filtered_data_phev.pivot_table(index='year', columns='region', values='value', aggfunc='sum').fillna(0)
pivot_data_bev = filtered_data_bev.pivot_table(index='year', columns='region', values='value', aggfunc='sum').fillna(0)

# Setup the dashboard with 2 rows
dashboard = lc.Dashboard(theme=lc.Themes.Dark, rows=2, columns=1)

# Row 1: Bar chart for PHEV vehicles
bar_chart_phev = dashboard.BarChart(row_index=0, column_index=0, vertical=False)

# Row 2: Bar chart for BEV vehicles
bar_chart_bev = dashboard.BarChart(row_index=1, column_index=0, vertical=False)

# Function to update the PHEV bar chart for each year
def update_bar_chart_for_phev(year):
    data_for_year_phev = pivot_data_phev.loc[year]

    # Prepare the data for the PHEV bar chart (list of dicts)
    bar_data_phev = [
        {"category": region, "value": value}
        for region, value in zip(data_for_year_phev.index, data_for_year_phev.values)
    ]

    # Update the PHEV bar chart
    bar_chart_phev.set_data(bar_data_phev)
    
    # Set the title for the PHEV chart
    bar_chart_phev.set_title(f"PHEV Vehicles by Country - Year {year}")

# Function to update the BEV bar chart for each year
def update_bar_chart_for_bev(year):
    data_for_year_bev = pivot_data_bev.loc[year]

    # Prepare the data for the BEV bar chart (list of dicts)
    bar_data_bev = [
        {"category": region, "value": value}
        for region, value in zip(data_for_year_bev.index, data_for_year_bev.values)
    ]

    # Update the BEV bar chart
    bar_chart_bev.set_data(bar_data_bev)
    
    # Set the title for the BEV chart
    bar_chart_bev.set_title(f"BEV Vehicles by Country - Year {year}")

# Function to simulate real-time updates
def update_dashboard():
    for year in range(2011, 2024):
        print(f"Updating data for year: {year}")
        update_bar_chart_for_phev(year)
        update_bar_chart_for_bev(year)
        time.sleep(2) 

# Open the dashboard and start real-time updates
dashboard.open(live=True)
update_dashboard()
