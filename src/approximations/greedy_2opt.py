import math
import numpy as np
import random
import pandas as pd



from .approximation_utils import draw_route, calc_fitness_memo, randomize_route, calc_distance, calc_route_distance
class GreedyTwoOpt:
    def __init__(self, cities):
        self.cities = cities
        self.num_cities = len(cities)
        self.tour = []

    def find_closest(self, current, others): 
        closest = None
        closest_dist = float('inf')

        for next_city in others:
            distance = calc_distance(current, self.cities[next_city])
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
                        continue 
                    new_tour = self.two_opt_swap(tour, i, j)
                    if calc_route_distance(new_tour) < calc_route_distance(best_tour):
                        best_tour = new_tour
                        improved = True

            tour = best_tour

        return best_tour

    def run(self):
        if not self.tour:
            self.tour = self.solve_greedy()
        self.tour = self.two_opt(self.tour)
        return calc_route_distance(self.tour), True
    
    def draw(self, window):
        draw_route(window, self.tour)