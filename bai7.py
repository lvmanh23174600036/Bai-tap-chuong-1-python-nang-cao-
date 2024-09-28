class Date:
    def __init__(self, day=1, month=1, year=2023):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        """Hiển thị thông tin ngày."""
        print(f"Ngày: {self.day:02d}/{self.month:02d}/{self.year}")

    def next(self):
        """Tính ngày tiếp theo."""
        # Số ngày trong mỗi tháng
        days_in_month = [31, 28 + (1 if self.is_leap_year() else 0), 31, 30, 31, 30, 
                         31, 31, 30, 31, 30, 31]
        
        self.day += 1
        
        # Kiểm tra nếu ngày vượt quá số ngày trong tháng
        if self.day > days_in_month[self.month - 1]:
            self.day = 1
            self.month += 1
            
            # Kiểm tra nếu tháng vượt quá 12
            if self.month > 12:
                self.month = 1
                self.year += 1

    def is_leap_year(self):
        """Kiểm tra xem năm có phải là năm nhuận hay không."""
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)

# Chương trình chính
if __name__ == "__main__":
    date = Date(28, 2, 2023)  # Khởi tạo ngày mặc định
    date.display()

    for _ in range(5):  # Tính 5 ngày tiếp theo
        date.next()
        date.display()
