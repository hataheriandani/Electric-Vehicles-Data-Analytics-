from PIL import Image, ImageTk
import tkinter as tk
import lightningchart as lc
import multiprocessing

# Set your LightningChart license key
lc.set_license('my_license_key')

# Data for Tesla Model 3 Long Range Dual Motor
tesla_data = {
    "AccelSec": 4.4, 
    "TopSpeed_KmH": 233,  
    "Range_Km": 580 
}

# Data for Volkswagen ID.3 Pure
volkswagen_data = {
    "AccelSec": 10,  
    "TopSpeed_KmH": 160, 
    "Range_Km": 330 
}

# Define gauge properties
gauge_intervals = {
    "AccelSec": (0, 15),  
    "TopSpeed_KmH": (0, 250), 
    "Range_Km": (0, 600) 
}

# Define color bands for gauges
gauge_colors = {
    "AccelSec": [
        { 'start': 0, 'end': 5, 'color': lc.Color('green') }, 
        { 'start': 5, 'end': 10, 'color': lc.Color('yellow') }, 
        { 'start': 10, 'end': 15, 'color': lc.Color('red') } 
    ],
    "TopSpeed_KmH": [
        { 'start': 0, 'end': 100, 'color': lc.Color('red') },
        { 'start': 100, 'end': 200, 'color': lc.Color('yellow') },
        { 'start': 200, 'end': 250, 'color': lc.Color('green') }
    ],
    "Range_Km": [
        { 'start': 0, 'end': 200, 'color': lc.Color('red') },
        { 'start': 200, 'end': 400, 'color': lc.Color('yellow') },
        { 'start': 400, 'end': 600, 'color': lc.Color('green') }
    ]
}

# Function to create gauge charts in LightningChart
def create_gauges():
    # Create a dashboard with 2 rows and 4 columns
    dashboard = lc.Dashboard(theme=lc.Themes.Dark, rows=2, columns=4)

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

    # Create Tesla gauges with titles
    create_gauge(0, 1, "Tesla Acceleration (0-100 km/h)", tesla_data["AccelSec"], gauge_intervals["AccelSec"], gauge_colors["AccelSec"])
    create_gauge(0, 2, "Tesla Top Speed (km/h)", tesla_data["TopSpeed_KmH"], gauge_intervals["TopSpeed_KmH"], gauge_colors["TopSpeed_KmH"])
    create_gauge(0, 3, "Tesla Range (km)", tesla_data["Range_Km"], gauge_intervals["Range_Km"], gauge_colors["Range_Km"])

    # Create Volkswagen gauges with titles
    create_gauge(1, 1, "Volkswagen Acceleration (0-100 km/h)", volkswagen_data["AccelSec"], gauge_intervals["AccelSec"], gauge_colors["AccelSec"])
    create_gauge(1, 2, "Volkswagen Top Speed (km/h)", volkswagen_data["TopSpeed_KmH"], gauge_intervals["TopSpeed_KmH"], gauge_colors["TopSpeed_KmH"])
    create_gauge(1, 3, "Volkswagen Range (km)", volkswagen_data["Range_Km"], gauge_intervals["Range_Km"], gauge_colors["Range_Km"])

    dashboard.open()


# Create a Tkinter window for image and LightningChart display
def show_images_and_gauges():
    window = tk.Tk()
    window.title("Car Images and Gauges")

    tesla_img = Image.open("tesla_image.png") 
    volkswagen_img = Image.open("volkswagen_image.png")

    tesla_img = tesla_img.resize((300, 200)) 
    volkswagen_img = volkswagen_img.resize((300, 200))

    tesla_photo = ImageTk.PhotoImage(tesla_img)
    volkswagen_photo = ImageTk.PhotoImage(volkswagen_img)

    tesla_label = tk.Label(window, image=tesla_photo)
    tesla_label.grid(row=0, column=0)

    volkswagen_label = tk.Label(window, image=volkswagen_photo)
    volkswagen_label.grid(row=1, column=0)

    window.mainloop()

if __name__ == '__main__':
    # Run both Tkinter and LightningChart in separate processes
    p1 = multiprocessing.Process(target=create_gauges)
    p2 = multiprocessing.Process(target=show_images_and_gauges)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
