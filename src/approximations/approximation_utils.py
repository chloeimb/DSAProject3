import pygame

from src.colors import MAXIMUM_GREEN


#https://codereview.stackexchange.com/questions/110221/tsp-brute-force-optimization-in-python
def memoize(func: callable) -> float:
    """Create a memoization dictionary for calculating the distance between cities

    Args:
        func (callable): Distance function

    Returns:
        float: Distance between cities
    """

    class memo_dict(dict):
        def __init__(self, func):
            self.func = func
        
        def __call__(self, *args):
            return self[args]
        
        def __missing__(self, key):
            result = self[key] = self.func(*key)
            return result
    
    return memo_dict(func)


@memoize
def calc_distance(city1, city2) -> float:
    """Allows memoization of distance calculation

    Args:
        city1 (City): Start City
        city2 (City): End City

    Returns:
        float: distance between cities
    """
    dist = city1.distance_from(city2)
    return dist


def calc_fitness_memo(route: list) -> float:
    """Determine the fitness of a route. Metric is 1 / total_distance, goal is to maximize the fitness. Utilizes memoization dict to reduce repeated calculations of distances

    Args:
        route (list): route of cities to be scored

    Returns:
        float: score of the input route
    """

    distance = calc_distance(route[0], route[-1])
    for i, start in enumerate(route[:-1]):
        end = route[i + 1]            
        distance += calc_distance(start, end)

    return 1 / distance


def draw_route(window: pygame.surface.Surface, route: list) -> None:
    """ Draw route when presented as sequential list of city objects

    Args:
        window (pygame.surface.Surface): Game window that route will be drawn onto
        route (list): Sequential list of city objects that represent the calculated route
    """

    # Connect first and last point
    pygame.draw.line(window, MAXIMUM_GREEN, route[0].get_pixel_tuple(), route[-1].get_pixel_tuple(), 2)

    # Loop through remaining connections
    for index, city in enumerate(route[1:]):
        pygame.draw.line(window, MAXIMUM_GREEN, route[index].get_pixel_tuple(), city.get_pixel_tuple(), 2)
