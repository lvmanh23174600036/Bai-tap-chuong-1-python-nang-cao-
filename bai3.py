class PS:
    def __init__(self):
        self.tu_so = 0
        self.mau_so = 1  
    def kiem_tra_hop_le(self):
        """Kiểm tra tính hợp lệ của phân số (mẫu số phải khác 0)."""
        return self.mau_so != 0

    def nhap_phan_so(self):
        """Nhập phân số từ người dùng."""
        self.tu_so = int(input("Nhập tử số: "))
        self.mau_so = int(input("Nhập mẫu số: "))
        while not self.kiem_tra_hop_le():
            print("Mẫu số không hợp lệ! Vui lòng nhập lại.")
            self.mau_so = int(input("Nhập mẫu số (khác 0): "))

    def in_phan_so(self):
        """In phân số ra màn hình."""
        print(f"Phân số: {self.tu_so}/{self.mau_so}")

phan_so = PS()
phan_so.nhap_phan_so()
phan_so.in_phan_so()
