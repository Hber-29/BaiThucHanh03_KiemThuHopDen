import math

# ===============================
# 1. Chu vi hình chữ nhật
# ===============================
def chu_vi_hcn(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Chieu dai va chieu rong phai la so")
    if a <= 0 or b <= 0:
        raise ValueError("Chieu dai va chieu rong phai lon hon 0")
    return 2 * (a + b)


# ===============================
# 2. Dien tich hình chữ nhật
# ===============================
def dien_tich_hcn(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Chieu dai va chieu rong phai la so")
    if a <= 0 or b <= 0:
        raise ValueError("Chieu dai va chieu rong phai lon hon 0")
    return a * b


# ===============================
# 3. Giai phuong trinh bac 2
# ===============================
def giai_pt_bac_2(a, b, c):
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        raise ValueError("He so phai la so")

    if a == 0:
        raise ValueError("Khong phai phuong trinh bac 2")

    delta = b*b - 4*a*c

    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return ("2 nghiem", x1, x2)
    elif delta == 0:
        x = -b / (2*a)
        return ("1 nghiem kep", x)
    else:
        return ("Vo nghiem",)


# ===============================
# 4. So ngay cua thang
# ===============================
def so_ngay_trong_thang(month, year):
    if not isinstance(month, int) or not isinstance(year, int):
        raise ValueError("Thang va nam phai la so nguyen")

    if month < 1 or month > 12:
        raise ValueError("Thang khong hop le")

    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    else:
        # Thang 2
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            return 29
        return 28


# ===============================
# 5. Kiem tra so nguyen to
# ===============================
def la_so_nguyen_to(n):
    if not isinstance(n, int):
        raise ValueError("n phai la so nguyen")
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# ===============================
# 6. Tinh S = 1 - 2 + 3 - 4 + ... + n
# ===============================
def tinh_tong_xen_ke(n):
    if not isinstance(n, int):
        raise ValueError("n phai la so nguyen")
    if n <= 0:
        raise ValueError("n phai lon hon 0")

    total = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            total -= i
        else:
            total += i
    return total


# ===============================
# 7. Tim UCLN
# ===============================
def ucln(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("a va b phai la so nguyen")
    if a == 0 and b == 0:
        raise ValueError("Khong ton tai UCLN")

    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a


# ===============================
# 8. S = 1! + 2! + ... + n!
# ===============================
def tong_giai_thua(n):
    if not isinstance(n, int):
        raise ValueError("n phai la so nguyen")
    if n <= 0:
        raise ValueError("n phai lon hon 0")

    total = 0
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        total += fact
    return total


# ===============================
# MENU TEST
# ===============================
def main():
    while True:
        print("\n===== MENU =====")
        print("1. Chu vi hcn")
        print("2. Dien tich hcn")
        print("3. Giai pt bac 2")
        print("4. So ngay trong thang")
        print("5. Kiem tra so nguyen to")
        print("6. Tong xen ke")
        print("7. UCLN")
        print("8. Tong giai thua")
        print("0. Thoat")

        choice = input("Chon: ")

        try:
            if choice == "1":
                a = float(input("Nhap a: "))
                b = float(input("Nhap b: "))
                print(chu_vi_hcn(a, b))

            elif choice == "2":
                a = float(input("Nhap a: "))
                b = float(input("Nhap b: "))
                print(dien_tich_hcn(a, b))

            elif choice == "3":
                a = float(input("Nhap a: "))
                b = float(input("Nhap b: "))
                c = float(input("Nhap c: "))
                print(giai_pt_bac_2(a, b, c))

            elif choice == "4":
                m = int(input("Nhap thang: "))
                y = int(input("Nhap nam: "))
                print(so_ngay_trong_thang(m, y))

            elif choice == "5":
                n = int(input("Nhap n: "))
                print(la_so_nguyen_to(n))

            elif choice == "6":
                n = int(input("Nhap n: "))
                print(tinh_tong_xen_ke(n))

            elif choice == "7":
                a = int(input("Nhap a: "))
                b = int(input("Nhap b: "))
                print(ucln(a, b))

            elif choice == "8":
                n = int(input("Nhap n: "))
                print(tong_giai_thua(n))

            elif choice == "0":
                break
            else:
                print("Lua chon khong hop le")

        except Exception as e:
            print("Loi:", e)


if __name__ == "__main__":
    main()