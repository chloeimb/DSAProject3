import math

def e_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1]**2))


def total_distance(route, cities):
    total = 0
    for i in range(len(route) - 1):
        total += e_distance(cities[route[i], cities[route[i + 1]]])
    return total

def swap_2opt(route, i, k):
    new_route = route[:i] + route[i:k+1][::-1] + route[k+1:]
    return new_route

def two_opt(cities, route):
    best = route
    better = True

    while better:
        better = False
        for i in range(i, len(cities) - 1):
            for k in range(i + 1, len(cities)):
                new_route = swap_2opt(best, i, k)
                new_dist = total_distance(new_route, cities)
                if new_dist < total_distance(best, cities):
                    best = new_route
                    better = True

    return best