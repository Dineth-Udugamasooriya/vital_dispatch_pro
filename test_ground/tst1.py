from pulp import *

current_ambulance_locations = {'A1': (1,2), 'A2': (3,4), 'A3': (5,6)}
hospitals = {'H1': (3,3), 'H2': (4,2), 'H3': (5,1)}
demand_locations = {'D1': (3,9), 'D2': (4,1), 'D3': (9,9), 'D4': (5,1)}

def calculate_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

prob = LpProblem("AmbulanceLocation", LpMinimize)

ambulance_locations = list(current_ambulance_locations.keys()) + ['New_{}'.format(i) for i in range(len(demand_locations))]
x = LpVariable.dicts("AmbulanceLocation", ambulance_locations, cat='Binary')
y = LpVariable.dicts("ServeDemand", (ambulance_locations, demand_locations), cat='Binary')

prob += lpSum(calculate_distance(current_ambulance_locations[amb_loc], demand_locations[dem_loc]) * y[amb_loc][dem_loc]
              for amb_loc in current_ambulance_locations
              for dem_loc in demand_locations)

for dem_loc in demand_locations:
    prob += lpSum(y[amb_loc][dem_loc] for amb_loc in current_ambulance_locations) >= 1

for dem_loc in demand_locations:
    for amb_loc in current_ambulance_locations:
        prob += y[amb_loc][dem_loc] <= x[amb_loc]

for amb_loc in current_ambulance_locations:
    prob += x[amb_loc] == 1

prob.solve()

print("Optimal solution:")
for amb_loc in ambulance_locations:
    if x[amb_loc].varValue == 1:
        print("Ambulance station {} is located.".format(amb_loc))
