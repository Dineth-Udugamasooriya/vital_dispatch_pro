import math
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import ttk

# Function to distribute ambulances and display results
def distribute_ambulances():
    # Retrieve inputs from entry fields
    num_current_ambulance_locations = int(num_current_ambulance_entry.get())
    num_demand_locations = int(num_demand_locations_entry.get())
    numberOfAmbulances = int(ambulances_entry.get())

    # Retrieve current ambulance locations
    current_ambulance_locations = {}
    for i in range(num_current_ambulance_locations):
        location_name = current_ambulance_entries[i].get()
        x = float(current_ambulance_x_entries[i].get())
        y = float(current_ambulance_y_entries[i].get())
        current_ambulance_locations[location_name] = (x, y)

    # Retrieve demand locations
    demand_locations = {}
    for i in range(num_demand_locations):
        location_name = demand_locations_entries[i].get()
        x = float(demand_locations_x_entries[i].get())
        y = float(demand_locations_y_entries[i].get())
        demand_locations[location_name] = (x, y)

    # Calculate ambulance distribution
    least_distances = {}
    assigned_counts = {}

    def calculate_distance(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    for demand_key, demand_point in demand_locations.items():
        min_distance = math.inf
        min_location_key = None

        for location_key, location_point in current_ambulance_locations.items():
            distance = calculate_distance(demand_point, location_point)

            if distance < min_distance:
                min_distance = distance
                min_location_key = location_key

        least_distances[demand_key] = min_location_key

        if min_location_key in assigned_counts:
            assigned_counts[min_location_key] += 1
        else:
            assigned_counts[min_location_key] = 1

    # Calculate proportions
    total_count = sum(assigned_counts.values())
    proportions = {location_key: count / total_count for location_key, count in assigned_counts.items()}

    # Calculate ambulance distribution
    ambulance_distribution = {location_key: proportions.get(location_key, 0) * numberOfAmbulances
                              for location_key in current_ambulance_locations}

    # Calculate remaining ambulances
    ambulance_distribution_sum = sum(math.floor(value) for value in ambulance_distribution.values())
    remaining_ambulances = numberOfAmbulances - ambulance_distribution_sum

    # Display results
    result_label.config(text="Results:\n")

    result_label.config(text=result_label.cget("text") +
                             "Closest current_ambulance_locations for demand_locations:\n")
    for demand_key, location_key in least_distances.items():
        result_label.config(text=result_label.cget("text") +
                                 f"{demand_key}: {location_key}\n")

    result_label.config(text=result_label.cget("text") +
                             "\nNumber of demand_locations assigned to each current_ambulance_locations:\n")
    for location_key, count in assigned_counts.items():
        result_label.config(text=result_label.cget("text") +
                                 f"{location_key}: {count}\n")

    result_label.config(text=result_label.cget("text") +
                             "\nDistribution of ambulances:\n")
    for location_key, count in ambulance_distribution.items():
        result_label.config(text=result_label.cget("text") +
                                 f"{location_key}: {math.floor(count)}\n")

    result_label.config(text=result_label.cget("text") +
                             "\nNumber of remaining ambulances: " + str(remaining_ambulances))

    # Plotting current_ambulance_locations and demand_locations
    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    # Plot current_ambulance_locations
    for location_key, location_point in current_ambulance_locations.items():
        x, y = location_point
        ax.plot(x, y, 'ro')
        ax.annotate(f"{location_key}: {math.floor(ambulance_distribution[location_key])}", (x, y),
                    textcoords="offset points", xytext=(0, -15), ha='center', fontsize=8)

    # Plot demand_locations
    for location_key, location_point in demand_locations.items():
        x, y = location_point
        ax.plot(x, y, 'bo')
        ax.annotate(location_key, (x, y), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=8)

    # Plot arrows between current_ambulance_locations and demand_locations
    for demand_key, location_key in least_distances.items():
        demand_point = demand_locations[demand_key]
        current_point = current_ambulance_locations[location_key]
        arrow_coords = np.array([current_point, demand_point])
        ax.arrow(*arrow_coords[0], *(arrow_coords[1] - arrow_coords[0]), length_includes_head=True, head_width=0.3)

    plt.show()

# Create main window
window = tk.Tk()
window.title("Ambulance Distribution")

# Create scrollable frame
canvas = tk.Canvas(window)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar = ttk.Scrollbar(window, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Create frame inside canvas
frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor=tk.NW)

# Number of current ambulance locations
num_current_ambulance_label = tk.Label(frame, text="Enter the number of current ambulance locations:")
num_current_ambulance_label.pack()

num_current_ambulance_entry = tk.Entry(frame)
num_current_ambulance_entry.pack()

# Current ambulance locations
current_ambulance_frame = tk.Frame(frame)
current_ambulance_frame.pack()

current_ambulance_entries = []
current_ambulance_x_entries = []
current_ambulance_y_entries = []

def add_current_ambulance_location():
    index = len(current_ambulance_entries)

    label = tk.Label(current_ambulance_frame, text=f"Current ambulance location {index + 1}:")
    label.pack()

    entry = tk.Entry(current_ambulance_frame)
    entry.pack()
    current_ambulance_entries.append(entry)

    x_label = tk.Label(current_ambulance_frame, text=f"x-coordinate for location {index + 1}:")
    x_label.pack()

    x_entry = tk.Entry(current_ambulance_frame)
    x_entry.pack()
    current_ambulance_x_entries.append(x_entry)

    y_label = tk.Label(current_ambulance_frame, text=f"y-coordinate for location {index + 1}:")
    y_label.pack()

    y_entry = tk.Entry(current_ambulance_frame)
    y_entry.pack()
    current_ambulance_y_entries.append(y_entry)

add_current_ambulance_button = tk.Button(frame, text="Add current ambulance location", command=add_current_ambulance_location)
add_current_ambulance_button.pack()

# Number of demand locations
num_demand_locations_label = tk.Label(frame, text="Enter the number of demand locations:")
num_demand_locations_label.pack()

num_demand_locations_entry = tk.Entry(frame)
num_demand_locations_entry.pack()

# Demand locations
demand_locations_frame = tk.Frame(frame)
demand_locations_frame.pack()

demand_locations_entries = []
demand_locations_x_entries = []
demand_locations_y_entries = []

def add_demand_location():
    index = len(demand_locations_entries)

    label = tk.Label(demand_locations_frame, text=f"Demand location {index + 1}:")
    label.pack()

    entry = tk.Entry(demand_locations_frame)
    entry.pack()
    demand_locations_entries.append(entry)

    x_label = tk.Label(demand_locations_frame, text=f"x-coordinate for location {index + 1}:")
    x_label.pack()

    x_entry = tk.Entry(demand_locations_frame)
    x_entry.pack()
    demand_locations_x_entries.append(x_entry)

    y_label = tk.Label(demand_locations_frame, text=f"y-coordinate for location {index + 1}:")
    y_label.pack()

    y_entry = tk.Entry(demand_locations_frame)
    y_entry.pack()
    demand_locations_y_entries.append(y_entry)

add_demand_location_button = tk.Button(frame, text="Add demand location", command=add_demand_location)
add_demand_location_button.pack()

# Number of ambulances
ambulances_label = tk.Label(frame, text="Enter the number of ambulances:")
ambulances_label.pack()

ambulances_entry = tk.Entry(frame)
ambulances_entry.pack()

# Calculate button
calculate_button = tk.Button(frame, text="Calculate", command=distribute_ambulances)
calculate_button.pack()

# Result label
result_label = tk.Label(frame, text="Results:")
result_label.pack()

# Run the GUI
window.mainloop()
