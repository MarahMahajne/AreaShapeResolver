from Square import Square
from Rectangle import Rectangle
from Triangle import Triangle
from Circle import Circle
from Hexagon import Hexagon

def main():
    s = Square(5)
    r = Rectangle(2,10)
    t = Triangle(6,3)
    c = Circle(5)
    h = Hexagon(3)

    print(s)
    print("Square area: ",s.get_area())
    print(r)
    print("Rectangle area: ",r.get_area())
    print(t)
    print("Triangle area: ",t.get_area())
    print(c)
    print("Circle area: ",c.get_area())
    print(h)
    print("Hexagon area: ",h.get_area())


if __name__ == "__main__":
    main()
