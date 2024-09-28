class Stack:
    def __init__(self, capacity):
        self.capacity = capacity  
        self.stack = []       

    def push(self, value):
        """Đưa một phần tử vào ngăn xếp."""
        if self.is_full():
            print("Ngăn xếp đã đầy! Không thể thêm phần tử.")
        else:
            self.stack.append(value)
            print(f"Đã thêm {value} vào ngăn xếp.")

    def pop(self):
        """Lấy một phần tử ra từ đỉnh ngăn xếp."""
        if self.is_empty():
            print("Ngăn xếp trống! Không thể lấy phần tử.")
            return None
        else:
            value = self.stack.pop()
            print(f"Đã lấy {value} ra từ ngăn xếp.")
            return value

    def is_empty(self):
        """Kiểm tra ngăn xếp đã trống chưa."""
        return len(self.stack) == 0

    def is_full(self):
        """Kiểm tra ngăn xếp đã đầy chưa."""
        return len(self.stack) >= self.capacity

    def display(self):
        """Hiển thị nội dung của ngăn xếp."""
        if self.is_empty():
            print("Ngăn xếp trống!")
        else:
            print("Nội dung ngăn xếp:", self.stack)

if __name__ == "__main__":
    capacity = int(input("Nhập sức chứa tối đa của ngăn xếp: "))
    stack = Stack(capacity)

    while True:
        print("\n1. Đưa phần tử vào ngăn xếp (push)")
        print("2. Lấy phần tử ra từ ngăn xếp (pop)")
        print("3. Kiểm tra ngăn xếp đã trống chưa (isEmpty)")
        print("4. Kiểm tra ngăn xếp đã đầy chưa (isFull)")
        print("5. Hiển thị ngăn xếp")
        print("6. Thoát")

        choice = input("Chọn chức năng: ")

        if choice == "1":
            value = float(input("Nhập phần tử cần thêm: "))
            stack.push(value)
        elif choice == "2":
            stack.pop()
        elif choice == "3":
            print("Ngăn xếp đã trống." if stack.is_empty() else "Ngăn xếp không trống.")
        elif choice == "4":
            print("Ngăn xếp đã đầy." if stack.is_full() else "Ngăn xếp không đầy.")
        elif choice == "5":
            stack.display()
        elif choice == "6":
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ! Vui lòng chọn lại.")
