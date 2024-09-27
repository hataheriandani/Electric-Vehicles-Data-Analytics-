import lightningchart as lc
import time
import numpy as np

# Set your LightningChart license key
lc.set_license('my_license_key')

# Data for Tesla, Volkswagen, BMW, Mercedes, and Skoda
car_data = {
    "Tesla": {"AccelSec": 4.4, "TopSpeed_KmH": 100},
    "Volkswagen": {"AccelSec": 10, "TopSpeed_KmH": 100},
    "BMW": {"AccelSec": 6.8, "TopSpeed_KmH": 100},
    "Mercedes": {"AccelSec": 5.1, "TopSpeed_KmH": 100},
    "Skoda CITIGOe iV": {"AccelSec": 12.3, "TopSpeed_KmH": 100}, 
}

# Define gauge properties
gauge_intervals = {
    "AccelSec": (0, 15), 
    "TopSpeed_KmH": (0, 250),
}

# Define color bands for gauges
gauge_colors = {
    "AccelSec": [
        {'start': 0, 'end': 5, 'color': lc.Color('green')},
        {'start': 5, 'end': 10, 'color': lc.Color('yellow')},
        {'start': 10, 'end': 15, 'color': lc.Color('red')}
    ]
}

# Function to create live gauges and line chart in LightningChart
def create_live_dashboard():
    # Create a dashboard with 2 rows and 5 columns (one column for each car)
    dashboard = lc.Dashboard(theme=lc.Themes.Dark, rows=2, columns=5)

    # Function to create a gauge chart with a title
    def create_gauge(row, column, title, value, value_range, value_indicators):
        chart = dashboard.GaugeChart(row_index=row, column_index=column)
        chart.set_angle_interval(start=225, end=-45)
        chart.set_interval(start=value_range[0], end=value_range[1])
        chart.set_value(value)
        chart.set_value_indicators(value_indicators)
        chart.set_bar_thickness(40)
        chart.set_value_indicator_thickness(10)
        chart.set_title(title) 
        return chart

    # Create gauges for Tesla, Volkswagen, BMW, Mercedes, and Skoda
    tesla_gauge = create_gauge(0, 0, "Tesla (0-100 km/h)", 0, gauge_intervals["AccelSec"], gauge_colors["AccelSec"])
    volkswagen_gauge = create_gauge(0, 1, "Volkswagen (0-100 km/h)", 0, gauge_intervals["AccelSec"], gauge_colors["AccelSec"])
    bmw_gauge = create_gauge(0, 2, "BMW (0-100 km/h)", 0, gauge_intervals["AccelSec"], gauge_colors["AccelSec"])
    mercedes_gauge = create_gauge(0, 3, "Mercedes (0-100 km/h)", 0, gauge_intervals["AccelSec"], gauge_colors["AccelSec"])
    skoda_gauge = create_gauge(0, 4, "Skoda CITIGOe iV (0-100 km/h)", 0, gauge_intervals["AccelSec"], gauge_colors["AccelSec"]) 

    # Line Chart for speed over time in row 2
    chart_speed = dashboard.ChartXY(row_index=1, column_index=0, column_span=5, title="Speed over Time (0-100 km/h)")
    chart_speed.get_default_x_axis().set_title("Time (seconds)")
    chart_speed.get_default_y_axis().set_title("Speed (km/h)")

    series_dict = {}
    for car in car_data.keys():
        series = chart_speed.add_line_series()
        series.set_name(f"{car} Speed")
        series_dict[car] = series

    def update_charts():
        max_time = 13 
        time_step = 0.1 

        time_data = np.arange(0, max_time, time_step) 


        for t in time_data:
            for car in car_data.keys():
                accel_time = car_data[car]["AccelSec"]
                top_speed = car_data[car]["TopSpeed_KmH"]

                speed = min(t / accel_time * top_speed, top_speed)

                series_dict[car].add(t, speed)

                if car == "Tesla" and t <= car_data["Tesla"]["AccelSec"]:
                    tesla_gauge.set_value(t)
                if car == "Volkswagen" and t <= car_data["Volkswagen"]["AccelSec"]:
                    volkswagen_gauge.set_value(t)
                if car == "BMW" and t <= car_data["BMW"]["AccelSec"]:
                    bmw_gauge.set_value(t)
                if car == "Mercedes" and t <= car_data["Mercedes"]["AccelSec"]:
                    mercedes_gauge.set_value(t)
                if car == "Skoda CITIGOe iV" and t <= car_data["Skoda CITIGOe iV"]["AccelSec"]:
                    skoda_gauge.set_value(t)

            time.sleep(time_step)

    # Open the dashboard and start real-time updates
    dashboard.open(live=True)
    update_charts()

# Run the function to create the dashboard
if __name__ == '__main__':
    create_live_dashboard()
