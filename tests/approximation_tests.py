import sys
import matplotlib.pyplot as plt
import time

from random_city import RandomCity

# Allows importing from directories higher in file path
sys.path.append('..')
from DSAProject3.src.approximations.brute_force import BruteForce
from DSAProject3.src.approximations.genetic_approximation import GeneticApproximation
from DSAProject3.src.approximations.nearest_neighbor import NearestNeighbor


if __name__ == '__main__':
    num_cities = 200
    map_size = 200
    city_list = [RandomCity(map_size) for _ in range(num_cities)]

    approximations = [GeneticApproximation, NearestNeighbor]
    names = []
    for approx in approximations:
        approx = approx(city_list)
        names.append(approx.__class__.__name__)
        start = time.time()
        done = False
        scores = []
        while not done:
            best, done = approx.run()
            scores.append(1 / best)

        print(f'{names[-1]}: {str(time.time() - start)}')
        plt.plot(scores)

    plt.ylabel('Distance')
    plt.xlabel('Generation') 
    plt.legend(names)
    plt.show()
