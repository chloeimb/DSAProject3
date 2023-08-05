import math

class GreedyTwoOpt:
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
            distance = self.cities_distance(current, self.cities[next_city])
            if distance < closest_dist:
                closest = next_city
                closest_dist = distance

        return closest, closest_dist

    def solve_greedy(self):
        self.tour = [0]
        others = list(range(1, self.num_cities))

        while others:
            current = self.cities[self.tour[-1]]
            closest, _ = self.find_closest(current, [self.cities[i] for i in others])
            self.tour.append(self.cities.index(closest))
            others.remove(closest)

        self.tour.append(self.tour[0])
        return self.tour

    def two_opt_swap(self, tour, i, j):
        new_tour = tour[:i] + tour[i:j + 1][::-1] + tour[j + 1:]
        return new_tour

    def two_opt(self, tour):
        best_tour = tour
        improved = True

        while improved:
            improved = False
            for i in range(1, self.num_cities - 2):
                for j in range(i + 1, self.num_cities):
                    if j - i == 1:
                        continue  # No improvement if indices are adjacent
                    new_tour = self.two_opt_swap(tour, i, j)
                    if self.calculate_tour_distance(new_tour) < self.calculate_tour_distance(best_tour):
                        best_tour = new_tour
                        improved = True

            tour = best_tour

        return best_tour

    def calculate_tour_distance(self, tour):
        distance = 0
        for i in range(len(tour) - 1):
            distance += self.cities_distance(self.cities[tour[i]], self.cities[tour[i + 1]])
        return distance

    def solve(self):
        greedy_tour = self.solve_greedy()
        optimized_tour = self.two_opt(greedy_tour)
        return optimized_tour