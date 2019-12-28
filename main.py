import data_manager
import displayer
import setup
import matplotlib.pyplot as plt
import route
from algorithm import Algorithm

def main():
    dr = data_manager.DataManager()
    dp = displayer.Displayer()
    cities = dr.read_data_from_file(setup.path_to_file)
    dp.plot_cities(cities)
    alg = Algorithm(cities, setup.instances, setup.parents_amount, setup.mutation_chance)
    alg.proceed()
    dp.plot_route(alg.children[31].city_route)
    print(alg.children[31].cost)
    plt.show()


main()