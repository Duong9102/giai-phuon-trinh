s = input("Enter 3 real number (separated by space): ")
s = s.split()
a = float(s[0])
b = float(s[1])
c = float(s[2])
print(f"a = {a}, b = {b}, c = {c}")

# Enter your code from here

if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình vô số nghiệm.")
        else:
            print("Phương trình vô nghiệm.")
    else:
        x = -c / b
        print("Phương trình bậc nhất, nghiệm x =", x)
else:
    delta = b*b - 4*a*c
    print("Delta =", delta)

    if delta > 0:
        x1 = (-b + delta**0.5) / (2*a)
        x2 = (-b - delta**0.5) / (2*a)
        print("Phương trình có 2 nghiệm phân biệt:")
        print("x1 =", x1)
        print("x2 =", x2)
    elif delta == 0:
        x = -b / (2*a)
        print("Phương trình có nghiệm kép x =", x)
    else:
        print("Phương trình vô nghiệm trong tập số thực.")