# please open Encoding UTF-8 because Program don't see Thai language
x = 0
while x == 0:
    TimeIn = input("โปรดกรอกเวลาเข้าโรงจอดรถ(เช่น 09:25) = ")
    TimeOut = input("โปรดกรอกเวลาออกโรงจอดรถ(เช่น 10:25) = ")
    if int(TimeIn[0:2]) < 7 or int(TimeIn[0:2]) > 23:
        print("ขณะนี้ระบบหยุดทำการ จะเปิดให้บริการอีกครั้ง 07:00 - 23:00")
        quit()
    else:
        x += 1

print("เวลาเข้า :"+ TimeIn +" เวลาออก :"+ TimeOut)
timehour = TimeOut[0:2]-TimeIn[0:2]
timemin = TimeOut[0:2]-TimeIn[0:2]
if()
