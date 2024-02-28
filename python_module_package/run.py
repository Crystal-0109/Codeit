# import <module>
import shapes2d

circle = shapes2d.Circle(2)
print(circle.area())

# from <module> import <member(s)>
from shapes2d import Square as sq

square = sq(3)
print(square.area())