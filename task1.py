class Triangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return 0.5 * self.width * self.height

    def perimeter(self):
        # простий варіант (умовний трикутник)
        return self.width + self.height + (self.width + self.height) / 2


# створення 2 фігур
triangle1 = Triangle(6, 4)
triangle2 = Triangle(10, 8)

print("Triangle 1:")
print("Area:", triangle1.area())
print("Perimeter:", triangle1.perimeter())

print("\nTriangle 2:")
print("Area:", triangle2.area())
print("Perimeter:", triangle2.perimeter())
