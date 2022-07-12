# please open Encoding UTF-8 because Program don't see Thai language
from time import time


try:
    x = 0
    while x == 0: # == คือการเปรียบเทียบค่า
        TimeIn = input("โปรดกรอกเวลาเข้าโรงจอดรถ(เช่น 09:25) = ")
        TimeOut = input("โปรดกรอกเวลาออกโรงจอดรถ(เช่น 10:25) = ")
        if int(TimeIn[0:2]) < 7 or int(TimeIn[0:2]) > 23:#(เปิดบริการตั้งแต่ 7:00 - 23:00)
            print("ขณะนี้ระบบหยุดทำการ จะเปิดให้บริการอีกครั้ง 07:00 - 23:00")
            quit()
        elif int(TimeIn[3:5]) > 60 or int(TimeOut[3:5]) > 60:#ป้องกัน Errorคำนวนนาทีผิด
            print("ค่าไม่ถูกต้อง นาทีจำกัดแค่ 60 นาที")
        else:
            x += 1

    print("เวลาเข้า :"+ TimeIn +" เวลาออก :"+ TimeOut)

    if(int(TimeOut[0:2]) >= int(TimeIn[0:2])):#ป้องกันตัวเลขติดลบแล้วคำนวณค่าไม่ได้
        timehour = int(TimeOut[0:2])-int(TimeIn[0:2])
    else:
        timehour = int(TimeIn[0:2])-int(TimeOut[0:2])

    if(int(TimeOut[3:5]) >= int(TimeIn[3:5])):#ป้องกันตัวเลขติดลบแล้วคำนวณค่าไม่ได้
        timemin = int(TimeOut[3:5])-int(TimeIn[3:5])
    else:
        timemin = int(TimeIn[3:5])-int(TimeOut[3:5])

    print("เวลาจอดของคุณคือ : "+ str(timehour) + " ชั่วโมง " + str(timemin) + " นาที ")


    if(timemin < 15 and timehour == 0):#จอดรถไม่เกิน 15 นาที ไม่คิดค่าบริการ
        print("Free")
    elif(timehour < 3):#จอดรถเกิน 15 นาที แต่ไม่เกิน 3 ชั่วโมง คิดค่าบริการชั่วโมงละ 10 บาท 
        if(timemin >= 30):#เศษของชั่วโมงคิดเป็นหนึ่งชั่วโมง เศษของชั่วโมง มากกว่า 30 นาที
            timehour += 1
        total = timehour * 10
        stringtotal = str(total)
        print("ค่าบริการ "+stringtotal+" บาท")
    elif(timehour < 6):#จอดรถตั้งแต่ 4 ชั่วโมง ถึง 6 ชั่วโมง คิดค่าบริการชั่วโมงที่ 4-6 ชั่วโมงละ 20 บาท
        if(timemin >= 30):
            timehour += 1
        total = timehour * 20
        stringtotal = str(total)
        print("ค่าบริการ "+stringtotal+" บาท")
    elif(timehour > 6):#จอดรถเกิน 6 ชั่วโมงขึ้นไป เหมาจ่าย 200 บาท
        print("ค่าบริการ 200 บาท")
except:
    print("ระบบตรวจพบความผิดปกติ โปรดตรวจสอบให้ว่าระบบทำงานอย่างถูกต้อง")
    print("ปัญหานี้อาจเกิดจากการ ป้อนค่าผิด โปรดกรอกดังตัวอย่าง")
    print("12:00,13:00,18:23,10:59,08:30")
    quit()