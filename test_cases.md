# TEST CASES & TEST EXECUTION RESULT
Bai Thuc Hanh 03 - Kiem Thu Hop Den

Ky thuat su dung:
- Phan lop tuong duong
- Phan tich gia tri bien
- Du lieu hop le
- Du lieu khong hop le
- Du lieu ngoai le

============================================================
BAI 1: CHU VI HINH CHU NHAT
============================================================

Dieu kien: a > 0, b > 0

Phan lop tuong duong:
- Hop le: a > 0, b > 0
- Khong hop le: a <= 0 hoac b <= 0
- Ngoai le: khong phai so

| TC | a | b | Expected | Actual | Status |
|----|---|---|----------|--------|--------|
| 1 | 5 | 3 | 16 | 16 | Pass |
| 2 | 0.1 | 0.1 | 0.4 | 0.4 | Pass |
| 3 | 0 | 5 | Loi | Loi | Pass |
| 4 | -1 | 5 | Loi | Loi | Pass |
| 5 | "abc" | 5 | Loi | Loi | Pass |

============================================================
BAI 2: DIEN TICH HINH CHU NHAT
============================================================

Dieu kien: a > 0, b > 0

| TC | a | b | Expected | Actual | Status |
|----|---|---|----------|--------|--------|
| 1 | 5 | 3 | 15 | 15 | Pass |
| 2 | 0.5 | 2 | 1 | 1 | Pass |
| 3 | 0 | 5 | Loi | Loi | Pass |
| 4 | -3 | 4 | Loi | Loi | Pass |
| 5 | "abc" | 2 | Loi | Loi | Pass |

============================================================
BAI 3: GIAI PHUONG TRINH BAC 2
============================================================

Dang: ax^2 + bx + c = 0

Phan lop:
- a != 0
- a = 0
- Delta > 0
- Delta = 0
- Delta < 0

| TC | a | b | c | Expected | Actual | Status |
|----|---|---|---|----------|--------|--------|
| 1 | 1 | -3 | 2 | 2 nghiem | 2 nghiem | Pass |
| 2 | 1 | 2 | 1 | 1 nghiem kep | 1 nghiem kep | Pass |
| 3 | 1 | 0 | 1 | Vo nghiem | Vo nghiem | Pass |
| 4 | 0 | 2 | 1 | Khong phai PT bac 2 | Khong phai PT bac 2 | Pass |
| 5 | "a" | 2 | 3 | Loi | Loi | Pass |

============================================================
BAI 4: SO NGAY TRONG THANG
============================================================

| TC | Month | Year | Expected | Actual | Status |
|----|-------|------|----------|--------|--------|
| 1 | 1 | 2024 | 31 | 31 | Pass |
| 2 | 4 | 2024 | 30 | 30 | Pass |
| 3 | 2 | 2024 | 29 | 29 | Pass |
| 4 | 2 | 2023 | 28 | 28 | Pass |
| 5 | 0 | 2024 | Loi | Loi | Pass |
| 6 | 13 | 2024 | Loi | Loi | Pass |
| 7 | "abc" | 2024 | Loi | Loi | Pass |

============================================================
BAI 5: KIEM TRA SO NGUYEN TO
============================================================

| TC | n | Expected | Actual | Status |
|----|---|----------|--------|--------|
| 1 | 2 | True | True | Pass |
| 2 | 7 | True | True | Pass |
| 3 | 8 | False | False | Pass |
| 4 | 1 | False | False | Pass |
| 5 | 0 | False | False | Pass |
| 6 | -5 | False | False | Pass |
| 7 | "abc" | Loi | Loi | Pass |

============================================================
BAI 6: TONG 1 - 2 + 3 - 4 + ... + n
============================================================

| TC | n | Expected | Actual | Status |
|----|---|----------|--------|--------|
| 1 | 1 | 1 | 1 | Pass |
| 2 | 4 | -2 | -2 | Pass |
| 3 | 5 | 3 | 3 | Pass |
| 4 | 0 | Loi | Loi | Pass |
| 5 | -1 | Loi | Loi | Pass |
| 6 | "abc" | Loi | Loi | Pass |

============================================================
BAI 7: UCLN
============================================================

| TC | a | b | Expected | Actual | Status |
|----|---|---|----------|--------|--------|
| 1 | 6 | 9 | 3 | 3 | Pass |
| 2 | 10 | 5 | 5 | 5 | Pass |
| 3 | 7 | 13 | 1 | 1 | Pass |
| 4 | 0 | 5 | 5 | 5 | Pass |
| 5 | 0 | 0 | Loi | Loi | Pass |
| 6 | "a" | 5 | Loi | Loi | Pass |

============================================================
BAI 8: TONG GIAI THUA
============================================================

| TC | n | Expected | Actual | Status |
|----|---|----------|--------|--------|
| 1 | 1 | 1 | 1 | Pass |
| 2 | 3 | 9 | 9 | Pass |
| 3 | 5 | 153 | 153 | Pass |
| 4 | 0 | Loi | Loi | Pass |
| 5 | -2 | Loi | Loi | Pass |
| 6 | "abc" | Loi | Loi | Pass |

============================================================

TONG KET

Tat ca test case deu duoc thuc thi thanh cong.
Ty le Pass: 100%

Chuong trinh dap ung day du:
- Phan lop tuong duong
- Gia tri bien
- Du lieu hop le
- Du lieu khong hop le
- Du lieu ngoai le