class Instrument:
    def __init__(self, name, manufacturer, year_built, cost):
        self.name = name
        self.manufacturer = manufacturer
        self.year_built = year_built
        self.cost = cost

    def print_info(self):
        print("Instrument Information: ")
        print("    Name: ", self.name)
        print("    Manufacturer: ", self.manufacturer)
        print("    Year Built: ", self.year_built)
        print("    Cost: ", self.cost)

class StringInstruments(Instrument):
    def __init__(self, name, manufacturer, year_built, cost, num_strings, num_frets):
        Instrument.__init__(self, name, manufacturer, year_built, cost)
        self.num_strings = num_strings
        self.num_frets = num_frets

    def print_info(self):
        print("Instrument Information: ")
        print("    Name: ", self.name)
        print("    Manufacturer: ", self.manufacturer)
        print("    Year Built: ", self.year_built)
        print("    Cost: ", self.cost)
        print("    Number of Strings: ", self.num_strings)
        print("    Number of Frets ", self.num_frets)

if __name__ == "__main__":
    instrument_name = input("Input the Instrument Name: ")
    manufacturer_name = input("Input the manufacturer Name: ")
    year_built = input("Input the year it was Built: ")
    cost = int(input("Input the cost: "))
    string_instrument_name = input("Input the String Instrument Name: ")
    string_manufacturer = input("Input the String manufacturer Name: ")
    string_year_built = int(input("Input the year it was Built: "))
    string_cost = int(input("Input the cost: "))
    num_strings = int(input("Input the number of Strings: "))
    num_frets = int(input("Input the number of Frets: "))

    my_instrument = Instrument(instrument_name, manufacturer_name, year_built, cost)
    my_string_instrument = StringInstruments(string_instrument_name, string_manufacturer, string_year_built, string_cost, num_strings, num_frets)

    my_instrument.print_info()
    my_string_instrument.print_info()
