import math


class circle():
    def __init__(self, radius):
        self.radius = radius

    def dien_tich(self):
        S = (self.radius ** 2) * math.pi
        return S

    def chu_vi(self):
        cv = 2 * math.pi * self.radius
        return cv


class chu_nhat(circle):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def dien_tich_hcn(self):
        S_chu_nhat = self.a * self.b
        return S_chu_nhat

    def chu_vi_hcn(self):
        Chu_vi_chu_nhat = (self.a + self.b) * 2
        return Chu_vi_chu_nhat


def main():
    a = int(input("chiều dài = "))
    b = int(input("chiều rộng = "))

    hcn = chu_nhat(a, b)

    print("diện tích hình chữ nhật = ", hcn.dien_tich_hcn())
    print("chu vi hình chữ nhật = ", hcn.chu_vi_hcn())


if __name__ == '__main__':
    main()
