class Plant:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def print_info(self):
        print("Plant Information: ")
        print("    Plant Name: ", self.name)
        print("    Cost: ", self.cost)

class Flower(Plant):
    def __init__(self, name, cost, annual, color):
        Plant.__init__(self, name, cost)
        self.annual = annual
        self.color = color

    def print_info(self):
        print("Plant Information: ")
        print("    Plant Name: ", self.name)
        print("    Cost: ", self.cost)
        print("    Annual: ", self.annual)
        print("    Color of Flowers: ", self.color)


if __name__ == "__main__":
    name = input("Input the name of the plant: ")
    cost = input("Input the cost: ")

    f_name = input("Input the name of the flower: ")
    f_cost = input("Input the cost: ")
    annual = input("input rather its annual or not: ")
    color = input("input its color: ")

    my_garden = Plant(name, cost)
    my_flowers = Flower(f_name, f_cost, annual, color)

    my_garden.print_info()
    my_flowers.print_info()
