import math

class TwoOpt:
    def __init__(self, cities, tour):
        self.cities = cities
        self.tour = tour

    def cities_distance(self, city1, city2):
        return math.sqrt((city1.x - city2.x)**2 + (city1.y - city2.y)**2)

    def total_distance(self):
        total = 0
        for i in range(len(self.tour) - 1):
            total += self.cities_distance(self.cities[self.tour[i]], self.cities[self.tour[i+1]])

        return total
    
    def swap(self, i, k):
        new_tour = self.tour[:i] + self.tour[i:k+1][::-1] + self.tour[k+1:]
        return new_tour
    
    def improve(self):
        best = self.tour.copy() 
        better = True

        while better:
            better = False
            for i in range(1, len(self.cities) - 1):
                for j in range(i + 1, len(self.cities)):
                    new_tour = self.swap(i, j)
                    new_dist = self.total_distance()
                    if new_dist < self.total_distance():
                        best = new_tour
                        better = True

        self.tour = best
        return self.tour