import city

class DataManager:
    def __init__(self):
        self.file_name = ""
        self.cities = []

    def read_data_from_file(self, _file_name):
        self.file_name = _file_name
        file = open(self.file_name, "r")
        lines = file.readlines()
        self.get_points(lines)
        return self.cities

    def get_points(self, lines):
        i = 8                               # Od 8 linii we wszystkich plikach zaczynają się dane
        while True:
            lines[i] = lines[i][:-1]        # Pozbycie sie '\n' z konca linii
            line = lines[i].split(" ")
            if line[0] == 'EOF':            # Sprawdzenie czy nie koniec pliku
                break
            ID = int(line[0])
            X = int(line[1])
            Y = int(line[2])
            self.cities.append(city.City(ID, X, Y))
            i += 1
        return 

    