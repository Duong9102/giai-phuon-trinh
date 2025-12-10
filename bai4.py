# khởi tạo danh sách areas
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# in ra phần tử thứ hai của areas
print(areas[1])

# in ra phần tử cuối cùng của areas
print(areas[-1])

# in ra diện tích của phòng khách (living room)
print(areas[5])

# khoi tao 
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# tong dien tich cua kitchen va bedroom: eat_sleep_area
eat_sleep_area = areas[3] + areas[-3]

# in ra gia tri cua eat_sleep_area
print(eat_sleep_area)

# trich xuat cac phan tu cua areas de khoi tao dowstairs
dowstairs = areas[:6]

# trich xuat cac phan tu cua areas de khoi tao upstairs
upstairs = areas[6:]

# in ra dowstairs va upstairs
print(dowstairs)
print(upstairs)

x = [["a", "b", "c"],
     ["d", "e", "f"],
     ["g", "h", "i"]]
x[2][0]
x[2][:2]