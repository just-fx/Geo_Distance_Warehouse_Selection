import geopy.distance
import csv


# Define class
class distribution_center:
    def __init__(self, name, coordinates):
        self.name = name
        self.coordinates = coordinates
        self.distances = []

    # get distance from user coordinates
    def compute_distance(self, user_coordinates):
        distance = geopy.distance.geodesic(user_coordinates, self.coordinates).km
        self.distances.append(distance)

    # get mean distance
    def mean_distance(self):
        mean = sum(self.distances) / len(self.distances)
        print("Average distance from {}: {:,.2f} km".format(self.name, mean))
        return mean


# Instantiate classes and return mean distance from users
def get_mean_distance(name, coordinates, filename):
    dc = distribution_center(name, coordinates)
    with open(filename) as file:
        rows = csv.reader(file)
        next(rows, None)
        for row in rows:
            country, user_coordinates = row[0], (float(row[1]), float(row[2]))
            dc.compute_distance(user_coordinates)
    return dc.mean_distance()


# Run main program
if __name__ == "__main__":
    file = "asia_coordinates.csv"
    mean_distance1 = get_mean_distance(
        name="China Distribution Center Co. Ltd.",
        coordinates=(31.457407498909543, 121.80406508534779),
        filename=file,
    )
    mean_distance2 = get_mean_distance(
        name="China Railway Logistics Z7haoqing Distribution Center",
        coordinates=(23.134548374827574, 112.4058499170713),
        filename=file,
    )
    mean_distance3 = get_mean_distance(
        name="China Distribution and Logistics Co Ltd",
        coordinates=(22.303953718116837, 114.1744830987732),
        filename=file,
    )
