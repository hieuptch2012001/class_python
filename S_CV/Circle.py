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


def main():
    radius = int(input("Nhập bán kính: "))
    bk = circle(radius)
    print('Diện tích hình tròn: ', bk.dien_tich())
    print('Chu vi hình tròn: ', bk.chu_vi())


if __name__ == '__main__':
    main()
