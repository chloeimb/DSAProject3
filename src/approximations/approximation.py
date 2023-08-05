from abc import ABC, abstractmethod


class Approximation(ABC):
    def __init__(self, cities: list) -> None:
        """ Initilization will always include a randomized list of city objects,
            all other parameters should be default initialized

        Args:
            cities (list): Randomized list of city objects
        """
        pass

    @abstractmethod
    def run(self) -> tuple[float, bool]:
        """ This function should execute one iteration of the underlying approximation function.
            Examples: adding one city to the current route in a nearest neighbor approach, or
            executing one swap in a k-opt function

        Returns:
            tuple[float, bool]: fitness of the currently calculated run, can be determined via the calc_fitness_memo_function in approximation_utils,
                                and a boolean of whether the approximation is complete or not
                                Note: all cities should be included in the call to calc_fitness_memo
        """
        pass

    @abstractmethod
    def draw(self, window) -> None:
        """ This function will draw the connections between cities.
            drawing functions can be imported from approximation_utils

        Args:
            window (pygame.surface.Surface): The pygame window that will be drawn on
        """
        pass
