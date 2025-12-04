# 1. Nhập một số nguyên dương n từ bàn phím.
n = int(input("Enter a positive integer:"))
print(n)

# 4 s = 0 # biến số dùng để lưu tổng
s = 0

# 5 # Nhập code của bạn vào đây

# 2. Dùng vòng lặp for để tính tổng các số từ 0 đến n.
for i in range(n + 1):
    s += i

# 3. Hiển thị kết quả ra màn hình.
print(f"The sum of 1 to {n} is {s}")