from random import randint
import random
from route import Route
import setup

class Algorithm:
    def __init__(self, _cities, _route_amount, _parent_amount, _mutation_chance):
        self.cities = _cities
        self.route_amount = _route_amount
        self.parent_amount = _parent_amount
        self.mutation_chance = _mutation_chance
        self.routes = []
        self.parents = []
        self.children = []
        self.now_best_cost = 10000.0

    #funkcja generująca losowe ścieżki (route_amount = 100)
    def random_routes(self):
        for i in range(self.route_amount):
            route = Route(self.cities)
            route.randomize_route()
            self.routes.append(route)

    def choose_parents(self):
        self.parents = []
        for i in range(self.parent_amount):
            random_route = self.routes[randint(0, len(self.routes) - 1)]
            self.parents.append(random_route)

    def generate_children(self):
        self.children = []
        for i in range(int(self.parent_amount/2)):
            parent1 = random.choice(self.parents)
            self.parents.remove(parent1)
            parent2 = random.choice(self.parents)
            self.parents.remove(parent2)
            child1 = self.cx_crossover(parent1, parent2)
            self.children.append(child1)
            child2 = self.cx_crossover(parent2, parent1)
            self.children.append(child2)


    def cx_crossover(self, parent1, parent2):
        #od parent1 dajemy loop, od parent2 dopełnienie
        index = 0
        child1 = Route(self.cities)
        chromosom_index = []
        while True:
            chromosom_index.append(index)
            chromosom = parent2.city_route[index]
            index = parent1.city_route.index(chromosom)
            if index == 0:
                break
        unused_indexes = list(range(0, len(parent1.city_route)))
        for i in chromosom_index:
            child1.city_route[i] = parent1.city_route[i]
            unused_indexes.remove(i)
        for i in unused_indexes:
            child1.city_route[i] = parent2.city_route[i]
        child1 = self.mutation(child1)
        child1.calc_cost()
        return child1
    
    def mutation(self, child):
        random_int = randint(0, 100)
        if random_int - self.mutation_chance <= 0:
            index1 = randint(0, len(child.city_route) - 1)
            index2 = randint(0, len(child.city_route) - 1)
            child.city_route[index1], child.city_route[index2] = child.city_route[index2], child.city_route[index1]
        return child
    
    def get_best_routes(self):
        self.routes = []
        for i in range(0, self.route_amount):
            best_route_cost = 100000.0
            best_route = Route(self.cities)
            for child in self.children:
                if child.cost < best_route_cost:
                    best_route = child
                    best_route_cost = child.cost
            if i == 0:
                self.now_best_cost = best_route_cost
            self.routes.append(best_route)
            self.children.remove(best_route)

    def proceed(self):
        self.random_routes()
        for epoch in range(0, 1000):
            self.choose_parents()
            self.generate_children()
            self.get_best_routes()
            print("Epoch: ", epoch, ", shortest path: ", self.now_best_cost)


    
        