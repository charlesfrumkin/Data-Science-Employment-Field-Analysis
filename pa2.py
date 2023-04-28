### PA2 CHARLES FRUMKIN ##
##Question 1
class Flight:
    def __init__(self, origin, dest, takeoff, land, airline, miles):
        if not isinstance(origin, str) or len(origin) != 3:
            raise TypeError("origin must be a length-three string")
        if not isinstance(dest, str) or len(dest) != 3:
            raise TypeError("dest must be a length-three string")
        if not isinstance(takeoff, int) or not 0 <= takeoff <= 2359:
            raise TypeError("takeoff must be an integer between 0 and 2359")
        if not isinstance(land, int) or not 0 <= land <= 2359:
            raise TypeError("land must be an integer between 0 and 2359")
        if not isinstance(airline, str) or airline not in ["Columbian", "Epsilon", "Divided", "Cardioid"]:
            raise TypeError("airline must be one of 'Columbian', 'Epsilon', 'Divided', 'Cardioid'")
        if not isinstance(miles, int) or miles <= 0:
            raise TypeError("miles must be a positive integer")
        if takeoff > land:
            raise ValueError("landing time must be after takeoff time")
        
        self.origin = origin
        self.dest = dest
        self.takeoff = takeoff
        self.land = land
        self.airline = airline
        self.miles = miles
        
    def can_connect(self, earlier, layover):
        if not isinstance(earlier, Flight):
            raise TypeError("earlier must be a Flight object")
        if not isinstance(layover, int) or layover < 0:
            raise TypeError("layover must be a non-negative integer")
        
        if earlier.land != self.origin:
            return False
        
        if earlier.land // 100 != self.takeoff // 100:
            return False
        
        if self.takeoff - earlier.land < layover:
            return False
        
        return True
    
    def duration(self):
        return (self.land // 100 * 60 + self.land % 100) - (self.takeoff // 100 * 60 + self.takeoff % 100)
    
    def average_speed(self):
        duration_in_minutes = self.duration()
        duration_in_hours = duration_in_minutes / 60
        return self.miles / duration_in_hours
    







## QUESTION 2
class Itinerary:
    def __init__(self, flights):
        if not isinstance(flights, list):
            raise TypeError("flights must be a list")
        if len(flights) == 0:
            raise ValueError("flights list must not be empty")
        for flight in flights:
            if not isinstance(flight, Flight):
                raise TypeError("all elements in flights must be Flight objects")
        self.flights = flights
        
    def is_plausible(self, layover):
        for i in range(len(self.flights)-1):
            if not self.flights[i].can_connect(self.flights[i+1], layover):
                return False
        return True
    
    def total_miles(self):
        return sum([flight.miles for flight in self.flights])
    
    def is_single_carrier(self):
        airline = self.flights[0].airline
        for flight in self.flights:
            if flight.airline != airline:
                return False
        return True
    
    def air_time(self):
        return sum([flight.duration() for flight in self.flights])
    
    def total_time(self):
        return (self.flights[-1].land - self.flights[0].takeoff)
    
    def miles_earned(self):
        airlines = set([flight.airline for flight in self.flights])
        miles = {airline: 0 for airline in airlines}
        for flight in self.flights:
            miles[flight.airline] += flight.miles
        return miles







##Question 3
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    


    
##Question 4

def remove_pairs(path):
    if len(path) < 2:
        return path
    elif path[0] == opposite_direction(path[1]):
        return remove_pairs(path[2:])
    else:
        return path[0] + remove_pairs(path[1:])
        
def opposite_direction(direction):
    if direction == "N":
        return "S"
    elif direction == "S":
        return "N"
    elif direction == "E":
        return "W"
    elif direction == "W":
        return "E"




t = 'SSNS'
print(remove_pairs(t))