ma_quan_sat=input("Nhập mã quan sát: ")
gia_tri_do=float(input("Nhập giá trị đo: "))
gia_tri_f = gia_tri_do * 9/5 + 32
ten_dai_luong = "Nhiệt độ"
don_vi = "°C"
print("Mã quan sát: ")
print(ma_quan_sat)
print("")
print(gia_tri_do)
print("Giá trị sau chuyển đổi: ")
print(gia_tri_f)

from datetime import datetime

thoi_diem= datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")

print(f"Mã quan sát: {ma_quan_sat}")
print(f"Đại lượng: {ten_dai_luong}")
print(f"Giá trị : {gia_tri_do:.2f} {don_vi}")
print(f"Thời điểm: {thoi_diem_text}")