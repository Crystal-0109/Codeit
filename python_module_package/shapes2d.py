# 원 클래스
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# 정사각형 클래스
class Square:
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length