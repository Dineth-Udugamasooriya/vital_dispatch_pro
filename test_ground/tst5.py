import math

# Take user inputs for the number of current ambulance locations and demand locations
num_current_ambulance_locations = int(input("Enter the number of current ambulance locations: "))
num_demand_locations = int(input("Enter the number of demand locations: "))

# Take user inputs for the coordinates of current ambulance locations
current_ambulance_locations = {}
for i in range(num_current_ambulance_locations):
    location_name = input("Enter the name of current ambulance location {}: ".format(i + 1))
    x = float(input("Enter the x-coordinate for {}: ".format(location_name)))
    y = float(input("Enter the y-coordinate for {}: ".format(location_name)))
    current_ambulance_locations[location_name] = (x, y)

# Take user inputs for the coordinates of demand locations
demand_locations = {}
for i in range(num_demand_locations):
    location_name = input("Enter the name of demand location {}: ".format(i + 1))
    x = float(input("Enter the x-coordinate for {}: ".format(location_name)))
    y = float(input("Enter the y-coordinate for {}: ".format(location_name)))
    demand_locations[location_name] = (x, y)

numberOfAmbulances = int(input("Enter the number of ambulances: "))

# Rest of the code remains the same as before

def calculate_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

least_distances = {}
assigned_counts = {}

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

print("Closest current_ambulance_locations for demand_locations:")
print(least_distances)

print("\nNumber of demand_locations assigned to each current_ambulance_locations:")
for location_key, count in assigned_counts.items():
    print(f"{location_key}: {count}")

# Calculate proportions
total_count = sum(assigned_counts.values())
proportions = {location_key: count / total_count for location_key, count in assigned_counts.items()}

print("\nDistribution of ambulances:")
ambulance_distribution = {location_key: proportions.get(location_key, 0) * numberOfAmbulances
                          for location_key in current_ambulance_locations}

for location_key, count in ambulance_distribution.items():
    print(f"{location_key}: {math.floor(count)}")

# Calculate remaining ambulances
ambulance_distribution_sum = sum(math.floor(value) for value in ambulance_distribution.values())
remaining_ambulances = numberOfAmbulances - ambulance_distribution_sum
print("\nNumber of remaining ambulances:", remaining_ambulances)
