class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

    def perimeter(self):
        return self.a + self.b + self.c


class RightTriangle(Triangle):
    def __init__(self, base, height):
        self.base = base
        self.height = height
        self.a = base
        self.b = height
        self.c = (base**2 + height**2) ** 0.5

    def area(self):
        return 0.5 * self.base * self.height


class IsoscelesTriangle(Triangle):
    def __init__(self, base, side):
        super().__init__(base, side, side)
        self.base = base
        self.side = side

    def area(self):
        height = (self.side**2 - (self.base / 2)**2) ** 0.5
        return 0.5 * self.base * height


class EquilateralTriangle(IsoscelesTriangle):
    def __init__(self, side):
        super().__init__(side, side)

    def area(self):
        return (3**0.5 / 4) * (self.a ** 2)


if __name__ == "__main__":
    a = float(input("Nhập cạnh a của tam giác: "))
    b = float(input("Nhập cạnh b của tam giác: "))
    c = float(input("Nhập cạnh c của tam giác: "))
    triangle = Triangle(a, b, c)
    print(f"Chu vi tam giác: {triangle.perimeter()}")
    print(f"Diện tích tam giác: {triangle.area()}")

    base = float(input("\nNhập cạnh đáy của tam giác vuông: "))
    height = float(input("Nhập chiều cao của tam giác vuông: "))
    right_triangle = RightTriangle(base, height)
    print(f"Chu vi tam giác vuông: {right_triangle.perimeter()}")
    print(f"Diện tích tam giác vuông: {right_triangle.area()}")

    base = float(input("\nNhập cạnh đáy của tam giác cân: "))
    side = float(input("Nhập cạnh bên của tam giác cân: "))
    isosceles_triangle = IsoscelesTriangle(base, side)
    print(f"Chu vi tam giác cân: {isosceles_triangle.perimeter()}")
    print(f"Diện tích tam giác cân: {isosceles_triangle.area()}")

    side = float(input("\nNhập cạnh của tam giác đều: "))
    equilateral_triangle = EquilateralTriangle(side)
    print(f"Chu vi tam giác đều: {equilateral_triangle.perimeter()}")
    print(f"Diện tích tam giác đều: {equilateral_triangle.area()}")
