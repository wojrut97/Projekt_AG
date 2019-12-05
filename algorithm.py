from random import randint
from route import Route

class Algorithm:
    def __init__(self, _cities):
        self.cities = _cities
        self.routes = []
        self.parents = []
        self.children = []

    #funkcja generująca losowe ścieżki (route_amount = 100)
    def random_routes(self, route_amount):
        for i in range(route_amount):
            route = Route(self.cities)
            route.randomize_route()
            self.routes.append(route)

    def choose_parents(self, parent_amount):
        for i in range(parent_amount):
            random_route = self.routes[randint(0, len(self.routes) - 1)]
            self.parents.append(random_route)

    def pmx_crossover(self):
        return 0 


    
        