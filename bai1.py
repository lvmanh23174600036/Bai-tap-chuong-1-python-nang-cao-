class hinh_chu_nhat:
    def __init__(self):
        self.chieu_dai = 0
        self.chieu_rong = 0
    def nhap_du_lieu(self):
        self.chieu_dai = int(input("nhập chiều dài:"))
        self.chieu_rong = int(input("nhập chiều rộng:"))
    def chu_vi_hcn(self):
        return (self.chieu_rong + self.chieu_dai)*2
    def dien_tich_hcn(self):
        return (self.chieu_dai * self.chieu_rong)
    def in_thong_tin(self):
        print(f"chiều dài của hình chữ nhật là:{self.chieu_dai}")
        print(f"chiều rộng của hình chữ nhật là:{self.chieu_rong}")
        print(f"chu vi của hình chữ nhật là:{self.chu_vi_hcn()}")
        print(f"diện tích hình chữ nhật là:{self.dien_tich_hcn()}")
in_thong_in = hinh_chu_nhat()
in_thong_in.nhap_du_lieu()
in_thong_in.in_thong_tin()
