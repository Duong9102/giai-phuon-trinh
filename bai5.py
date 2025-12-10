# khoi tao 
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

#sua lai dien tich cua phong tam (bathroom)
areas[-1] = 10.50

#sua "living room" thanh "chill zone"
areas[4] = 'chill zone'

# in ra areas
print(areas)
# khởi tạo
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# thêm dữ liệu của poolhouse vào areas, tạo danh sách mới tên areas_1
areas_1 = areas  + ["poolhouse", 24.5]

# thêm dữ liệu của garage vào areas_1, tạo danh sách mới tên areas_2
areas_2 = list(areas_1)
areas_2.extend(["garage", 15.45])

# in ra areas_1 và areas_2
print(areas_1)
print(areas_2)

# khởi tạo
areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

# xóa "poolhouse"
del(areas[-4])

# xóa diện tích của poolhouse
del(areas[-3])

# in ra areas
print(areas)
# khởi tạo areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# tạo areas_copy
areas_copy = list(areas)

# thay đổi areas_copy
areas_copy[0] = 5.0

# in ra areas
print(areas)