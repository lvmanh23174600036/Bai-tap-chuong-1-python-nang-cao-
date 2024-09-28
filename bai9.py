class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def perimeter(self):
        raise NotImplementedError("Chu vi không được xác định cho đa giác tổng quát.")

    def area(self):
        raise NotImplementedError("Diện tích không được xác định cho đa giác tổng quát.")


class Parallelogram(Polygon):
    def __init__(self, base, height):
        super().__init__(4)
        self.base = base
        self.height = height

    def perimeter(self):
        return 2 * (self.base + self.height)

    def area(self):
        return self.base * self.height


class Rectangle(Parallelogram):
    def __init__(self, width, height):
        super().__init__(width, height)

    def area(self):
        return self.base * self.height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def area(self):
        return self.base ** 2


if __name__ == "__main__":
    side = float(input("Nhập cạnh của hình vuông: "))
    square = Square(side)
    print(f"Chu vi hình vuông: {square.perimeter()}")
    print(f"Diện tích hình vuông: {square.area()}")

    width = float(input("\nNhập chiều rộng của hình chữ nhật: "))
    height = float(input("Nhập chiều cao của hình chữ nhật: "))
    rectangle = Rectangle(width, height)
    print(f"Chu vi hình chữ nhật: {rectangle.perimeter()}")
    print(f"Diện tích hình chữ nhật: {rectangle.area()}")

    base = float(input("\nNhập đáy của hình bình hành: "))
    height = float(input("Nhập chiều cao của hình bình hành: "))
    parallelogram = Parallelogram(base, height)
    print(f"Chu vi hình bình hành: {parallelogram.perimeter()}")
    print(f"Diện tích hình bình hành: {parallelogram.area()}")
