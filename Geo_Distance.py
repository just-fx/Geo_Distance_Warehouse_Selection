import geopy.distance
import csv
import json


# Define class
class distribution_center:
    def __init__(self, name, coordinates):
        self.name = name
        self.coordinates = (coordinates[0], coordinates[1])
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
    with open("distribution_centers.json", "r") as file:
        file = json.load(file)
        for dist_center in file["distribution_centers"]:
            mean_distance = get_mean_distance(
                name=dist_center["name"],
                coordinates=dist_center["coordinates"],
                filename=file["customer_coordinates_file"],
            )
