# please open Encoding UTF-8 because Program don't see Thai language
x = 0
while x == 0: # == คือการเปรียบเทียบค่า
    TimeIn = input("โปรดกรอกเวลาเข้าโรงจอดรถ(เช่น 09:25) = ")
    TimeOut = input("โปรดกรอกเวลาออกโรงจอดรถ(เช่น 10:25) = ")
    if int(TimeIn[0:2]) < 7 or int(TimeIn[0:2]) > 23:
        print("ขณะนี้ระบบหยุดทำการ จะเปิดให้บริการอีกครั้ง 07:00 - 23:00")
        quit()
    else:
        x += 1

print("เวลาเข้า :"+ TimeIn +" เวลาออก :"+ TimeOut)

if(int(TimeOut[0:2]) >= int(TimeIn[0:2])):#ป้องกันตัวเลขติดลบแล้วคำนวณค่าไม่ได้
    timehour = int(TimeOut[0:2])-int(TimeIn[0:2])
else:
    timehour = int(TimeIn[0:2])-int(TimeOut[0:2])

if(int(TimeOut[4:6]) >= int(TimeIn[4:6])):#ป้องกันตัวเลขติดลบแล้วคำนวณค่าไม่ได้
    timemin = int(TimeOut[4:6])-int(TimeIn[4:6])
else:
    timemin = int(TimeIn[4:6])-int(TimeOut[4:6])

print(timehour)
print(timemin)
