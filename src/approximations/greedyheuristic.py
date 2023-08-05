import math

class Greedy:
    def __init__(self, cities):
        self.cities = cities
        self.num_cities = len(cities)
        self.tour = []

    def cities_distance(self, city1, city2): 
        return math.sqrt((city1.x - city2.x)**2 + (city1.y - city2.y)**2)

    def find_closest(self, current, others):
        closest = None
        closest_dist = float('inf')

        for next_city in others:
            distance = self.cities_distance(current, next_city)
            if distance < closest_dist:
                closest = next_city
                closest_dist = distance

        return closest, closest_dist
    
    def solve(self):
        self.tour = [0]
        others = list(range(1, self.num_cities))

        while others:
            current = self.cities[self.tour[-1]]
            closest, _ = self.find_closest(current, [self.cities[i] for i in others])
            self.tour.append(self.cities.index(closest))
            others.remove(closest)

        self.tour.append(self.tour[0])
        return self.tour
