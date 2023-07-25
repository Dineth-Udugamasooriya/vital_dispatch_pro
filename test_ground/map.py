import matplotlib.pyplot as plt

current_ambulance_locations = {'A1': (1, 2), 'A2': (3, 4), 'A3': (5, 6), 'A4':(8,8)}
demand_locations = {'D1': (3, 9), 'D2': (4, 1), 'D3': (9, 9), 'D4': (5, 1), 'D5':(3,3), 'D6':(9,9), 'D7':(2,8)}

# Extract x and y coordinates of current ambulance locations
current_x = [loc[0] for loc in current_ambulance_locations.values()]
current_y = [loc[1] for loc in current_ambulance_locations.values()]

# Extract x and y coordinates of demand locations
demand_x = [loc[0] for loc in demand_locations.values()]
demand_y = [loc[1] for loc in demand_locations.values()]

# Create the plot
plt.scatter(current_x, current_y, color='blue', label='Current Ambulance Locations')
plt.scatter(demand_x, demand_y, color='red', label='Demand Locations')

# Add labels to the points
for label, (x, y) in current_ambulance_locations.items():
    plt.annotate(label, (x, y), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
for label, (x, y) in demand_locations.items():
    plt.annotate(label, (x, y), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)

# Set axis labels and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Ambulance and Demand Locations')

# Add legend
plt.legend()

# Show the plot
plt.show()
