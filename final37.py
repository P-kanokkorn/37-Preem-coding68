from datetime import date

# 1. ดึงปีปัจจุบันจากระบบ
current_year = date.today().year

# 2. รับค่าปีเกิดจากผู้ใช้ (ค.ศ.)
birth_year = int(input("กรุณาใส่ปีเกิดของคุณ (ค.ศ.): "))

# 3. คำนวณอายุ
age = current_year - birth_year

# 4. แสดงผล
print(f"ปีนี้ปี {current_year} คุณอายุ {age} ปี")
