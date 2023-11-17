import os

print("ป้อนตัวเลขเพื่อเริ่มต้นการทำงาน \n1. สร้างไฟล์วิชาใหม่เพื่อเพิ่มข้อมูล \n2. เลือกวิชาและเพิ่มข้อมูลต่อท้ายไฟล์ \n3. เลือกวิชาและอ่านข้อมูลจากไฟล์มาแสดงผล \n4. เลือกวิชาและลบไฟล์ \n0. จบการทํางาน")

try:
    selected = input("โปรดเลือกคำสั่งที่คุณต้องการใช้งาน: ")
    if selected not in ["0","1","2","3","4"] :
        print("\n***********************************\nกรุณาเลือกเมนู 1, 2, 3, 4 หรือ 0 เท่านั้น\n***********************************")

    if selected == "1" :
        subjectName = input("ป้อนชื่อไฟล์วิชาของคุณเพื่อเก็บข้อมูลคะแนน (.txt):")

        if ".txt" not in subjectName :
            print("นามสกุลไฟล์ของคุณไม่ถูกต้อง กรุณาป้อนใหม่")

        else :
            stuName = input("กรุณาป้อนชื้อ - นามสกุล ของคุณ: ")
            midScore = int(input("กรุณาป้อนคะแนนกลางภาคของคุณ: "))
            finalScore = int(input("กรุณาป้อนคะแนนปลายภาคของคุณ: "))
            colletedScore = int(input("กรุณาป้อนคะแนนก็บของคุณ: "))
            totalScore = midScore + finalScore + colletedScore

            if totalScore >= 50 :
                result = "ผ่าน"
                subjectDetail = open(f"{subjectName}.txt", "w", encoding="utf-8")
                subjectDetail.write(f"\nนักศึกษา {stuName} มีคะแนนแต่ละภาคเท่านี้ \nคะแนนกลางภาค: {midScore} \nคะแนนปลายภาค: {finalScore} \nคะแนนเก็บ: {colletedScore} \nคะแนนรวม: {totalScore} \nผลลัพธ์ :{result} \n \n")
                print("\n-------------------------------\nสร้างไฟล์ใหม่และเพิ่มข้อมูลลงไฟล์เรียบร้อยแล้ว\n-------------------------------")
                subjectDetail.close()

            else : 
                result = "ไม่ผ่าน"
                subjectDetail = open(f"{subjectName}.txt", "w", encoding="utf-8")
                subjectDetail.write(f"\nนักศึกษา {stuName} มีคะแนนแต่ละภาคเท่านี้\nคะแนนกลางภาค: {midScore} \nคะแนนปลายภาค: {finalScore} \nคะแนนเก็บ: {colletedScore} \nคะแนนรวม: {totalScore} \nผลลัพธ์ :{result} \n \n")
                print("\n-------------------------------\nสร้างไฟล์ใหม่และเพิ่มข้อมูลลงไฟล์เรียบร้อยแล้ว\n-------------------------------")
                subjectDetail.close()

    if selected == "2" :

        subjectFilesName = os.listdir()
        if not subjectFilesName :
            print("XX--ไม่มีไฟล์ใดๆ อยู่เลย--XX")
            exit

        else :
            for i in subjectFilesName :
                if i.endswith(".txt"):
                    print(i)
            fileSelected = input("คุณต้องการเพิ่มข้อมูลต่อท้ายด้วยไฟล์อะไร (พิมพ์ชื่อไฟล์ให้ถูกต้อง): ")

            if fileSelected not in subjectFilesName :
                print("!!!คุณพิมพ์ชื่อไฟล์ผิด!!!")

            if not fileSelected.endswith(".txt"):
                print("ต้องเป็นนามสกุลไฟล์ .txt เท่านั้น")

            elif fileSelected in subjectFilesName :
                subjectMod = open(f"{fileSelected}", "a+", encoding="utf-8")
                stuName = input("กรุณาป้อนชื่อ - นามสกุล ของคุณ: ")
                midScore = int(input("กรุณาป้อนคะแนนกลางภาคของคุณ: "))
                finalScore = int(input("กรุณาป้อนคะแนนปลายภาคของคุณ: "))
                accuScore = int(input("กรุณาป้อนคะแนนก็บของคุณ: "))
                totalScore = midScore + finalScore + accuScore

                if totalScore >= 50 :
                    result = "ผ่าน"
                    if fileSelected.endswith(".txt"):
                        subjectMod.write(f"\nนักศึกษา {stuName} มีคะแนนแต่ละภาคเท่านี้\nคะแนนกลางภาค: {midScore} \nคะแนนปลายภาค: {finalScore} \nคะแนนเก็บ: {accuScore} \nคะแนนรวม: {totalScore} \nผลลัพธ์ :{result} \n \n")
                        print("\n******************************\nเพิ่มข้อมูลต่อท้ายไฟล์เรียบร้อยแล้ว\n******************************")
                        subjectMod.close()

                else : 
                    result = "ไม่ผ่าน"
                    if fileSelected.endswith(".txt"):
                        subjectMod.write(f"\nนักศึกษา {stuName} มีคะแนนแต่ละภาคเท่านี้\nคะแนนกลางภาค: {midScore} \nคะแนนปลายภาค: {finalScore} \nคะแนนเก็บ: {accuScore} \nคะแนนรวม: {totalScore} \nผลลัพธ์ :{result} \n \n")
                        print("\n******************************\nเพิ่มข้อมูลต่อท้ายไฟล์เรียบร้อยแล้ว\n******************************")
                        subjectMod.close

    if selected == "3" :
        subjectFileName = os.listdir()
        if not subjectFileName :
            print("X--ไม่มีไฟล์ใดๆ อยู่เลย--X")
            exit

        else :
            for i in subjectFileName :
                if i.endswith(".txt"):
                    print(i)
            fileSelected = input("คุณต้องการอ่านไฟล์อะไร (พิมพ์ชื่อไฟล์ให้ถูกต้อง): ")

            if fileSelected not in subjectFileName :
                print("!!!คุณพิมพ์ชื่อไฟล์ผิด!!!")

            if not fileSelected.endswith(".txt"):
                print("ต้องเป็นนามสกุลไฟล์ .txt เท่านั้น")

            elif fileSelected in subjectFileName :
                fileSelecteded = open(f"{fileSelected}", "r", encoding="utf-8")
                sRead = fileSelecteded.read()
                print(sRead)

    if selected == "4" :
        subjectFileName = os.listdir()
        if not subjectFileName :
            print("X--ไม่มีไฟล์ใดๆ อยู่เลย--X")
            exit

        else :
            for i in subjectFileName :
                if i.endswith(".txt"):
                    print(i)
            fileSelected = input("คุณต้องการลบไฟล์อะไร (พิมพ์ชื่อไฟล์ให้ถูกต้อง): ")

            if fileSelected not in subjectFileName :
                print("!!!คุณพิมพ์ชื่อไฟล์ผิด!!!")

            if not fileSelected.endswith(".txt"):
                print("ต้องเป็นไฟล์ .txt เท่านั้น")

            elif fileSelected in subjectFileName :
                os.remove(f"{fileSelected}")
                print("ลบไฟล์เรียบร้อยแล้ว")

    if selected == "0" :
        print("จบการทำงานเรียบร้อยแล้ว")
        exit

except Exception :
    print("\n***********************************\nเกิดข้อผิดพลาด กรุณาตรวจสอบข้อมูลที่ป้อนให้ถูกต้อง\n***********************************")
