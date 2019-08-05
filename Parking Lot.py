VEHICLE_TYPE = {
    'UNKNOWN': 0,
    'MOTORCYCLE': 1,
    'CAR': 2,
    'BUS': 3,
}


class Vehicle:
    def __init__(self):
        self.TYPE = VEHICLE_TYPE['UNKNOWN']
        self.COST_SPOTS = 0
        self.at_level = None
        self.at_spots = None

    def get_range(self, n):
        raise NotImplementedError('This method should have implemented.')

    def unpark(self):
        if not self.at_level:
            return
        for x, y in self.at_spots:
            self.at_level.spots[x, y] = None
        self.at_level = None
        self.at_spots = None


class Motorcycle(Vehicle):
    def __init__(self):
        self.TYPE = VEHICLE_TYPE['MOTORCYCLE']
        self.COST_SPOTS = 1

    def get_range(self, n):
        return range(n)


class Car(Vehicle):
    def __init__(self):
        self.TYPE = VEHICLE_TYPE['CAR']
        self.COST_SPOTS = 1

    def get_range(self, n):
        return range(n // 4, n)


class Bus(Vehicle):
    def __init__(self):
        self.TYPE = VEHICLE_TYPE['BUS']
        self.COST_SPOTS = 5

    def get_range(self, n):
        return range(n // 4 * 3, n)


class Level:
    def __init__(self, id, m, n):
        self.id = id
        self.m = m # rows
        self.n = n # colums/spots
        self.spots = {}

    def park_vehicle(self, vehicle):
        RANGE = vehicle.get_range(self.n) # where this vehicle should be parked in this row

        for x in range(self.m): # check every row to find if there exists a valid space for parking
            found_spots = 0
            spots = []
            for y in RANGE: # in the available 
                if self.spots.get((x, y)): # [x, y] row,col, this space has been occupied
                    found_spots = 0 # set to zero
                    spots = []
                    continue

                found_spots += 1
                spots.append((x, y))

                if found_spots == vehicle.COST_SPOTS:
                    vehicle.at_level = self # set it to this current level 
                    vehicle.at_spots = spots # occupied indexes/spaces
                    for _x, _y in spots:
                        self.spots[_x, _y] = vehicle
                    return True

        return False


class ParkingLot:
    # @param {int} k number of levels
    # @param {int} m each level has m rows of spots
    # @param {int} n each row has n spots
    def __init__(self, k, m, n):
        self.levels = [Level(i, m, n) for i in range(k)]

    # Park the vehicle in a spot (or multiple spots)
    # Return false if failed
    def park_vehicle(self, vehicle):
        for level in self.levels:
            if level.park_vehicle(vehicle):
                return True
        return False

    # unPark the vehicle
    def unpark_vehicle(self, vehicle):
        vehicle.unpark()
