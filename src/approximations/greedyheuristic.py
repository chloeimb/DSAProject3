import math

def e_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def closest_city(curr_city, other_cities):
    nearest_city = None
    nearest_dist = float('inf')

    for next_city in other_cities:
        distance = e_distance(curr_city, next_city)
        if distance < nearest_dist:
            nearest_city = next_city
            nearest_dist = distance

    return nearest_city, nearest_dist

def greedy(cities):
    num_cities = len(cities)
    tour = [0]
    remaining = list(range(1, num_cities))

    while remaining:
        curr = cities[tour[-1]]
        nearest_city, nearest_distance = closest_city(curr, [cities[i] for i in remaining])
        tour.append(cities.index(nearest_city))
        remaining.remove(nearest_city)

    tour.append(tour[0])
    return tour