import geopy.distance
import csv

class distribution_center:
    def __init__(self, name, coordinates):
        self.name=name
        self.coordinates=coordinates
        self.distances=[]
    def compute_distance(self, user_coordinates):
        distance = geopy.distance.geodesic(user_coordinates, self.coordinates).km
        self.distances.append(distance)
    def mean_distance(self):
        mean = sum(self.distances)/len(self.distances)
        print('Average distance from {}: {:,.2f} km'.format(self.name, mean))


if __name__ == "__main__":
    dc1=distribution_center(name='China Distribution Center Co. Ltd.'
        ,coordinates=(31.457407498909543, 121.80406508534779))
    dc2=distribution_center(name='China Railway Logistics Z7haoqing Distribution Center'
        , coordinates=(23.134548374827574, 112.4058499170713))
    dc3 = distribution_center(name='Taotaole South China Distrib Ctr'
        , coordinates=(23.392681976113746, 113.22044147365186))
    with open("asia_coordinates.csv") as file:
        rows=csv.reader(file)
        next(rows,None)
        for row in rows:
            country,user_coordinates = row[0],(float(row[1]),float(row[2]))
            dc1.compute_distance(user_coordinates)
            dc2.compute_distance(user_coordinates)
            dc3.compute_distance(user_coordinates)
    dc1.mean_distance()
    dc2.mean_distance()
    dc3.mean_distance()