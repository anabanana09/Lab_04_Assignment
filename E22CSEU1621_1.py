class Flight:
    def __init__(self, flight_id, from_city, to_city, price):
        self.flight_id = flight_id
        self.from_city = from_city
        self.to_city = to_city
        self.price = price

class FlightTable:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def search_by_city(self, city):
        result = [flight for flight in self.flights if flight.from_city == city or flight.to_city == city]
        return result

    def search_from_city(self, city):
        result = [flight for flight in self.flights if flight.from_city == city]
        return result

    def search_between_cities(self, from_city, to_city):
        result = [flight for flight in self.flights if flight.from_city == from_city and flight.to_city == to_city]
        return result

def main():
    flight_table = FlightTable()

    # Adding flights to the table
    flight_table.add_flight(Flight("AI161E90", "BLR", "BOM", 5600))
    flight_table.add_flight(Flight("BR161F91", "BOM", "BBI", 6750))
    flight_table.add_flight(Flight("AI161F99", "BBI", "BLR", 8210))
    flight_table.add_flight(Flight("VS171E20", "JLR", "BBI", 5500))
    flight_table.add_flight(Flight("AS171G30", "HYD", "JLR", 4400))
    flight_table.add_flight(Flight("AI131F49", "HYD", "BOM", 3499))

    print("Options:")
    print("1. Flights for a particular City")
    print("2. Flights From a city")
    print("3. Flights between two given cities")

    option = int(input("Enter option: "))

    if option == 1:
        city = input("Enter city: ")
        result = flight_table.search_by_city(city)
    elif option == 2:
        city = input("Enter city: ")
        result = flight_table.search_from_city(city)
    elif option == 3:
        from_city = input("Enter source city: ")
        to_city = input("Enter destination city: ")
        result = flight_table.search_between_cities(from_city, to_city)
    else:
        print("Invalid option")
        return

    if result:
        print("Flight ID\tFrom\tTo\tPrice")
        for flight in result:
            print(f"{flight.flight_id}\t{flight.from_city}\t{flight.to_city}\t{flight.price}")
    else:
        print("No flights found.")

if __name__ == "__main__":
    main()
