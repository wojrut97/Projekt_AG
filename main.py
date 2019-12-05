import data_reader
import displayer
import setup

def main():
    dr = data_reader.DataReader()
    dp = displayer.Displayer()
    cities = dr.read_data_from_file(setup.path_to_file)
    dp.plot_data(cities)


main()