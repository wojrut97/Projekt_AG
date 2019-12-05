import matplotlib.pyplot as plt

class Displayer:
    def __init__(self):
        self.all_X = []
        self.all_Y = []
        return

    def plot_data(self, cities):
        for city in cities:
            self.all_X.append(city.X)
            self.all_Y.append(city.Y)
        plt.scatter(self.all_X, self.all_Y, s=2, c='navy')
        plt.show()
        
