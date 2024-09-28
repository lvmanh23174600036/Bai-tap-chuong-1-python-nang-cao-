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
        days_in_month = [31, 28 + (1 if self.is_leap_year() else 0), 31, 30, 31, 30, 
                         31, 31, 30, 31, 30, 31]
        
        self.day += 1
        
        if self.day > days_in_month[self.month - 1]:
            self.day = 1
            self.month += 1
            
            if self.month > 12:
                self.month = 1
                self.year += 1

    def is_leap_year(self):
        """Kiểm tra xem năm có phải là năm nhuận hay không."""
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)


class Employee:
    def __init__(self, name, birth_date, hire_date):
        self.name = name
        self.birth_date = birth_date
        self.hire_date = hire_date      

    def display(self):
        """Hiển thị thông tin nhân viên."""
        print(f"Họ tên: {self.name}")
        print("Ngày sinh:", end=" ")
        self.birth_date.display()
        print("Ngày vào công ty:", end=" ")
        self.hire_date.display()


if __name__ == "__main__":

    birth_date = Date(15, 5, 1990)
    hire_date = Date(1, 1, 2020)

    employee = Employee("Nguyễn Văn A", birth_date, hire_date)
    employee.display()
