# 1. Nhập một số nguyên dương n từ bàn phím.
n = int(input("Enter a positive integer:"))
print(n)

s = 0 # Khởi tạo biến 's' để lưu tổng
# Khởi tạo biến đếm 'i' là số chẵn đầu tiên (0)
i = 0 

# 5 # Nhập code của bạn vào đây

# 2. Dùng vòng lặp while để tìm và cộng dồn tất cả các số chẵn nhỏ hơn n.
# Điều kiện lặp: i < n (số chẵn hiện tại phải nhỏ hơn n)
while i < n:
    # Cộng dồn số chẵn hiện tại (i) vào tổng (s)
    s += i 
    
    # Tăng biến đếm 'i' lên 2 để nhảy đến số chẵn kế tiếp
    i += 2

# 3. Hiển thị kết quả ra màn hình.
print(f"The sum of even numbers less than {n} is {s}")