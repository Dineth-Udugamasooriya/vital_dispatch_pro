import math

current_ambulance_locations = {'A1': (1, 2), 'A2': (3, 4), 'A3': (5, 6), 'A4':(8,8)}
demand_locations = {'D1': (3, 9), 'D2': (4, 1), 'D3': (9, 9), 'D4': (5, 1), 'D5':(3,3), 'D6':(9,9), 'D7':(2,8)}
numberOfAmbulances = 10

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
ambulance_distribution = {location_key: proportions[location_key] * numberOfAmbulances
                          for location_key in current_ambulance_locations}

for location_key, count in ambulance_distribution.items():
    print(f"{location_key}: {count}")
