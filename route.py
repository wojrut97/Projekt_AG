import random
import math

class Route:
    def __init__(self, _cities):
        self.city_route = list(_cities)
        self.cost = 0

    def calc_cost(self):
        prev_city = None
        for city in self.city_route:
            if prev_city is not None:
                self.cost += math.sqrt((prev_city.X - city.X)**2 + (prev_city.Y - city.Y)**2)
                prev_city = city
            else:
                prev_city = city

    def randomize_route(self):
        random.shuffle(self.city_route)
        self.calc_cost()