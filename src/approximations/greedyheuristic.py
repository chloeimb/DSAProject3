import numpy as np
import random
import pandas as pd
import math
import heapq


from .approximation_utils import draw_route, calc_fitness_memo, randomize_route, calc_distance

class Greedy:
    def __init__(self, cities):
        self.cities = cities
        self.num_cities = len(cities)
        self.tour = []
        self.mst = self.build_tree()
        self.current = 0

    def build_tree(self):
        visited = [False] * self.num_cities

        mst = [[] for _ in range(self.num_cities)]
        visited[0] = True
        heap = [(0, 0)]

        while heap:
            distance, current = heapq.heappop(heap)
            if visited[current]:
                continue
            visited[current] = True

            for next_city in range(self.num_cities):
                if not visited[next_city]:
                    next_distance = calc_distance(self.cities[current], self.cities[next_city])
                    heapq.heappush(heap, (next_distance, next_city))
                    mst[current].append(next_city)
                    mst[next_city].append(current)

        return mst
    
    def find_closest(self, current, others):
        closest = None
        closest_dist = float('inf')

        for next_city in others:
            distance = calc_distance(self.cities[current], self.cities[next_city])
            if distance < closest_dist:
                closest = next_city
                closest_dist = distance

        return closest, closest_dist       
                

    def solve(self):
        self.tour = [0]
        current = 0

        while len(self.tour) < self.num_cities:
            closest, _ = self.find_closest(current, self.mst[current])
            self.tour.append(closest)
            current = closest

        self.tour.append(self.tour[0])
        return self.tour
    
    def run(self): 
        closest, _ = self.find_closest(self.tour[-1], self.mst[self.current])
        self.tour.append(closest)
        self.current += 1

        return calc_fitness_memo(), len(self.tour) == self.num_cities


    def draw(self, window):
        draw_route(window, self.tour)