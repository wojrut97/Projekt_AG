import matplotlib.pyplot as plt

class Displayer:
    def __init__(self):
        self.all_X = []
        self.all_Y = []
        return

    def plot_cities(self, cities):
        self.all_X = []
        self.all_Y = []
        for city in cities:
            self.all_X.append(city.X)
            self.all_Y.append(city.Y)
        plt.scatter(self.all_X, self.all_Y, s=4, c='navy')
        # plt.show()

    def plot_route(self, route):
        self.all_X = []
        self.all_Y = []
        for city in route:
            self.all_X.append(city.X)
            self.all_Y.append(city.Y)
        plt.plot(self.all_X, self.all_Y, linewidth = 0.5, c='red')
        # plt.show()

    
        
