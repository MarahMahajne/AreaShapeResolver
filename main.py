from Circle import Circle
from Hexagon import Hexagon

def main():
    c = Circle(5)
    h = Hexagon(3)
    print(c)
    print("Circle area: ",c.get_area())
    print(h)
    print("Hexagon area: ",h.get_area())


if __name__ == "__main__":
    main()
