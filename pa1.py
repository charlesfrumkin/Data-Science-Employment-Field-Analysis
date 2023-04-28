# Code to read the CSV file
# Do not modify this section
flights = []
with open("flights.csv") as f:
    for line in f:
        flights.append(line)

# Write your functions below



## PROBLEM 1: CLEANING DATA

def clean_data():
    cleaned_data = []
    for flight in flights:
        flight_data = flight.strip().split(',')
        origin = flight_data[0].upper()
        dest = flight_data[1].upper()
        dep_time = flight_data[2].strip()
        if len(dep_time) == 3:
            dep_time = "0" + dep_time
        airline = flight_data[3].strip()
        cleaned_data.append((origin, dest, dep_time, airline))
    return cleaned_data

cleaned_flights = clean_data()
#print(cleaned_flights)




## PROBLEM 2: FLIGHTS PER AIRPORT
def flights_per_airport(cleaned_flights):
    airports = {}
    for flight in cleaned_flights:
        origin, dest = flight[0], flight[1]
        if origin not in airports:
            airports[origin] = 1
        else:
            airports[origin] += 1
        if dest not in airports:
            airports[dest] = 1
        else:
            airports[dest] += 1
    return airports

airport_counts = flights_per_airport(cleaned_flights)
#print(airport_counts)



##PROBLEM 3: TOP AIRPORTS
def top_airports(airport_counts, num):
    sorted_airports = sorted(airport_counts.items(), key=lambda x: x[1], reverse=True)
    if len(sorted_airports) <= num:
        return dict(sorted_airports)
    else:
        top_airports = dict(sorted_airports[:num])
        last_count = sorted_airports[num-1][1]
        for airport, count in sorted_airports[num:]:
            if count == last_count:
                top_airports[airport] = count
            else:
                break
        return top_airports

top_10_airports = top_airports(airport_counts, 10)
#print(top_10_airports)



##PROBLEM 4: PRINTING RESULTS
def print_counts(airport_counts):
    for airport, count in airport_counts.items():
        if count == 1:
            print(f"There is 1 flight at {airport}")
        else:
            print(f"There are {count} flights at {airport}")

top_airports_counts = top_airports(airport_counts, 30)
#print_counts(top_airports_counts)



##PROBLEM 5: WELL-SERVED AIRPORTS

def get_carriers(cleaned_flights, airport_code):
    flights = set()
    for record in cleaned_flights:
        if record[0] == airport_code or record[1] == airport_code:
            flights.add(record[3])
    return flights

def well_served(cleaned_flights, airport_code):
    carriers = get_carriers(cleaned_flights, airport_code)
    return len(carriers) == 4

def missing_carriers(cleaned_flights, airport_code):
    all_carriers = set(["Columbian", "Epsilon", "Divided", "Cardioid"])
    served_carriers = get_carriers(cleaned_flights, airport_code)
    return all_carriers - served_carriers

#print(well_served(cleaned_flights, 'KORD'))
#print(missing_carriers(cleaned_flights, 'KORD'))


##PROBLEM 6: LIST COMPREHENSIONS

def icao_to_iata(cleaned_flights):
    return [(flight[0][1:], flight[1][1:], flight[2], flight[3]) for flight in cleaned_flights]


def carrier_flights(cleaned_flights, carrier_name):
    return [(flight[0], flight[1], flight[2], flight[3]) for flight in cleaned_flights if flight[3] == carrier_name]



#print(icao_to_iata(cleaned_flights)) 
#print(carrier_flights(cleaned_flights, 'Columbian')) 



##Problem 7: NONE

def carrier_for(cleaned_flights, origin, dest, dep_time):
    for flight in cleaned_flights:
        if flight[0] == origin.upper() and flight[1] == dest.upper() and flight[2] == dep_time:
            return flight[3]
    return None

# print(carrier_for(cleaned_flights, 'JFK','LAX',1720))


