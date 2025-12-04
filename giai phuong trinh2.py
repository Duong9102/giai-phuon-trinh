import math

# 1. Nhập giá trị của các hệ số a, b, và c từ người dùng.
# Các dòng 1-6 đã được cung cấp trong hình ảnh và được dùng để nhập liệu.
s = input("Enter 3 real number (separated by space): ")
s_list = s.split() # Đổi tên biến để tránh xung đột với biến s_list trong code mẫu
a = float(s_list[0])
b = float(s_list[1])
c = float(s_list[2])
print(f"a = {a}, b = {b}, c = {c}")

# --- Enter your code from here ---

print("\n--- Solving the quadratic equation ---")

# 2. Kiểm tra điều kiện:
# Nếu a = 0, phương trình trở thành phương trình bậc nhất (bx + c = 0) hoặc không hợp lệ.
if a == 0:
    if b == 0:
        if c == 0:
            # 0x^2 + 0x + 0 = 0
            print("Phương trình có vô số nghiệm (với mọi x thuộc R).")
        else:
            # 0x^2 + 0x + c = 0 (với c != 0)
            print("Phương trình vô nghiệm.")
    else:
        # Phương trình bậc nhất: bx + c = 0 => x = -c/b
        x = -c / b
        print("Đây là phương trình bậc nhất (a=0).")
        print(f"Phương trình có một nghiệm: x = {-c}/{b} = {x}")
else:
    # Nếu a != 0, tiếp tục giải phương trình bậc hai.

    # 3. Tính và phân loại nghiệm dựa trên delta = b^2 - 4ac:
    delta = b**2 - 4 * a * c
    
    print(f"Delta = b^2 - 4ac = {b}^2 - 4({a})({c}) = {delta}")

    # 4. Hiển thị kết quả nghiệm ra màn hình
    if delta > 0:
        # Nếu delta > 0: Phương trình có hai nghiệm phân biệt.
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("Phương trình có hai nghiệm phân biệt.")
        print(f"Nghiệm x1 = (-b + sqrt(delta)) / 2a = {x1}")
        print(f"Nghiệm x2 = (-b - sqrt(delta)) / 2a = {x2}")
    
    elif delta == 0:
        # Nếu delta = 0: Phương trình có nghiệm kép.
        x = -b / (2 * a)
        print("Phương trình có nghiệm kép.")
        print(f"Nghiệm x1 = x2 = -b / 2a = {x}")
    
    else: # delta < 0
        # Nếu delta < 0: Phương trình vô nghiệm trong tập số thực.
        # Lưu ý: Có nghiệm phức nếu xét trong tập C.
        print("Phương trình vô nghiệm trong tập số thực (Delta < 0).")
        # (Không bắt buộc theo yêu cầu nhưng cung cấp thêm thông tin)
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(abs(delta)) / (2 * a)
        print(f"Trong tập số phức, phương trình có hai nghiệm phức liên hợp:")
        print(f"Nghiệm z1 = {real_part} + {imaginary_part}i")
        print(f"Nghiệm z2 = {real_part} - {imaginary_part}i")

# --- End of code ---