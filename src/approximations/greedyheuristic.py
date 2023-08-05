import math
import heapq

from .approximation_utils import calc_fitness_memo

class Greedy:
    def __init__(self, cities):
        self.cities = cities
        self.num_cities = len(cities)
        self.tour = []
        self.mst = self.build_tree()
        self.current = 0

    def cities_distance(self, city1, city2): 
        return math.sqrt((city1.x - city2.x)**2 + (city1.y - city2.y)**2)

    def build_tree(self):
        visited =  [False] * self.num_cities

        tree = [[] for _ in range(self.num_cities)]
        visited[0] = True
        heap = [(0, 0)]

        while heap:
            distance, current = heapq.heappop(heap)
            visited[current] = True

            for next_city in range(self.num_cities):
                if not visited[next_city]:
                    distance = self.cities_distance(self.cities[current], self.cities[next_city])
                    heapq.heappush(heap,(distance, next_city))
                    tree[current].append(next_city)
                    tree[next_city].append(current)
        
        return tree
    
    def find_closest(self, current, others):
        closest = None
        closest_dist = float('inf')

        for next_city in others:
            distance = self.cities_distance(current, self.cities[next_city])
            if distance < closest_dist:
                closest = next_city
                closest_dist = distance

        return closest, closest_dist       
                

    def solve(self):
        mst = self.build_tree()
        self.tour = [0]
        current = 0

        while len(self.tour) < self.num_cities:
            closest, _ = self.find_closest(current, mst[current])
            self.tour.append(closest)
            current = closest

        self.tour.append(self.tour[0])
        return self.tour
    

    def run(self): 
        closest, _ = self.find_closest(self.tour[-1], self.mst[self.current])
        self.tour.append(closest)
        self.current += 1

        return calc_fitness_memo(self.tour), len(self.tour) == self.num_cities
    